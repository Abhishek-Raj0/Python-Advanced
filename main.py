class Shape:
    def area(self):
        return 0

# class Square(Shape): ...
class Square(Shape):
    def __init__(self, sides):
        self.sides = sides
    def area(self):
        return self.sides ** 2

# class Circle(Shape): ...
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2

kind = input().strip()
val = float(input())
# Build shape and print area.
if kind == "square":
    shape = Square(val)
elif kind == "circle":
    shape = Circle(val)
else:
    raise ValueError(f"Unknown shape: {kind}")
print(shape.area())