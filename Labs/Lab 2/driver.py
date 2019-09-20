from library import Library
from catalogue import Catalogue
from book import Book
from journal import Journal
from item import Item

def main():
    # def __init__(self, title, call_no, author, num_copies):
    # issue, publisher):
    # release,     region)
    b1 = Book("Provenance", "342.2", "Anne Leckie", 20)
    b2 = Book("Ancillary Justice", "342.2A", "Anne Leckie", 1)
    j1 = Journal("Individual Psychology", "123.4", "Gabriela Pap", 1,
                 23, "Journal of Psychology")
    d1 = Dvd("Mad Max: Fury Road", "789.0", "George Miller", 8,
             "May 15, 2015", "1")
    cat = Catalogue([b1, b2, j1, d1])
    vpl = Library(cat)

if __name__ == "__main__":
    main()