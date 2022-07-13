# -*- coding:utf-8 _*-

import torch
import torch.nn as nn
from .. import create_module


class DetModel(nn.Module):
    def __init__(self, config):
        super(DetModel, self).__init__()
        self.algorithm = config['base']['algorithm']
        self.backbone = create_module(config['backbone']['function'])(config['base']['pretrained'])

        self.head = create_module(config['head']['function']) \
                (config['base']['in_channels'],
                 config['base']['inner_channels'])
        self.mulclass = False

        if 'n_class' in config['base'].keys():
            self.mulclass = True
            self.seg_out = create_module(config['segout']['function'])(config['base']['n_class'],config['base']['inner_channels'],
                                                                   config['base']['k'],
                                                                   config['base']['adaptive'])
        else:
            self.seg_out = create_module(config['segout']['function'])(config['base']['inner_channels'],
                                                                   config['base']['k'],
                                                                   config['base']['adaptive'])

    def forward(self, data):
        if self.training:
            if self.algorithm == "DB":
                if self.mulclass:
                    img, gt,gt_class, gt_mask, thresh_map, thresh_mask = data
                else:
                    img, gt, gt_mask, thresh_map, thresh_mask = data
                if torch.cuda.is_available():
                    if self.mulclass:
                        gt_class = gt_class.cuda()
                    img, gt, gt_mask, thresh_map, thresh_mask = \
                        img.cuda(), gt.cuda(), gt_mask.cuda(), thresh_map.cuda(), thresh_mask.cuda()
                gt_batch = dict(gt=gt)
                gt_batch['mask'] = gt_mask
                gt_batch['thresh_map'] = thresh_map
                gt_batch['thresh_mask'] = thresh_mask
                if self.mulclass:
                    gt_batch['gt_class'] = gt_class

        else:
            img = data

        x = self.backbone(img)
        x = self.head(x)
        x = self.seg_out(x, img)

        if self.training:
            return x, gt_batch
        return x


class DetLoss(nn.Module):
    def __init__(self, config):
        super(DetLoss, self).__init__()
        self.algorithm = config['base']['algorithm']
        if (config['base']['algorithm']) == 'DB':
            if 'n_class' in config['base'].keys():
                self.loss = create_module(config['loss']['function'])(config['base']['n_class'],config['loss']['l1_scale'],
                                                 config['loss']['bce_scale'],config['loss']['class_scale'])
            else:
                self.loss = create_module(config['loss']['function'])(config['loss']['l1_scale'],config['loss']['bce_scale'])
                
        elif (config['base']['algorithm']) == 'PAN':
            self.loss = create_module(config['loss']['function'])(config['loss']['kernel_rate'],
                                                                  config['loss']['agg_dis_rate'])
        elif (config['base']['algorithm']) == 'PSE':
            self.loss = create_module(config['loss']['function'])(config['loss']['text_tatio'])

        elif (config['base']['algorithm']) == 'SAST':
            self.loss = create_module(config['loss']['function'])(config['loss']['tvo_lw'],
                                                                  config['loss']['tco_lw'],
                                                                  config['loss']['score_lw'],
                                                                  config['loss']['border_lw']
                                                                  )
        else:
            assert True == False, ('not support this algorithm !!!')

    def forward(self, pre_batch, gt_batch):
        return self.loss(pre_batch, gt_batch)

