class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # __add__ and __repr__ go here
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
v1 = Vector(x1, y1)
v2 = Vector(x2, y2)
# print(repr(v1 + v2)
print(repr(v1 + v2))