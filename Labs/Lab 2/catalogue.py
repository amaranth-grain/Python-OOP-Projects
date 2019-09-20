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
        return [v.get_title() for k, v in self._list.items()]

    def get_call_no_list(self):
        """
        Return list of Item call numbers in Catalogue.
        :return: list of Strings
        """
        return [item for item in self._list]

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
            return f"\nClosest matches:\n {temp}\n"
        else:
            return "No matches found."

    def add_item(self):
        """
        Add item to Catalogue if it's not already in the
        collection.
        """
        item = LibraryItemGenerator.create_item()
        if item.get_call_no() not in self._list:
            self._list[item.get_call_no()] = item
            return "\nItem has been added.\n"

    def remove_item(self, call_no):
        """
        Remove Item from Library's Catalogue by checking
        against call number.
        :param call_no: as String
        :return: as String
        """
        if call_no in self._list:
            del self._list[call_no]
            return "\nItem has been removed.\n"
        else:
            return "\nThis item is not currently in the catalogue. " \
                   "Try again."
