import numpy as np
from scipy.spatial.distance import cosine

from face import Face


class FaceRepo:
    def __init__(self):
        self._faces = []
        self._id_count = 0

    def _get_new_id(self):
        new_id = self._id_count
        self._id_count += 1
        return new_id

    def _get_rect_dists(self, face, rectangles):
        dists = np.zeros((len(rectangles)), np.float)
        for idx, rect in enumerate(rectangles):
            dists[idx] = face.rectangle.dist(rect) / rect.width
        return dists

    def _get_descr_dists(self, descriptors, face):
        dists = np.zeros((len(descriptors)), np.float)
        for idx, descriptor in enumerate(descriptors):
            dists[idx] = cosine(face.descriptor, descriptor)
        return dists

    def track_by_rectangles(self, rectangles, rect_dist_thr=1.2):
        for face in self._faces:
            if rectangles:
                dists = self._get_rect_dists(face, rectangles)
                argmin = dists.argmin()

                if dists[argmin] <= rect_dist_thr:
                    face.rectangle = rectangles.pop(argmin)
                    face.register()
                else:
                    face.loss()
            else:
                face.loss()

        return rectangles

    def track_by_descriptors(self, rectangles, descriptors, desc_dist_thr=0.06):
        for face in self.get_unregistered_faces():
            if descriptors:
                dists = self._get_descr_dists(descriptors, face)
                argmin = dists.argmin()

                if dists[argmin] <= desc_dist_thr:
                    face.rectangle = rectangles.pop(argmin)
                    descriptors.pop(argmin)
                    face.register()
                else:
                    face.loss()
            else:
                face.loss()

        return rectangles, descriptors

    def add_faces(self, rectangles, descriptors):
        for rectangle, descriptor in zip(rectangles, descriptors):
            self._faces.append(Face(self._get_new_id(), rectangle, descriptor))

    def get_registered_faces(self):
        return [face for face in self._faces if face.registered]

    def get_unregistered_faces(self):
        return [face for face in self._faces if not face.registered]
