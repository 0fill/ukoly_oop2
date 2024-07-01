from .shape import Shape

class Square(Shape):
    def __init__(self, side,leftup_corner):
        self.side = side
        self.left_corner = leftup_corner
