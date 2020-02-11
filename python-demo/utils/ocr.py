import pytesseract
import requests
import json
import base64
import cv2
import os
from time import time
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'


def _remove_duplicates(li):
    temp_set = set()
    result = []
    for e in li:
        if e not in temp_set:
            result.append(e)
            temp_set.add(e)

    return result


def tesseract(img):
    return pytesseract.image_to_string(img, lang="kor")


def naver(img):
    _, buffer = cv2.imencode('.jpeg', img)
    headers = {
        "X-OCR-SECRET": os.environ['X-OCR-SECRET'],
        "Content-Type": "application/json"
    }
    img_data = base64.b64encode(buffer).decode('utf-8')
    data = {
        "version": "V1",
        "requestId": "1",
        "timestamp": int(time()),
        "lang": "ko",
        "images": [{
            "format": "jpeg",
            "name": "jpeg-image",
            "data": img_data
        }]
    }
    req = requests.post(os.environ['OCR_URL'],
                        headers=headers,
                        data=json.dumps(data))
    ocr_data = json.loads(req.text)
    words = []
    for i in range(0, len(ocr_data['images'][0]['fields'])):
        words.append(ocr_data['images'][0]['fields'][i]['inferText'])
    words = _remove_duplicates(words)
    return ''.join(words)