import numpy as np


class Rectangle:

    def __init__(self, box):
        self._x = box[0]
        self._y = box[1]
        self._width = box[2]
        self._height = box[3]

    @property
    def cv_rect(self):
        return (self._x, self._y), (self._x + self._width, self._y + self._height)

    @property
    def box(self):
        return self._x, self._y, self._width, self._height

    @property
    def center(self):
        return self._x + self._width // 2, self._y + self._height // 2

    def expand(self, a):
        box = (self._x - a, self._y - a, self._width + 2 * a, self._height + 2 * a)
        return Rectangle(box)

    def scale(self, ratio):
        box = [int(val * ratio) for val in self.box]
        return Rectangle(box)

    def dist(self, rectangle):
        a = np.array(self.center)
        b = np.array(rectangle.center)
        return np.linalg.norm(a - b, axis=1)
