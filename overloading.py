import math
class Shape:
    def area(self, *args):
        if len(args) == 1:  
            radius = args[0]
            return round(4 * math.pi * radius ** 2, 2)
        elif len(args) == 2:  
            length, breadth = args
            return length * breadth
        elif len(args) == 3:  
            side = args[0]
            return 6 * side ** 2
        else:
            return "Invalid number of arguments"
shape = Shape()
print("Rectangle Area:", shape.area(5, 10))
print("Sphere Area:", shape.area(7))
print("Cube Area:", shape.area(4, 4, 4))
