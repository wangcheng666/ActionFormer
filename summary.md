# origin reproduce [same with att]
total time:899.9387023448944
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 82.59 (%) Recall@1x = 84.45 (%) Recall@5x = 96.90 (%) 
|tIoU = 0.40: mAP = 78.20 (%) Recall@1x = 80.31 (%) Recall@5x = 95.34 (%) 
|tIoU = 0.50: mAP = 71.63 (%) Recall@1x = 74.62 (%) Recall@5x = 92.03 (%) 
|tIoU = 0.60: mAP = 58.59 (%) Recall@1x = 64.21 (%) Recall@5x = 84.02 (%) 
|tIoU = 0.70: mAP = 43.22 (%) Recall@1x = 52.75 (%) Recall@5x = 70.92 (%) 
Average mAP: 66.85 (%)
All done! Total time: 34.04 sec
FLOPs: 45.0302976 G
Params: 29.19631 M
rgb_to_flow:1.1920928955078125e-06
forward:0.5941576957702637
rgb_to_flow:7.152557373046875e-07
forward:0.027169466018676758
rgb_to_flow:9.5367431640625e-07
forward:0.027546405792236328
CPU
rgb_to_flow:7.152557373046875e-07
forward:0.41350603103637695
rgb_to_flow:1.430511474609375e-06
forward:0.2960958480834961
rgb_to_flow:9.5367431640625e-07
forward:0.2800760269165039


# reproduce_1024rgb
|tIoU = 0.30: mAP = 74.26 (%) Recall@1x = 78.45 (%) Recall@5x = 94.87 (%) 
|tIoU = 0.40: mAP = 69.09 (%) Recall@1x = 73.42 (%) Recall@5x = 91.75 (%) 
|tIoU = 0.50: mAP = 60.98 (%) Recall@1x = 66.44 (%) Recall@5x = 87.08 (%) 
|tIoU = 0.60: mAP = 48.70 (%) Recall@1x = 56.72 (%) Recall@5x = 77.84 (%) 
|tIoU = 0.70: mAP = 32.51 (%) Recall@1x = 43.31 (%) Recall@5x = 61.85 (%) 
Average mAP: 57.11 (%)
FLOPs: 41.406418944 G
Params: 27.623446 M
rgb_to_flow:3.337860107421875e-06
forward:0.5722289085388184
rgb_to_flow:7.152557373046875e-07
forward:0.02907252311706543
rgb_to_flow:7.152557373046875e-07
forward:0.051450490951538086

# improve only soft label
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 76.65 (%) Recall@1x = 80.29 (%) Recall@5x = 94.70 (%) 
|tIoU = 0.40: mAP = 71.82 (%) Recall@1x = 76.10 (%) Recall@5x = 92.66 (%) 
|tIoU = 0.50: mAP = 63.77 (%) Recall@1x = 69.57 (%) Recall@5x = 88.47 (%) 
|tIoU = 0.60: mAP = 51.08 (%) Recall@1x = 58.95 (%) Recall@5x = 78.99 (%) 
|tIoU = 0.70: mAP = 37.07 (%) Recall@1x = 46.40 (%) Recall@5x = 64.67 (%) 
Average mAP: 60.08 (%)
All done! Total time: 101.88 sec

# improve_soft_hard lambda_, T = 0.6, 3
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 76.93 (%) Recall@1x = 80.00 (%) Recall@5x = 94.77 (%) 
|tIoU = 0.40: mAP = 71.69 (%) Recall@1x = 75.31 (%) Recall@5x = 92.98 (%) 
|tIoU = 0.50: mAP = 63.72 (%) Recall@1x = 69.10 (%) Recall@5x = 88.76 (%) 
|tIoU = 0.60: mAP = 50.95 (%) Recall@1x = 59.08 (%) Recall@5x = 79.14 (%) 
|tIoU = 0.70: mAP = 37.12 (%) Recall@1x = 46.99 (%) Recall@5x = 65.34 (%) 
Average mAP: 60.08 (%)
All done! Total time: 96.87 sec

# improve_soft_hard lambda_, T = 0.6, 2
FLOPs: 59.525812224 G
Params: 35.489814 M
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 77.13 (%) Recall@1x = 80.60 (%) Recall@5x = 94.76 (%) 
|tIoU = 0.40: mAP = 71.47 (%) Recall@1x = 75.59 (%) Recall@5x = 92.83 (%) 
|tIoU = 0.50: mAP = 63.42 (%) Recall@1x = 69.21 (%) Recall@5x = 88.57 (%) 
|tIoU = 0.60: mAP = 50.91 (%) Recall@1x = 58.87 (%) Recall@5x = 78.60 (%) 
|tIoU = 0.70: mAP = 37.20 (%) Recall@1x = 47.30 (%) Recall@5x = 64.75 (%) 
Average mAP: 60.03 (%)
All done! Total time: 51.49 sec

# improve_sim (1,1,5)
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 80.82 (%) Recall@1x = 82.69 (%) Recall@5x = 96.13 (%) 
|tIoU = 0.40: mAP = 76.53 (%) Recall@1x = 79.13 (%) Recall@5x = 94.30 (%) 
|tIoU = 0.50: mAP = 69.02 (%) Recall@1x = 73.23 (%) Recall@5x = 91.43 (%) 
|tIoU = 0.60: mAP = 57.02 (%) Recall@1x = 63.61 (%) Recall@5x = 83.33 (%) 
|tIoU = 0.70: mAP = 41.40 (%) Recall@1x = 51.70 (%) Recall@5x = 68.85 (%) 
Average mAP: 64.96 (%)
All done! Total time: 28.27 sec

# improve_aud early_fusion
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 80.22 (%) Recall@1x = 83.22 (%) Recall@5x = 96.19 (%) 
|tIoU = 0.40: mAP = 76.35 (%) Recall@1x = 79.78 (%) Recall@5x = 94.89 (%) 
|tIoU = 0.50: mAP = 69.23 (%) Recall@1x = 74.15 (%) Recall@5x = 91.25 (%) 
|tIoU = 0.60: mAP = 55.73 (%) Recall@1x = 63.72 (%) Recall@5x = 83.77 (%) 
|tIoU = 0.70: mAP = 42.96 (%) Recall@1x = 52.84 (%) Recall@5x = 71.62 (%) 
Average mAP: 64.90 (%)
All done! Total time: 59.39 sec

# improve_aud_neck_fusion
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 77.46 (%) Recall@1x = 83.04 (%) Recall@5x = 96.14 (%) 
|tIoU = 0.40: mAP = 72.89 (%) Recall@1x = 78.77 (%) Recall@5x = 94.27 (%) 
|tIoU = 0.50: mAP = 65.55 (%) Recall@1x = 72.37 (%) Recall@5x = 90.89 (%) 
|tIoU = 0.60: mAP = 54.16 (%) Recall@1x = 62.88 (%) Recall@5x = 82.31 (%) 
|tIoU = 0.70: mAP = 39.83 (%) Recall@1x = 51.06 (%) Recall@5x = 68.38 (%) 
Average mAP: 61.98 (%)
All done! Total time: 62.24 sec

# improve_aud_rgb lambda_, T = 0.6, 2
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 74.69 (%) Recall@1x = 80.23 (%) Recall@5x = 94.43 (%) 
|tIoU = 0.40: mAP = 69.91 (%) Recall@1x = 75.33 (%) Recall@5x = 92.44 (%) 
|tIoU = 0.50: mAP = 62.32 (%) Recall@1x = 69.38 (%) Recall@5x = 87.15 (%) 
|tIoU = 0.60: mAP = 50.06 (%) Recall@1x = 59.13 (%) Recall@5x = 77.12 (%) 
|tIoU = 0.70: mAP = 36.77 (%) Recall@1x = 47.34 (%) Recall@5x = 63.75 (%) 
Average mAP: 58.75 (%)
All done! Total time: 61.59 sec

# improve_tem_att 時間注意力 比reproduce的avg高
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 82.18 (%) Recall@1x = 84.45 (%) Recall@5x = 96.32 (%) 
|tIoU = 0.40: mAP = 78.69 (%) Recall@1x = 80.69 (%) Recall@5x = 94.97 (%) 
|tIoU = 0.50: mAP = 70.87 (%) Recall@1x = 73.82 (%) Recall@5x = 91.73 (%) 
|tIoU = 0.60: mAP = 59.08 (%) Recall@1x = 64.81 (%) Recall@5x = 84.30 (%) 
|tIoU = 0.70: mAP = 45.30 (%) Recall@1x = 54.47 (%) Recall@5x = 70.99 (%) 
Average mAP: 67.23 (%)
All done! Total time: 85.43 sec
FLOPs: 45.034393608 G
Params: 30.96535 M
rgb_to_flow:1.6689300537109375e-06
forward:0.5887374877929688
rgb_to_flow:7.152557373046875e-07
forward:0.028340816497802734
rgb_to_flow:4.76837158203125e-07
forward:0.02995920181274414
CPU
rgb_to_flow:7.3909759521484375e-06
forward:0.39037656784057617
rgb_to_flow:1.1920928955078125e-06
forward:0.30884599685668945
rgb_to_flow:4.76837158203125e-07
forward:0.2749202251434326

