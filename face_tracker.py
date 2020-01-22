import numpy as np

from descriptor_calculator.descriptorcalculator import DescriptorCalculator
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

    def _find_by_descriptor(self, face_descriptor):
        if self._descriptors:
            distances = []
            for descriptor in self._descriptors:
                distances.append(cosine(descriptor, face_descriptor))
            min_val = min(distances)
            if min_val < 0.1:
                return distances.index(min_val)

    def _get_id(self, rectangle, frame):
        descriptor = self._descriptor_calculator.calculate(frame, rectangle)
        idx = self._find_by_descriptor(descriptor)
        if idx is not None:
            return self._descriptor_ids[idx]
        else:
            id = self._count
            self._count += 1
            self._descriptors.append(descriptor)
            self._descriptor_ids.append(id)
            return id

    def track(self, new_rectangles, frame):
        new_rectangles = [rect.expand(int(rect.width / 3)) for rect in new_rectangles]
        if not new_rectangles:
            self._rectangles = []
            self._rectangle_ids = []

        elif not self._rectangles:
            for rect in new_rectangles:
                self._rectangles.append(rect)
                new_id = self._get_id(rect, frame)
                self._rectangle_ids.append(new_id)
        else:
            dists = np.zeros((len(new_rectangles), len(self._rectangles)), np.float)
            for i, rect in enumerate(new_rectangles):
                for j, hist_rect in enumerate(self._rectangles):
                    dists[i, j] = rect.dist(hist_rect) / rect.width

            argmins = dists.argmin(axis=1)
            rectangles = []
            ids = []
            for idx, arg in enumerate(argmins):
                rectangles.append(new_rectangles[idx])
                if dists[idx, arg] <= 1.:
                    ids.append(self._rectangle_ids[arg])
                else:
                    ids.append(self._get_id(new_rectangles[idx], frame))
            self._rectangles = rectangles
            self._rectangle_ids = ids

        return self._rectangles, self._rectangle_ids
