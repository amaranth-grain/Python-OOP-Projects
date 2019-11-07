"""
Module for the creation of Catalogue Items using the
Factory design pattern.
"""
from abc import ABC, abstractmethod
from item import Item, Book, Journal, DVD


class NegativeNumberError(Exception):
    """
    Error when an attribute or input should not be a negative value (e.g.
    counting the number of objects.)
    """
    def __init__(self, num):
        super().__init__(f"The number of copies must be a positive integer. "
                         f"You entered {num}")
        self.num = num


class ItemFactory(ABC):
    """
    Defines a factory interface for creating Items.
    """

    @abstractmethod
    def create_item(self) -> Item:
        pass

    @staticmethod
    def get_basic_item_dict(self):
        title = input("Enter title: ").title()
        call_no = input("Enter call number: ").upper()
        author = input("Enter author(s): ").title()
        try:
            num_copies = int(input("Enter number of copies: "))
            if num_copies < 1:
                raise NegativeNumberError(num_copies)
        except ValueError as e:
            print(f"Exception: {e}")
        else:
            return {
                "title": title,
                "call_no": call_no,
                "author": author,
                "num_copies": num_copies
            }


class BookFactory(ItemFactory):
    """
    Create Book objects.
    """
    def create_item(self) -> Item:
        info_dict = self.get_basic_item_dict(self)
        return Book(**info_dict)


class JournalFactory(ItemFactory):
    """
    Create Journal Objects
    """

    def create_item(self) -> Item:
        info_dict = self.get_basic_item_dict(self)
        journal_name = input("Enter journal name: ").title()
        journal_issue = input("Enter journal issue: ").title()
        journal_publisher = input("Enter journal publishing house: ").title()
        return Journal(**info_dict,
                       journal_name=journal_name,
                       journal_issue=journal_issue,
                       journal_publisher=journal_publisher)


class DVDFactory(ItemFactory):
    """
    Create Journal Objects
    """

    def create_item(self) -> Item:
        info_dict = self.get_basic_item_dict(self)
        dvd_release = input("Enter release date: ")
        try:
            dvd_region = int(input("Enter DVD region: "))
            if dvd_region < 1:
                raise ValueError
        except ValueError as e:
            print("DVD Region must be a positive integer.")
        else:
            return DVD(**info_dict,
                       dvd_release=dvd_release,
                       dvd_region=dvd_region)


class LibraryItemGenerator:
    factory_type = {
        1: BookFactory,
        2: DVDFactory,
        3: JournalFactory
    }

    @staticmethod
    def pick_item_creation_type(choice):
        """
        Return the specified Factory based on user choice.
        :param choice: int
        :return: ItemFactory
        """
        return LibraryItemGenerator.factory_type.get(choice)()


def main():
    # book_factory = BookFactory()
    # book = book_factory.create_item()
    # print(book)

    journal_factory = JournalFactory()
    journal = journal_factory.create_item()
    print(journal)


if __name__ == "__main__":
    main()
