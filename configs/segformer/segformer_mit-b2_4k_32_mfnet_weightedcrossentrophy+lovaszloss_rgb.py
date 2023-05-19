_base_ = [
    "../_base_/models/segformer_mit-b2_weightedcrossentrophy.py",
    "../_base_/datasets/mfnet_rgb.py",
    "../_base_/default_runtime.py",
    "../_base_/schedules/mfnet_schedule_4k.py",
]


checkpoint = "https://download.openmmlab.com/mmsegmentation/v0.5/pretrain/segformer/mit_b2_20220624-66e8bf70.pth"  # noqa


model = dict(
    backbone=dict(init_cfg=dict(type="Pretrained", checkpoint=checkpoint)),
)

# optimizer
optimizer = dict(
    _delete_=True,
    type="AdamW",
    lr=0.00006,
    betas=(0.9, 0.999),
    weight_decay=0.01,
    paramwise_cfg=dict(
        custom_keys={
            "pos_block": dict(decay_mult=0.0),
            "norm": dict(decay_mult=0.0),
            "head": dict(lr_mult=10.0),
        }
    ),
)

lr_config = dict(
    _delete_=True,
    policy="CosineAnnealing",
    warmup="linear",
    warmup_iters=250,
    warmup_ratio=1e-06,
    min_lr=0.0,
    by_epoch=False,
)
