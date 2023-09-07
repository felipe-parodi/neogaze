auto_scale_lr = dict(base_batch_size=4096)
data_prefix = '/mmpose/fparodi/neogaze/data/prepped_training_data/'
data_preprocessor = dict(
    mean=[
        123.675,
        116.28,
        103.53,
    ],
    num_classes=7,
    std=[
        58.395,
        57.12,
        57.375,
    ],
    to_rgb=True)
data_root = '/mmpose/fparodi/neogaze/data/prepped_training_data/all_data'
dataset_type = 'CustomDataset'
default_hooks = dict(
    checkpoint=dict(
        interval=1, rule='greater', save_best='auto', type='CheckpointHook'),
    logger=dict(interval=100, type='LoggerHook'),
    param_scheduler=dict(type='ParamSchedulerHook'),
    sampler_seed=dict(type='DistSamplerSeedHook'),
    timer=dict(type='IterTimerHook'),
    visualization=dict(enable=False, type='VisualizationHook'))
default_scope = 'mmpretrain'
env_cfg = dict(
    cudnn_benchmark=False,
    dist_cfg=dict(backend='nccl'),
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0))
launcher = 'pytorch'
load_from = 'https://download.openmmlab.com/mmclassification/v0/clip/clip-vit-base-p32_laion2b-pre_3rdparty_in1k_20221220-194df57f.pth'
log_level = 'INFO'
model = dict(
    backbone=dict(
        arch='b',
        drop_rate=0.1,
        frozen_stages=4,
        img_size=224,
        init_cfg=[
            dict(
                layer='Conv2d',
                mode='fan_in',
                nonlinearity='linear',
                type='Kaiming'),
        ],
        patch_size=32,
        pre_norm=True,
        type='VisionTransformer'),
    head=dict(
        in_channels=768,
        loss=dict(loss_weight=1.0, type='CrossEntropyLoss'),
        num_classes=7,
        topk=(
            1,
            3,
        ),
        type='VisionTransformerClsHead'),
    neck=None,
    type='ImageClassifier')
optim_wrapper = dict(
    clip_grad=dict(max_norm=1.0),
    optimizer=dict(lr=0.003, type='AdamW', weight_decay=0.3),
    paramwise_cfg=dict(
        custom_keys=dict({
            '.cls_token': dict(decay_mult=0.0),
            '.pos_embed': dict(decay_mult=0.0)
        })))
param_scheduler = [
    dict(
        begin=0,
        by_epoch=True,
        convert_to_iter_based=True,
        end=30,
        start_factor=0.0001,
        type='LinearLR'),
    dict(
        T_max=270, begin=30, by_epoch=True, end=300, type='CosineAnnealingLR'),
]
randomness = dict(deterministic=False, seed=None)
resume = False
test_cfg = dict()
test_dataloader = dict(
    batch_size=128,
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        ann_file=
        '/mmpose/fparodi/neogaze/data/prepped_training_data/val_full.txt',
        classes=[
            'Airway-Equipment',
            'CMAC-Screen',
            'Infant',
            'Non-Team-Member',
            'Other-Physical-Objects',
            'Airway-Provider',
            'Vitals-Monitor',
        ],
        data_root='/mmpose/fparodi/neogaze/data/prepped_training_data/all_data',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(
                backend='pillow',
                edge='short',
                interpolation='bicubic',
                scale=224,
                type='ResizeEdge'),
            dict(crop_size=224, type='CenterCrop'),
            dict(type='PackInputs'),
        ],
        type='CustomDataset',
        with_label=True),
    num_workers=5,
    persistent_workers=True,
    pin_memory=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
test_evaluator = [
    dict(topk=(
        1,
        3,
    ), type='Accuracy'),
    dict(items=[
        'precision',
        'recall',
    ], type='SingleLabelMetric'),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        backend='pillow',
        edge='short',
        interpolation='bicubic',
        scale=224,
        type='ResizeEdge'),
    dict(crop_size=224, type='CenterCrop'),
    dict(type='PackInputs'),
]
train_cfg = dict(by_epoch=True, max_epochs=300, val_interval=1)
train_dataloader = dict(
    batch_size=128,
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        ann_file=
        '/mmpose/fparodi/neogaze/data/prepped_training_data/train_full.txt',
        classes=[
            'Airway-Equipment',
            'CMAC-Screen',
            'Infant',
            'Non-Team-Member',
            'Other-Physical-Objects',
            'Airway-Provider',
            'Vitals-Monitor',
        ],
        data_root='/mmpose/fparodi/neogaze/data/prepped_training_data/all_data',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(
                backend='pillow',
                interpolation='bicubic',
                scale=224,
                type='RandomResizedCrop'),
            dict(direction='horizontal', prob=0.5, type='RandomFlip'),
            dict(direction='vertical', prob=0.5, type='RandomFlip'),
            dict(direction='diagonal', prob=0.5, type='RandomFlip'),
            dict(type='PackInputs'),
        ],
        type='CustomDataset',
        with_label=True),
    num_workers=5,
    persistent_workers=True,
    pin_memory=True,
    sampler=dict(shuffle=True, type='DefaultSampler'))
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        backend='pillow',
        interpolation='bicubic',
        scale=224,
        type='RandomResizedCrop'),
    dict(direction='horizontal', prob=0.5, type='RandomFlip'),
    dict(direction='vertical', prob=0.5, type='RandomFlip'),
    dict(direction='diagonal', prob=0.5, type='RandomFlip'),
    dict(type='PackInputs'),
]
val_cfg = dict()
val_dataloader = dict(
    batch_size=128,
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        ann_file=
        '/mmpose/fparodi/neogaze/data/prepped_training_data/val_full.txt',
        classes=[
            'Airway-Equipment',
            'CMAC-Screen',
            'Infant',
            'Non-Team-Member',
            'Other-Physical-Objects',
            'Airway-Provider',
            'Vitals-Monitor',
        ],
        data_root='/mmpose/fparodi/neogaze/data/prepped_training_data/all_data',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(
                backend='pillow',
                edge='short',
                interpolation='bicubic',
                scale=224,
                type='ResizeEdge'),
            dict(crop_size=224, type='CenterCrop'),
            dict(type='PackInputs'),
        ],
        type='CustomDataset',
        with_label=True),
    num_workers=5,
    persistent_workers=True,
    pin_memory=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
val_evaluator = [
    dict(topk=(
        1,
        3,
    ), type='Accuracy'),
    dict(items=[
        'precision',
        'recall',
    ], type='SingleLabelMetric'),
]
vis_backends = [
    dict(type='LocalVisBackend'),
]
visualizer = dict(
    type='UniversalVisualizer', vis_backends=[
        dict(type='LocalVisBackend'),
    ])
work_dir = '/mmpose/fparodi/neogaze/results/clip_vit_b32/'
