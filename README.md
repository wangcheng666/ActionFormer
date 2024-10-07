# ActionFormer
Temporal Action Localization Enhanced through Cross-Modal and Cross-Structural Distillation
actionformer项目下的ckpt是模型权重，train和eval训练推理，data存着thumos数据集。
里面的readme里写着运行参数和方法，数据集里提供的是已经提取好的i3d特征，如果要自己提取特征，则需要另外两个文件。
视频级推理：
1.提取光流：这里环境我配不出来，直接用的docker，
sudo docker run -it --runtime=nvidia --gpus all bitxiong/tsn /bin/bash启动容器。
/home/wc/Desktop/SYX/tsn/videos下的txt存着之前的记录
bash scripts/extract_optical_flow.sh /app/videos/src /app/videos/out 1提取src文件夹下的视频。输出rgb图片和光流图到后者。
详细的参考可以看这个https://github.com/yjxiong/temporal-segment-networks，这个docker就是把项目给打包了。
2.rgb和光流提取i3d特征：pytorch-i3d-feature-extraction文件夹下，这里不需要训练，直接用预训练的模型提取特征就可以。

以上提到的4个项目，除了docker之外，都可以在pychram打开，可以在pycharm中看之前的打开记录。
