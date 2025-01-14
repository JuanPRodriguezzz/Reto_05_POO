from math import sqrt, acos, degrees

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


class Shape:
    """Superclase que representa una figura geométrica."""
    def __init__(self, vertices: list[Point], edges: list[Line]):
        self.vertices = vertices
        self.edges = edges
        self.inner_angles = self.compute_inner_angles()
        self.is_regular = self.check_regular()

    def compute_area(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def compute_perimeter(self):
        return sum(edge.get_length() for edge in self.edges)

    def compute_inner_angles(self):
        """Calcula los ángulos internos (solo para polígonos convexos)."""
        angles = []
        for i in range(len(self.vertices)):
            p1 = self.vertices[i - 1]
            p2 = self.vertices[i]
            p3 = self.vertices[(i + 1) % len(self.vertices)]

            a = p1.compute_distance(p2)
            b = p2.compute_distance(p3)
            c = p1.compute_distance(p3)

            angle = acos((a**2 + b**2 - c**2) / (2 * a * b))
            angles.append(degrees(angle))
        return angles

    def check_regular(self):
        """Verifica si la figura es regular."""
        if len(self.edges) < 3:
            return False

        first_length = self.edges[0].get_length()
        first_angle = self.inner_angles[0]

        return all(edge.get_length() == first_length for edge in self.edges) and \
               all(angle == first_angle for angle in self.inner_angles)


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


class Square(Rectangle):
    """Clase que representa un cuadrado (subclase de Rectángulo)."""
    def __init__(self, bottom_left: Point, side_length: float):
        top_right = Point(bottom_left.get_x() + side_length, bottom_left.get_y() + side_length)
        super().__init__(bottom_left, top_right)

    def compute_area(self):
        return self.width**2


class Triangle(Shape):
    """Clase que representa un triángulo."""
    def __init__(self, vertex1: Point, vertex2: Point, vertex3: Point):
        vertices = [vertex1, vertex2, vertex3]

        edges = [
            Line(vertices[0], vertices[1]),
            Line(vertices[1], vertices[2]),
            Line(vertices[2], vertices[0])
        ]

        super().__init__(vertices, edges)

    def compute_area(self):
        """Calcula el área usando la fórmula de Herón."""
        a, b, c = (edge.get_length() for edge in self.edges)
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Isosceles(Triangle):
    """Clase que representa un triángulo isósceles."""
    def __init__(self, vertex1: Point, vertex2: Point, vertex3: Point):
        super().__init__(vertex1, vertex2, vertex3)
        a, b, c = (edge.get_length() for edge in self.edges)
        if not (a == b or b == c or a == c):
            raise ValueError("No es un triángulo isósceles.")


class Equilateral(Triangle):
    """Clase que representa un triángulo equilátero."""
    def __init__(self, vertex1: Point, vertex2: Point, vertex3: Point):
        super().__init__(vertex1, vertex2, vertex3)
        a, b, c = (edge.get_length() for edge in self.edges)
        if not (a == b == c):
            raise ValueError("No es un triángulo equilátero.")


class Scalene(Triangle):
    """Clase que representa un triángulo escaleno."""
    def __init__(self, vertex1: Point, vertex2: Point, vertex3: Point):
        super().__init__(vertex1, vertex2, vertex3)
        a, b, c = (edge.get_length() for edge in self.edges)
        if a == b or b == c or a == c:
            raise ValueError("No es un triángulo escaleno.")


class TriRectangle(Triangle):
    """Clase que representa un triángulo rectángulo."""
    def __init__(self, vertex1: Point, vertex2: Point, vertex3: Point):
        super().__init__(vertex1, vertex2, vertex3)
        a, b, c = sorted(edge.get_length() for edge in self.edges)
        if not abs(c**2 - (a**2 + b**2)) < 1e-9:
            raise ValueError("No es un triángulo rectángulo.")

