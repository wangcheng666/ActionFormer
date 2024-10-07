# ActionFormer: Localizing Moments of Actions with Transformers

## Introduction




## Installation
* Follow INSTALL.md for installing necessary dependencies and compiling the code.



## To Reproduce Our Results on THUMOS14
**Download Features and Annotations**
* Download *thumos.tar.gz* (`md5sum 375f76ffbf7447af1035e694971ec9b2`) from [this Box link](https://uwmadison.box.com/s/glpuxadymf3gd01m1cj6g5c3bn39qbgr) or [this Google Drive link](https://drive.google.com/file/d/1zt2eoldshf99vJMDuu8jqxda55dCyhZP/view?usp=sharing) or [this BaiduYun link](https://pan.baidu.com/s/1TgS91LVV-vzFTgIHl1AEGA?pwd=74eh).
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

We also provide a pre-trained model for THUMOS 14. The model with all training logs can be downloaded from [this Google Drive link](https://drive.google.com/file/d/1isG3bc1dG5-llBRFCivJwz_7c_b0XDcY/view?usp=sharing). To evaluate the pre-trained model, please follow the steps listed below.

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



