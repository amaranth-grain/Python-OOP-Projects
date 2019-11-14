from abc import ABC, abstractmethod


class KeyLengthError(Exception):

    def __init__(self, length):
        super().__init__(f"Keys must be 8, 16, or 24 characters long."
                         f"Your key is {length} characters long.")
        self.length = length


class EmptyStringError(Exception):

    def __init__(self):
        super().__init__(f"You cannot use cryptography on an empty string.")


class BaseCryptographyHandler(ABC):
    """
    Abstract base handler that all CryptographyHandlers inherit from.
    """

    def __init__(self, next_handler=None) -> None:
        """
        Initialises a CryptographyHandler and sets up the next Handler.
        :param next_handler: CryptographyHandler
        """
        self._next_handler = next_handler

    @abstractmethod
    def handle_request(self, request) -> bool:
        """
        Handles the Request through args.
        :param request: Request
        :return: bool
        """
        pass

    @property
    def next_handler(self):
        """
        Returns the next CryptographyHandler
        :return:
        """
        return self._next_handler

    @next_handler.setter
    def next_handler(self, next_handler):
        """
        Sets the next handler in the chain.
        :param handler: CryptographyHandler
        :return: None
        """
        self._next_handler = next_handler


class KeyCryptographyValidator(BaseCryptographyHandler):

    def handle_request(self, request) -> bool:
        """
        Handles the Request through args.
        :param request: Request
        :return: bool
        """
        print("KeyCryptography running...")
        if len(request.key) in [8, 16, 24]:
            if not self.next_handler:
                return True

            return self.next_handler.handle_request(request)
        else:
            raise KeyLengthError(len(request.key))


class StringCryptographyValidator(BaseCryptographyHandler):

    def handle_request(self, request) -> bool:
        """
        Handles the Request through args.
        :param request: Request
        :return: bool
        """
        print("String Empty cryptography running...")
        if len(request.data_input) > 0:
            if not self.next_handler:
                return True

            return self.next_handler.handle_request(request)
        else:
            raise EmptyStringError


