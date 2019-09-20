from difflib import get_close_matches
from libraryitemgenerator import LibraryItemGenerator

class Catalogue:
    """
    Catalogue responsible for curating Lbirary collection
    of Items.
    """

    def __init__(self, list):
        """
        Initialise Catalogue with list of Items.
        :param list: as list of Items
        """
        self._list = list

    def get_list(self):
        """
        Return Catalogue list of Items.
        :return: list of Items
        """
        return self._list

    def get_title_list(self):
        """
        Return list of Item titles in Catalogue
        :return: list of Strings
        """
        return [item.get_title() for item in self._list]

    def get_call_no_list(self):
        """
        Return list of Item call numbers in Catalogue.
        :return: list of Strings
        """
        return [item.get_call_no() for item in self._list]

    def search(self, title):
        """
        Find Item in Catalogue based on title.
        :param title: as String
        :return: String
        """
        close_matches = get_close_matches(title, self.get_title_list())
        if title in self.get_title_list():
            return f"{title} is available in the library catalogue."
        elif len(close_matches) > 0:
            for title in close_matches:
                temp = str(f"* {title}")
            return temp
        else:
            return "No matches found."

    def add_item(self):
        """
        Add item to Catalogue if it's not already in the
        collection.
        """
        item = LibraryItemGenerator.create_item()
        if item.get_call_no() not in self._list.get_call_no_list():
            self._list.append(item)

    def remove_book(self, call_no):
        """
        Remove Item from Library's Catalogue by checking
        against call number.
        :param call_no: as String
        :return: as String
        """
        if call_no in self.get_call_no_list():
            i = self.get_call_no_list().index(call_no)
            self._list.pop(i)
            return "Book has been removed."
        else:
            return "This book is not currently in the catalogue. " \
                   "Try again."
