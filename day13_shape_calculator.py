#Day13 Shape Calculator
import math

class Circle:
    shapes_created = 0

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("radius must be positive")

        self.radius = radius
        Circle.shapes_created += 1

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    @staticmethod
    def cm_to_inch(cm):
        return round(cm * 0.3937, 3)

    @staticmethod
    def is_valid_dimension(val):
        return val > 0

    @classmethod
    def total_created(cls):
        return f"Circles created: {cls.shapes_created}"

    def __str__(self):
        return f"Circle(r={self.radius})"


class Rectangle:
    shapes_created = 0

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("dimensions must be positive")

        self.width = width
        self.height = height
        Rectangle.shapes_created += 1

    def area(self):
        return round(self.width * self.height, 2)

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def is_square(self):
        return self.width == self.height

    @staticmethod
    def cm_to_inch(cm):
        return round(cm * 0.3937, 3)

    @staticmethod
    def is_valid_dimension(val):
        return val > 0

    @classmethod
    def total_created(cls):
        return f"Rectangles created: {cls.shapes_created}"

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"


# Create shapes
c1 = Circle(5)
c2 = Circle(3)
c3 = Circle(7)

r1 = Rectangle(4, 6)
r2 = Rectangle(5, 5)

print("\n-------------circles-------------")
# Print circles
print(c1)
print("Area:", c1.area())
print("Perimeter:", c1.perimeter())
print(r2.is_square())

print("\n--------------------------")
print(c2)
print("Area:", c2.area())
print("Perimeter:", c2.perimeter())
print(r2.is_square())

print("\n--------------------------")
print(c3)
print("Area:", c3.area())
print("Perimeter:", c3.perimeter())
print(r2.is_square())

print("\n-----------Rectangles---------------")
# Print rectangles
print(r1)
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())
print(r2.is_square())

print(r2)
print("Area:", r2.area())
print("Perimeter:", r2.perimeter())
print("Is Square?", r2.is_square())


print("\n--------------------------")
# Static methods
print(Circle.cm_to_inch(10))
print(Rectangle.is_valid_dimension(-2))
print("\n--------------------------")

# Class methods
print(Circle.total_created())
print(Rectangle.total_created())
print("\n--------------------------")

# Validation examples
try:
    Circle(-3)
except ValueError as e:
    print("ValueError:", e)

try:
    Rectangle(0, 5)
except ValueError as e:
    print( "VlueError:", e)