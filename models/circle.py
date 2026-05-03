from .shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def is_valid(self):
        return self.radius > 0

    def bounding_box(self):
        if not self.is_valid():
            return None

        diameter = self.radius * 2

        return [
            (0, 0),
            (diameter, diameter)
        ]
    
    def area(self):
        if not self.is_valid():
            return None

        return math.pi * self.radius ** 2

    def perimeter(self):
        if not self.is_valid():
            return None

        return 2 * 3.14159 * self.radius