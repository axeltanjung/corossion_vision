import os, cv2
import numpy as np
import torch
from torch.utils.data import Dataset

class RustDataset(Dataset):
    def __init__(self, root="data", size=256):
        self.imgs = sorted(os.listdir(root+"/images"))
        self.root = root
        self.size = size

    def __len__(self):
        return len(self.imgs)

    def __getitem__(self, i):
        img = cv2.imread(f"{self.root}/images/{self.imgs[i]}",0)
        mask = cv2.imread(f"{self.root}/masks/{self.imgs[i]}",0)

        img = cv2.resize(img,(self.size,self.size))/255.
        mask = cv2.resize(mask,(self.size,self.size))/255.

        return (
            torch.tensor(img).unsqueeze(0).float(),
            torch.tensor(mask).unsqueeze(0).float()
        )
