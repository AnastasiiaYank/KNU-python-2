from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def intersects(self, other):
        # Check if two shapes intersect
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius ** 2

    def intersects(self, other):
        # Check if two circles intersect
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def intersects(self, other):
        # Check if two rectangles intersect
        pass


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def intersects(self, other):
        # Check if two triangles intersect
        pass


shapes = [Circle(5), Rectangle(3, 4), Triangle(3, 4, 5)]

# Check if shapes intersect
for i in range(len(shapes)):
    for j in range(i+1, len(shapes)):
        if shapes[i].intersects(shapes[j]):
            print("Shapes intersect")
            break

# Calculate total area
total_area = 0
for shape in shapes:
    total_area += shape.area()

print("Total area:", total_area)
