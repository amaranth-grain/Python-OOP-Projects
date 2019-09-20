from item import Item

class Dvd(Item):
    """
    Represent a Dvd Item in Library Catalogue.
    """

    def __init__(self, title, call_no, author, num_copies, release,
                 region):
        """
        Initialises a Dvd object.
        :param title: as String
        :param call_no: as String
        :param author: as String
        :param num_copies: as int
        :param release: as String
        :param region: as String
        """
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