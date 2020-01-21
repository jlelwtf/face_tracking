from mtcnn import MTCNN

from rectangle import Rectangle


class FaceDetector:
    def __init__(self, confidence_threshold=0.8):
        self._confidence_threshold = confidence_threshold
        self._detector = MTCNN()
        # self._detector = dlib.get_frontal_face_detector()

    def __call__(self, image):
        faces = self._detector.detect_faces(image)
        rects = []
        for face in faces:
            box = face['box']
            if face['confidence'] > self._confidence_threshold:
                rects.append(Rectangle(box))
        return rects
