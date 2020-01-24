from scipy.spatial.distance import cosine


class Face:
    def __init__(self, face_id, rectangle, descriptor, loss_threshold=10):
        self._loss_threshold = loss_threshold
        self.id = face_id
        self.rectangle = rectangle
        self.descriptor = descriptor
        self.registered = True
        self.loss_count = 0

    def distance(self, descriptor):
        return cosine(self.descriptor, descriptor)

    def loss(self):
        if self.registered:
            self.loss_count += 1
            if self.loss_count >= self._loss_threshold:
                self.registered = False

    def register(self):
        self.registered = True
        self.loss_count = 0
