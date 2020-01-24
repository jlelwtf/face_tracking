import numpy as np

from descriptor_calculator.descriptorcalculator import DescriptorCalculator
from face_repo import FaceRepo
from utils import euclidean_distance
from scipy.spatial.distance import cosine


class FaceTracker:

    def __init__(self):
        self._rectangles = []
        self._rectangle_ids = []
        self._count = 0
        self._empty_count = 0
        self._descriptors = []
        self._descriptor_ids = []
        self._descriptor_calculator = DescriptorCalculator()
        self._face_repo = FaceRepo()

    def track(self, rectangles, frame):
        rectangles = self._face_repo.track_by_rectangles(rectangles)

        rectangles = [rect.expand(int(rect.width / 2.5)) for rect in rectangles]
        descriptors = [
            self._descriptor_calculator.calculate(frame, rect)
            for rect in rectangles
        ]

        rectangles, descriptors = self._face_repo.track_by_descriptors(
            rectangles, descriptors
        )

        self._face_repo.add_faces(rectangles, descriptors)

        return self._face_repo.get_registered_faces()
