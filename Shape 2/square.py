from rectangle import Rectangle
from point import Point

class Square(Rectangle):
    """Clase que representa un cuadrado (subclase de Rectángulo)."""
    def __init__(self, bottom_left: Point, side_length: float):
        top_right = Point(bottom_left.get_x() + side_length, bottom_left.get_y() + side_length)
        super().__init__(bottom_left, top_right)

    def compute_area(self):
        return self.width**2