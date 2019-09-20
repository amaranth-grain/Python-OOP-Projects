from book import Book
from dvd import Dvd
from journal import Journal

class LibraryItemGenerator:
    """
    Prompt for user to specify type of Library Item to generate.
    Create Item based on user input.
    """

    @staticmethod
    def create_item():
        """
        Create Item based on user input.
        :return: as Item
        """
        print("What type of item would you like to add to"
              "the library catalogue?")
        print("1. Book")
        print("2. DVD")
        print("3. Scientific Journal")

        choice = int(input("Select type of item: "))

        title = input("Enter title: ")
        call_no = input("Enter call number: ")
        author = input("Enter author name: ")
        num_copies = input("Enter the number of copies: ")

        if choice == 1:
            return Book(title, call_no, author, num_copies)

        if choice == 2:
            release = input("Enter release date: ")
            region = input("Enter region code: ")
            return Dvd(title, call_no, author, num_copies, release,
                       region)

        if choice == 3:
            name = input("Enter name of publication: ")
            issue = input("Enter issue number: ")
            publisher = input("Enter publisher: ")
            return Journal(title, call_no, author, num_copies,
                           name, issue, publisher)
