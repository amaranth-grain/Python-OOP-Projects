"""
Module for the representation of Catalogue Items using the
Factory design pattern.
"""
# Do the methods in ABC have to be abstract?

from abc import ABC, abstractmethod


class Item(ABC):
    """
    Represents an Item that is stored in a Catalogue.
    """
    default_item_data = {
        'title': 'Title Not Available',
        'call_no': 'Call Number Not Assigned',
        'author': 'Author Not Available',
        'num_copies': 0,
        'journal_name': "Journal Name Not Available",
        'journal_issue': "Journal Issue Not Available",
        'journal_publisher': "Journal Publisher Not Available",
        'dvd_release': "DVD Release Date Not Available",
        'dvd_region': "DVD Region Information Not Available"
    }

    def __init__(self, **kwargs) -> None:
        """
        Initialises Item object.
        :param kwargs: Variable arguments accepted. See default_item_data.
        """
        self._item = Item.default_item_data
        for k, v in kwargs.items():
            self._item[k] = v



    # def __init__(self, title: str, call_no: str,
    #              author: str, num_copies: int) -> None:
    #     """
    #     Initialises Item object.
    #     :param title: String
    #     :param call_no: string
    #     :param author: String
    #     :param num_copies: int
    #     """
    #     self._title = str(title).title()
    #     self._call_no = str(call_no)
    #     self._author = str(author).title()
    #     if not isinstance(num_copies, int):
    #         raise TypeError("The number of copies must be an integer.")
    #     else:
    #         self._num_copies = num_copies

    @property
    def call_no(self) -> str:
        """
        Get the Item call number.
        :return: as String
        """
        return self._item.get("call_no")

    @property
    def title(self) -> str:
        """
        Return title of Item.
        :return: as String
        """
        return self._item.get("title")

    @property
    def num_copies(self) -> int:
        """
        Return number of copies available.
        :return: as int
        """
        return self._item.get("num_copies")

    @num_copies.setter
    def num_copies(self, num_copies: int) -> None:
        self._item["num_copies"] = num_copies

    def check_availability(self) -> bool:
        """
        Return true if there is at least 1 copy.
        :return: as boolean
        """
        return self._item.get("num_copies") > 0

    def __str__(self) -> str:
        """
        String format for Item
        :return: as String
        """
        return f"Title: {self._item.get('title')}\n" \
               f"Call Number: {self._item.get('call_no')}\n" \
               f"Author: {self._item.get('author')}\n" \
               f"Copies Available: {self._item.get('num_copies')}"


class Book(Item):
    """
    Represents a Book Item that is stored in a Catalogue.
    """

    def __str__(self) -> str:
        """
        String format for Book Item
        :return: as String
        """
        return f"Book {super().__str__()}\n\n"


class Journal(Item):
    """
    Represents a Journal Item that is stored in a Catalogue.
    """

    def __str__(self) -> str:
        """
        String format for Journal Item
        :return: as String
        """
        return f"Journal {super().__str__()}\n" \
               f"Joural Name: {self._item.get('journal_name')}\n" \
               f"Journal Issue: {self._item.get('journal_issue')}\n" \
               f"Journal Publisher: {self._item.get('journal_publisher')}\n\n"


class DVD(Item):
    """
    Represents a DVD Item that is stored in a Catalogue.
    """

    def __str__(self) -> str:
        """
        String format for DVD Item
        :return: as String
        """
        return f"DVD {super().__str__()}\n" \
               f"Release Date: {self._item.get('dvd_release')}\n" \
               f"Region: {self._item.get('dvd_region')}\n\n"


def main():
    dvd = DVD(title="Mad Max Fury Road", call_no="329.A",
              author="George Miller", num_copies=10,
              dvd_release="5/15/2015", dvd_region=1)

    book = Book(title="Ancillary Justice", call_no="653.2",
                author="Ann Leckie", num_copies=15)

    journal = Journal(title="Sleep Deprivation and False Memories",
                      call_no="451.2",
                      author="Lawrence Patihis, Elizabeth F. Loftus, "
                             "Holly C. Lewis, Kimberly M. Fenn",
                      num_copies=1,
                      journal_name="Psychology Journal",
                      journal_issue="Q2 2019",
                      journal_publisher="AP Publishing House")

    print(f"{dvd}\n"
          f"{book}\n"
          f"{journal}")


if __name__ == "__main__":
    main()