# reproduce filter audio test
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 45.80 (%) Recall@1x = 46.75 (%) Recall@5x = 53.53 (%) 
|tIoU = 0.40: mAP = 43.45 (%) Recall@1x = 44.58 (%) Recall@5x = 52.34 (%) 
|tIoU = 0.50: mAP = 39.88 (%) Recall@1x = 41.66 (%) Recall@5x = 50.85 (%) 
|tIoU = 0.60: mAP = 31.68 (%) Recall@1x = 35.27 (%) Recall@5x = 45.63 (%) 
|tIoU = 0.70: mAP = 23.04 (%) Recall@1x = 28.50 (%) Recall@5x = 37.50 (%) 
Average mAP: 36.77 (%)
All done! Total time: 29.61 sec

Process finished with exit code 0

# aud_rgb filter audio
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 41.48 (%) Recall@1x = 43.85 (%) Recall@5x = 51.50 (%) 
|tIoU = 0.40: mAP = 39.05 (%) Recall@1x = 41.87 (%) Recall@5x = 50.28 (%) 
|tIoU = 0.50: mAP = 34.11 (%) Recall@1x = 37.92 (%) Recall@5x = 46.87 (%) 
|tIoU = 0.60: mAP = 27.26 (%) Recall@1x = 32.17 (%) Recall@5x = 41.42 (%) 
|tIoU = 0.70: mAP = 19.46 (%) Recall@1x = 25.15 (%) Recall@5x = 33.48 (%) 
Average mAP: 32.27 (%)
All done! Total time: 15.45 sec

Process finished with exit code 0

# soft_hard_T2
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 42.90 (%) Recall@1x = 44.69 (%) Recall@5x = 52.11 (%) 
|tIoU = 0.40: mAP = 39.81 (%) Recall@1x = 41.69 (%) Recall@5x = 50.99 (%) 
|tIoU = 0.50: mAP = 35.37 (%) Recall@1x = 37.99 (%) Recall@5x = 48.29 (%) 
|tIoU = 0.60: mAP = 27.72 (%) Recall@1x = 31.71 (%) Recall@5x = 42.27 (%) 
|tIoU = 0.70: mAP = 20.10 (%) Recall@1x = 24.98 (%) Recall@5x = 34.48 (%) 
Average mAP: 33.18 (%)
All done! Total time: 15.87 sec

# improve_reproduce_filter
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 43.86 (%) Recall@1x = 45.72 (%) Recall@5x = 52.72 (%) 
|tIoU = 0.40: mAP = 40.77 (%) Recall@1x = 42.81 (%) Recall@5x = 51.52 (%) 
|tIoU = 0.50: mAP = 35.75 (%) Recall@1x = 38.39 (%) Recall@5x = 49.06 (%) 
|tIoU = 0.60: mAP = 28.04 (%) Recall@1x = 32.49 (%) Recall@5x = 44.50 (%) 
|tIoU = 0.70: mAP = 17.92 (%) Recall@1x = 23.83 (%) Recall@5x = 34.68 (%) 
Average mAP: 33.27 (%)
All done! Total time: 75.65 sec

# improve_improve_early_fusion_filter
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 43.27 (%) Recall@1x = 45.85 (%) Recall@5x = 52.01 (%) 
|tIoU = 0.40: mAP = 40.06 (%) Recall@1x = 42.58 (%) Recall@5x = 50.79 (%) 
|tIoU = 0.50: mAP = 35.65 (%) Recall@1x = 38.55 (%) Recall@5x = 48.29 (%) 
|tIoU = 0.60: mAP = 27.55 (%) Recall@1x = 31.88 (%) Recall@5x = 43.74 (%) 
|tIoU = 0.70: mAP = 17.83 (%) Recall@1x = 24.15 (%) Recall@5x = 34.72 (%) 
Average mAP: 32.87 (%)
All done! Total time: 16.22 sec

# improve_reproduce_filter_rgb_T2
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 40.88 (%) Recall@1x = 43.14 (%) Recall@5x = 51.83 (%) 
|tIoU = 0.40: mAP = 38.32 (%) Recall@1x = 40.79 (%) Recall@5x = 50.29 (%) 
|tIoU = 0.50: mAP = 32.88 (%) Recall@1x = 36.15 (%) Recall@5x = 47.12 (%) 
|tIoU = 0.60: mAP = 25.41 (%) Recall@1x = 30.08 (%) Recall@5x = 42.47 (%) 
|tIoU = 0.70: mAP = 16.21 (%) Recall@1x = 22.57 (%) Recall@5x = 32.79 (%) 
Average mAP: 30.74 (%)
All done! Total time: 131.59 sec

# improve_improve_early_fusion_filter_rgb_T2
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 40.23 (%) Recall@1x = 43.86 (%) Recall@5x = 51.71 (%) 
|tIoU = 0.40: mAP = 37.13 (%) Recall@1x = 40.64 (%) Recall@5x = 50.08 (%) 
|tIoU = 0.50: mAP = 31.74 (%) Recall@1x = 35.92 (%) Recall@5x = 47.32 (%) 
|tIoU = 0.60: mAP = 24.33 (%) Recall@1x = 29.51 (%) Recall@5x = 41.73 (%) 
|tIoU = 0.70: mAP = 15.81 (%) Recall@1x = 22.54 (%) Recall@5x = 31.71 (%) 
Average mAP: 29.85 (%)
All done! Total time: 43.84 sec

# reproduce_conv
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 74.54 (%) Recall@1x = 81.86 (%) Recall@5x = 95.51 (%) 
|tIoU = 0.40: mAP = 69.97 (%) Recall@1x = 77.27 (%) Recall@5x = 93.34 (%) 
|tIoU = 0.50: mAP = 62.80 (%) Recall@1x = 70.90 (%) Recall@5x = 90.44 (%) 
|tIoU = 0.60: mAP = 51.45 (%) Recall@1x = 60.80 (%) Recall@5x = 81.47 (%) 
|tIoU = 0.70: mAP = 36.75 (%) Recall@1x = 47.74 (%) Recall@5x = 65.49 (%) 
Average mAP: 59.10 (%)
All done! Total time: 35.84 sec

# improve_conv_T2
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 70.45 (%) Recall@1x = 77.03 (%) Recall@5x = 94.18 (%) 
|tIoU = 0.40: mAP = 65.42 (%) Recall@1x = 72.48 (%) Recall@5x = 91.41 (%) 
|tIoU = 0.50: mAP = 57.06 (%) Recall@1x = 65.10 (%) Recall@5x = 86.17 (%) 
|tIoU = 0.60: mAP = 46.34 (%) Recall@1x = 56.17 (%) Recall@5x = 75.30 (%) 
|tIoU = 0.70: mAP = 34.17 (%) Recall@1x = 45.64 (%) Recall@5x = 61.29 (%) 
Average mAP: 54.69 (%)
All done! Total time: 42.37 sec

# reproduce_local2cnn 添加了時間注意力
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 74.62 (%) Recall@1x = 80.85 (%) Recall@5x = 95.36 (%) 
|tIoU = 0.40: mAP = 70.02 (%) Recall@1x = 76.26 (%) Recall@5x = 93.32 (%) 
|tIoU = 0.50: mAP = 62.38 (%) Recall@1x = 69.74 (%) Recall@5x = 88.67 (%) 
|tIoU = 0.60: mAP = 51.20 (%) Recall@1x = 60.35 (%) Recall@5x = 80.30 (%) 
|tIoU = 0.70: mAP = 36.46 (%) Recall@1x = 48.66 (%) Recall@5x = 66.28 (%) 
Average mAP: 58.94 (%)
All done! Total time: 51.44 sec

# reproduce_local2cnn_tem_then_ln
total time:609.435836315155
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 74.12 (%) Recall@1x = 80.91 (%) Recall@5x = 95.55 (%) 
|tIoU = 0.40: mAP = 69.56 (%) Recall@1x = 76.42 (%) Recall@5x = 92.87 (%) 
|tIoU = 0.50: mAP = 61.68 (%) Recall@1x = 69.93 (%) Recall@5x = 89.11 (%) 
|tIoU = 0.60: mAP = 50.97 (%) Recall@1x = 60.45 (%) Recall@5x = 80.71 (%) 
|tIoU = 0.70: mAP = 35.15 (%) Recall@1x = 47.05 (%) Recall@5x = 64.33 (%) 
Average mAP: 58.29 (%)
All done! Total time: 52.59 sec

Process finished with exit code 0

