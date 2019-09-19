
class Book:
    def __init__(self, title, call_no, author, num_copies):
        self._title = title
        self._call_no = call_no
        self._author = author
        self._num_copies = num_copies

    def check_availability(self):
        return self._num_copies > 0

    def __str__(self):
        return f"Title: {self._title}\n" \
               f"Call Number: {self._call_no}\n" \
               f"Author: {self._author}\n" \
               f"Copies Available: {self._num_copies}\n"


def main():
    book1 = Book("Green Eggs and Ham", "394.21A", "Dr. Seuss", 10)
    print(book1)
    print(book1.check_availability())

if __name__ == "__main__":
    main()
