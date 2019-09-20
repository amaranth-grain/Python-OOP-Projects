from item import Item

class Journal(Item):

    def __init__(self, title, call_no, author, num_copies, name,
                 issue, publisher):
        self._name = name
        self._issue = issue
        self._publisher = publisher
        super().__init__(title, call_no, author, num_copies)

    def __repr__(self):
        """
        Format for representing Journal object.
        :return: as String
        """
        return f"{super().__repr__()}" \
               f"Name: {self._name}\n" \
               f"Issue Number: {self._issue}\n" \
               f"Publisher: {self._publisher}\n\n"

    def __str__(self):
        """
        Format for representing Journal object.
        :return: as String
        """
        return f"{super().__repr__()}" \
               f"" \
               f"Name: {self._name}\n" \
               f"Issue Number: {self._issue}\n" \
               f"Publisher: {self._publisher}\n\n"


