import numpy as np


def crop_image(rectangle, image):
    cv_rect = rectangle.cv_rect
    return image[cv_rect[0][1]: cv_rect[1][1], cv_rect[0][0]: cv_rect[1][0]]


def euclidean_distance(a, b):
    return np.linalg.norm(a - b)


