import torch.nn as nn

class UNet(nn.Module):
    def __init__(self):
        super().__init__()
        def C(i,o): return nn.Sequential(
            nn.Conv2d(i,o,3,1,1), nn.ReLU(),
            nn.Conv2d(o,o,3,1,1), nn.ReLU()
        )

        self.d1=C(1,64); self.d2=C(64,128); self.d3=C(128,256)
        self.pool=nn.MaxPool2d(2)
        self.u2=nn.ConvTranspose2d(256,128,2,2)
        self.u1=nn.ConvTranspose2d(128,64,2,2)
        self.o=nn.Conv2d(64,1,1)

    def forward(self,x):
        c1=self.d1(x)
        c2=self.d2(self.pool(c1))
        c3=self.d3(self.pool(c2))
        x=self.u2(c3)
        x=self.u1(x+c2)
        return torch.sigmoid(self.o(x+c1))
