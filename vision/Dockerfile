FROM python:3.10
WORKDIR /app

RUN pip install fastapi uvicorn torch torchvision opencv-python pillow numpy

COPY . .
CMD ["uvicorn","server:app","--host","0.0.0.0","--port","8001"]
