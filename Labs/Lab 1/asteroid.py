import math
from random import randint
from datetime import datetime
from vector import Vector

'''
Asteroid has circumference (calculated from radius) and timestamp on when it was
created as attributes as records, but methods do not interact with these
instance variables.
Position and velocity 
'''
class Asteroid:

    _id = 0
    _MIN_RADIUS = 1
    _MAX_RADIUS = 4
    _MIN_POS = 0
    _MAX_POS = 100
    _MIN_VELOCITY = -5
    _MAX_VELOCITY = 5

    def __init__(self, radius, position, velocity, timestamp):
        self._circumference = 2 * math.pi * radius
        self._position = position
        self._velocity = velocity
        self._timestamp = timestamp
        self._id = Asteroid.increment_id()

    @classmethod
    def increment_id(cls):
        cls._id += 1
        return cls._id

    @classmethod
    def rand_radius(cls):
        return randint(cls._MIN_RADIUS, cls._MAX_RADIUS)

    @classmethod
    def rand_pos(cls):
        return Vector(randint(cls._MIN_POS, cls._MAX_POS),
                randint(cls._MIN_POS, cls._MAX_POS),
                randint(cls._MIN_POS, cls._MAX_POS))

    @classmethod
    def rand_velocity(cls):
        return Vector(randint(cls._MIN_VELOCITY, cls._MAX_VELOCITY),
                randint(cls._MIN_VELOCITY, cls._MAX_VELOCITY),
                randint(cls._MIN_VELOCITY, cls._MAX_VELOCITY))

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

    def set_min_radius(self, r):
        self._MIN_RADIUS = r

    def set_max_radius(self, r):
        self._MAX_RADIUS = r

    def set_min_pos(self, pos):
        self._MIN_POS = pos

    def set_max_pos(self, pos):
        self._MAX_POS = pos

    def set_min_velocity(self, v):
        self._MIN_VELOCITY = v

    def set_max_velocity(self, v):
        self._MAX_VELOCITY = v

    def move(self):
        self._position.add(self._velocity)
        return self._position

    def __str__(self):
        return f"Asteroid ID: {self._id}" \
               f"\nCircumference: {self._circumference} " \
               f"\nPosition: {self._position} " \
               f"\nVelocity: {self._velocity} " \
               f"\nTimestamp: {self._timestamp}"

def main():
    pos = Vector(40, 40, 40)
    v1 = Vector(2, 2, 2)
    v2 = Vector(3, 3, 3)
    ast = Asteroid(3, pos, v1, datetime.now())
    v1.add(v2)
    ast.set_velocity(v1)
    print(ast)
    print(ast.move())

if __name__ == "__main__":
    main()
