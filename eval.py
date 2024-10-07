# python imports
import argparse
import os
import glob
import time
from collections import OrderedDict
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
import thop
from fvcore.nn import FlopCountAnalysis, parameter_count_table, parameter_count
from torchinfo import summary


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
        args.epoch = 35
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

    # val_dataset = make_dataset(
    #     cfg['dataset_name'], False, cfg['train_split'], **cfg['dataset']
    # )

    # set bs = 1, and disable shuffle
    val_loader = make_data_loader(
        val_dataset, False, None, 1, cfg['loader']['num_workers']
    )

    step = 2

    # cfg['model']['rgbOnly'] = True
    """3. create model and evaluator"""
    if step == 1:
        ncfg_model = copy.deepcopy(cfg['model'])
        ncfg_model['rgbOnly'] = True
        ncfg_model['backbone_type'] = 'conv'
        model = make_meta_arch(cfg['model_name'], **ncfg_model)
    elif step==2:
        ncfg_model = copy.deepcopy(cfg['model'])
        # ncfg_model['backbone_arch'] = (1,1,5)
        # todo syx no dw and gatefusion
        ncfg_model['backbone_type'] = 'conv'
        ncfg_model['rgbOnly'] = True

        # todo syx dw and gatefusion
        # ncfg_model['backbone_type'] = 'conv'
        ncfg_model['dw'] = True
        # ncfg_model['gateFusion'] = True

        model = make_meta_arch(cfg['model_name'], **ncfg_model)
    else:
        # model
        model = make_meta_arch(cfg['model_name'], **cfg['model'])
    isSummary = False
    # not ideal for multi GPU training, ok for now
    if isSummary:
        checkpoint = torch.load(
            ckpt_file,
            map_location='cpu'
        )
        new_state_dict = OrderedDict()
        for k, v in checkpoint['state_dict_ema'].items():
            name = k[7:]  # remove `module.`
            new_state_dict[name] = v
        # load params
        model.load_state_dict(new_state_dict)
    else:
        # checkpoint = torch.load(
        #     ckpt_file,
        #     map_location='cpu'
        # )
        # new_state_dict = OrderedDict()
        # for k, v in checkpoint['state_dict_ema'].items():
        #     name = k[7:]  # remove `module.`
        #     new_state_dict[name] = v
        # # load params
        # model.load_state_dict(new_state_dict)

        model = nn.DataParallel(model, device_ids=cfg['devices'])

        """4. load ckpt"""
        print("=> loading checkpoint '{}'".format(ckpt_file))
        # load ckpt, reset epoch / best rmse
        checkpoint = torch.load(
            ckpt_file,
            map_location = lambda storage, loc: storage.cuda(cfg['devices'][0])
        )
        model.load_state_dict(checkpoint['state_dict_ema'])

    # load ema model instead
    print("Loading from EMA model ...")
    # del checkpoint
    if isSummary:
        from libs.utils.flop_count.flop_count import flop_count
        # todo syx summary model
        for iter_idx, video_list in enumerate(val_loader, 0):
            # model.eval()
            model(video_list)
            flop_count(model, (video_list,))
            flops = FlopCountAnalysis(model, video_list)
            print(flops.total()/1e9)

            flops, params = thop.profile(model, inputs=(video_list,))

            # flops = FlopCountAnalysis(model, video_list).total()
            # params = parameter_count(model)['']

            print(f"FLOPs: {flops / 1e9} G")  # 打印计算量（以十亿次浮点运算为单位）
            print(f"Params: {params / 1e6} M")  # 打印参数量（以百万为单位）
            break
        return


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
