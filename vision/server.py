from fastapi import FastAPI, UploadFile
from PIL import Image
import numpy as np, cv2
from inference.segment import RustUNet
from inference.texture import surface_entropy

model = RustUNet()
app = FastAPI()

@app.post("/infer")
async def infer(file: UploadFile):
    img = np.array(Image.open(file.file).convert("L"))
    mask = model.predict(img)

    rust_area = float((mask > 0.5).mean())
    entropy = surface_entropy(img)

    return {
        "rust_area": rust_area,
        "surface_entropy": entropy
    }
