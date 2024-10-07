import torch
from torchvision.models import resnet18
import torch_pruning as tp

class MyMagnitudeImportance(tp.importance.Importance):
    def __call__(self, group, **kwargs):
        # 1. 首先定义一个列表用于存储分组内每一层的重要性
        group_imp = []
        # 2. 迭代分组内的各个层，对Conv层计算重要性
        for dep, idxs in group: # idxs是一个包含所有可剪枝索引的列表，用于处理DenseNet中的局部耦合的情况
            layer = dep.target.module # 获取 nn.Module
            prune_fn = dep.handler    # 获取 剪枝函数
            # 3. 这里我们简化问题，仅计算卷积输出通道的重要性
            if isinstance(layer, nn.Conv2d) and prune_fn == tp.prune_conv_out_channels:
                w = layer.weight.data[idxs].flatten(1) # 用索引列表获取耦合通道对应的参数，并展开成2维
                local_norm = w.abs().sum(1) # 计算每个通道参数子矩阵的 L1 Norm
                group_imp.append(local_norm) # 将其保存在列表中

        if len(group_imp)==0: return None # 跳过不包含卷积层的分组
        # 4. 按通道计算平均重要性
        group_imp = torch.stack(group_imp, dim=0).mean(dim=0)
        return group_imp

# python imports
import argparse
import os
import glob
import time
from pprint import pprint

# torch imports
import torch
import torch.nn as nn
import torch.backends.cudnn as cudnn
import torch.utils.data

# our code
from libs.core import load_config
from libs.datasets import make_dataset, make_data_loader
from libs.modeling import make_meta_arch
from libs.utils import valid_one_epoch, ANETdetection, fix_random_seed
import copy


