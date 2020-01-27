import argparse
import sys

import cv2
import imutils

from face_detector import FaceDetector
from face_tracker import FaceTracker


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--video_path', default='video/4p-c0.avi')
arg_parser.add_argument('--scale_view', type=float, default=3.)


def draw_labeled_rectangle(image, rectangle, text):
    cv_rect = rectangle.cv_rect
    cv2.rectangle(image, cv_rect[0], cv_rect[1], (0, 255, 0), 2)
    cv2.putText(
        image, text, (cv_rect[0][0], cv_rect[0][1] - 5),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0,), 2
    )


if __name__ == '__main__':
    argv = arg_parser.parse_args(sys.argv[1:])

    video_capture = cv2.VideoCapture(argv.video_path)
    face_rect_detector = FaceDetector()

    ret = True
    ratio = argv.scale_view
    tracker = FaceTracker()
    while ret:
        ret, frame = video_capture.read()
        if ret:
            rects = face_rect_detector(frame)
            faces = tracker.track(rects, frame)
            frame = imutils.resize(frame, width=int(frame.shape[1] * ratio))
            for face in faces:
                rect = face.rectangle
                rect = rect.scale(ratio).expand(10)
                draw_labeled_rectangle(frame, rect, str(face.id))
            cv2.imshow('face tracking', frame)
            cv2.waitKey(1)
