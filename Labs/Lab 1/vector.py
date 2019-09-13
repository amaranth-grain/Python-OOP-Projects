
'''Vector in 3D space.'''
class Vector:

    '''Create Vector with x, y, and z (Unit: m/s)'''
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = y

    '''Return x co-ordinate.'''
    def get_x(self):
        return self._x

    '''Return y co-ordinate.'''
    def get_y(self):
        return self._y

    '''Return z co-ordinate.'''
    def get_z(self):
        return self._z

    ''' 
    Add vector to itself.
    :param vector as Vector
    '''
    def add(self, vector):
        self._x += vector.get_x()
        self._y += vector.get_y()
        self._z += vector.get_z()

    '''Return tuple of Vector.'''
    def tuple(self):
        return self._x, self._y, self._z

    '''Format Vector as tuple.'''
    def __str__(self):
        return f"{self.tuple()}"


'''Drive the program.'''
def main():
    vec = Vector(1, 2, 3)
    vec2 = Vector(3, 2, 1)
    print(f"Before: {vec}")
    vec.add(vec2)
    print(f"After: {vec}")


if __name__ == "__main__":
    main()


