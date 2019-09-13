import math
from random import randint
from datetime import datetime
from vector import Vector

'''
Asteroid has circumference (calculated from radius) and timestamp on when it was
created as attributes as records, but methods do not interact with these
instance variables.
Position and velocity are Vectors in 3D space and can be added.
'''
class Asteroid:
    # Lifetime Asteroid ID of all Asteroids created
    _id = 0
    # Lower range for Asteroid radius
    _MIN_RADIUS = 1
    # Upper range for Asteroid radius
    _MAX_RADIUS = 4
    # Lower range for Asteroid position
    _MIN_POS = 0
    # Upper range for Asteroid position
    _MAX_POS = 100
    # Lower range for Asteroid velocity
    _MIN_VELOCITY = -5
    # Upper range for Asteroid velocity
    _MAX_VELOCITY = 5

    ''' 
    Create Asteroid object.
    :param radius: int
    :param position: Vector(x, y, z)
    :param velocity: Vector(x, y, z)
    :param timestamp: datetime
    '''
    def __init__(self, radius, position, velocity, timestamp):
        self._circumference = 2 * math.pi * radius
        self._position = position
        self._velocity = velocity
        self._timestamp = timestamp
        self._id = Asteroid.increment_id()

    ''' Return Asteroid ID (lifetime of Asteroids created) as int'''
    @classmethod
    def increment_id(cls):
        cls._id += 1
        return cls._id

    '''Return radius as int determined by min and max radius'''
    @classmethod
    def rand_radius(cls):
        return randint(cls._MIN_RADIUS, cls._MAX_RADIUS)

    '''Return position as Vector determined by min and max position'''
    @classmethod
    def rand_pos(cls):
        return Vector(randint(cls._MIN_POS, cls._MAX_POS),
                randint(cls._MIN_POS, cls._MAX_POS),
                randint(cls._MIN_POS, cls._MAX_POS))

    '''Return velocity as Vector determined by min and max velocity'''
    @classmethod
    def rand_velocity(cls):
        return Vector(randint(cls._MIN_VELOCITY, cls._MAX_VELOCITY),
                randint(cls._MIN_VELOCITY, cls._MAX_VELOCITY),
                randint(cls._MIN_VELOCITY, cls._MAX_VELOCITY))

    '''Return position as Vector'''
    def get_position(self):
        return self._position

    ''' Return velocity as Vector in m/s '''
    def get_velocity(self):
        return self._velocity

    '''
    Set Asteroid position.
    :param position: Vector
    '''
    def set_position(self, position):
        self._position = position

    '''
    Set Asteroid velocity.
    :param velocity: Vector
    '''
    def set_velocity(self, velocity):
        self._velocity = velocity

    '''
    Set lower range for asteroid radius.
    :param r: int
    '''
    def set_min_radius(self, r):
        self._MIN_RADIUS = r

    '''
        Set upper range for asteroid radius.
        :param r: int
    '''
    def set_max_radius(self, r):
        self._MAX_RADIUS = r

    '''
        Set lower range for asteroid position.
        :param pos: int
    '''
    def set_min_pos(self, pos):
        self._MIN_POS = pos

    '''
        Set upper range for asteroid position.
        :param pos: int
    '''
    def set_max_pos(self, pos):
        self._MAX_POS = pos

    '''
        Set lower range for asteroid velocity.
        :param v: int
    '''
    def set_min_velocity(self, v):
        self._MIN_VELOCITY = v

    '''
        Set upper range for asteroid velocity.
        :param v: int
    '''
    def set_max_velocity(self, v):
        self._MAX_VELOCITY = v

    '''
        Move Asteroid in 1 second increment based on current velocity.
        Return position as Vector
    '''
    def move(self):
        self._position.add(self._velocity)
        return self._position

    ''' Format Asteroid with unique ID, circumference, pos, velocity, and time created. '''
    def __str__(self):
        return f"Asteroid ID: {self._id}" \
               f"\nCircumference: {self._circumference} " \
               f"\nPosition: {self._position} " \
               f"\nVelocity: {self._velocity} " \
               f"\nTimestamp: {self._timestamp}"

''' Drive the program. '''
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
