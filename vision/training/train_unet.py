import torch
from torch.utils.data import DataLoader
from dataset import RustDataset
from unet import UNet

ds = RustDataset("data")
dl = DataLoader(ds, batch_size=8, shuffle=True)

model = UNet().cuda()
opt = torch.optim.Adam(model.parameters(),1e-3)
loss_fn = torch.nn.BCELoss()

for e in range(40):
    for x,y in dl:
        x,y=x.cuda(),y.cuda()
        pred=model(x)
        loss=loss_fn(pred,y)
        opt.zero_grad(); loss.backward(); opt.step()
    print("Epoch",e,"Loss",loss.item())

torch.jit.script(model).save("models/unet_rust.pt")
