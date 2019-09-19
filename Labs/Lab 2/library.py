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
            print(f"{title} is available in the library catalogoue.")
        elif len(close_matches) > 0:
            print("Did you mean...")
            for title in close_matches:
                print(f"* {title}")
        else:
            print("No matches found.")

    '''
        Add book to catalogue if it's not already in the
        collection.
    '''
    def add_book(self, book):
        if book.get_call_no() not in self.get_call_no_list():
            self._book_list.append(book)
            print(f"{book.get_title()} has been added to the catalogue.")
        else:
            print(f"{book.get_title()} is already in the catalogue.")

    '''
        Remove book from library catalogue by checking call number.    
    '''
    def remove_book(self, call_no):
        if call_no in self.get_call_no_list():
            i = self.get_call_no_list().index(call_no)
            self._book_list.pop(i)
            print("Book has been removed.")
        else:
            print("This book is not currently in the catalogue. "
                  "Try again.")

    '''
        Check out book in catalogue if there are copies available.
    '''
    def check_out(self, call_no):
        if call_no in self.get_call_no_list():
            i = self.get_call_no_list().index(call_no)
            copies = self._book_list[i].get_copies()
            if copies > 0:
                self._book_list[i].set_copies(copies - 1)
                print("Book is checked out.")
            elif copies == 0:
                print("There are no copies available.")
        else:
            print("This book is not in the catalogue.")

    '''
        If book is in the catalogue, return it to Library.
    '''
    def return_book(self, call_no):
        if call_no in self.get_call_no_list():
            i = self.get_call_no_list().index(call_no)
            copies = self._book_list[i].get_copies()
            self._book_list[i].set_copies(copies + 1)
            print("Book has been returned.")
        else:
            print("This book is not in the catalogue.")

    def display_available_books(self):
        print(*self._book_list)


#iterate over attribute in list of objects
#[object, object, object]
#iterate over object.title

#Is find_books() the same as search() in Part 2 of the lab

#For the add book function, how are we checking if it's the
#same book?  By call no

def main():
    b1 = Book("Provenance", "234.3", "Anne Leckie", 0)
    b2 = Book("Ancillary Justice", "234.3A", "Anne Leckie", 10)
    vpl = Library([b1, b2])
    vpl.display_available_books()

if __name__ == "__main__":
    main()