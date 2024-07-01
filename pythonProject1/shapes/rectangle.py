from .shape import Shape

class Rectangle(Shape):
    def __init__(self, side1, side2, lefrup_corner: list):
        self.side1 = side1
        self.side2 = side2
        self.lefrup_corner = lefrup_corner