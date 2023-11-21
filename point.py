"""importing shit"""
import math
from enum import Enum


class Color(Enum):
    """creating colors"""
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4


class Point:
    """creating class point"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x:{self.x}, y:{self.y}"

    def __repr__(self):
        return f"Point{self.x}, {self.y}"


class Polynom:
    """creating polynom"""
    def __init__(self, points, color):
        self.points = points
        self.color = color

    @staticmethod
    def calculate_distance(point1, point2):
        """creating distance formula"""
        distance = math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)
        return distance

    def calculate_perimeter(self):
        """creating perimeter formula"""
        perimeter = 0

        for i in range(len(self.points) - 1):
            point1 = self.points[i]
            point2 = self.points[i + 1]
            perimeter += Polynom.calculate_distance(point1, point2)

        perimeter += Polynom.calculate_distance(self.points[-1], self.points[0])

        if perimeter == 0:
            perimeter = None

        return perimeter

    def calculate_longest_diagonal(self):
        """calculating longest diagonal"""
        max_diagonal = 0
        for i in range(len(self.points) - 1):
            point1 = self.points[i]
            for j in range(i + 1, len(self.points)):
                point2 = self.points[j]
                distance = Polynom.calculate_distance(point1, point2)
                if distance > max_diagonal:
                    max_diagonal = distance
        return max_diagonal

    def sort_by_x(self):
        """sorting by x"""
        return self.points.sort(key=lambda point: point.x)

    def sort_by_y(self):
        """sorting by y"""
        return self.points.sort(key=lambda point: point.y)


a = Point(1, 1)
b = Point(1, 7)
c = Point(1, 12)
d = Point(22, 7)
e = Point(6, 7)

polygon = Polynom([a, b, c, d, e], Color.RED)

perimeter = polygon.calculate_perimeter()
max_diagonal = polygon.calculate_longest_diagonal()

print(f"Периметр: {perimeter}")
print(f"Найдовша діагональ: {max_diagonal}")

polygon.sort_by_x()
print("Точки, відсортовані за абсцисою:")
for point in polygon.points:
    print(f"({point.x}, {point.y})")

polygon.sort_by_y()
print("Точки, відсортовані за ординатою:")
for point in polygon.points:
    print(f"({point.x}, {point.y})")
