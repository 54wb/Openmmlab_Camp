_base_ = [
    '../_base_/models/efficientnet_b7.py',
    '../_base_/datasets/cifar10_bs16.py',
    '../_base_/schedules/cifar10_bs128.py',
    '../_base_/default_runtime.py',
]


model = dict(
    head=dict(
        num_classes=10
    )
)

data=dict(
    samples_per_gpu=128,
    workers_per_gpu=4
)
lr_config = dict(policy='step', step=[70, 100])
runner = dict(type='EpochBasedRunner', max_epochs=120)
load_from = '/disk0/lwb/pretrain/efficientnet-b7_3rdparty_8xb32-aa-advprop_in1k_20220119-c6dbff10.pth'
