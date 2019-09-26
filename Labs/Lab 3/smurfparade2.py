class Smurf:
    def __init__(self, name, next=None):
        self._name = name
        self._next = next

    @property
    def name(self):
        return self._name

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, smurf):
        if type(smurf) == Smurf:
            self._next = smurf


class SmurfParade:
    def __init__(self, leader=None):
        self._leader = leader

    def __len__(self):
        curr = self._leader
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count


    # contains(self, item)
    # iter(self)
    # getitem(self, key)
    # count(self, item)
    # index(self, item)
    # reversed(self)

def main():
    blue = Smurf("Blue")
    turq = Smurf("Turquoise")
    cerry = Smurf("Cerulean")
    parade = SmurfParade(blue)
    print(len(parade))

if __name__ == "__main__":
    main()