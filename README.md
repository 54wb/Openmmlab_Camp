# Openmmlab_Camp
> This repo is homework for [Openmmlab_AI_Camp](https://github.com/open-mmlab/OpenMMLabCamp)    

## intro   
the format of every dir is:   
      hw/    
      |——base    
      |————config    
      |————work_dirs    
      |——————xxx.log   
      |——advanced   
      |————config    
      |————work_dirs   
## install 
for hw01 and hw02,install mmcls and mmdet
```
conda activate mmlab1  # 切换至 OpenMMLab 1.0 系列环境（假设已安装好 PyTorch）
pip install -U openmim # 安装 mim
mim install mmcv-full  # 安装基础库 mmcv 完整版
# 源码安装 mmdet
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
mim install -v -e .
# 源码安装 mmcls
cd ..
git clone https://github.com/open-mmlab/mmclassification.git
cd mmclassification
mim install -v -e .
```

## requirements for hw
requirements for hw01 can be found:[mmcls_hw1](https://github.com/open-mmlab/OpenMMLabCamp/issues/6)   
requirements for hw01 can be found:[mmdet_hw2](https://github.com/open-mmlab/OpenMMLabCamp/issues/30)   

