from item import Item

class Dvd(Item):

    def __init__(self, title, call_no, author, num_copies, release,
                 region):
        self._release = release
        self._region = region
        super().__init__(title, call_no, author, num_copies)

    def __repr__(self):
        """
        Format for representing Dvd object.
        :return: as String
        """
        return f"{super().__repr__()}" \
               f"Release date: {self._release}\n" \
               f"Region Code: {self._region}\n\n"

    def __str__(self):
        """
        Format for representing Dvd object.
        :return: as String
        """
        return f"{super().__repr__()}" \
               f"Release Date: {self._release}\n" \
               f"Region Code: {self._region}\n\n"