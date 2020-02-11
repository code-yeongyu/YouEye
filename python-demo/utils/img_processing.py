import cv2


def draw_box_on_image_green(img, p1, p2):
    cv2.rectangle(img, tuple(p1), tuple(p2), (77, 255, 9), 3, 1)


def draw_box_on_image_red(img, p1, p2):
    cv2.rectangle(img, tuple(p1), tuple(p2), (9, 77, 255), 3, 1)


def cut_image(img, p1, p2):
    copied = img.copy()
    copied = copied[p1[1]:p2[1], p1[0]:p2[0]]
    return copied