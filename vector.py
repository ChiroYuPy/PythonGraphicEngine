import math

class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other):
        return Vector3(self.x / other, self.y / other, self.z / other)

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def normalize(self):
        length = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        if length == 0:
            return Vector3(0, 0, 0)  # Avoid division by zero
        return Vector3(self.x / length, self.y / length, self.z / length)

    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

class Vector2:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector2(self.x / other, self.y / other)

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def normalize(self):
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        if length == 0:
            return Vector2(0, 0)  # Avoid division by zero
        return Vector2(self.x / length, self.y / length)

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"
