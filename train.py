# python imports
import argparse
import os
import time
import datetime
from pprint import pprint

# torch imports
import torch
import torch.nn as nn
import torch.utils.data
# for visualization
from torch.utils.tensorboard import SummaryWriter

# our code
from libs.core import load_config
from libs.datasets import make_dataset, make_data_loader
from libs.modeling import make_meta_arch
from libs.utils import (train_one_epoch, valid_one_epoch, ANETdetection,
                        save_checkpoint, make_optimizer, make_scheduler,
                        fix_random_seed, ModelEma)
from libs.utils.train_utils import train_one_epoch_rgb, train_one_epoch_sim, train_one_epoch_multi

import copy


################################################################################
def main(args):
    """main function that handles training / inference"""

    """1. setup parameters / folders"""
    # parse args
    args.start_epoch = 0
    if os.path.isfile(args.config):
        cfg = load_config(args.config)
    else:
        raise ValueError("Config file does not exist.")
    pprint(cfg)

    # prep for output folder (based on time stamp)
    if not os.path.exists(cfg['output_folder']):
        os.mkdir(cfg['output_folder'])
    cfg_filename = os.path.basename(args.config).replace('.yaml', '')
    if len(args.output) == 0:
        ts = datetime.datetime.fromtimestamp(int(time.time()))
        ckpt_folder = os.path.join(
            cfg['output_folder'], cfg_filename + '_' + str(ts))
    else:
        ckpt_folder = os.path.join(
            cfg['output_folder'], cfg_filename + '_' + str(args.output))
    if not os.path.exists(ckpt_folder):
        os.mkdir(ckpt_folder)
    # tensorboard writer
    tb_writer = SummaryWriter(os.path.join(ckpt_folder, 'logs'))

    # fix the random seeds (this will fix everything)
    rng_generator = fix_random_seed(cfg['init_rand_seed'], include_cuda=True)

    # re-scale learning rate / # workers based on number of GPUs
    cfg['opt']["learning_rate"] *= len(cfg['devices'])
    cfg['loader']['num_workers'] *= len(cfg['devices'])

    """2. create dataset / dataloader"""
    train_dataset = make_dataset(
        cfg['dataset_name'], True, cfg['train_split'], **cfg['dataset']
    )
    # update cfg based on dataset attributes (fix to epic-kitchens)
    train_db_vars = train_dataset.get_attributes()
    cfg['model']['train_cfg']['head_empty_cls'] = train_db_vars['empty_label_ids']

    # data loaders
    train_loader = make_data_loader(
        train_dataset, True, rng_generator, **cfg['loader'])

    step = 0

    """3. create model, optimizer, and scheduler"""
    # cfg_model = copy.deepcopy(cfg['model'])
    # cfg_model['backbone_type'] = 'conv'
    # model
    model = make_meta_arch(cfg['model_name'], **cfg['model'])
    # model = make_meta_arch(cfg['model_name'], **cfg_model)
    # model = None
    if step == 1:
        ncfg_model = copy.deepcopy(cfg['model'])

        ncfg_model['backbone_type'] = 'conv'
        # ncfg_model['dw'] = True
        # ncfg_model['gateFusion'] = True
        model = make_meta_arch(cfg['model_name'], **ncfg_model)

        ncfg_model['rgbOnly'] = True

        rgbModel = make_meta_arch(cfg['model_name'], **ncfg_model)

        # ckpt = './ckpt/thumos_i3d_reproduce/epoch_035.pth.tar'
        ckpt = './ckpt/thumos_i3d_improve_tem_att_tf2cnn_no_feat_60/epoch_050.pth.tar'        # ckpt = './ckpt/thumos_i3d_improve_improve_early_fusion_filter/epoch_035.pth.tar'
        # ckpt = './ckpt/thumos_i3d_reproduce_conv/epoch_035.pth.tar'
        # ckpt = './ckpt/thumos_i3d_improve_tf_tem_att_2_FC_gate_dw_cnn_ori_head_neck_tem_attn_T2_no_feat_loss/epoch_035.pth.tar'
        # improve_reproduce_filter

        checkpoint = torch.load(ckpt)

        model = nn.DataParallel(model, device_ids=cfg['devices'])
        rgbModel = nn.DataParallel(rgbModel, device_ids=cfg['devices'])
        model.load_state_dict(checkpoint['state_dict_ema'])

        # 获取现有模型的参数字典
        modelRgbOnly_dict = rgbModel.state_dict()
        # 获取两个模型相同网络层的参数字典
        state_dict = {k: v for k, v in checkpoint['state_dict'].items() if k in modelRgbOnly_dict.keys()}
        # update必不可少，实现相同key的value同步
        modelRgbOnly_dict.update(state_dict)
        # 加载模型部分参数
        rgbModel.load_state_dict(modelRgbOnly_dict)

        # enable model EMA
        print("Using model EMA ...")
        model_ema = ModelEma(rgbModel)


        '''
        0 rgb2flow.extractor.0.weight
        1 rgb2flow.extractor.0.bias
        2 rgb2flow.extractor.1.weight
        3 rgb2flow.extractor.1.bias
        '''

        # for i, p in enumerate(rgbModel.parameters()):
        #     if i > 3:
        #         p.requires_grad = False

        cfg['opt']['rgbOnly'] = True
        # optimizer
        optimizer = make_optimizer(rgbModel, cfg['opt'])
        # schedule
        num_iters_per_epoch = len(train_loader)
        scheduler = make_scheduler(optimizer, cfg['opt'], num_iters_per_epoch)
    elif step == 2:
        ncfg_model = copy.deepcopy(cfg['model'])
        # ncfg_model['backbone_arch'] = (1,1,5)
        ncfg_model['rgbOnly'] = True
        ncfg_model['backbone_type'] = 'conv'
        model = make_meta_arch(cfg['model_name'], **ncfg_model)
        ncfg_model['dw'] = True
        simModel = make_meta_arch(cfg['model_name'], **ncfg_model)
        # ncfg_model['gateFusion'] = True


        # ckpt = './ckpt/thumos_i3d_reproduce/epoch_035.pth.tar'
        # ckpt = './ckpt/thumos_i3d_rp_nosave_attn/epoch_035.pth.tar'
        ckpt = './ckpt/thumos_i3d_rp_nosave_attn_tf2cnn_rgb/epoch_035.pth.tar'

        # ckpt = './ckpt/thumos_i3d_improve_tem_att_tf2cnn_no_feat_to_rgb/epoch_035.pth.tar'
        # ckpt = './ckpt/thumos_i3d_improve_tem_att_tf2cnn_no_feat_to_rgb_trans/epoch_035.pth.tar'
        checkpoint = torch.load(ckpt)

        model = nn.DataParallel(model, device_ids=cfg['devices'])
        simModel = nn.DataParallel(simModel, device_ids=cfg['devices'])
        # model.load_state_dict(checkpoint['state_dict'])
        model.load_state_dict(checkpoint['state_dict_ema'])

        # enable model EMA
        print("Using model EMA ...")
        model_ema = ModelEma(simModel)
        # optimizer
        optimizer = make_optimizer(simModel, cfg['opt'])
        # schedule
        num_iters_per_epoch = len(train_loader)
        scheduler = make_scheduler(optimizer, cfg['opt'], num_iters_per_epoch)

        if args.resume:
            if os.path.isfile(args.resume):
                # load ckpt, reset epoch / best rmse
                checkpoint = torch.load(args.resume,
                                        map_location=lambda storage, loc: storage.cuda(
                                            cfg['devices'][0]))
                args.start_epoch = checkpoint['epoch']
                model.load_state_dict(checkpoint['state_dict'])
                model_ema.module.load_state_dict(checkpoint['state_dict_ema'])
                # also load the optimizer / scheduler if necessary
                optimizer.load_state_dict(checkpoint['optimizer'])
                scheduler.load_state_dict(checkpoint['scheduler'])
                print("=> loaded checkpoint '{:s}' (epoch {:d}".format(
                    args.resume, checkpoint['epoch']
                ))
                del checkpoint
            else:
                print("=> no checkpoint found at '{}'".format(args.resume))
                return
    elif step == 3:
        # multi-teacher learning
        modal_teacher = model
        ncfg_model = copy.deepcopy(cfg['model'])
        ncfg_model['backbone_type'] = 'conv'
        # ncfg_model['dw'] = True
        # ncfg_model['gateFusion'] = True
        structure_teacher = make_meta_arch(cfg['model_name'], **ncfg_model)
        ncfg_model['rgbOnly'] = True
        ncfg_model['dw'] = True
        rgbModel = make_meta_arch(cfg['model_name'], **ncfg_model)

        # ckpt = './ckpt/thumos_i3d_reproduce/epoch_035.pth.tar'
        # ckpt = './ckpt/thumos_i3d_improve_aud_early_fusion/epoch_035.pth.tar'
        # ckpt = './ckpt/thumos_i3d_improve_improve_early_fusion_filter/epoch_035.pth.tar'
        # ckpt = './ckpt/thumos_i3d_reproduce_conv/epoch_035.pth.tar'

        # ckpt1 = './ckpt/thumos_i3d_reproduce/epoch_035.pth.tar' # 71.63
        # ckpt2 = './ckpt/thumos_i3d_improve_tf_to_cnn/epoch_035.pth.tar' # 67.85

        ckpt1 = './ckpt/thumos_i3d_improve_tem_att/epoch_035.pth.tar' # 70.87
        ckpt2 = './ckpt/thumos_i3d_improve_tem_att_tf2cnn_no_feat/epoch_035.pth.tar' # 68.48

        checkpoint1 = torch.load(ckpt1)
        checkpoint2 = torch.load(ckpt2)

        modal_teacher = nn.DataParallel(modal_teacher, device_ids=cfg['devices'])
        structure_teacher = nn.DataParallel(structure_teacher, device_ids=cfg['devices'])
        rgbModel = nn.DataParallel(rgbModel, device_ids=cfg['devices'])
        modal_teacher.load_state_dict(checkpoint1['state_dict'])
        structure_teacher.load_state_dict(checkpoint2['state_dict_ema'])

        # 获取现有模型的参数字典
        modelRgbOnly_dict = rgbModel.state_dict()
        # 获取两个模型相同网络层的参数字典
        state_dict = {k: v for k, v in checkpoint2['state_dict'].items() if k in modelRgbOnly_dict.keys()}
        # update必不可少，实现相同key的value同步
        modelRgbOnly_dict.update(state_dict)
        # 加载模型部分参数
        rgbModel.load_state_dict(modelRgbOnly_dict)

        del checkpoint1
        del checkpoint2

        # enable model EMA
        print("Using model EMA ...")
        model_ema = ModelEma(rgbModel)

        # optimizer
        optimizer = make_optimizer(rgbModel, cfg['opt'])
        # schedule
        num_iters_per_epoch = len(train_loader)
        scheduler = make_scheduler(optimizer, cfg['opt'], num_iters_per_epoch)
    else:
        # not ideal for multi GPU training, ok for now
        model = nn.DataParallel(model, device_ids=cfg['devices'])
        # optimizer
        optimizer = make_optimizer(model, cfg['opt'])
        # schedule
        num_iters_per_epoch = len(train_loader)
        scheduler = make_scheduler(optimizer, cfg['opt'], num_iters_per_epoch)

        # enable model EMA
        print("Using model EMA ...")
        model_ema = ModelEma(model)

    """4. Resume from model / Misc"""
    # resume from a checkpoint?
    # if args.resume:
    #     if os.path.isfile(args.resume):
    #         # load ckpt, reset epoch / best rmse
    #         checkpoint = torch.load(args.resume,
    #             map_location = lambda storage, loc: storage.cuda(
    #                 cfg['devices'][0]))
    #         args.start_epoch = checkpoint['epoch']
    #         model.load_state_dict(checkpoint['state_dict'])
    #         model_ema.module.load_state_dict(checkpoint['state_dict_ema'])
    #         # also load the optimizer / scheduler if necessary
    #         optimizer.load_state_dict(checkpoint['optimizer'])
    #         scheduler.load_state_dict(checkpoint['scheduler'])
    #         print("=> loaded checkpoint '{:s}' (epoch {:d}".format(
    #             args.resume, checkpoint['epoch']
    #         ))
    #         del checkpoint
    #     else:
    #         print("=> no checkpoint found at '{}'".format(args.resume))
    #         return

    # save the current config
    with open(os.path.join(ckpt_folder, 'config.txt'), 'w') as fid:
        pprint(cfg, stream=fid)
        fid.flush()

    """4. training / validation loop"""
    print("\nStart training model {:s} ...".format(cfg['model_name']))

    # start training
    start = time.time()
    max_epochs = cfg['opt'].get(
        'early_stop_epochs',
        cfg['opt']['epochs'] + cfg['opt']['warmup_epochs']
    )

    if step==1:
        for epoch in range(args.start_epoch, max_epochs):
            # train for one epoch
            train_one_epoch_rgb(
                train_loader,
                model,
                rgbModel,
                optimizer,
                scheduler,
                epoch,
                model_ema=model_ema,
                clip_grad_l2norm=cfg['train_cfg']['clip_grad_l2norm'],
                tb_writer=tb_writer,
                print_freq=args.print_freq
            )

            # save ckpt once in a while
            if (
                    ((epoch + 1) == max_epochs) #or
                    # ((args.ckpt_freq > 0) and ((epoch + 1) % args.ckpt_freq == 0))
            ):
                save_states = {
                    'epoch': epoch + 1,
                    'state_dict': model.state_dict(),
                    'scheduler': scheduler.state_dict(),
                    'optimizer': optimizer.state_dict(),
                }

                save_states['state_dict_ema'] = model_ema.module.state_dict()
                save_checkpoint(
                    save_states,
                    False,
                    file_folder=ckpt_folder,
                    file_name='epoch_{:03d}.pth.tar'.format(epoch + 1)
                )
    elif step==2:
        for epoch in range(args.start_epoch, max_epochs):
            # train for one epoch
            train_one_epoch_sim(
                train_loader,
                model,
                simModel,
                optimizer,
                scheduler,
                epoch,
                model_ema=model_ema,
                clip_grad_l2norm=cfg['train_cfg']['clip_grad_l2norm'],
                tb_writer=tb_writer,
                print_freq=args.print_freq
            )

            # save ckpt once in a while
            if (
                    ((epoch + 1) == max_epochs)
                    # ((args.ckpt_freq > 0) and ((epoch + 1) % args.ckpt_freq == 0))
            ):
                save_states = {
                    'epoch': epoch + 1,
                    'state_dict': model.state_dict(),
                    'scheduler': scheduler.state_dict(),
                    'optimizer': optimizer.state_dict(),
                }

                save_states['state_dict_ema'] = model_ema.module.state_dict()
                save_checkpoint(
                    save_states,
                    False,
                    file_folder=ckpt_folder,
                    file_name='epoch_{:03d}.pth.tar'.format(epoch + 1)
                )
    elif step==3:
        for epoch in range(args.start_epoch, max_epochs):
            # train for one epoch
            train_one_epoch_multi(
                train_loader,
                modal_teacher,
                structure_teacher,
                rgbModel,
                optimizer,
                scheduler,
                epoch,
                model_ema=model_ema,
                clip_grad_l2norm=cfg['train_cfg']['clip_grad_l2norm'],
                tb_writer=tb_writer,
                print_freq=args.print_freq
            )

            # save ckpt once in a while
            if (
                    ((epoch + 1) == max_epochs) or
                    ((args.ckpt_freq > 0) and ((epoch + 1) % args.ckpt_freq == 0))
            ):
                save_states = {
                    'epoch': epoch + 1,
                    'state_dict': model.state_dict(),
                    'scheduler': scheduler.state_dict(),
                    'optimizer': optimizer.state_dict(),
                }

                save_states['state_dict_ema'] = model_ema.module.state_dict()
                save_checkpoint(
                    save_states,
                    False,
                    file_folder=ckpt_folder,
                    file_name='epoch_{:03d}.pth.tar'.format(epoch + 1)
                )
    else:
        for epoch in range(args.start_epoch, max_epochs):
            # train for one epoch
            train_one_epoch(
                train_loader,
                model,
                optimizer,
                scheduler,
                epoch,
                model_ema = model_ema,
                clip_grad_l2norm = cfg['train_cfg']['clip_grad_l2norm'],
                tb_writer=tb_writer,
                print_freq=args.print_freq
            )

            # save ckpt once in a while
            # if (
            #     ((epoch + 1) == max_epochs) or
            #     ((args.ckpt_freq > 0) and ((epoch + 1) % args.ckpt_freq == 0))
            # ):
            if (
                ((epoch + 1) == max_epochs)
            ):
                save_states = {
                    'epoch': epoch + 1,
                    'state_dict': model.state_dict(),
                    'scheduler': scheduler.state_dict(),
                    'optimizer': optimizer.state_dict(),
                }

                save_states['state_dict_ema'] = model_ema.module.state_dict()
                save_checkpoint(
                    save_states,
                    False,
                    file_folder=ckpt_folder,
                    file_name='epoch_{:03d}.pth.tar'.format(epoch + 1)
                )



    # wrap up
    tb_writer.close()
    print("All done!")
    end = time.time()
    print("total time:{}".format(end-start))
    return

################################################################################
if __name__ == '__main__':
    """Entry Point"""
    # the arg parser
    parser = argparse.ArgumentParser(
      description='Train a point-based transformer for action localization')
    parser.add_argument('config', metavar='DIR',
                        help='path to a config file')
    parser.add_argument('-p', '--print-freq', default=10, type=int,
                        help='print frequency (default: 10 iterations)')
    parser.add_argument('-c', '--ckpt-freq', default=5, type=int,
                        help='checkpoint frequency (default: every 5 epochs)')
    parser.add_argument('--output', default='', type=str,
                        help='name of exp folder (default: none)')
    parser.add_argument('--resume', default='', type=str, metavar='PATH',
                        help='path to a checkpoint (default: none)')
    args = parser.parse_args()
    main(args)
