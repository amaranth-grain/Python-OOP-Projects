"""
Client side that uses the Factory pattern.
Library holds a Catalogue, which can create items.  The Library has no
dependencies on Items as a result of the design pattern.
"""
from book import Book
from difflib import get_close_matches
from libraryitemgenerator import LibraryItemGenerator


class Catalogue:
    """
    Catalogue responsible for curating collection
    of Items.
    """
    def __init__(self):
        """
        Initialise Catalogue with dictionary.
        Dictionary: {key (call_no): value (Item)}
        """
        self._data = {}

    @property
    def data(self):
        """
        Return entire Catalogue data as a dictionary.
        :return: dictionary of Items
        """
        return self._data

    def get_all_titles(self):
        """
        Return list of Item titles in Catalogue
        :return: list of Strings
        """
        return [item.title for item in self._data.values()]

    def get_all_call_nos(self):
        """
        Return list of all call numbers in Catalogue.
        :return:
        """
        return [item.call_no for item in self._data.values()]

    def search(self, title):
        """
        Find Item in Catalogue based on title.
        :param title: as String
        :return: String
        """
        title = title.title()
        output = f"No books called '{title}' were found in the catalogue."
        if title in self.get_all_titles():
            return f"{title} is available in the library catalogue."
        else:
            close_matches = get_close_matches(title, self.get_all_titles())
            if len(close_matches) > 0:
                output = "\n=== Closest matches ====\n"
                for title in close_matches:
                    output += f"* {title}\n"
                return output
        return output

    def add_item(self):
        """
        Add item to Catalogue if it's not already in the collection.
        This system assumes call numbers are unique.
        :return: None
        """
        factory = LibraryItemGenerator.pick_item_creation_type(choice)
        item = factory.createItem()
        if item.call_no not in self.get_all_call_nos():
            self._data[item.call_no] = item
            print("\nItem has been added.\n")

    def add_item(self):
        """
        Add item to Catalogue if it's not already in the
        collection.
        """
        item = LibraryItemGenerator.create_item()
        if item.get_call_no() not in self._data:
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