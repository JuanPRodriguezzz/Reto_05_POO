from point import Point
from triangle import Triangle


class Equilateral(Triangle):
    """Clase que representa un triángulo equilátero."""
    def __init__(self, vertex1: Point, vertex2: Point, vertex3: Point):
        super().__init__(vertex1, vertex2, vertex3)
        a, b, c = (edge.get_length() for edge in self.edges)
        if not (a == b == c):
            raise ValueError("No es un triángulo equilátero.")