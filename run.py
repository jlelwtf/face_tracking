import cv2
import imutils

from face_detector import FaceDetector
from face_tracker import FaceTracker

video_capture = cv2.VideoCapture('video/4p-c0.avi')
# video_capture = cv2.VideoCapture(0)
face_detector = FaceDetector()


def draw_labeled_rectangle(image, rectangle, text):
    cv_rect = rectangle.cv_rect
    cv2.rectangle(image, cv_rect[0], cv_rect[1], (0, 255, 0), 2)
    cv2.putText(
        image, text, (cv_rect[0][0], cv_rect[0][1] - 5),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0,), 2
    )


if __name__ == '__main__':
    ret = True
    ratio = 4.
    tracker = FaceTracker()
    while ret:
        ret, frame = video_capture.read()
        if ret:
            rects = face_detector(frame)
            rects, ids = tracker.track(rects, frame)

            frame = imutils.resize(frame, width=int(frame.shape[1] * ratio))
            rects = [rect.scale(ratio) for rect in rects]

            for rect, idx in zip(rects, ids):
                # rect = rect.scale(ratio).expand(10)
                draw_labeled_rectangle(frame, rect, str(idx))
            cv2.imshow('video', frame)
            cv2.waitKey(1)
