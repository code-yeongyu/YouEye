import json
from socket import *
from .hand_detection import get_hand_in_image

# ipc code for https://github.com/code-yeongyu/east-detector-socket-wrapper
# for main logic, check https://github.com/code-yeongyu/east-detector-socket-wrapper/blob/master/main.py


def calibrate_word_coords(words):
    for i in range(len(words)):
        for j in range(len(words[i])):
            r = (words[i][j][0] * 4, words[i][j][1] * 4)
            words[i][j] = r
    return words


def get_hand_coord(img_path):
    return get_hand_in_image(img_path)


def get_word_coord(img_path):
    client_socket = socket(AF_INET, SOCK_DGRAM)
    client_socket.connect(('127.0.0.1', 8080))
    content = {'img_path': img_path}
    client_socket.send(json.dumps(content).encode('utf-8'))
    data = client_socket.recv(65000)
    client_socket.close()
    return json.loads(data.decode('utf-8'))['return']


def get_touchable_word_coord(hands, words):
    left_hand = hands[0][0]
    right_hand = hands[1][0]
    top_hand = hands[0][1]
    bottom_hand = hands[1][1]

    touchable_words_pos = []

    for word in words:
        left_word = word[0][0]
        right_word = word[1][0]
        top_word = word[0][1]
        bottom_word = word[1][1]
        middle_x = int((left_word + right_word) / 2)
        middle_y = int((top_word + bottom_word) / 2)
        middle_dot = [middle_x, middle_y]
        if will_click_word_coord(left_hand, right_hand, bottom_hand, top_hand,
                                 middle_dot):
            touchable_words_pos.append(word)
    return get_biggest_area(touchable_words_pos)


def will_click_word_coord(left_pos, right_pos, bottom_pos, top_pos,
                          letter_dot):
    DOT_RANGE = 200
    # filter dots between left_pos and right_pos letter_dots
    if not (left_pos <= letter_dot[0] and letter_dot[0] <= right_pos):
        return False
    # filter dots between top_pos and top_pos + DOT_RANGE
    if not (top_pos - DOT_RANGE <= letter_dot[1]
            and bottom_pos >= letter_dot[1]):
        return False
    return True


def get_biggest_area(dots):
    WEIGHT = 200
    left = None
    top = None
    right = None
    bottom = None
    for dot in dots:
        dot_left = dot[0][0]
        dot_right = dot[1][0]
        dot_top = dot[0][1]
        dot_bottom = dot[1][1]
        if left == None or left > dot_left:
            left = dot_left
        if right == None or right < dot_right:
            right = dot_right
        if top == None or top > dot_top:
            top = dot_top
        if bottom == None or bottom < dot_bottom:
            bottom = dot_bottom
    if left == None:
        return []
    left -= WEIGHT
    if left < 0:
        left = 0
    top -= WEIGHT
    if top < 0:
        top = 0
    p1 = (left, top)
    p2 = (right + WEIGHT, bottom + WEIGHT)
    return [p1, p2]
