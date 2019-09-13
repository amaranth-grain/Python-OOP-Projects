import time
from datetime import datetime
from asteroid import Asteroid

class Controller:
    # One second in microseconds
    _ONE_MICROSECOND = 0.000001

    def __init__(self, num):
        self._ast_list = []
        for i in range(num):
            # def __init__(self, radius, position, velocity, timestamp):
            temp = Asteroid(Asteroid.rand_radius(),
                            Asteroid.rand_pos(),
                            Asteroid.rand_velocity(),
                            time.time())
            self._ast_list.append(temp)

    def simulate(self, seconds):
        cur = datetime.now()
        start = datetime(cur.year, cur.month, cur.day, cur.hour, cur.minute, cur.second + 1)
        while datetime.now() < start:
            time.sleep(Controller._ONE_MICROSECOND)

        for i in range(seconds):
            for ast in self._ast_list:
                ast.move()
                print(f"============== {datetime.now()} ==============")
                print(ast)
                time.sleep(1)


def main():
    con = Controller(2)
    con.simulate(2)

if __name__ == "__main__":
    main()