# improve_tf_to_cnn T=2
total time:1201.3697128295898
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 79.17 (%) Recall@1x = 82.18 (%) Recall@5x = 95.96 (%) 
|tIoU = 0.40: mAP = 74.93 (%) Recall@1x = 78.22 (%) Recall@5x = 94.12 (%) 
|tIoU = 0.50: mAP = 67.85 (%) Recall@1x = 72.03 (%) Recall@5x = 90.49 (%) 
|tIoU = 0.60: mAP = 55.47 (%) Recall@1x = 62.43 (%) Recall@5x = 82.43 (%) 
|tIoU = 0.70: mAP = 41.31 (%) Recall@1x = 51.12 (%) Recall@5x = 68.06 (%) 
Average mAP: 63.74 (%)
All done! Total time: 52.63 sec

Process finished with exit code 0

# improve_i3dtf_2_rgbcnn T=2
total time:1258.3733162879944
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 49.23 (%) Recall@1x = 55.78 (%) Recall@5x = 86.11 (%) 
|tIoU = 0.40: mAP = 34.11 (%) Recall@1x = 42.37 (%) Recall@5x = 76.64 (%) 
|tIoU = 0.50: mAP = 15.97 (%) Recall@1x = 25.29 (%) Recall@5x = 60.25 (%) 
|tIoU = 0.60: mAP = 6.22 (%) Recall@1x = 13.93 (%) Recall@5x = 40.96 (%) 
|tIoU = 0.70: mAP = 2.19 (%) Recall@1x = 6.45 (%) Recall@5x = 24.75 (%) 
Average mAP: 21.54 (%)
All done! Total time: 56.44 sec3

# improve_ft2cnn_to_rgb T=2
total time:934.3903908729553
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 74.21 (%) Recall@1x = 78.61 (%) Recall@5x = 94.39 (%) 
|tIoU = 0.40: mAP = 69.32 (%) Recall@1x = 73.91 (%) Recall@5x = 92.23 (%) 
|tIoU = 0.50: mAP = 61.45 (%) Recall@1x = 67.35 (%) Recall@5x = 86.62 (%) 
|tIoU = 0.60: mAP = 49.70 (%) Recall@1x = 57.63 (%) Recall@5x = 77.33 (%) 
|tIoU = 0.70: mAP = 36.81 (%) Recall@1x = 45.86 (%) Recall@5x = 62.21 (%) 
Average mAP: 58.30 (%)
All done! Total time: 44.33 sec

# improve_2_teacher T=2 average map更高 cnn_reproduce的参数参考这个
total time:1870.3074567317963
FLOPs: 60.079398912 G
Params: 36.749334 M
[modal_time] 0.11, [structure_time] 0.05, [main_time] 0.05
[modal_time] reproduce, [structure_time] tf_to_cnn, [main_time] student
Epoch: [000][00010/00100]	Time 0.02 (0.02)	Loss 3.07 (3.07)
		cls_loss 2.42 (2.42)	reg_loss 0.65 (0.65)	i3d_loss 0.09 (0.09)	bound_loss 0.51 (0.51)	logits_loss 0.26 (0.26)	soft_loss 0.95 (0.95)	total_loss 3.51 (3.51)	forward_time: [modal_time] 0.11, [structure_time] 0.05, [main_time] 0.05

Epoch: [000][00020/00100]	Time 0.02 (0.02)	Loss 2.08 (2.57)
		cls_loss 1.66 (2.04)	reg_loss 0.42 (0.54)	i3d_loss 0.14 (0.12)	bound_loss 0.49 (0.50)	logits_loss 0.36 (0.31)	soft_loss 1.13 (1.04)	total_loss 3.54 (3.53)	forward_time: [modal_time] 0.11, [structure_time] 0.06, [main_time] 0.06

Epoch: [000][00030/00100]	Time 0.02 (0.02)	Loss 3.63 (2.93)
		cls_loss 3.13 (2.40)	reg_loss 0.50 (0.53)	i3d_loss 0.07 (0.10)	bound_loss 0.27 (0.42)	logits_loss 0.25 (0.29)	soft_loss 0.67 (0.92)	total_loss 3.06 (3.37)	forward_time: [modal_time] 0.09, [structure_time] 0.05, [main_time] 0.05

Epoch: [000][00040/00100]	Time 0.02 (0.02)	Loss 0.58 (2.34)
		cls_loss 0.44 (1.91)	reg_loss 0.14 (0.43)	i3d_loss 0.04 (0.09)	bound_loss 0.19 (0.36)	logits_loss 0.16 (0.26)	soft_loss 0.45 (0.80)	total_loss 1.31 (2.86)	forward_time: [modal_time] 0.11, [structure_time] 0.05, [main_time] 0.05

