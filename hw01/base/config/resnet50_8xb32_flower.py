_base_ = [
    '../_base_/models/resnet50.py', '../_base_/datasets/imagenet_bs32.py',
    '../_base_/default_runtime.py'
]

model = dict(
    head=dict(
        num_classes=5
    )
)

dataset_type = 'CustomDataset'
classes = ['daisy','dandelion','rose','sunflower','tulip']
data = dict(
    train=dict(
        type=dataset_type,
        data_prefix='data/flower_dataset/train',
        classes = classes
    ),
    val=dict(
        type=dataset_type,
        data_prefix='data/flower_dataset/val',
        classes = classes,
        ann_file = None        
    ),
    test=dict(
        type=dataset_type,
        data_prefix='data/flower_dataset/val',
        classes=classes,
        ann_file=None
    )
)

optimizer = dict(type='SGD',lr=0.001,momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)

lr_config=dict(
    policy='step',
    step=[1])

runner = dict(type='EpochBasedRunner', max_epochs=100)

load_from = '/disk0/lwb/pretrain/resnet50_8xb32_in1k_20210831-ea4938fc.pth'