from .shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def is_valid(self):
        return self.radius > 0

    def area(self):
        if not self.is_valid():
            return None

        return 3.14159 * self.radius ** 2

    def perimeter(self):
        if not self.is_valid():
            return None

        return 2 * 3.14159 * self.radius