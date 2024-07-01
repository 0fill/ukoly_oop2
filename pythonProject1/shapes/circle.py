from .shape import Shape

class Circle(Shape):
    def __init__(self, radius, center: list):
        self.radius = radius
        self.center = center

    def __eq__ (self, other: 'Circle'):
        return self.radius == other.radius

    def __lt__ (self, other: 'Circle'):
        return self.radius < other.radius

    def __gt__ (self, other: 'Circle'):
        return self.radius > other.radius

    def __le__ (self, other: 'Circle'):
        return self.radius <= other.radius

    def __ge__ (self, other: 'Circle'):
        return self.radius >= other.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius, self.center)

    def __sub__(self, other):
        return Circle(self.radius - other.radius, self.center)

    def __iadd__ (self, other):
        self.radius += other.radius

    def __isub__ (self, other):
        self.radius -= other.radius




