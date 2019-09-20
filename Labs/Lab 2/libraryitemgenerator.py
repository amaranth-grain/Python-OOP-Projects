from book import Book
from journal import Journal

class LibraryItemGenerator:

    @staticmethod
    def create_item(self):
        print("What type of item would you like to add to"
              "the library catalogue?")
        print("1. Book")
        print("2. DVD")
        print("3. Scientific Journal")

        choice = int(input("Select type of item: "))

        title = input("Enter book title: ")
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
            issue = input("Enter issue number: ")
            publisher = input("Enter publisher: ")
            return Journal(title, call_no, author, num_copies, issue,
                           publisher)