[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 74.37 (%) Recall@1x = 79.14 (%) Recall@5x = 94.79 (%) 
|tIoU = 0.40: mAP = 69.94 (%) Recall@1x = 74.93 (%) Recall@5x = 92.40 (%) 
|tIoU = 0.50: mAP = 60.64 (%) Recall@1x = 67.29 (%) Recall@5x = 87.26 (%) 
|tIoU = 0.60: mAP = 50.05 (%) Recall@1x = 59.21 (%) Recall@5x = 78.04 (%) 
|tIoU = 0.70: mAP = 37.47 (%) Recall@1x = 47.64 (%) Recall@5x = 64.08 (%) 
Average mAP: 58.50 (%)
All done! Total time: 24.35 sec

Process finished with exit code 0

# improve_tfrgb_to_cnnrgb
total time:1236.594621181488
FLOPs: 60.079398912 G
Params: 36.749334 M
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 72.20 (%) Recall@1x = 78.07 (%) Recall@5x = 94.07 (%) 
|tIoU = 0.40: mAP = 66.95 (%) Recall@1x = 73.54 (%) Recall@5x = 91.38 (%) 
|tIoU = 0.50: mAP = 59.01 (%) Recall@1x = 66.40 (%) Recall@5x = 87.54 (%) 
|tIoU = 0.60: mAP = 47.23 (%) Recall@1x = 56.45 (%) Recall@5x = 77.79 (%) 
|tIoU = 0.70: mAP = 33.01 (%) Recall@1x = 43.82 (%) Recall@5x = 60.80 (%) 
Average mAP: 55.68 (%)
All done! Total time: 44.82 sec

# improve_gate_fusion tf flops不准确
total time:2187.873645544052
FLOPs: 49.8668544 G
Params: 30.246934 M
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 79.68 (%) Recall@1x = 83.07 (%) Recall@5x = 96.18 (%) 
|tIoU = 0.40: mAP = 75.78 (%) Recall@1x = 79.72 (%) Recall@5x = 94.32 (%) 
|tIoU = 0.50: mAP = 68.38 (%) Recall@1x = 74.13 (%) Recall@5x = 91.02 (%) 
|tIoU = 0.60: mAP = 56.74 (%) Recall@1x = 64.63 (%) Recall@5x = 83.50 (%) 
|tIoU = 0.70: mAP = 42.43 (%) Recall@1x = 52.77 (%) Recall@5x = 69.77 (%) 
Average mAP: 64.60 (%)
All done! Total time: 59.93 sec

# improve_gate_fusion_cnn 比纯cnn高
total time:797.6037912368774
FLOPs: 50.420441088 G
Params: 31.506454 M
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 75.79 (%) Recall@1x = 80.85 (%) Recall@5x = 95.26 (%) 
|tIoU = 0.40: mAP = 71.55 (%) Recall@1x = 77.21 (%) Recall@5x = 93.18 (%) 
|tIoU = 0.50: mAP = 64.89 (%) Recall@1x = 71.12 (%) Recall@5x = 89.26 (%) 
|tIoU = 0.60: mAP = 53.26 (%) Recall@1x = 61.47 (%) Recall@5x = 80.66 (%) 
|tIoU = 0.70: mAP = 39.94 (%) Recall@1x = 50.07 (%) Recall@5x = 67.30 (%) 
Average mAP: 61.09 (%)
All done! Total time: 62.52 sec

# improve_dw_cnn 三个程序在跑 瓶颈在io，可以考虑不要动分类头的conv
total time:1145.0862154960632
FLOPs: 15.676858368 G
Params: 11.103766 M
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 71.31 (%) Recall@1x = 80.16 (%) Recall@5x = 94.45 (%) 
|tIoU = 0.40: mAP = 65.49 (%) Recall@1x = 75.31 (%) Recall@5x = 91.65 (%) 
|tIoU = 0.50: mAP = 57.68 (%) Recall@1x = 68.50 (%) Recall@5x = 86.58 (%) 
|tIoU = 0.60: mAP = 47.32 (%) Recall@1x = 59.82 (%) Recall@5x = 76.93 (%) 
|tIoU = 0.70: mAP = 34.63 (%) Recall@1x = 48.09 (%) Recall@5x = 63.73 (%) 
Average mAP: 55.29 (%)
All done! Total time: 293.30 sec

# improve_conv_gate_fusion_cnn
total time:1367.1020293235779
FLOPs: 60.084117504 G
Params: 33.603606 M
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 74.19 (%) Recall@1x = 80.23 (%) Recall@5x = 95.35 (%) 
|tIoU = 0.40: mAP = 69.88 (%) Recall@1x = 76.33 (%) Recall@5x = 93.47 (%) 
|tIoU = 0.50: mAP = 62.35 (%) Recall@1x = 69.33 (%) Recall@5x = 89.33 (%) 
|tIoU = 0.60: mAP = 51.61 (%) Recall@1x = 60.75 (%) Recall@5x = 80.69 (%) 
|tIoU = 0.70: mAP = 36.69 (%) Recall@1x = 48.27 (%) Recall@5x = 65.36 (%) 
Average mAP: 58.95 (%)
All done! Total time: 53.03 sec

# improve_dw_cnn_ori_head (两个head最后一层不是dw)
total time:828.9209566116333
FLOPs: 15.765110784 G
Params: 11.122198 M
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 73.17 (%) Recall@1x = 79.91 (%) Recall@5x = 95.14 (%) 
|tIoU = 0.40: mAP = 68.37 (%) Recall@1x = 75.58 (%) Recall@5x = 92.02 (%) 
|tIoU = 0.50: mAP = 62.15 (%) Recall@1x = 70.15 (%) Recall@5x = 87.93 (%) 
|tIoU = 0.60: mAP = 50.88 (%) Recall@1x = 60.08 (%) Recall@5x = 79.11 (%) 
|tIoU = 0.70: mAP = 36.68 (%) Recall@1x = 47.28 (%) Recall@5x = 64.32 (%) 
Average mAP: 58.25 (%)
All done! Total time: 49.44 sec

# improve_FC_gate_dw_cnn_ori_head
total time:647.2323970794678
FLOPs: 20.601667584 G
Params: 12.172822 M
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 74.24 (%) Recall@1x = 80.80 (%) Recall@5x = 95.52 (%) 
|tIoU = 0.40: mAP = 69.39 (%) Recall@1x = 76.44 (%) Recall@5x = 93.07 (%) 
|tIoU = 0.50: mAP = 61.59 (%) Recall@1x = 69.45 (%) Recall@5x = 88.85 (%) 
|tIoU = 0.60: mAP = 51.17 (%) Recall@1x = 60.34 (%) Recall@5x = 80.26 (%) 
|tIoU = 0.70: mAP = 36.65 (%) Recall@1x = 48.53 (%) Recall@5x = 66.85 (%) 
Average mAP: 58.61 (%)
All done! Total time: 40.03 sec

# improve_FC_gate_dw_cnn_ori_head_neck_tem_attn
total time:717.0151371955872
FLOPs: 20.605763592 G
Params: 13.941862 M
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 74.10 (%) Recall@1x = 80.25 (%) Recall@5x = 94.71 (%) 
|tIoU = 0.40: mAP = 70.21 (%) Recall@1x = 76.65 (%) Recall@5x = 92.38 (%) 
|tIoU = 0.50: mAP = 62.13 (%) Recall@1x = 69.88 (%) Recall@5x = 88.42 (%) 
|tIoU = 0.60: mAP = 50.99 (%) Recall@1x = 61.12 (%) Recall@5x = 80.00 (%) 
|tIoU = 0.70: mAP = 36.29 (%) Recall@1x = 48.60 (%) Recall@5x = 65.40 (%) 
Average mAP: 58.74 (%)
All done! Total time: 44.75 sec

# improve_tf_dw_tem_att tf只有neck的tem_att有用，dw和gate_fusion没用
total time:2279.2664682865143
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 77.37 (%) Recall@1x = 81.51 (%) Recall@5x = 96.14 (%) 
|tIoU = 0.40: mAP = 73.98 (%) Recall@1x = 77.98 (%) Recall@5x = 94.50 (%) 
|tIoU = 0.50: mAP = 65.95 (%) Recall@1x = 71.53 (%) Recall@5x = 89.99 (%) 
|tIoU = 0.60: mAP = 53.40 (%) Recall@1x = 61.82 (%) Recall@5x = 81.57 (%) 
|tIoU = 0.70: mAP = 38.87 (%) Recall@1x = 49.37 (%) Recall@5x = 66.99 (%) 
Average mAP: 61.91 (%)
All done! Total time: 51.11 sec

# improve_tf_tem_att_2_FC_gate_dw_cnn_ori_head_neck_tem_attn_T2
total time:2400.9896194934845
FLOPs: 20.605763592 G
Params: 13.941862 M
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 77.50 (%) Recall@1x = 81.42 (%) Recall@5x = 96.04 (%) 
|tIoU = 0.40: mAP = 73.29 (%) Recall@1x = 77.22 (%) Recall@5x = 94.04 (%) 
|tIoU = 0.50: mAP = 65.63 (%) Recall@1x = 70.40 (%) Recall@5x = 90.18 (%) 
|tIoU = 0.60: mAP = 53.87 (%) Recall@1x = 61.28 (%) Recall@5x = 81.52 (%) 
|tIoU = 0.70: mAP = 40.06 (%) Recall@1x = 50.46 (%) Recall@5x = 68.08 (%) 
Average mAP: 62.07 (%)
All done! Total time: 85.96 sec

# improve_2_teacher_gate_dw_tematt
Epoch: [027][00090/00100]	Time 0.03 (0.03)	Loss 0.08 (0.22)
forward_time: [modal_time] 0.29, [structure_time] 0.18, [main_time] 0.20
total time:3566.8119690418243
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 70.86 (%) Recall@1x = 77.68 (%) Recall@5x = 92.55 (%) 
|tIoU = 0.40: mAP = 66.16 (%) Recall@1x = 73.09 (%) Recall@5x = 90.37 (%) 
|tIoU = 0.50: mAP = 57.95 (%) Recall@1x = 65.58 (%) Recall@5x = 85.12 (%) 
|tIoU = 0.60: mAP = 46.74 (%) Recall@1x = 56.14 (%) Recall@5x = 75.16 (%) 
|tIoU = 0.70: mAP = 34.70 (%) Recall@1x = 45.56 (%) Recall@5x = 61.19 (%) 
Average mAP: 55.28 (%)
All done! Total time: 200.86 sec

# thumos_i3d_improve_tf_tem_att_2_FC_gate_dw_cnn_ori_head_neck_tem_attn_T2_no_feat_loss
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 77.83 (%) Recall@1x = 81.79 (%) Recall@5x = 96.41 (%) 
|tIoU = 0.40: mAP = 74.13 (%) Recall@1x = 78.02 (%) Recall@5x = 94.58 (%) 
|tIoU = 0.50: mAP = 66.53 (%) Recall@1x = 71.46 (%) Recall@5x = 90.82 (%) 
|tIoU = 0.60: mAP = 55.39 (%) Recall@1x = 62.58 (%) Recall@5x = 82.47 (%) 
|tIoU = 0.70: mAP = 41.49 (%) Recall@1x = 51.52 (%) Recall@5x = 69.17 (%) 
Average mAP: 63.07 (%)
All done! Total time: 43.65 sec

# try sb 28 nosave
total time:1731.3898136615753
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 69.82 (%) Recall@1x = 76.03 (%) Recall@5x = 93.37 (%) 
|tIoU = 0.40: mAP = 65.18 (%) Recall@1x = 71.43 (%) Recall@5x = 90.55 (%) 
|tIoU = 0.50: mAP = 56.87 (%) Recall@1x = 64.23 (%) Recall@5x = 85.85 (%) 
|tIoU = 0.60: mAP = 46.61 (%) Recall@1x = 55.84 (%) Recall@5x = 76.07 (%) 
|tIoU = 0.70: mAP = 34.50 (%) Recall@1x = 44.91 (%) Recall@5x = 61.49 (%) 
Average mAP: 54.60 (%)
All done! Total time: 86.37 sec

# try_2 sb 37
total time:1833.9154522418976
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 71.23 (%) Recall@1x = 77.29 (%) Recall@5x = 93.76 (%) 
|tIoU = 0.40: mAP = 66.71 (%) Recall@1x = 72.72 (%) Recall@5x = 91.17 (%) 
|tIoU = 0.50: mAP = 58.60 (%) Recall@1x = 65.84 (%) Recall@5x = 86.30 (%) 
|tIoU = 0.60: mAP = 47.50 (%) Recall@1x = 56.70 (%) Recall@5x = 76.19 (%) 
|tIoU = 0.70: mAP = 35.15 (%) Recall@1x = 45.50 (%) Recall@5x = 61.59 (%) 
Average mAP: 55.84 (%)

# try sb 28 no stem
total time:1058.0494892597198
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 69.82 (%) Recall@1x = 76.03 (%) Recall@5x = 93.37 (%) 
|tIoU = 0.40: mAP = 65.18 (%) Recall@1x = 71.43 (%) Recall@5x = 90.55 (%) 
|tIoU = 0.50: mAP = 56.87 (%) Recall@1x = 64.23 (%) Recall@5x = 85.85 (%) 
|tIoU = 0.60: mAP = 46.61 (%) Recall@1x = 55.84 (%) Recall@5x = 76.07 (%) 
|tIoU = 0.70: mAP = 34.50 (%) Recall@1x = 44.91 (%) Recall@5x = 61.49 (%) 
Average mAP: 54.60 (%)
All done! Total time: 79.24 sec

# try_2 sb 55
total time:1047.922259092331
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 70.51 (%) Recall@1x = 77.25 (%) Recall@5x = 94.01 (%) 
|tIoU = 0.40: mAP = 66.32 (%) Recall@1x = 73.18 (%) Recall@5x = 91.77 (%) 
|tIoU = 0.50: mAP = 58.39 (%) Recall@1x = 65.87 (%) Recall@5x = 86.87 (%) 
|tIoU = 0.60: mAP = 47.26 (%) Recall@1x = 56.86 (%) Recall@5x = 76.75 (%) 
|tIoU = 0.70: mAP = 34.53 (%) Recall@1x = 46.41 (%) Recall@5x = 62.86 (%) 
Average mAP: 55.40 (%)
All done! Total time: 76.95 sec

# try sb 37 fpnfeats
total time:2280.3694932460785
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 70.45 (%) Recall@1x = 76.44 (%) Recall@5x = 93.23 (%) 
|tIoU = 0.40: mAP = 65.71 (%) Recall@1x = 71.75 (%) Recall@5x = 90.61 (%) 
|tIoU = 0.50: mAP = 57.74 (%) Recall@1x = 65.08 (%) Recall@5x = 85.62 (%) 
|tIoU = 0.60: mAP = 45.66 (%) Recall@1x = 55.39 (%) Recall@5x = 75.87 (%) 
|tIoU = 0.70: mAP = 32.91 (%) Recall@1x = 44.19 (%) Recall@5x = 60.53 (%) 
Average mAP: 54.49 (%)
All done! Total time: 87.64 sec

# sb 37 dyn
total time:2698.6899542808533
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 70.51 (%) Recall@1x = 77.25 (%) Recall@5x = 93.89 (%) 
|tIoU = 0.40: mAP = 66.18 (%) Recall@1x = 72.98 (%) Recall@5x = 91.15 (%) 
|tIoU = 0.50: mAP = 58.55 (%) Recall@1x = 66.34 (%) Recall@5x = 86.18 (%) 
|tIoU = 0.60: mAP = 46.98 (%) Recall@1x = 56.48 (%) Recall@5x = 76.03 (%) 
|tIoU = 0.70: mAP = 35.05 (%) Recall@1x = 45.70 (%) Recall@5x = 61.02 (%) 
Average mAP: 55.46 (%)
All done! Total time: 51.85 sec

# ---------------------------- 使用之前的方法， tf tem att 蒸馏 cnn tem att， 共同蒸馏rgb cnn tem att， 最后
简化蒸馏rgb dw

# improve_tem_att_tf2cnn
total time:2317.643242120743
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 78.85 (%) Recall@1x = 82.09 (%) Recall@5x = 96.25 (%) 
|tIoU = 0.40: mAP = 74.65 (%) Recall@1x = 78.08 (%) Recall@5x = 94.66 (%) 
|tIoU = 0.50: mAP = 66.62 (%) Recall@1x = 70.83 (%) Recall@5x = 90.62 (%) 
|tIoU = 0.60: mAP = 54.40 (%) Recall@1x = 61.34 (%) Recall@5x = 82.39 (%) 
|tIoU = 0.70: mAP = 39.48 (%) Recall@1x = 50.15 (%) Recall@5x = 68.02 (%) 
Average mAP: 62.80 (%)
All done! Total time: 106.52 sec

# improve_tem_att_tf2cnn_no_feat
FLOPs: 45.587980296 G
Params: 32.22487 M
total time:2283.759346485138
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 78.98 (%) Recall@1x = 82.13 (%) Recall@5x = 96.28 (%) 
|tIoU = 0.40: mAP = 75.47 (%) Recall@1x = 78.42 (%) Recall@5x = 94.59 (%) 
|tIoU = 0.50: mAP = 68.48 (%) Recall@1x = 72.25 (%) Recall@5x = 90.91 (%) 
|tIoU = 0.60: mAP = 56.42 (%) Recall@1x = 62.76 (%) Recall@5x = 83.44 (%) 
|tIoU = 0.70: mAP = 41.22 (%) Recall@1x = 51.29 (%) Recall@5x = 68.58 (%) 
Average mAP: 64.11 (%)
All done! Total time: 54.59 sec
rgb_to_flow:9.5367431640625e-07
forward:0.5999791622161865
rgb_to_flow:4.76837158203125e-07
forward:0.01507711410522461
rgb_to_flow:4.76837158203125e-07
forward:0.015178918838500977
CPU
rgb_to_flow:3.0994415283203125e-06
forward:0.2951984405517578
rgb_to_flow:7.152557373046875e-07
forward:0.21334576606750488
rgb_to_flow:9.5367431640625e-07
forward:0.18990492820739746
rgb_to_flow:7.152557373046875e-07

# improve_2_teacher_temtf_temcnn_nofeat dyn
Epoch: [019][00020/00100]	Time 0.03 (0.03)	Loss 0.17 (0.16)
		cls_loss 0.10 (0.09)	reg_loss 0.07 (0.07)	i3d_loss 0.02 (0.03)	bound_loss 0.03 (0.03)	logits_loss 0.04 (0.05)	soft_loss 0.13 (0.14)	total_loss 0.38 (0.41)	forward_time: [modal_time] 0.15, [structure_time] 0.07, [main_time] 0.08
total time:1923.4216668605804
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 73.53 (%) Recall@1x = 78.55 (%) Recall@5x = 94.05 (%) 
|tIoU = 0.40: mAP = 68.64 (%) Recall@1x = 74.14 (%) Recall@5x = 91.37 (%) 
|tIoU = 0.50: mAP = 61.09 (%) Recall@1x = 67.71 (%) Recall@5x = 86.34 (%) 
|tIoU = 0.60: mAP = 49.42 (%) Recall@1x = 57.88 (%) Recall@5x = 76.93 (%) 
|tIoU = 0.70: mAP = 37.63 (%) Recall@1x = 47.69 (%) Recall@5x = 63.90 (%) 
Average mAP: 58.06 (%)
All done! Total time: 42.52 sec

# improve_tem_att_tf2cnn_no_feat_to_rgb
total time:1454.803112745285
FLOPs: 60.08349492 G
Params: 38.518374 M
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 74.29 (%) Recall@1x = 79.01 (%) Recall@5x = 94.59 (%) 
|tIoU = 0.40: mAP = 69.83 (%) Recall@1x = 74.69 (%) Recall@5x = 92.52 (%) 
|tIoU = 0.50: mAP = 61.73 (%) Recall@1x = 67.99 (%) Recall@5x = 87.89 (%) 
|tIoU = 0.60: mAP = 50.21 (%) Recall@1x = 58.59 (%) Recall@5x = 78.73 (%) 
|tIoU = 0.70: mAP = 37.70 (%) Recall@1x = 47.71 (%) Recall@5x = 64.02 (%) 
Average mAP: 58.75 (%)
All done! Total time: 25.88 sec
rgb_to_flow:0.5639700889587402
forward:0.5816080570220947
rgb_to_flow:0.0004260540008544922
forward:0.01683497428894043
rgb_to_flow:0.0005383491516113281
forward:0.015247821807861328
CPU
rgb_to_flow:0.07521557807922363
forward:0.3463923931121826
rgb_to_flow:0.0642998218536377
forward:0.26557040214538574
rgb_to_flow:0.05348515510559082
forward:0.2190089225769043

# improve_2_teacher_temtf_temcnn_nofeat_try 28
total time:1790.4601180553436
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 73.50 (%) Recall@1x = 78.22 (%) Recall@5x = 93.12 (%) 
|tIoU = 0.40: mAP = 68.93 (%) Recall@1x = 74.04 (%) Recall@5x = 90.97 (%) 
|tIoU = 0.50: mAP = 61.11 (%) Recall@1x = 67.69 (%) Recall@5x = 86.71 (%) 
|tIoU = 0.60: mAP = 49.75 (%) Recall@1x = 58.33 (%) Recall@5x = 77.38 (%) 
|tIoU = 0.70: mAP = 37.02 (%) Recall@1x = 47.64 (%) Recall@5x = 62.72 (%) 
Average mAP: 58.06 (%)
All done! Total time: 49.14 sec

# improve_tem_att_tf2cnn_no_feat_to_rgb_dw
FLOPs: 30.264721416 G
Params: 19.184742 M
total time:1237.1541502475739

[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 71.15 (%) Recall@1x = 76.88 (%) Recall@5x = 94.35 (%) 
|tIoU = 0.40: mAP = 66.63 (%) Recall@1x = 71.85 (%) Recall@5x = 92.27 (%) 
|tIoU = 0.50: mAP = 58.97 (%) Recall@1x = 65.17 (%) Recall@5x = 87.20 (%) 
|tIoU = 0.60: mAP = 46.97 (%) Recall@1x = 55.15 (%) Recall@5x = 76.11 (%) 
|tIoU = 0.70: mAP = 34.41 (%) Recall@1x = 44.90 (%) Recall@5x = 61.93 (%) 
Average mAP: 55.63 (%)
All done! Total time: 108.70 sec

# improve_tem_att_tf2cnn_no_feat_to_rgb_dw_2_teacher
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 71.08 (%) Recall@1x = 76.01 (%) Recall@5x = 92.05 (%) 
|tIoU = 0.40: mAP = 66.90 (%) Recall@1x = 72.17 (%) Recall@5x = 90.29 (%) 
|tIoU = 0.50: mAP = 58.35 (%) Recall@1x = 64.52 (%) Recall@5x = 85.40 (%) 
|tIoU = 0.60: mAP = 45.77 (%) Recall@1x = 54.08 (%) Recall@5x = 74.02 (%) 
|tIoU = 0.70: mAP = 32.41 (%) Recall@1x = 43.02 (%) Recall@5x = 57.95 (%) 
Average mAP: 54.90 (%)
All done! Total time: 23.20 sec

# improve_tf_tem_att_2_FC_gate_dw_cnn_ori_head_neck_tem_attn_T2_no_feat_loss_to_rgb
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 70.53 (%) Recall@1x = 76.34 (%) Recall@5x = 93.80 (%) 
|tIoU = 0.40: mAP = 65.94 (%) Recall@1x = 71.78 (%) Recall@5x = 91.11 (%) 
|tIoU = 0.50: mAP = 58.06 (%) Recall@1x = 64.52 (%) Recall@5x = 86.79 (%) 
|tIoU = 0.60: mAP = 46.27 (%) Recall@1x = 54.76 (%) Recall@5x = 76.16 (%) 
|tIoU = 0.70: mAP = 32.29 (%) Recall@1x = 42.63 (%) Recall@5x = 59.83 (%) 
Average mAP: 54.62 (%)
All done! Total time: 58.80 sec

# try1 improve_tem_att_tf2cnn_no_feat_to_rgb_dw_try1 删除了boundloss/3 improve_tem_att_tf2cnn_no_feat_to_rgb_dw_try1_feat_nostem
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 71.00 (%) Recall@1x = 77.24 (%) Recall@5x = 93.95 (%) 
|tIoU = 0.40: mAP = 66.42 (%) Recall@1x = 72.55 (%) Recall@5x = 91.17 (%) 
|tIoU = 0.50: mAP = 58.92 (%) Recall@1x = 65.63 (%) Recall@5x = 85.60 (%) 
|tIoU = 0.60: mAP = 47.69 (%) Recall@1x = 55.89 (%) Recall@5x = 77.05 (%) 
|tIoU = 0.70: mAP = 34.50 (%) Recall@1x = 44.61 (%) Recall@5x = 61.22 (%) 
Average mAP: 55.70 (%)
All done! Total time: 102.28 sec

# try2 1+stemloss improve_tem_att_tf2cnn_no_feat_to_rgb_dw_try1_feat_stem
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 70.28 (%) Recall@1x = 77.63 (%) Recall@5x = 94.08 (%) 
|tIoU = 0.40: mAP = 66.02 (%) Recall@1x = 72.94 (%) Recall@5x = 91.77 (%) 
|tIoU = 0.50: mAP = 58.39 (%) Recall@1x = 66.14 (%) Recall@5x = 86.39 (%) 
|tIoU = 0.60: mAP = 47.59 (%) Recall@1x = 56.91 (%) Recall@5x = 77.15 (%) 
|tIoU = 0.70: mAP = 34.14 (%) Recall@1x = 45.33 (%) Recall@5x = 61.39 (%) 
Average mAP: 55.28 (%)
All done! Total time: 82.47 sec

# try2 1-featLoss improve_tem_att_tf2cnn_no_feat_to_rgb_dw_try1_nofeat_nostem
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 71.30 (%) Recall@1x = 77.76 (%) Recall@5x = 93.78 (%) 
|tIoU = 0.40: mAP = 66.59 (%) Recall@1x = 72.90 (%) Recall@5x = 91.34 (%) 
|tIoU = 0.50: mAP = 59.26 (%) Recall@1x = 66.26 (%) Recall@5x = 86.95 (%) 
|tIoU = 0.60: mAP = 47.53 (%) Recall@1x = 56.00 (%) Recall@5x = 77.05 (%) 
|tIoU = 0.70: mAP = 34.56 (%) Recall@1x = 45.32 (%) Recall@5x = 61.90 (%) 
Average mAP: 55.85 (%)
All done! Total time: 52.30 sec

# 1-feat+stem thumos_i3d_improve_tem_att_tf2cnn_no_feat_to_rgb_dw_59.44_56.10
[RESULTS] Action detection results on thumos14.

|tIoU = 0.30: mAP = 71.33 (%) Recall@1x = 77.78 (%) Recall@5x = 93.99 (%) 
|tIoU = 0.40: mAP = 66.76 (%) Recall@1x = 72.39 (%) Recall@5x = 91.80 (%) 
|tIoU = 0.50: mAP = 59.44 (%) Recall@1x = 65.76 (%) Recall@5x = 85.77 (%) 
|tIoU = 0.60: mAP = 47.78 (%) Recall@1x = 56.18 (%) Recall@5x = 76.37 (%) 
|tIoU = 0.70: mAP = 35.19 (%) Recall@1x = 45.64 (%) Recall@5x = 61.30 (%) 
Average mAP: 56.10 (%)
All done! Total time: 52.48 sec
rgb_to_flow:0.5402088165283203
forward:0.5602035522460938
rgb_to_flow:0.0004057884216308594
forward:0.017669200897216797
rgb_to_flow:0.0005345344543457031
forward:0.0180814266204834
CPU
rgb_to_flow:0.09163689613342285
forward:0.3265860080718994
rgb_to_flow:0.061379432678222656
forward:0.22339391708374023
rgb_to_flow:0.05655169486999512
forward:0.20718598365783691



# improve_tem_att 時間注意力 比reproduce的avg高
|tIoU = 0.30: mAP = 82.18 (%) Recall@1x = 84.45 (%) Recall@5x = 96.32 (%) 
|tIoU = 0.40: mAP = 78.69 (%) Recall@1x = 80.69 (%) Recall@5x = 94.97 (%) 
|tIoU = 0.50: mAP = 70.87 (%) Recall@1x = 73.82 (%) Recall@5x = 91.73 (%) 
|tIoU = 0.60: mAP = 59.08 (%) Recall@1x = 64.81 (%) Recall@5x = 84.30 (%) 
|tIoU = 0.70: mAP = 45.30 (%) Recall@1x = 54.47 (%) Recall@5x = 70.99 (%) 
Average mAP: 67.23 (%)

# improve_tem_att_tf2cnn_no_feat
|tIoU = 0.30: mAP = 78.99 (%) Recall@1x = 81.90 (%) Recall@5x = 96.37 (%) 
|tIoU = 0.40: mAP = 75.32 (%) Recall@1x = 78.28 (%) Recall@5x = 94.60 (%) 
|tIoU = 0.50: mAP = 68.58 (%) Recall@1x = 72.18 (%) Recall@5x = 90.79 (%) 
|tIoU = 0.60: mAP = 56.21 (%) Recall@1x = 63.01 (%) Recall@5x = 82.73 (%) 
|tIoU = 0.70: mAP = 40.64 (%) Recall@1x = 50.49 (%) Recall@5x = 68.25 (%) 
Average mAP: 63.95 (%)

# improve_tem_att_tf2cnn_no_feat_ori
|tIoU = 0.30: mAP = 78.71 (%) Recall@1x = 82.01 (%) Recall@5x = 96.01 (%) 
|tIoU = 0.40: mAP = 74.92 (%) Recall@1x = 78.13 (%) Recall@5x = 94.25 (%) 
|tIoU = 0.50: mAP = 67.09 (%) Recall@1x = 71.21 (%) Recall@5x = 90.45 (%) 
|tIoU = 0.60: mAP = 55.27 (%) Recall@1x = 61.86 (%) Recall@5x = 82.30 (%) 
|tIoU = 0.70: mAP = 41.17 (%) Recall@1x = 50.67 (%) Recall@5x = 69.02 (%) 
Average mAP: 63.43 (%)

# improve_tem_att_tf2cnn_no_feat_60 real50
|tIoU = 0.30: mAP = 78.97 (%) Recall@1x = 82.19 (%) Recall@5x = 96.32 (%) 
|tIoU = 0.40: mAP = 75.69 (%) Recall@1x = 79.20 (%) Recall@5x = 94.64 (%) 
|tIoU = 0.50: mAP = 68.62 (%) Recall@1x = 73.01 (%) Recall@5x = 90.22 (%) 
|tIoU = 0.60: mAP = 56.39 (%) Recall@1x = 63.36 (%) Recall@5x = 82.44 (%) 
|tIoU = 0.70: mAP = 42.50 (%) Recall@1x = 53.09 (%) Recall@5x = 69.20 (%) 
Average mAP: 64.43 (%)

# improve_tem_att_tf2cnn_no_feat_60
|tIoU = 0.30: mAP = 78.97 (%) Recall@1x = 82.19 (%) Recall@5x = 96.32 (%) 
|tIoU = 0.40: mAP = 75.69 (%) Recall@1x = 79.20 (%) Recall@5x = 94.64 (%) 
|tIoU = 0.50: mAP = 68.62 (%) Recall@1x = 73.01 (%) Recall@5x = 90.22 (%) 
|tIoU = 0.60: mAP = 56.39 (%) Recall@1x = 63.36 (%) Recall@5x = 82.44 (%) 
|tIoU = 0.70: mAP = 42.50 (%) Recall@1x = 53.09 (%) Recall@5x = 69.20 (%) 
Average mAP: 64.43 (%)

# improve_tem_att_tf2cnn_no_feat_60_to_rgb
|tIoU = 0.30: mAP = 72.05 (%) Recall@1x = 76.84 (%) Recall@5x = 93.84 (%) 
|tIoU = 0.40: mAP = 66.71 (%) Recall@1x = 70.89 (%) Recall@5x = 90.92 (%) 
|tIoU = 0.50: mAP = 57.99 (%) Recall@1x = 63.74 (%) Recall@5x = 85.63 (%) 
|tIoU = 0.60: mAP = 46.77 (%) Recall@1x = 54.81 (%) Recall@5x = 75.61 (%) 
|tIoU = 0.70: mAP = 30.70 (%) Recall@1x = 41.21 (%) Recall@5x = 58.07 (%) 
Average mAP: 54.85 (%)

# improve_tem_att_tf2cnn_no_feat_60_to_rgb_pretrained
|tIoU = 0.30: mAP = 74.14 (%) Recall@1x = 78.35 (%) Recall@5x = 94.38 (%) 
|tIoU = 0.40: mAP = 69.01 (%) Recall@1x = 73.26 (%) Recall@5x = 91.96 (%) 
|tIoU = 0.50: mAP = 61.12 (%) Recall@1x = 67.12 (%) Recall@5x = 87.04 (%) 
|tIoU = 0.60: mAP = 49.54 (%) Recall@1x = 58.11 (%) Recall@5x = 77.33 (%) 
|tIoU = 0.70: mAP = 35.98 (%) Recall@1x = 46.33 (%) Recall@5x = 63.18 (%) 
Average mAP: 57.96 (%)

# improve_tem_att_tf2cnn_no_feat_60_to_rgb_pretrained_200
75
|tIoU = 0.30: mAP = 74.58 (%) Recall@1x = 79.13 (%) Recall@5x = 94.64 (%) 
|tIoU = 0.40: mAP = 69.62 (%) Recall@1x = 73.84 (%) Recall@5x = 91.55 (%) 
|tIoU = 0.50: mAP = 61.76 (%) Recall@1x = 67.37 (%) Recall@5x = 86.58 (%) 
|tIoU = 0.60: mAP = 50.18 (%) Recall@1x = 57.32 (%) Recall@5x = 77.40 (%) 
|tIoU = 0.70: mAP = 37.18 (%) Recall@1x = 46.49 (%) Recall@5x = 62.95 (%) 
Average mAP: 58.67 (%)

# improve_tem_att_tf2cnn_no_feat_to_rgb_trans wjm computer
rgb_to_flow:0.7396860122680664
forward:0.7567451000213623
rgb_to_flow:0.0005428791046142578
forward:0.015571832656860352
rgb_to_flow:0.001010894775390625
forward:0.015758037567138672
|tIoU = 0.30: mAP = 74.29 (%) Recall@1x = 79.01 (%) Recall@5x = 94.59 (%) 
|tIoU = 0.40: mAP = 69.83 (%) Recall@1x = 74.69 (%) Recall@5x = 92.52 (%) 
|tIoU = 0.50: mAP = 61.73 (%) Recall@1x = 67.99 (%) Recall@5x = 87.89 (%) 
|tIoU = 0.60: mAP = 50.21 (%) Recall@1x = 58.59 (%) Recall@5x = 78.73 (%) 
|tIoU = 0.70: mAP = 37.70 (%) Recall@1x = 47.71 (%) Recall@5x = 64.02 (%) 
Average mAP: 58.75 (%)

# thumos_i3d_improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw
python ./train.py ./configs/thumos_i3d.yaml --output improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw
python ./eval.py ./configs/thumos_i3d.yaml ./ckpt/thumos_i3d_improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw
35
|tIoU = 0.30: mAP = 71.76 (%) Recall@1x = 77.17 (%) Recall@5x = 93.53 (%) 
|tIoU = 0.40: mAP = 66.87 (%) Recall@1x = 72.07 (%) Recall@5x = 91.07 (%) 
|tIoU = 0.50: mAP = 59.42 (%) Recall@1x = 65.81 (%) Recall@5x = 86.89 (%) 
|tIoU = 0.60: mAP = 48.21 (%) Recall@1x = 56.59 (%) Recall@5x = 77.55 (%) 
|tIoU = 0.70: mAP = 35.91 (%) Recall@1x = 46.02 (%) Recall@5x = 62.47 (%) 
Average mAP: 56.43 (%)
40
|tIoU = 0.30: mAP = 72.19 (%) Recall@1x = 78.03 (%) Recall@5x = 94.03 (%) 
|tIoU = 0.40: mAP = 67.41 (%) Recall@1x = 72.93 (%) Recall@5x = 91.66 (%) 
|tIoU = 0.50: mAP = 59.81 (%) Recall@1x = 66.45 (%) Recall@5x = 87.47 (%) 
|tIoU = 0.60: mAP = 48.68 (%) Recall@1x = 57.13 (%) Recall@5x = 77.98 (%) 
|tIoU = 0.70: mAP = 36.47 (%) Recall@1x = 46.85 (%) Recall@5x = 63.31 (%) 
Average mAP: 56.91 (%)
45
|tIoU = 0.30: mAP = 72.34 (%) Recall@1x = 77.85 (%) Recall@5x = 94.00 (%) 
|tIoU = 0.40: mAP = 67.30 (%) Recall@1x = 72.84 (%) Recall@5x = 91.47 (%) 
|tIoU = 0.50: mAP = 59.57 (%) Recall@1x = 66.70 (%) Recall@5x = 86.62 (%) 
|tIoU = 0.60: mAP = 48.40 (%) Recall@1x = 57.44 (%) Recall@5x = 77.14 (%) 
|tIoU = 0.70: mAP = 36.38 (%) Recall@1x = 46.92 (%) Recall@5x = 62.52 (%) 
Average mAP: 56.80 (%)
50
|tIoU = 0.30: mAP = 72.54 (%) Recall@1x = 78.28 (%) Recall@5x = 94.04 (%) 
|tIoU = 0.40: mAP = 67.37 (%) Recall@1x = 73.02 (%) Recall@5x = 91.25 (%) 
|tIoU = 0.50: mAP = 59.62 (%) Recall@1x = 66.95 (%) Recall@5x = 86.38 (%) 
|tIoU = 0.60: mAP = 48.09 (%) Recall@1x = 57.29 (%) Recall@5x = 76.42 (%) 
|tIoU = 0.70: mAP = 36.22 (%) Recall@1x = 46.97 (%) Recall@5x = 62.70 (%) 
Average mAP: 56.77 (%)
55
|tIoU = 0.30: mAP = 72.23 (%) Recall@1x = 78.05 (%) Recall@5x = 94.13 (%) 
|tIoU = 0.40: mAP = 67.08 (%) Recall@1x = 73.17 (%) Recall@5x = 90.94 (%) 
|tIoU = 0.50: mAP = 59.34 (%) Recall@1x = 67.25 (%) Recall@5x = 85.75 (%) 
|tIoU = 0.60: mAP = 48.20 (%) Recall@1x = 58.16 (%) Recall@5x = 75.87 (%) 
|tIoU = 0.70: mAP = 35.96 (%) Recall@1x = 47.38 (%) Recall@5x = 61.85 (%) 
Average mAP: 56.56 (%)
70
|tIoU = 0.30: mAP = 71.15 (%) Recall@1x = 78.04 (%) Recall@5x = 93.70 (%) 
|tIoU = 0.40: mAP = 65.34 (%) Recall@1x = 72.80 (%) Recall@5x = 90.12 (%) 
|tIoU = 0.50: mAP = 58.35 (%) Recall@1x = 67.08 (%) Recall@5x = 84.93 (%) 
|tIoU = 0.60: mAP = 47.50 (%) Recall@1x = 57.86 (%) Recall@5x = 75.48 (%) 
|tIoU = 0.70: mAP = 34.75 (%) Recall@1x = 46.28 (%) Recall@5x = 60.03 (%) 
Average mAP: 55.42 (%)
80
|tIoU = 0.30: mAP = 70.45 (%) Recall@1x = 77.56 (%) Recall@5x = 93.40 (%) 
|tIoU = 0.40: mAP = 65.01 (%) Recall@1x = 72.76 (%) Recall@5x = 89.91 (%) 
|tIoU = 0.50: mAP = 57.73 (%) Recall@1x = 66.80 (%) Recall@5x = 84.64 (%) 
|tIoU = 0.60: mAP = 47.21 (%) Recall@1x = 57.86 (%) Recall@5x = 75.14 (%) 
|tIoU = 0.70: mAP = 34.42 (%) Recall@1x = 46.30 (%) Recall@5x = 59.92 (%) 
Average mAP: 54.96 (%)



# thumos_i3d_improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw_headsame
python ./train.py ./configs/thumos_i3d.yaml --output improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw_headsame
python ./eval.py ./configs/thumos_i3d.yaml ./ckpt/thumos_i3d_improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw_headsame
35
|tIoU = 0.30: mAP = 72.35 (%) Recall@1x = 77.83 (%) Recall@5x = 93.89 (%) 
|tIoU = 0.40: mAP = 67.74 (%) Recall@1x = 72.60 (%) Recall@5x = 91.68 (%) 
|tIoU = 0.50: mAP = 59.76 (%) Recall@1x = 65.66 (%) Recall@5x = 86.89 (%) 
|tIoU = 0.60: mAP = 49.28 (%) Recall@1x = 57.28 (%) Recall@5x = 77.99 (%) 
|tIoU = 0.70: mAP = 35.63 (%) Recall@1x = 45.68 (%) Recall@5x = 62.20 (%) 
Average mAP: 56.95 (%)
40
FLOPs: 39.749533704 G
Params: 21.273702 M
rgb_to_flow:0.6873056888580322
forward:0.7104973793029785
rgb_to_flow:0.0005414485931396484
forward:0.015144586563110352
rgb_to_flow:0.0008375644683837891
forward:0.015620708465576172
|tIoU = 0.30: mAP = 72.61 (%) Recall@1x = 78.24 (%) Recall@5x = 93.73 (%) 
|tIoU = 0.40: mAP = 68.04 (%) Recall@1x = 73.35 (%) Recall@5x = 91.64 (%) 
|tIoU = 0.50: mAP = 59.85 (%) Recall@1x = 66.30 (%) Recall@5x = 86.41 (%) 
|tIoU = 0.60: mAP = 49.25 (%) Recall@1x = 57.80 (%) Recall@5x = 77.23 (%) 
|tIoU = 0.70: mAP = 36.32 (%) Recall@1x = 46.68 (%) Recall@5x = 62.58 (%) 
Average mAP: 57.21 (%)
45
|tIoU = 0.30: mAP = 72.30 (%) Recall@1x = 78.05 (%) Recall@5x = 93.62 (%) 
|tIoU = 0.40: mAP = 67.68 (%) Recall@1x = 73.10 (%) Recall@5x = 91.15 (%) 
|tIoU = 0.50: mAP = 60.01 (%) Recall@1x = 66.66 (%) Recall@5x = 86.52 (%) 
|tIoU = 0.60: mAP = 49.08 (%) Recall@1x = 57.61 (%) Recall@5x = 76.87 (%) 
|tIoU = 0.70: mAP = 36.63 (%) Recall@1x = 46.77 (%) Recall@5x = 62.88 (%) 
Average mAP: 57.14 (%)
60
|tIoU = 0.30: mAP = 71.19 (%) Recall@1x = 77.19 (%) Recall@5x = 93.42 (%) 
|tIoU = 0.40: mAP = 66.30 (%) Recall@1x = 72.64 (%) Recall@5x = 90.34 (%) 
|tIoU = 0.50: mAP = 58.62 (%) Recall@1x = 66.34 (%) Recall@5x = 85.13 (%) 
|tIoU = 0.60: mAP = 47.92 (%) Recall@1x = 57.32 (%) Recall@5x = 74.99 (%) 
|tIoU = 0.70: mAP = 35.85 (%) Recall@1x = 46.88 (%) Recall@5x = 61.31 (%) 
Average mAP: 55.98 (%)

# thumos_i3d_improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw_bbsame
python ./train.py ./configs/thumos_i3d.yaml --output improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw_bbsame
python ./eval.py ./configs/thumos_i3d.yaml ./ckpt/thumos_i3d_improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw_bbsame
60
FLOPs: 50.598682632 G
Params: 36.429414 M
|tIoU = 0.30: mAP = 72.65 (%) Recall@1x = 78.74 (%) Recall@5x = 94.34 (%) 
|tIoU = 0.40: mAP = 67.70 (%) Recall@1x = 73.80 (%) Recall@5x = 91.16 (%) 
|tIoU = 0.50: mAP = 60.01 (%) Recall@1x = 67.13 (%) Recall@5x = 86.45 (%) 
|tIoU = 0.60: mAP = 49.16 (%) Recall@1x = 58.17 (%) Recall@5x = 75.97 (%) 
|tIoU = 0.70: mAP = 36.36 (%) Recall@1x = 46.55 (%) Recall@5x = 62.15 (%) 
Average mAP: 57.18 (%)

# thumos_i3d_improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw_feat_stem
python ./train.py ./configs/thumos_i3d.yaml --output improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw_feat_stem
python ./eval.py ./configs/thumos_i3d.yaml ./ckpt/thumos_i3d_improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw_feat_stem


# thumos_i3d_improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw_feat_nostem
python ./train.py ./configs/thumos_i3d.yaml --output improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw_feat_nostem
python ./eval.py ./configs/thumos_i3d.yaml ./ckpt/thumos_i3d_improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw_feat_nostem
|tIoU = 0.30: mAP = 71.46 (%) Recall@1x = 77.52 (%) Recall@5x = 94.14 (%) 
|tIoU = 0.40: mAP = 66.25 (%) Recall@1x = 71.51 (%) Recall@5x = 91.50 (%) 
|tIoU = 0.50: mAP = 59.34 (%) Recall@1x = 65.30 (%) Recall@5x = 86.42 (%) 
|tIoU = 0.60: mAP = 47.92 (%) Recall@1x = 56.04 (%) Recall@5x = 76.50 (%) 
|tIoU = 0.70: mAP = 35.71 (%) Recall@1x = 46.00 (%) Recall@5x = 62.10 (%) 
Average mAP: 56.13 (%)


# thumos_i3d_improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw_nofeat_nostem
python ./train.py ./configs/thumos_i3d.yaml --output improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw_nofeat_nostem
python ./eval.py ./configs/thumos_i3d.yaml ./ckpt/thumos_i3d_improve_tem_att_tf2cnn_no_feat_to_rgb_trans_dw_nofeat_nostem
|tIoU = 0.30: mAP = 71.43 (%) Recall@1x = 77.61 (%) Recall@5x = 94.34 (%) 
|tIoU = 0.40: mAP = 66.67 (%) Recall@1x = 72.54 (%) Recall@5x = 91.22 (%) 
|tIoU = 0.50: mAP = 58.63 (%) Recall@1x = 64.99 (%) Recall@5x = 86.53 (%) 
|tIoU = 0.60: mAP = 47.80 (%) Recall@1x = 56.30 (%) Recall@5x = 77.52 (%) 
|tIoU = 0.70: mAP = 34.76 (%) Recall@1x = 45.62 (%) Recall@5x = 62.08 (%) 
Average mAP: 55.86 (%)

# rp_nosave
3538mb
rgb+flow
1.5137330541070902e-06 0.04258750407200939 0.10001366655781584 1.5135262071729291e-05 0.4258168462146164
rgb
2.2177426320201946e-06 0.04030439426314156 0.09905502481280633 2.238899678447684e-05 0.40688894217439847

# rp_nosave_attn
3530mb
All done!
total time:877.6534399986267
1.5733376988824808e-06 0.04523652791976929 0.12673642725314735 1.2414250054089393e-05 0.35693390527265234

# rp_nosave_attn_tf2cnn
3042mb
total time:689.4435420036316
1.2843114025187941e-06 0.022476759721648018 0.04925426109781805 2.6075132869584127e-05 0.45634142550650775

# rp_nosave_attn_tf2cnn_rgb
3260mb
All done!
total time:789.5121960639954
0.00414644884613325 0.023616401654369425 0.05027404371297584 0.08247693123326466 0.46975337391199307

# rp_nosave_attn_tf2cnn_rgb_dw
3338mb
All done!
total time:748.6679055690765
rgbtoflow forward total rgbtoflow占比 forward占比
0.004189375436530923 0.024715145803847403 0.04896814305827303 0.0855530795101927 0.5047188694583723
3103S 35EPOCH 1.48MIN/EPOCH