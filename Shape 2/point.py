from math import sqrt

class Point:
    """Clase que representa un punto en un plano bidimensional."""
    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value

    def compute_distance(self, other_point):
        return sqrt((self.get_x() - other_point.get_x())**2 + (self.get_y() - other_point.get_y())**2)