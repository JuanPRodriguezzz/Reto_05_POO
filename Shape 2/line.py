from point import Point

class Line:
    """Clase que representa una línea en un plano bidimensional."""
    def __init__(self, start_point: Point, end_point: Point):
        self._start_point = start_point
        self._end_point = end_point
        self._length = self.compute_length()

    def get_start_point(self):
        return self._start_point

    def set_start_point(self, value):
        self._start_point = value
        self._length = self.compute_length()

    def get_end_point(self):
        return self._end_point

    def set_end_point(self, value):
        self._end_point = value
        self._length = self.compute_length()

    def get_length(self):
        return self._length

    def compute_length(self):
        return self.get_start_point().compute_distance(self.get_end_point())