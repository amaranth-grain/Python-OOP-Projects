""" Represent Node and LinkedList as Smurfs and SmurfParade
through Pythonic sequence protocol implementation. """


class Smurf:
    """
    Represent a single Smurf.
    """
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

    def __str__(self):
        return self.name


class SmurfParade:
    """
    Represent a parade of Smurfs as a linked list,
    demonstrating the sequence protocol within Python.
    """
    def __init__(self, leader=None):
        self._leader = leader

    def __len__(self):
        """
        Return the number of Smurfs in the parade.
        :return: int
        """
        curr = self._leader
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count

    def append(self, smurf):
        """
        Add a Smurf at the end of the parade.
        :param smurf: Smurf
        :return: None
        """
        curr = self._leader
        while curr.next is not None:
            curr = curr.next
        curr.next = smurf

    def __contains__(self, smurf_name):
        """
        Return whether there is at least 1 Smurf with the given name.
        :param smurf_name: String
        :return: boolean
        """
        curr = self._leader
        while curr.next is not None:
            if smurf_name == curr.name:
                return True
            curr = curr.next
        return False

    def __getitem__(self, num):
        """
        Allows retrieval of Smurf based on bracket notation
        e.g. parade[0] returns the parade leader.
        :param num:
        :return:
        """
        curr = self._leader
        while num > 0:
            curr = curr.next
            num -= 1
        return curr

    def count(self, smurf_name):
        """
        Count the number of Smurfs with the given name.
        :param smurf_name: String
        :return: int
        """
        curr = self._leader
        count = 0
        while curr.next is not None:
            if smurf_name == curr.next.name:
                count += 1
            curr = curr.next
        return count

    def index(self, smurf_name):
        """
        Return the index of the first Smurf that has the given name.
        :param smurf_name: String
        :return: int
        """
        curr = self._leader
        i = 0
        while curr.next is not None:
            if smurf_name == curr.name:
                return i
            curr = curr.next
            i += 1
        return -1

    def __reversed__(self):
        rev = list()
        curr = self._leader
        while curr is not None:
            rev.append(curr.name)
            curr = curr.next
        return reversed(rev)

    def __iter__(self):
        """
        Allow SmurfParade to be iterated over.
        e.g. for smurf in parade:
                print(smurf)
        """
        curr = self._leader
        while curr is not None:
            yield curr.name
            curr = curr.next


def main():
    blue = Smurf("Blue")
    turq = Smurf("Turquoise")
    turq2 = Smurf("Turquoise")
    cerry = Smurf("Cerulean")
    parade = SmurfParade(blue)
    parade.append(turq)
    parade.append(cerry)
    parade.append(turq2)

    print("\n\nLet's check out the SmurfParade!\n")
    print("Leader: Blue -> Member: Turquoise -> Member: Cerulean"
          "-> Member: Turquoise\n")

    print(f"len(parade): {len(parade)}\n")

    print(f"Is Cerulean in the parade?")
    print("Cerulean" in parade)
    print("*" * 30)

    print(f"\nparade[1]: {parade[1]}\n")
    print("*" * 30)
    print(f"\nparade.count('Turquoise'): {parade.count('Turquoise')}\n")
    print("*" * 30)
    # print(f"\nreversed(parade):\n {reversed(parade)}")
    for smurf in reversed(parade):
        print(smurf)

    print()
    print("*" * 30)

    print(f"parade.index('Cerulean'): {parade.index('Cerulean')}\n")

    print("*" * 30)
    for smurf in parade:
        print(smurf)


if __name__ == "__main__":
    main()