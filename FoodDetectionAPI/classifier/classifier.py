import torch
from PIL import Image
import numpy as np

def predict(file_name):
    # yolo 관련 파일 불러오기
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./classifier/best.pt', force_reload=True)

    # 이미지 불러오기
    file_name = "." + file_name
    img = Image.open(file_name).convert("RGB")
    img = np.array(img)

    # 결과 받아옴
    detect = model(img).pandas().xyxy[0].to_numpy()
    result = list(set([i[6] for i in detect]))

    ingredient_dict = {'bean sprouts': '콩나물',
                       'beef': '소고기',
                       'chicken': '닭고기',
                       'egg': '계란',
                       'fork': '포크',
                       'garlic': '마늘',
                       'green onion': '파',
                       'kimchi': '김치',
                       'onion': '양파',
                       'potato': '감자',
                       'spam': '스팸'
                       }
    result = [ingredient_dict[i] for i in result]
    return result
