import torch
import numpy as np
import cv2

class RustUNet:
    def __init__(self, path="models/unet_rust.pt"):
        self.model = torch.jit.load(path)
        self.model.eval()

    def predict(self, img):
        img = cv2.resize(img,(256,256))
        x = torch.from_numpy(img/255.).float().unsqueeze(0).unsqueeze(0)
        with torch.no_grad():
            mask = self.model(x)[0,0].numpy()
        return mask
