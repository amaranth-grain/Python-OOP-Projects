from book import Book

class Library():
    """
        Library is responsible for checking out and returning
        books.  Library has a Catalogue responsible for searching,
        adding, and removing from Catalogue.
    """
    def __init__(self, list):
        """
        Initialise Library with list of Items.
        :param list: a Catalogue
        """
        self._list = list

    def get_cat(self):
        """
        Return Library Catalogue.
        :return: Catalogue
        """
        return self._list

    def get_list(self):
        """
        Return Catalogue list of Items.
        :return: a list of Items
        """
        return self._list.get_list()

    def get_title_list(self):
        """
        Return list of titles in Catalogue.
        :return: list of Strings
        """
        return self._list.get_title_list()

    '''
        Return list of call numbers in Catalogue.
    '''
    def get_call_no_list(self):
        return self._list.get_call_no_list()

    def search(self, title):
        """
        Search for Item in Catalogue
        :param title: a String
        :return: a String message on results of search
        """
        return self._list.search(title)

    def check_out(self, call_no):
        """
        Check out an Item from Catalogue if
        a) Item exists in Catalogue and
        b) There is at least 1 copy available
        :param call_no: as String
        :return: a String message on result of checking out.
        """
        cat = self._list.get_list()
        if call_no in cat:
            copies = cat[call_no].get_copies()
            if copies > 0:
                cat[call_no].set_copies(copies - 1)
                return "\nItem has been checked out.\n"
            elif copies == 0:
                return "\nNo copies available at this time.\n"
        else:
            return "\nYou cannot check out this item. No copies " \
                   "available at this time.\n"
        # lst = self.get_call_no_list()
        # if call_no in lst:
        #     i = lst.index(call_no)
        #     copies = self._list[i].get_copies()
        #     if copies > 0:
        #         self._list[i].set_copies(copies - 1)
        #         return "The book has been checked out."
        #     elif copies == 0:
        #         return "No copies available at the moment."
        # else:
        #     return "Book is not in catalogue."

    def return_item(self, call_no):
        """
        Return Item to Library if Item is available in Catalogue.
        :param call_no: as String
        :return: a String message on the results of returning an Item
        """
        cat = self._list.get_list()
        if call_no in cat:
            copies = cat[call_no].get_copies()
            cat[call_no].set_copies(copies + 1)
            return "\nItem has been returned.\n"
        else:
            return "\nYou cannot return this item. It is not in " \
                   "the catalogue.\n"

    def display_available_books(self):
        """
        Display a formatted list of all Items in Catalogue
        :return: a formatted String
        """
        for k, v in self._list.get_list().items():
            print(v)


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