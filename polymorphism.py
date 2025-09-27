import math
class Shape:
    def area(self):
        pass  
    def perimeter(self):
        pass  
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius  
class Triangle(Shape):
    def __init__(self, a, b, c, height):
        self.a = a  
        self.b = b  
        self.c = c  
        self.height = height  
    def area(self):
        return 0.5 * self.b * self.height  
    def perimeter(self):
        return self.a + self.b + self.c
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Triangle(3, 4, 5, 6)
]
for shape in shapes:
    print(f"{shape.__class__.__name__}:")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}\n")
