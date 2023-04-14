import math


class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is None and diameter is None:
            raise ValueError("Invalid Input")
        if radius is not None:
            self.radius = radius
        else:
            self.radius = diameter / 2

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

#Input Radius
radius = float(input("Input radius: "))

c = Circle(radius=radius)

# computation for area and perimeter
area = c.area()
perimeter = c.perimeter()

print(f"The area of the circle is: {area:.2f}")
print(f"The perimeter of the circle is: {perimeter:.2f}")
