import cv2, numpy as np, os, random

def gen(img):
    h,w=img.shape
    for _ in range(random.randint(20,100)):
        cv2.circle(img,(random.randint(0,w),random.randint(0,h)),
                   random.randint(5,20),(random.randint(0,80)), -1)
    return img

os.makedirs("data/images",exist_ok=True)
os.makedirs("data/masks",exist_ok=True)

for i in range(200):
    base=np.ones((256,256),np.uint8)*200
    rust=gen(base.copy())
    cv2.imwrite(f"data/images/s{i}.png",rust)
    cv2.imwrite(f"data/masks/s{i}.png",(rust<150)*255)
