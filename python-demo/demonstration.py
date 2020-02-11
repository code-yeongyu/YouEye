import os, cv2
from utils import coords
from utils import ocr
from utils import img_processing


def main():
    for i in range(0, 5):
        DEMO_PATH = os.getcwd() + "/demo-images/"
        IMG_PATH = f"{DEMO_PATH}{i}.jpeg"
        RESULT_IMG_PATH = f"{DEMO_PATH}result_{i}.jpeg"
        RESULT_TXT_PATH = f"{DEMO_PATH}result_{i}.txt"

        hand_coord = coords.get_hand_coord(IMG_PATH)[0]
        words_coord = coords.get_word_coord(IMG_PATH)
        touchable_words_coord = coords.get_touchable_word_coord(
            hand_coord, words_coord)
        img = cv2.imread(IMG_PATH)
        img_processing.draw_box_on_image_green(img, tuple(hand_coord[0]),
                                               tuple(hand_coord[1]))

        img_processing.draw_box_on_image_red(img, touchable_words_coord[0],
                                             touchable_words_coord[1])
        cv2.imwrite(RESULT_IMG_PATH, img)
        roi = img_processing.cut_image(img, touchable_words_coord[0],
                                       touchable_words_coord[1])
        text = ocr.naver(roi)
        f = open(RESULT_TXT_PATH, 'w')
        f.write(text)
        f.close()


main()