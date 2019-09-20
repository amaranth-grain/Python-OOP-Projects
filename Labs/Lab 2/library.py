from difflib import get_close_matches

from book import Book

class Library():
    """
        Initialise Library with list of books.
        :param book_list as a list of Books
    """
    def __init__(self, book_list):
        self._book_list = book_list

    '''
        Return list of book titles in catalogue.
    '''
    def get_title_list(self):
        return [book.get_title() for book in self._book_list]

    '''
        Return list of call numbers in catalogue.
    '''
    def get_call_no_list(self):
        return [book.get_call_no() for book in self._book_list]

    '''
        Find book in catalogue based on title.
        :param title as String
    '''
    def find_books(self, title):
        close_matches = get_close_matches(title, self.get_title_list())
        if title in self.get_title_list():
            return f"{title} is available in the library catalogoue."
        elif len(close_matches) > 0:
            for title in close_matches:
                temp = str(f"* {title}")
            return temp
        else:
            return "No matches found."

    '''
        Add book to catalogue if it's not already in the
        collection.
    '''
    def add_book(self, book):
        if book.get_call_no() not in self.get_call_no_list():
            self._book_list.append(book)
            return f"{book.get_title()} has been added to the " \
                   "catalogue."
        else:
            return f"{book.get_title()} is already in the catalogue."

    '''
        Remove book from library catalogue by checking call number.    
    '''
    def remove_book(self, call_no):
        if call_no in self.get_call_no_list():
            i = self.get_call_no_list().index(call_no)
            self._book_list.pop(i)
            return "Book has been removed."
        else:
            return "This book is not currently in the catalogue. " \
                   "Try again."

    '''
        Check out book in catalogue if there are copies available.
    '''
    def check_out(self, call_no):
        lst = self.get_call_no_list()
        if call_no in lst:
            i = lst.index(call_no)
            copies = self._book_list[i].get_copies()
            if copies > 0:
                self._book_list[i].set_copies(copies - 1)
                return "The book has been checked out."
            elif copies == 0:
                return "No copies available at the moment."
        else:
            return "Book is not in catalogue."

    '''
        If book is in the catalogue, return it to Library.
    '''
    def return_book(self, call_no):
        if call_no in self.get_call_no_list():
            i = self.get_call_no_list().index(call_no)
            copies = self._book_list[i].get_copies()
            self._book_list[i].set_copies(copies + 1)
            return "Book has been returned."
        else:
            return "You cannot return this book. It is not in " \
                   "the catalogue."

    def display_available_books(self):
        print(*self._book_list)


def main():
    b1 = Book("Provenance", "432.2", "Anne Leckie", 1)
    b2 = Book("Ancillary Justice", "234.3A", "Anne Leckie", 10)
    b3 = Book("Ancillary Sword", "234.3B", "Anne Leckie", 1)
    b4 = Book("Ancillary Mercy", "234.4", "Anne Leckie", 2)
    vpl = Library([b1, b2, b3, b4])
    # print(vpl.get_call_no_list())
    # print(vpl.remove_book("432.2"))
    # print(vpl.get_call_no_list())
    display_menu = True

    while display_menu:
        print("What would you like to do?")
        print("1. Find a book by title")
        print("2. Add book to collection")
        print("3. Remove book from collection")
        print("4. Check out a copy")
        print("5. Return your copy")
        print("6. Display all available books")
        print("7. Quit menu")

        choice = int(input("Select action: "))

        if choice == 2:
            title = input("Enter book title: ")
            call_no = input("Enter call number: ")
            author = input("Enter author name: ")
            num_copies = input("Enter the number of copies: ")
            temp_book = Book(title, call_no, author, num_copies)
            vpl.add_book(temp_book)
        elif choice == 6:
            vpl.display_available_books()
        elif choice == 7:
            display_menu = False
        elif choice not in range(1, 6):
            print("\nInvalid input.  Try again.\n")
        else:
            par = input("Enter parameter: ")
            input_dict = {1: vpl.find_books,
                          3: vpl.remove_book,
                          4: vpl.check_out,
                          5: vpl.return_book}

            print(input_dict.get(choice)(par))

if __name__ == "__main__":
    main()