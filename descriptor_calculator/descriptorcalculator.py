import os

import dlib
import numpy as np


class DescriptorCalculator:
    def __init__(self):

        landmarks_path = os.path.join(
            os.path.dirname(__file__),
            "shape_predictor_68_face_landmarks.dat"
        )
        model_path = os.path.join(
            os.path.dirname(__file__),
            "dlib_face_recognition_resnet_model_v1.dat"
        )
        self._detector = dlib.get_frontal_face_detector()
        self._sp = dlib.shape_predictor(landmarks_path)
        self._face_recognition_model = dlib.face_recognition_model_v1(model_path)

    def calculate(self, image, rectangle):
        shape = self._sp(image, rectangle.dlib_rect)
        descriptor = self._face_recognition_model.compute_face_descriptor(
            image, shape
        )
        return np.array(descriptor)
