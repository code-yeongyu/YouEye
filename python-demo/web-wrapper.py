import cv2
from utils import coords
from utils import img_processing
from utils import ocr
from utils import tts
import os
from flask import Flask, request, Response, make_response
import datetime
import json

app = Flask(__name__)


@app.route('/i_am_ironman', methods=['POST'])
def i_am_ironman():
    img_file = request.files.get('image')
    if img_file == None:
        return Response(json.dumps({'error': "field 'image' not found"}),
                        status=400)
    now = datetime.datetime.now()
    FILE_NAME = now.strftime('%Y-%m-%dT%H:%M:%S') + (
        '-%02d' % (now.microsecond / 10000)) + '.jpeg'
    img_file.save(FILE_NAME)

    IMAGE_PATH = os.getcwd() + "/" + FILE_NAME
    hand_coord = coords.get_hand_coord(IMAGE_PATH)[0]
    img = cv2.imread(IMAGE_PATH)

    cv2.imwrite('./resized.jpeg', img)
    words_coord = coords.get_word_coord(os.getcwd() + "/resized.jpeg")
    if len(words_coord) == 0 or len(hand_coord) == 0:
        return Response(json.dumps(
            {'error': "neither hands nor words are not found."}),
                        status=400)

    touchable_words_coord = coords.get_touchable_word_coord(
        hand_coord, words_coord)
    if len(touchable_words_coord) == 0:
        return Response(json.dumps({'text': ''}))
    roi = img_processing.cut_image(img, touchable_words_coord[0],
                                   touchable_words_coord[1])
    cv2.imwrite("./test.jpeg", roi)
    text = ocr.naver(roi)
    data = {'text': text}
    json_data = json.dumps(data, ensure_ascii=False).encode('utf8')
    return Response(json_data)


app.run(host='0.0.0.0', port='8000')