from math import sqrt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, number):
        self.x *= number
        self.y *= number
        return self

    def __lt__(self, other):
        length1 = sqrt(self.x ** 2 + self.y ** 2)
        length2 = sqrt(other.x ** 2 + other.y ** 2)
        return length1 < length2

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print("v1 =", v1)
print("v2 =", v2)

v1 += v2
print("v1 =", v1)

v1 -= v2
print("v1 =", v1)

v1 *= 2
print("v1 =", v1)

print("v1 < v2:", v1 < v2)
