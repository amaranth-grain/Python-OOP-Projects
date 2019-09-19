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
        lst = []
        for item in self._book_list:
            lst.append(item.get_title())
        if book.get_title() not in lst:
            self._book_list.append(book)

    '''
    If book with call number exists, remove from library.
    :param call_no as String
    '''
    def remove_book(self, call_no):
        # Create list of call numbers.
        lst = []
        for item in self._book_list:
            lst.append(item.get_call_no())
        if call_no in lst:
            i = lst.index(call_no)
            checked_book = self._book_list[i]
            self._book_list.pop(lst.index(call_no))
            return f"\n{checked_book.get_title()} has been removed from" \
                   f" the collection.\n"
        else:
            return "\nThis book is not in our collection.  Try again.\n"

    '''
    Check out book from call number if there are
    copies available.
    :param call_no as String
    '''
    def check_out(self, call_no):
        # Create list of call numbers.
        lst = []
        for item in self._book_list:
            lst.append(item.get_call_no())
        # If call number is registered, check copies available.
        if call_no in lst:
            i = lst.index(call_no)
            checked_book = self._book_list[i]
            copies = checked_book.get_copies()
            if copies > 0:
                checked_book.set_copies(copies - 1)
                return f"\nThank you for borrowing {checked_book.get_title()}.\n"
            else:
                return "\nThere are no copies available.\n"

    def return_book(self, call_no):
        # Create list of call numbers.
        lst = []
        for item in self._book_list:
            lst.append(item.get_call_no())
        # If call number is registered, check copies available.
        if call_no in lst:
            i = lst.index(call_no)
            checked_book = self._book_list[i]
            copies = checked_book.get_copies()
            checked_book.set_copies(copies + 1)
            return f"\nThank you for returning {checked_book.get_title()}.\n"
        else:
            return "\nThis book is not part of our collection.\n"

    def display_available_books(self):
        for item in self._book_list:
            print(item)

    '''
    Return formatted string representation.
    '''
    def __str__(self):
        return str(self._book_list)


def test_choice(input):
    return f"You have decided to {input} a book\n"


def main():
    display_menu = True
    book1 = Book("Provenance", "342.2", "Ann Leckie", 10)
    book2 = Book("Ancillary Justice", "342.1", "Ann Leckie", 2)
    book3 = Book("And Then There Were None", "123.2", "AC", 0)
    book4 = Book("Hungry Caterpillar", "765.2", "McPerson", 0)

    vpl = Library([book1, book2, book3, book4])
    print(vpl.display_available_books())
    print(vpl.find_books("Provenandfdce"))
    # print(vpl.display_available_books())

    # display_menu = False
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

        if choice == 7:
            display_menu = False
        elif choice == 6:
            vpl.display_available_books()
        elif choice == 2:
            title = input("Enter book title: ")
            call_no = input("Enter call number: ")
            author = input("Enter author name: ")
            num_copies = input("Enter the number of copies: ")
            temp_book = Book(title, call_no, author, num_copies)
            vpl.add_book(temp_book)
            print(f"\n{title} has been added to our collection. Thank you.\n")
        elif choice not in range(1, 6):
            print("\nInvalid input.  Try again.\n")
        else:
            par = input("Enter parameter: ")
            input_dict = {1: vpl.find_books(par), 3: vpl.remove_book(par), 4: vpl.check_out(par), 5: vpl.return_book(par)}
            print(input_dict.get(choice))



if __name__ == "__main__":
    main()