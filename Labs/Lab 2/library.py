from difflib import get_close_matches
from book import Book

'''
Maintain, add, and remove books from collection.
Check out books through its call number if available.
'''
class Library:
    '''
    Initialiser for Library.
    '''
    def __init__(self, book_list):
        self._book_list = book_list

    '''
    Return true if book is in collection.
    Return list of closest matches if there are any.
    Return prompt to try again if no matches found.
    :param title as String
    '''
    def find_books(self, title):
        book_titles = []
        for item in self._book_list:
            book_titles.append(item.get_title())

        if title in book_titles:
            return True
        elif len(get_close_matches(title, book_titles)) > 0:
            return f"Closest Matches: " \
                   f"{get_close_matches(title, book_titles)}\n"
        else:
            return "No available matches. Try again."

    '''
    Add book to library collection if it's not already listed.
    :param book as Book
    '''
    def add_book(self, book):
        if book not in self._book_list:
            self._book_list.append(book)

    '''
    If book with call number exists, remove from library.
    :param call_no as String
    '''
    def remove_book(self, call_no):
        lst = self.get_call_no_list()
        if call_no in lst:
            self._book_list.pop(lst.index(call_no))

    '''
    Helper function to get a list of call numbers 
    within library collection.
    '''
    def get_call_no_list(self):
        call_no_list = []
        for item in self._book_list:
            call_no_list.append(item._call_no)
        return call_no_list
    '''
    Return formatted string representation.
    '''
    def __str__(self):
        return str(self._book_list)

def main():
    book1 = Book("Provenance", "342.2", "Ann Leckie", 20)
    book2 = Book("Ancillary Justice", "342.2", "Ann Leckie", 2)
    vpl = Library([book1, book2])
    vpl.remove_book("123.3")
    print(vpl)


if __name__ == "__main__":
    main()