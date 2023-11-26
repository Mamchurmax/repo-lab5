"""importing Point, Polynom, Color"""
from point import Point, Polynom, Color

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
