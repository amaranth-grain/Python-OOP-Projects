class Vector:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_z(self):
        return self._z

    def add(self, vector):
        self._x += vector.get_x()
        self._y += vector.get_y()
        self._z += vector.get_z()

    def tuple(self):
        return self._x, self._y, self._z

    def __str__(self):
        return f"{self.tuple()}"

def main():
    vec = Vector(1, 2, 3)
    vec2 = Vector(3, 2, 1)
    print(f"Before: {vec}")
    vec.add(vec2)
    print(f"After: {vec}")

if __name__ == "__main__":
    main()


