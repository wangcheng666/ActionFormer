# ActionFormer: Localizing Moments of Actions with Transformers

## Introduction

we propose a novel fully supervised approach for temporal action localization, leveraging cross-modal and cross-structural distillation techniques.Our method effectively integrates information from multiple modalities and structural representations, enhancing the discriminative power of action proposals. We introduce a distillation framework that transfers knowledge from a strong teacher model, trained on rich multi-modal data, to a student model designed for efficient inference. This distillation process not only improves the temporal localization accuracy but also enhances the robustness of action detection against variations in visual content. Experimental results on benchmark datasets demonstrate that
our approach outperforms state-of-the-art methods, particularly in challenging scenarios where complex actions occur within dynamic backgrounds.


## Installation
* Follow INSTALL.md for installing necessary dependencies and compiling the code.



## To Reproduce Our Results on THUMOS14
**Download Features and Annotations**
* Download *thumos.zip* (`md5sum 375f76ffbf7447af1035e694971ec9b2`) from [this BaiduYun link](https://pan.baidu.com/s/11dw7LKO941CF02aSNCkPcA?pwd=hu2r).
* The file includes I3D features, action annotations in json format (similar to ActivityNet annotation format), and external classification scores.

**Details**: The features are extracted from two-stream I3D models pretrained on Kinetics using clips of `16 frames` at the video frame rate (`~30 fps`) and a stride of `4 frames`. This gives one feature vector per `4/30 ~= 0.1333` seconds.

**Unpack Features and Annotations**
* Unpack the file under *./data* (or elsewhere and link to *./data*).
* The folder structure should look like
```
This folder
│   README.md
│   ...  
│
└───data/
│    └───thumos/
│    │	 └───annotations
│    │	 └───i3d_features   
│    └───...
|
└───libs
│
│   ...
```

**Training and Evaluation**
* Train our ActionFormer with I3D features. This will create an experiment folder under *./ckpt* that stores training config, logs, and checkpoints.
```shell
python ./train.py ./configs/thumos_i3d.yaml --output reproduce
```
* [Optional] Monitor the training using TensorBoard
```shell
tensorboard --logdir=./ckpt/thumos_i3d_reproduce/logs
```
* Evaluate the trained model. The expected average mAP should be around 62.6(%) as in Table 1 of our main paper. **With recent commits, the expected average mAP should be higher than 66.0(%)**.
```shell
python ./eval.py ./configs/thumos_i3d.yaml ./ckpt/thumos_i3d_reproduce
```
* Training our model on THUMOS requires ~4.5GB GPU memory, yet the inference might require over 10GB GPU memory. We recommend using a GPU with at least 12 GB of memory.

**[Optional] Evaluating Our Pre-trained Model**

We also provide a pre-trained model for THUMOS 14. The model with all training logs can be downloaded from [this BaiduYun link](https://pan.baidu.com/s/1KsVWVQ6RF9mg87c0YUwH9Q?pwd=fknf). To evaluate the pre-trained model, please follow the steps listed below.

* Create a folder *./pretrained* and unpack the file under *./pretrained* (or elsewhere and link to *./pretrained*).
* The folder structure should look like
```
This folder
│   README.md
│   ...  
│
└───pretrained/
│    └───thumos_i3d_reproduce/
│    │	 └───thumos_reproduce_log.txt
│    │	 └───thumos_reproduce_results.txt
│    │   └───...    
│    └───...
|
└───libs
│
│   ...
```
* The training config is recorded in *./pretrained/thumos_i3d_reproduce/config.txt*.
* The training log is located at *./pretrained/thumos_i3d_reproduce/thumos_reproduce_log.txt* and also *./pretrained/thumos_i3d_reproduce/logs*.
* The pre-trained model is *./pretrained/thumos_i3d_reproduce/epoch_034.pth.tar*.
* Evaluate the pre-trained model.
```shell
python ./eval.py ./configs/thumos_i3d.yaml ./pretrained/thumos_i3d_reproduce/
```
## Citation
WangCheng. (2024). wangcheng666/ActionFormer: First release of ActionFormer (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.13897289



