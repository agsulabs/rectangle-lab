from .shape import Shape


class Triangle(Shape):
    def __init__(self, left_side, right_side, base):
        self.left_side = left_side
        self.right_side = right_side
        self.base = base

    def is_valid(self):
        return (
            self.left_side + self.right_side > self.base
            and self.left_side + self.base > self.right_side
            and self.right_side + self.base > self.left_side
        )

    def area(self):
        if not self.is_valid():
            return None

        s = (self.left_side + self.right_side + self.base) / 2

        return (
            s
            * (s - self.left_side)
            * (s - self.right_side)
            * (s - self.base)
        ) ** 0.5

    def perimeter(self):
        if not self.is_valid():
            return None

        return self.left_side + self.right_side + self.base