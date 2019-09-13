import time
from datetime import datetime
from asteroid import Asteroid

'''Create and track Asteroids in field.'''
class Controller:
    # One second in microseconds
    _ONE_SECOND = 1000000

    ''' 
    Create Controller to track Asteroids.
    :param num as int (Asteroids to create)
    '''
    def __init__(self, num):
        self._ast_list = []
        for i in range(num):
            # Asteroid def __init__(self, radius, position, velocity, timestamp)
            temp = Asteroid(Asteroid.rand_radius(),
                            Asteroid.rand_pos(),
                            Asteroid.rand_velocity(),
                            time.time())
            self._ast_list.append(temp)

    ''' 
    Simulate Asteroid movement in one second increments.
    :param seconds as int (Track Asteroids under Controller for that many seconds)
    '''
    def simulate(self, seconds):
        cur = datetime.now()
        diff = (Controller._ONE_SECOND - cur.microsecond) / Controller._ONE_SECOND
        time.sleep(diff)

        for i in range(seconds):
            for ast in self._ast_list:
                print(f"============== {datetime.now()} ==============")
                ast.move()
                print(ast)
                time.sleep(1)

'''Drive the program.'''
def main():
    con = Controller(100)
    con.simulate(2)

if __name__ == "__main__":
    main()
