class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.pi * self.radius * self.radius
    def circumference(self):
        return 2 * self.pi * self.radius
circle1 = Circle(5)
print(circle1.area())