################################################################################
def main(args):
    """0. load config"""
    # sanity check
    if os.path.isfile(args.config):
        cfg = load_config(args.config)
    else:
        raise ValueError("Config file does not exist.")
    assert len(cfg['val_split']) > 0, "Test set must be specified!"
    if ".pth.tar" in args.ckpt:
        assert os.path.isfile(args.ckpt), "CKPT file does not exist!"
        ckpt_file = args.ckpt
    else:
        assert os.path.isdir(args.ckpt), "CKPT file folder does not exist!"
        if args.epoch > 0:
            ckpt_file = os.path.join(
                args.ckpt, 'epoch_{:03d}.pth.tar'.format(args.epoch)
            )
        else:
            ckpt_file_list = sorted(glob.glob(os.path.join(args.ckpt, '*.pth.tar')))
            ckpt_file = ckpt_file_list[-1]
        assert os.path.exists(ckpt_file)

    if args.topk > 0:
        cfg['model']['test_cfg']['max_seg_num'] = args.topk
    pprint(cfg)

    """1. fix all randomness"""
    # fix the random seeds (this will fix everything)
    _ = fix_random_seed(0, include_cuda=True)

    """2. create dataset / dataloader"""
    val_dataset = make_dataset(
        cfg['dataset_name'], False, cfg['val_split'], **cfg['dataset']
    )
    # set bs = 1, and disable shuffle
    val_loader = make_data_loader(
        val_dataset, False, None, 1, cfg['loader']['num_workers']
    )

    step = 0
    """3. create model and evaluator"""
    if step == 1:
        ncfg_model = copy.deepcopy(cfg['model'])
        ncfg_model['rgbOnly'] = True
        model = make_meta_arch(cfg['model_name'], **ncfg_model)
    elif step==2:
        ncfg_model = copy.deepcopy(cfg['model'])
        ncfg_model['backbone_arch'] = (1,1,5)
        model = make_meta_arch(cfg['model_name'], **ncfg_model)
    else:
        # model
        model = make_meta_arch(cfg['model_name'], **cfg['model'])
    # not ideal for multi GPU training, ok for now
    model = nn.DataParallel(model, device_ids=cfg['devices'])

    ckpt_file = './reproduce.pth.tar'

    """4. load ckpt"""
    print("=> loading checkpoint '{}'".format(ckpt_file))
    # load ckpt, reset epoch / best rmse
    checkpoint = torch.load(
        ckpt_file,
        map_location = lambda storage, loc: storage.cuda(cfg['devices'][0])
    )
    # load ema model instead
    print("Loading from EMA model ...")
    model.load_state_dict(checkpoint['state_dict_ema'])
    del checkpoint

    # set up evaluator
    det_eval, output_file = None, None
    if not args.saveonly:
        val_db_vars = val_dataset.get_attributes()
        det_eval = ANETdetection(
            val_dataset.json_file,
            val_dataset.split[0],
            tiou_thresholds = val_db_vars['tiou_thresholds']
        )
    else:
        output_file = os.path.join(os.path.split(ckpt_file)[0], 'eval_results.pkl')

    model.eval()

    # 1. 使用我们上述定义的重要性评估
    imp = MyMagnitudeImportance()
    c = 0
    # 2. 忽略无需剪枝的层，例如最后的分类层
    ignored_layers = []
    for m in model.modules():
        c += 1
        if isinstance(m, torch.nn.Conv1d) and (m.out_channels==2 or m.out_channels==20) :
            ignored_layers.append(m)  # DO NOT prune the final classifier!
    for iter_idx, video_list in enumerate(val_loader, 0):
        example_inputs = video_list
        break
    # example_inputs = torch.randn(1,2048,2304)
    # 3. 初始化剪枝器
    iterative_steps = 5  # 迭代式剪枝，重复5次Pruning-Finetuning的循环完成剪枝。
    pruner = tp.pruner.MetaPruner(
        model,
        example_inputs,  # 用于分析依赖的伪输入
        importance=imp,  # 重要性评估指标
        iterative_steps=iterative_steps,  # 迭代剪枝，设为1则一次性完成剪枝
        ch_sparsity=0.5,  # 目标稀疏性，这里我们移除50%的通道 ResNet18 = {64, 128, 256, 512} => ResNet18_Half = {32, 64, 128, 256}
        ignored_layers=ignored_layers,  # 忽略掉最后的分类层
    )

    # 4. Pruning-Finetuning的循环
    base_macs, base_nparams = tp.utils.count_ops_and_params(model, example_inputs)
    for i in range(iterative_steps):
        pruner.step()  # 执行裁剪，本例子中我们每次会裁剪10%，共执行5次，最终稀疏度为50%
        macs, nparams = tp.utils.count_ops_and_params(model, example_inputs)
        print("  Iter %d/%d, Params: %.2f M => %.2f M" % (i + 1, iterative_steps, base_nparams / 1e6, nparams / 1e6))
        print("  Iter %d/%d, MACs: %.2f G => %.2f G" % (i + 1, iterative_steps, base_macs / 1e9, macs / 1e9))
        # finetune your model here
        # finetune(model)
        # ...
    print(model)
    return

    """5. Test the model"""
    print("\nStart testing model {:s} ...".format(cfg['model_name']))
    start = time.time()
    mAP = valid_one_epoch(
        val_loader,
        model,
        -1,
        evaluator=det_eval,
        output_file=output_file,
        ext_score_file=cfg['test_cfg']['ext_score_file'],
        tb_writer=None,
        print_freq=args.print_freq
    )
    end = time.time()
    print("All done! Total time: {:0.2f} sec".format(end - start))
    return

################################################################################
if __name__ == '__main__':
    """Entry Point"""
    # the arg parser
    parser = argparse.ArgumentParser(
      description='Train a point-based transformer for action localization')
    parser.add_argument('config', type=str, metavar='DIR',
                        help='path to a config file')
    parser.add_argument('ckpt', type=str, metavar='DIR',
                        help='path to a checkpoint')
    parser.add_argument('-epoch', type=int, default=-1,
                        help='checkpoint epoch')
    parser.add_argument('-t', '--topk', default=-1, type=int,
                        help='max number of output actions (default: -1)')
    parser.add_argument('--saveonly', action='store_true',
                        help='Only save the ouputs without evaluation (e.g., for test set)')
    parser.add_argument('-p', '--print-freq', default=10, type=int,
                        help='print frequency (default: 10 iterations)')
    args = parser.parse_args()
    main(args)
