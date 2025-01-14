from point import Point
from triangle import Triangle

class Scalene(Triangle):
    """Clase que representa un triángulo escaleno."""
    def __init__(self, vertex1: Point, vertex2: Point, vertex3: Point):
        super().__init__(vertex1, vertex2, vertex3)
        a, b, c = (edge.get_length() for edge in self.edges)
        if a == b or b == c or a == c:
            raise ValueError("No es un triángulo escaleno.")