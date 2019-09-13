from random import randint
from time import time
from asteroid import Asteroid

class Controller:

    def __init__(self, num):
        self._ast_list = []
        for i in range(num):
            #def __init__(self, radius, position, velocity, timestamp):
            temp = Asteroid(randint(1, 4),
                            [randint(0, 100), randint(0, 100), randint(0, 100)],
                            [randint(0, 100), randint(0, 100), randint(0, 100)],
                            time())
            self._ast_list.append(temp)

def main():
    con = Controller(3)
    for i in con._ast_list:
        print(f"{i}\n")


if __name__ == "__main__":
    main()



# The __init__(self, ...) method must create some Asteroids and store
# them in the list. Each Asteroid should be assigned a random
# circumference, starting position and starting velocity. Let's make 100
# Asteroids with circumferences in the range 1, 4, assuming that they are
# starting in a cube that is 100 metres per side, and each asteroid should
# have a velocity no greater than 5 metres per second in each direction.
# Where should these methods go? In the controller? Or should some helper
# COMP3522 Lab #1 Off With A Bang! 4
# methods be added to the Asteroid (or Vector class if you have one)?
# Consider encapsulation and information hiding.
