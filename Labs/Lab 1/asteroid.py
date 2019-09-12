import random
import math
import time
import random

class Asteroid:

    def __init__(self, radius, position, velocity, timestamp):
        self._circumference = 2 * math.pi * radius
        self._position = position
        self._velocity = velocity
        self._timestamp = timestamp

    def get_position(self):
        return self._position

    def get_velocity(self):
        return self._velocity

    def set_position(self, position):
        self._position = position

    def set_velocity(self, velocity):
        self._velocity = velocity



    def __str__(self):
        return f"Circumference: {ast.circumference} \nPosition: {ast.position} \nVelocity: {ast.velocity} \nTimestamp: {ast.timestamp}"

ast = Asteroid(1, [1, 1, 1], [1, 2, 3], time.time())

# self.position = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
# self.velocity = [random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)]

print(f"Before position change: {ast._position}")
print(f"Before velocity change: {ast._velocity}\n")
ast.set_position([0, 0, 0])
ast.set_velocity([10, 10, 10])
print(f"After position change: {ast._position}")
print(f"After velocity change: {ast._velocity}")




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
