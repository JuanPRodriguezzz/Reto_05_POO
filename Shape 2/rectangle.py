from shape import Shape
from point import Point
from line import Line

class Rectangle(Shape):
    """Clase que representa un rectángulo."""
    def __init__(self, bottom_left: Point, top_right: Point):
        width = top_right.get_x() - bottom_left.get_x()
        height = top_right.get_y() - bottom_left.get_y()

        vertices = [
            bottom_left,
            Point(top_right.get_x(), bottom_left.get_y()),
            top_right,
            Point(bottom_left.get_x(), top_right.get_y())
        ]

        edges = [
            Line(vertices[0], vertices[1]),
            Line(vertices[1], vertices[2]),
            Line(vertices[2], vertices[3]),
            Line(vertices[3], vertices[0])
        ]

        super().__init__(vertices, edges)
        self.width = width
        self.height = height

    def compute_area(self):
        return self.width * self.height