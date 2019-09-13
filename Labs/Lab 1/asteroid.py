import math
import time


class Asteroid:

    asteroid_id = 0

    def __init__(self, radius, position, velocity, timestamp):
        self._circumference = 2 * math.pi * radius
        self._position = position
        self._velocity = velocity
        self._timestamp = timestamp
        self._id = Asteroid.increment_id()

    @classmethod
    def increment_id(cls):
        cls.asteroid_id += 1
        return cls.asteroid_id

    def get_position(self):
        return self._position

    ''' Return velocity as list [x, y, z] in m/s '''
    def get_velocity(self):
        return self._velocity

    '''
    Set asteroid position.
    :param position: a list
    :precondition a:  a list representing a vector [x, y, z]
    '''
    def set_position(self, position):
        self._position = position

    def set_velocity(self, velocity):
        self._velocity = velocity

    def move(self):
        x = self._velocity[0] + self._position[0]
        y = self._velocity[1] + self._position[1]
        z = self._velocity[2] + self._position[2]
        self._position = [x, y, z]
        return (x, y, z)


    def __str__(self):
        return f"Asteroid ID: {self._id}" \
               f"\nCircumference: {self._circumference} " \
               f"\nPosition: {self._position} " \
               f"\nVelocity: {self._velocity} " \
               f"\nTimestamp: {self._timestamp}"

def main():
    pass

if __name__ == "__main__":
    main()

# ast = Asteroid(1, [1, 1, 1], [1, 2, 3], time.time())
# ast2 = Asteroid(3, [5, 5, 5], [4, 4, 4], time.time())
# self.position = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
# self.velocity = [random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)]
# print(f"Ast: {ast}\n")
# print(f"Ast2: {ast2}")
# print(f"Before position change: {ast._position}")
# print(f"Before velocity change: {ast._velocity}\n")
# ast.set_position([1, 2, 3])
# ast.set_velocity([2, 2, 2])
# print(f"After position change: {ast._position}")
# print(f"After velocity change: {ast._velocity}")
#
# print(f"\nBefore ast move: \n{ast}")
# print(f"\nast.move() returns {ast.move()}")
# print(f"\nAfter ast move: \n{ast}")





# class Vector:
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def get_x(self):
#         return self.x
#
#     def get_y(self):
#         return self.y
#
#     def get_z(self):
#         return self.z
#
#     def add(self, vector):
