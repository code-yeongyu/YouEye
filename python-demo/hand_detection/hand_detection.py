from utils import detector_utils as detector_utils
import cv2

detection_graph, sess = detector_utils.load_inference_graph()


def _calc_hand_pos(score_thresh, scores, boxes, im_width, im_height, image_np):
    result = []
    for i in range(len(scores)):
        result.append({
            "left": boxes[i][1] * im_height,
            "right": boxes[i][3] * im_height,
            "top": boxes[i][0] * im_width,
            "bottom": boxes[i][2] * im_width
        })
    return result


def get_hand_in_image(image_path):
    image = cv2.imread(image_path)
    width, height, _ = image.shape
    cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes, scores = detector_utils.detect_objects(image, detection_graph, sess)
    return _calc_hand_pos(0.48, scores, boxes, width, height, image)