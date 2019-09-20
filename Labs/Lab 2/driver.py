from library import Library
from catalogue import Catalogue
from book import Book
from dvd import Dvd
from journal import Journal
from item import Item


def main():
    # def __init__(self, title, call_no, author, num_copies):
    # issue, publisher):
    # def __init__(self, title, call_no, author, num_copies, name,
    #              issue, publisher):
    b1 = Book("Provenance", "342.2", "Anne Leckie", 20)
    b2 = Book("Ancillary Justice", "342.2A", "Anne Leckie", 1)
    j1 = Journal("Individual Psychology", "123.4", "Gabriela Pap", 1,
                 "Journal of Psychology", 23, "SAGE Publications")
    d1 = Dvd("Mad Max: Fury Road", "789.0", "George Miller", 8,
             "May 15, 2015", "1")
    cat = Catalogue(
        {"342.2": Book("Provenance", "342.2", "Anne Leckie", 20),
         "342.2A": Book("Ancillary Justice", "342.2A", "Anne Leckie", 1),
         "123.4": Journal("Individual Psychology", "123.4",
                               "Gabriela Pap", 1,
                               "Journal of Psychology", 23,
                               "SAGE Publications"),
         "789.0": Dvd("Mad Max: Fury Road", "789.0", "George Miller", 8,
                      "May 15, 2015", "1")})
    vpl = Library(cat)

    display_menu = True

    while display_menu:
        print("What would you like to do?")
        print("1. Find item by title (String)")
        print("2. Add item to catalogue")
        print("3. Remove item from catalogue (call no)")
        print("4. Check out a copy (call no)")
        print("5. Return your copy (call no)")
        print("6. Display library catalogue")
        print("7. Quit menu")

        choice = int(input("Select action: "))

        if choice == 2:
            vpl.get_cat().add_item()
        elif choice == 6:
            vpl.display_available_books()
        elif choice == 7:
            display_menu = False
        elif choice not in range(1, 6):
            print("\nInvalid input.  Try again.\n")
        else:
            par = input("Enter parameter: ")
            input_dict = {1: vpl.search,
                          3: cat.remove_item,
                          4: vpl.check_out,
                          5: vpl.return_item}

            print(input_dict.get(choice)(par))


if __name__ == "__main__":
    main()
