from .shape import Shape

class Circle(Shape):
    def __init__(self, radius, center: list):
        self.radius = radius
        self.center = center