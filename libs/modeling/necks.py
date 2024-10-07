import torch
from torch import nn
from torch.nn import functional as F

from .models import register_neck
from .blocks import MaskedConv1D, LayerNorm

class se_block(nn.Module):
    # 定义init函数；
    # channel表示输入进来的通道数；
    # ratio表示缩放的比例，用于第一次全连接
    def __init__(self, channel, ratio=8):
        # 初始化
        super(se_block, self).__init__()
        self.t = channel
        # 定义全局平均池化，输出高宽为1，AdaptiveAvgPool2d表示自适应平均池化
        self.avg_pool = nn.AdaptiveAvgPool1d(1)
        # 定义两次全连接fc
        # 定义序列模型Sequential
        self.fc = nn.Sequential(
            # 定义第一个全连接，神经元个数减少
            # 输入神经元个数channel，输出神经元个数channel//ratio，不使用偏置量
            nn.Linear(channel, channel // ratio, bias=False),
            # 激活函数ReLU
            nn.ReLU(inplace=True),
            # 定义第二个全连接，神经元个数变为原来个数
            # 输入神经元个数channel//ratio，输出神经元个数channel，不使用偏置量
            nn.Linear(channel // ratio, channel, bias=False),
            # 激活函数Sigmoid，把值固定到0-1之间
            nn.Sigmoid()
        )

    # 前传函数
    def forward(self, x):
        # batch channel time
        # 计算输入进来的特征层的size，batch_size，通道数，高，宽
        # 其中batch_size表示一次训练所抓取的数据样本数量
        b, c, t = x.size()
        if t > self.t:
            nx = F.interpolate(x, self.t)
            nx = nx.transpose(-1,-2)
            y = self.avg_pool(nx).view(b, self.t)
            # 进行两次全连接fc，b, c -> b, c // ratio -> b, c
            # reshape：b, c -> b, c, 1, 1
            y = self.fc(y).view(b, self.t, 1)
            # 把两次全连接的结果×特征层
            y = F.interpolate(y.transpose(-1,-2), t)
            return (x * y)
        x = x.transpose(-1,-2)
        # 全局平均池化，结果为y（b, c, 1, 1），即去掉后面两个维度
        # view(b,c)：进行reshape，即只保留b, c
        y = self.avg_pool(x).view(b, t)
        # 进行两次全连接fc，b, c -> b, c // ratio -> b, c
        # reshape：b, c -> b, c, 1, 1
        y = self.fc(y).view(b, t, 1)
        # 把两次全连接的结果×特征层
        return (x * y).transpose(-1,-2)

@register_neck("fpn")
class FPN1D(nn.Module):
    """
        Feature pyramid network
    """
    def __init__(
        self,
        in_channels,      # input feature channels, len(in_channels) = # levels
        out_channel,      # output feature channel
        scale_factor=2.0, # downsampling rate between two fpn levels
        start_level=0,    # start fpn level
        end_level=-1,     # end fpn level
        with_ln=True,     # if to apply layer norm at the end
    ):
        super().__init__()
        assert isinstance(in_channels, list) or isinstance(in_channels, tuple)

        self.in_channels = in_channels
        self.out_channel = out_channel
        self.scale_factor = scale_factor

        self.start_level = start_level
        if end_level == -1:
            self.end_level = len(in_channels)
        else:
            self.end_level = end_level
        assert self.end_level <= len(in_channels)
        assert (self.start_level >= 0) and (self.start_level < self.end_level)

        self.lateral_convs = nn.ModuleList()
        self.fpn_convs = nn.ModuleList()
        self.fpn_norms = nn.ModuleList()
        for i in range(self.start_level, self.end_level):
            # disable bias if using layer norm
            l_conv = MaskedConv1D(
                in_channels[i], out_channel, 1, bias=(not with_ln)
            )
            # use depthwise conv here for efficiency
            fpn_conv = MaskedConv1D(
                out_channel, out_channel, 3,
                padding=1, bias=(not with_ln), groups=out_channel
            )
            # layer norm for order (B C T)
            if with_ln:
                fpn_norm = LayerNorm(out_channel)
            else:
                fpn_norm = nn.Identity()

            self.lateral_convs.append(l_conv)
            self.fpn_convs.append(fpn_conv)
            self.fpn_norms.append(fpn_norm)

    def forward(self, inputs, fpn_masks):
        # inputs must be a list / tuple
        assert len(inputs) == len(self.in_channels)
        assert len(fpn_masks) ==  len(self.in_channels)

        # build laterals, fpn_masks will remain the same with 1x1 convs
        laterals = []
        for i in range(len(self.lateral_convs)):
            x, _ = self.lateral_convs[i](
                inputs[i + self.start_level], fpn_masks[i + self.start_level]
            )
            laterals.append(x)

        # build top-down path
        used_backbone_levels = len(laterals)
        for i in range(used_backbone_levels - 1, 0, -1):
            laterals[i - 1] += F.interpolate(
                laterals[i], scale_factor=self.scale_factor, mode='nearest'
            )

        # fpn conv / norm -> outputs
        # mask will remain the same
        fpn_feats = tuple()
        new_fpn_masks = tuple()
        for i in range(used_backbone_levels):
            x, new_mask = self.fpn_convs[i](
                laterals[i], fpn_masks[i + self.start_level])
            x = self.fpn_norms[i](x)
            fpn_feats += (x, )
            new_fpn_masks += (new_mask, )

        return fpn_feats, new_fpn_masks


@register_neck('identity_ori')
class FPNIdentity(nn.Module):
    def __init__(
        self,
        in_channels,      # input feature channels, len(in_channels) = #levels
        out_channel,      # output feature channel
        scale_factor=2.0, # downsampling rate between two fpn levels
        start_level=0,    # start fpn level
        end_level=-1,     # end fpn level
        with_ln=True,     # if to apply layer norm at the end
    ):
        super().__init__()

        self.in_channels = in_channels
        self.out_channel = out_channel
        self.scale_factor = scale_factor

        self.start_level = start_level
        if end_level == -1:
            self.end_level = len(in_channels)
        else:
            self.end_level = end_level
        assert self.end_level <= len(in_channels)
        assert (self.start_level >= 0) and (self.start_level < self.end_level)

        self.fpn_norms = nn.ModuleList()
        for i in range(self.start_level, self.end_level):
            # check feat dims
            assert self.in_channels[i] == self.out_channel
            # layer norm for order (B C T)
            if with_ln:
                fpn_norm = LayerNorm(out_channel)
            else:
                fpn_norm = nn.Identity()
            self.fpn_norms.append(fpn_norm)

    def forward(self, inputs, fpn_masks):
        # inputs must be a list / tuple
        assert len(inputs) == len(self.in_channels)
        assert len(fpn_masks) ==  len(self.in_channels)

        # apply norms, fpn_masks will remain the same with 1x1 convs
        fpn_feats = tuple()
        new_fpn_masks = tuple()
        for i in range(len(self.fpn_norms)):
            x = self.fpn_norms[i](inputs[i + self.start_level])
            fpn_feats += (x, )
            new_fpn_masks += (fpn_masks[i + self.start_level], )

        return fpn_feats, new_fpn_masks

@register_neck('identity')
class FPNIdentity(nn.Module):
    def __init__(
        self,
        in_channels,      # input feature channels, len(in_channels) = #levels
        out_channel,      # output feature channel
        scale_factor=2.0, # downsampling rate between two fpn levels
        start_level=0,    # start fpn level
        end_level=-1,     # end fpn level
        with_ln=True,     # if to apply layer norm at the end
    ):
        super().__init__()

        self.in_channels = in_channels
        self.out_channel = out_channel
        self.scale_factor = scale_factor

        self.start_level = start_level
        if end_level == -1:
            self.end_level = len(in_channels)
        else:
            self.end_level = end_level
        assert self.end_level <= len(in_channels)
        assert (self.start_level >= 0) and (self.start_level < self.end_level)

        self.fpn_norms = nn.ModuleList()

        # todo syx seblock
        time = 2304
        self.seblocks = nn.ModuleList()

        for i in range(self.start_level, self.end_level):
            # check feat dims
            assert self.in_channels[i] == self.out_channel
            # layer norm for order (B C T)
            if with_ln:
                fpn_norm = LayerNorm(out_channel)
            else:
                fpn_norm = nn.Identity()
            self.fpn_norms.append(fpn_norm)
            self.seblocks.append(se_block(time))
            time //= 2

    def forward(self, inputs, fpn_masks):
        # inputs must be a list / tuple
        assert len(inputs) == len(self.in_channels)
        assert len(fpn_masks) ==  len(self.in_channels)

        # apply norms, fpn_masks will remain the same with 1x1 convs
        fpn_feats = tuple()
        new_fpn_masks = tuple()
        for i in range(len(self.fpn_norms)):
            # x = self.fpn_norms[i](inputs[i + self.start_level])
            # x = self.seblocks[i](x)
            x = self.seblocks[i](inputs[i + self.start_level])
            x = self.fpn_norms[i](x)

            fpn_feats += (x, )
            new_fpn_masks += (fpn_masks[i + self.start_level], )

        return fpn_feats, new_fpn_masks