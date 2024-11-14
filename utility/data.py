import albumentations as A
from albumentations.pytorch import ToTensorV2

train_transform = A.Compose([
    A.Resize(64, 64),  
    # <<-----여기에 작성해보세요----->>
    A.OneOf([
        A.HorizontalFlip(p=0.5),
        A.VerticalFilp(p=0.5),
        A.RandomRotate(p=0.5)
    ], p = 0.5),
    A.OneOf([  # 밝기, 대비, 색조, 채도 등 색상 관련 증강 중 하나를 무작위로 선택
        A.RandomBrightnessContrast(brightness_limit=0.2, contrast_limit=0.2, p=0.5),
        A.HueSaturationValue(hue_shift_limit=20, sat_shift_limit=30, val_shift_limit=20, p=0.5),
        A.RGBShift(r_shift_limit=20, g_shift_limit=20, b_shift_limit=20, p=0.5)
    ], p=0.5),
    A.OneOf([  # 블러, 노이즈, 모자이크 효과 등 중 하나를 무작위로 선택
        A.GaussianBlur(blur_limit=(3, 7), p=0.5),
        A.MotionBlur(blur_limit=7, p=0.5),
        A.MedianBlur(blur_limit=7, p=0.5)
    ], p=0.5),
    A.OneOf([  # 부분적으로 픽셀을 제거하거나 드롭아웃 효과를 무작위로 선택
        A.CoarseDropout(max_holes=8, max_height=16, max_width=16, p=0.5)
    ], p=0.5),
    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225), max_pixel_value=255.0),
    ToTensorV2()
])