from .shape import Shape


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def is_valid(self):
        return self.width > 0 and self.height > 0

    def points(self):

        if not self.is_valid():
            return None

        return [
            (0, 0),
            (self.width, 0),
            (self.width, self.height),
            (0, self.height)
        ]


    def area(self):
        if not self.is_valid():
            return None

        return self.width * self.height

    def perimeter(self):
        if not self.is_valid():
            return None

        return 2 * (self.width + self.height)