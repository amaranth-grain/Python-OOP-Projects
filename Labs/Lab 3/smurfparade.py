# class Node:
#     def __init__(self, data, node=None):
#         self._data = data
#         self._next = node
#
#     @property
#     def data(self):
#         return self._data
#
#     @property
#     def next(self):
#         return self._next
#
#     @next.setter
#     def next(self, node):
#         if type(node) == Node:
#             self._next = node
#
#
# class LinkedList:
#     def __init__(self, head=None):
#         self._head = head
#
#     def insert(self, data):
#         new_node = Node(data)
#         new_node.next = self._head


class SmurfParade:
    def __init__(self, smurfs=None, parade_name="The Blues"):
        """
        Initialises a parade of smurfs with the given name and members.
        :param parade_name: String
        :param smurfs: List
        """
        if smurfs is None:
            smurfs = []
        self.parade_name = parade_name
        self.smurfs = smurfs

    def __str__(self):
        """
        Format SmurfParade with name and list of parade members.
        :return:
        """
        output = ""
        for smurf in self.smurfs:
            output += f"{smurf} "
        return output
        # output = f"Let's welcome {self.parade_name} to the Parade!\n" \
        #          f"Parade members:\n"
        # for smurf in self.smurfs:
        #     output += f"\t* {smurf}\n"
        # return output

    def __len__(self):
        """
        Return the number of parade members.
        :return: int
        """
        return len(self.smurfs)

    def __contains__(self, name):
        """
        Checks to see if name is present in list of members.
        :param name: String
        :return: boolean
        """
        return name in self.smurfs

    def __iter__(self):
        """
        Allows SmurfParade to be iteratable over its members.
        :return: iterator
        """
        return iter(self.smurfs)

    def __reversed__(self):
        return reversed(self.smurfs)

# +linked list, and how to make it iterator
    # def __reversed__(self):
    #     for elem in 'Reversing: ' + self.seq[::-1]:
    #         yield elem

    def __getitem__(self, item):
        """
        Retrive Smurf by index using bracket notation.
        :param item: int
        :return: String
        """
        return self.smurfs[item]

    def count(self, name):
        """
        Count the number of times name appears in member list.
        :param name: String
        :return: int
        """
        # count = 0
        # for smurf in self.smurfs:
        #     if smurf == name:
        #         count += 1
        # return count
        return self.smurfs.count(name)

    def index(self, name):
        return self.smurfs.index(name)


def main():
    blues = SmurfParade(["12345", "Cerry", "Blue", "Cerry", "Royal",
                         "Skye", "Cerry"])
    print(f"__str__: {blues}\n")
    print(f"len(blues): {len(blues)}\n")
    print("Iterator: ")
    output = ""
    for smurf in blues:
        output += f"{smurf}\t"
    print(f"{output}\n")

    print("blues.count('Cerry')")
    print(blues.count("Cerry"))

    print("\nblues[3]")
    print(f"{blues[3]}\n")

    print(f"Index for Skye: ")
    print(blues.index("Skye"))

    print()
    print(reversed(blues))


if __name__ == "__main__":
    main()