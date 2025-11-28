# Create a class Shape with a method area(). Create subclasses Circle, Rectangle, and Triangle that override the area() method

class Shape:
    def area(self):
        return "Area cannot be determined for generic shape."


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius   # πr²


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth     #length * breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height  #1/2 * base * height

c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(10, 5)

print("Circle area:", c.area())
print("Rectangle area:", r.area())
print("Triangle area:", t.area())
