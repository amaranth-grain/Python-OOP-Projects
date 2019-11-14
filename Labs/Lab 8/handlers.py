from abc import ABC, abstractmethod
from pathlib import Path
import os
from enum import Enum


class CryptoMode(Enum):
    """
    Enum that lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class KeyLengthError(Exception):

    def __init__(self, length):
        super().__init__(f"Keys must be 8, 16, or 24 characters long."
                         f"Your key is {length} characters long.")
        self.length = length


class EmptyStringError(Exception):

    def __init__(self):
        super().__init__(f"You cannot use cryptography on an empty string.")


class MultipleInputSourceError(Exception):

    def __init__(self, string, file):
        super().__init__(f"You have multiple sources of input. String '"
                         f"{string}' and file path '{file}' were detected.")
        self.string = string
        self.file = file


class NoInputSourceError(Exception):
    def __init__(self):
        super().__init__(f"No input source detected.")


class FileExtensionError(Exception):

    def __init__(self, path):
        super().__init__(f"Your file path '{path}' does not end with the "
                         f".txt file extension.")
        self.path = path


class InvalidModeError(Exception):

    def __init__(self, mode):
        super().__init__(f"The mode you entered '{mode}' is not a valid "
                         f"CryptoMode.")
        self.mode = mode


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
    """
    Check the key used for DES cryptography is a valid length (8, 16, or 24).
    """

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


class ModeCryptographyValidator(BaseCryptographyHandler):

    """
    Check the cryptography mode is a CryptoMode Enum.
    """

    def handle_request(self, request) -> bool:
        """
        Ensures that the mode is a valid input.
        :param request: Request
        :return: bool
        """
        if not isinstance(request.encryption_state, CryptoMode):
            raise InvalidModeError(request.encryption_state)


class InputCryptographyValidator(BaseCryptographyHandler):

    """
    Check for the right number of inputs, and that the input can be used
    for encryption / decryption.
    """

    def handle_request(self, request) -> bool:
        """
        Ensures there is only one input (either a string directly from
        command line or an input file, but not both).
        Ensures that file input is a text file and that it can be read.
        :param request: Request
        :return: bool
        """
        print("Input validator running...")

        # If there are two input sources
        if request.data_input and request.input_file:
            raise MultipleInputSourceError(request.data_input,
                                           request.input_file)

        # If there are no input sources
        if request.data_input is None and not request.input_file:
            raise NoInputSourceError

        # If there is only a raw string
        if request.data_input is not None:
            # Check that data has at least 1 character
            if len(request.data_input) > 0:
                if not self.next_handler:
                    return True
                return self.next_handler.handle_request(request)
            else:
                raise EmptyStringError
        # If there is a file path
        else:
            # Check if path exists
            if not Path(request.input_file).exists():
                raise FileNotFoundError(f"The file '{request.input_file}' "
                                        f"was not found.")
            # Check if extension is correct
            elif not request.input_file.endswith(".txt"):
                raise FileExtensionError(request.input_file)
            # Check if the file is empty
            elif os.stat(request.input_file).st_size == 0:
                raise EmptyStringError
            # If there are no errors
            else:
                if not self.next_handler:
                    return True
                return self.next_handler.handle_request(request)

