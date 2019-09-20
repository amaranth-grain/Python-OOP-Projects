import abc

class Item(abc.ABC):
    """
    An Abstract Base Class that provides a simple interface that all
    Library Items need to implement. Any class that inherits from this
    class MUST implement all the @abstractmethods and
    @abstractclassmethods.
    """

    """
        Represents an Item that is stored
        in a Catalogue at the Library.
        """

    def __init__(self, title, call_no, author, num_copies):
        """
        Initialises Item object.
        :param title: as String
        :param call_no: as string
        :param author: as String
        :param num_copies: as int
        """
        self._title = title
        self._call_no = call_no
        self._author = author
        self._num_copies = num_copies

    def get_title(self):
        """
        Return title of Item.
        :return: as String
        """
        return self._title

    def get_copies(self):
        """
        Return number of copies available.
        :return: as int
        """
        return self._num_copies

    def set_copies(self, num_copies):
        """
        Set number of copies available.
        :param num_copies: as int
        """
        self._num_copies = num_copies

    def get_call_no(self):
        """
        Get the call number of Item.
        :return: as String
        """
        return self._call_no

    def check_availability(self):
        """
        Return true if there is at least 1 copy.
        :return: as boolean
        """
        return self._num_copies > 0

    @abc.abstractmethod
    def __repr__(self):
        """
        Format for representing Item object.
        :return: as String
        """
        return f"Title: {self._title}\n" \
               f"Call Number: {self._call_no}\n" \
               f"Author: {self._author}\n" \
               f"Copies Available: {self._num_copies}\n"

    @abc.abstractmethod
    def __str__(self):
        """
            Format for representing Book object.
            :return: as String
        """
        return f"Title: {self._title}\n" \
               f"Call Number: {self._call_no}\n" \
               f"Author: {self._author}\n" \
               f"Copies Available: {self._num_copies}\n\n"
