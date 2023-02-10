## 基础作业

#### 数据准备
下载balloon数据集后按照coco格式准备数据 
```
python base/ballon2coco.py data/balloon/val/via_region_data.json instances_val.json data/balloon/val
```
数据格式如下：   
data   
|——balloon   
|————annotations  
|——————train.json  
|——————val.json  
|————train  
|——————xxx.jpg  
|————val  
|——————xx.jpg  
  
#### 训练网络:
这里是使用了两种网络分别是mask_rcnn和HTC，具体的网络结果可参考论文[Mask RCNN](https://arxiv.org/abs/1703.06870),[Hybrid Task Cascade for Instance Segmentation](https://arxiv.org/abs/1901.07518) 
```
python tools/train.py configs/htc/htc_without_semantic_r50_fpn_1x_balloon.py
python tools/train.py configs/mask_rcnn/mask_rcnn_r50_fpn_1x_balloon.py
```
#### 转化color_splash视频
```
python base/colar_splash.py 
```

#### 视频展示
本仓库不支持gif展示   
请下载视频后进行查看    
[video](https://github.com/54wb/Openmmlab_Camp/releases/download/hw02_base_pth/color_splash_balloon.mp4)

## results


| Hw       | Training Dateset | Bbox_AP | Segm_AP | Config                                                                                                          | Download                                                                                |
|:--------:|:----------------:|:-------:|:-------:|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| Base     | Balloon          | 78.35   | 79.62   | [config](https://github.com/54wb/Openmmlab_Camp/blob/master/hw02/base/configs/htc_without_semantic_r50_fpn_1x_balloon.py) | [model](https://github.com/54wb/Openmmlab_Camp/releases/download/hw02_base_pth/htc_epoch_12.pth) |
| advanced | DOTA             | 78.03   |         | [config](https://github.com/54wb/Openmmlab_Camp/blob/master/hw02/advanced/config/roi_trans_swin_tiny_fpn_1x_dota_more.py) | [model](https://github.com/54wb/Openmmlab_Camp/releases/download/hw02_advanced/epoch_12.pth)     |

