# dataset settings
dataset_type = 'MFnet_ir'
data_root = 'data/MFnet'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
ir_img_norm_cfg = dict( mean=114.495, std=57.63)
crop_size = (480, 640)    
train_pipeline = [
    dict(type='LoadImageFromFile'),#,imdecode_backend='pillow'),
    dict(type='LoadAnnotations'),
    dict(type='Resize', img_scale=(480, 640), ratio_range=(0.5, 2.0)),
    dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PhotoMetricDistortion'),
    dict(type='RGB2Gray',out_channels=1,weights=(1, 1, 1)),
    dict(type='NormalizeIR', **ir_img_norm_cfg),
    dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_semantic_seg']),
 
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
         type='MultiScaleFlipAug',
         img_scale=(480, 640),
         # img_ratios=[0.5, 0.75, 1.0, 1.25, 1.5, 1.75],
         flip=False,
         transforms=[
             dict(type='RGB2Gray',out_channels=1,weights=(1, 1, 1)),
             dict(type='NormalizeIR', **ir_img_norm_cfg),
             dict(type='ImageToTensor', keys=['img']),
             dict(type='Collect', keys=['img']),])      
]
data = dict(
    samples_per_gpu=32,
    workers_per_gpu=4,
    train=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='img_dir/ir/train',
        ann_dir='ann_dir/train',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='img_dir/ir/val',
        ann_dir='ann_dir/val',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        data_root=data_root,
        
        img_dir='img_dir/ir/test',
        ann_dir='ann_dir/test',
        pipeline=test_pipeline))
    # test_day=dict(
    #     type=dataset_type,
    #     data_root=data_root,
    #     img_dir='img_dir/rgb/test_day',
    #     ann_dir='ann_dir/test_day',
    #     pipeline=test_pipeline))