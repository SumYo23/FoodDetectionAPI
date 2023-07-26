import torch
from PIL import Image
import numpy as np


def predict(file_name):
    # yolo 관련 파일 불러오기
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./classifier/last.pt', force_reload=True)

    # 이미지 불러오기
    file_name = "." + file_name
    img = Image.open(file_name).convert("RGB")
    img = np.array(img)

    # 결과 받아옴
    detect = model(img).pandas().xyxy[0].to_numpy()
    result = list(set([i[6] for i in detect]))

    return result
