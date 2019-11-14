from des import DesKey
# from handlers import KeyCryptographyValidator, InputCryptographyValidator, \
#     ModeCryptographyValidator
from abc import ABC, abstractmethod
from pathlib import Path
from enum import Enum
from des import DesKey
import argparse
import os
import ast


class CryptoMode(Enum):
    """
    Enum that lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.

    """

    def __init__(self):
        """
        Initialises Request.
        """
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        """
        String representation of Request
        :return: String
        """
        return f"Request: State: {self.encryption_state}\n " \
               f"Data: {self.data_input}\n" \
               f"Input file: {self.input_file}\n" \
               f"Output: {self.output}\n" \
               f"Key: {self.key}"


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to "
                                               "be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        print(f"args: {args}")
        request = Request()
        print(f"args.mode: {args.mode}")
        request.encryption_state = CryptoMode(args.mode)
        # request.encryption_state = args.mode
        request.data_input = args.string
        request.input_file = args.file
        request.output = args.output
        request.key = args.key
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class KeyLengthError(Exception):
    """
    Error thrown when the DES key is not 8, 16, or 24 in length.
    """
    def __init__(self, length):
        super().__init__(f"Keys must be 8, 16, or 24 characters long."
                         f"Your key is {length} characters long.")
        self.length = length


class EmptyStringError(Exception):
    """
    Error thrown when user uses empty string literal.
    """
    def __init__(self):
        super().__init__(f"You cannot use cryptography on an empty string.")


class MultipleInputSourceError(Exception):
    """
    Error thrown when there are multiple input sources.
    """
    def __init__(self, string, file):
        super().__init__(f"You have multiple sources of input. String '"
                         f"{string}' and file path '{file}' were detected.")
        self.string = string
        self.file = file


class NoInputSourceError(Exception):
    """
    Error thrown when there are no input sources.
    """
    def __init__(self):
        super().__init__(f"No input source detected.")


class FileExtensionError(Exception):
    """
    Error thrown when the file extension is incorrect.
    """
    def __init__(self, path):
        super().__init__(f"Your file path '{path}' does not end with the "
                         f".txt file extension.")
        self.path = path


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


class OutputCryptographyValidator(BaseCryptographyHandler):

    def handle_request(self, request) -> bool:
        """
        Check whether output value is valid or not.
        :param request:
        :return:
        """
        print("Output validator running...")
        if request.output.lower() == "print":
            if not self.next_handler:
                return True
            return self.next_handler.handle_request(request)

        # Check if output path is valid
        if not request.output.endswith(".txt"):
            raise FileExtensionError(request.output)
        else:
            if not self.next_handler:
                return True
            return self.next_handler.handle_request(request)


class EncryptionCryptographyHandler(BaseCryptographyHandler):

    def handle_request(self, request) -> bool:
        print("Encryption handler running")
        # Set up encryption key
        bytes_key = request.key.encode()
        key0 = DesKey(bytes_key)

        # Encrypting from direct string
        if request.data_input:
            print("Encrypting request from direct string... ...")
            bytes_str = request.data_input.encode()
            output = key0.encrypt(bytes_str, padding=True)
        else:
            print("Encrypting from input file... ...")
            bytes_str = request.data_input.encode()
            output = key0.encrypt(bytes_str, padding=True)

        # Whether it's direct or from input file, output results:
        if request.output.lower() == "print":
            print(f"=== ENCRYPTED OUTPUT ===\n{output}")
        else:
            with open(request.output, "wb+") as output_file:
                output_file.write(output)
                # output_file.write("Write text by encoding\n".encode('utf8'))
                # output_file.write(b'\xDE\xAD\xBE\xEF')


class DecryptionCryptographyHandler(BaseCryptographyHandler):

    def handle_request(self, request) -> bool:
        # Set up decryption key
        bytes_key = request.key.encode()
        key0 = DesKey(bytes_key)

        if request.data_input:
            print("Decrypting request from direct string... ...")
            coded_msg = ast.literal_eval(r"{0}".format(request.data_input))
        else:
            with open(request.input_file, "rb+") as input_file:
                coded_msg = input_file.read()

        decrypted_output = key0.decrypt(coded_msg, padding=True)
        print(f"=== DECRPYTED MESSAGE===\n{decrypted_output}")


class Crypto:

    def __init__(self):
        # Chain for encrypting data
        en_key = KeyCryptographyValidator()
        # en_mode = ModeCryptographyValidator()
        en_input = InputCryptographyValidator()
        en_output = OutputCryptographyValidator()
        en_handler = EncryptionCryptographyHandler()
        en_key.next_handler = en_input
        en_input.next_handler = en_output
        en_output.next_handler = en_handler

        # Chain for decrypting data
        de_key = KeyCryptographyValidator()
        # de_mode = ModeCryptographyValidator()
        de_input = InputCryptographyValidator()
        de_output = OutputCryptographyValidator()
        de_handler = DecryptionCryptographyHandler()
        de_key.next_handler = de_input
        de_input.next_handler = de_output
        de_output.next_handler = de_handler

        self.encryption_start_handler = en_key
        self.decryption_start_handler = de_key

    def execute_request(self, request: Request):
        if request.encryption_state is CryptoMode.EN:
            return self.encryption_start_handler.handle_request(request)
        elif request.encryption_state is CryptoMode.DE:
            return self.decryption_start_handler.handle_request(request)


def main(request: Request):
    driver = Crypto()
    # execute_request() will throw an error if it doesn't pass validation
    driver.execute_request(request)

    # # Encryption
    # if request.encryption_state == CryptoMode.EN:
    #     # Set up encryption key
    #     bytes_key = request.key.encode()
    #     key0 = DesKey(bytes_key)
    #
    #     # Encrypting from direct string
    #     if request.data_input:
    #         print("Encrypting request from direct string... ...")
    #         bytes_str = request.data_input.encode()
    #         output = key0.encrypt(bytes_str, padding=True)
    #     else:
    #         print("Encrypting from input file... ...")
    #         bytes_str = request.data_input.encode()
    #         output = key0.encrypt(bytes_str, padding=True)
    #
    #     # Whether it's direct or from input file, output results:
    #     if request.output.lower() == "print":
    #         print(f"=== ENCRYPTED OUTPUT ===\n{output}")
    #     else:
    #         with open(request.output, "wb+") as output_file:
    #             output_file.write(output)
    #             # output_file.write("Write text by encoding\n".encode('utf8'))
    #             # output_file.write(b'\xDE\xAD\xBE\xEF')
    # else:
    #     # Set up decryption key
    #     bytes_key = request.key.encode()
    #     key0 = DesKey(bytes_key)
    #
    #     if request.data_input:
    #         print("Decrypting request from direct string... ...")
    #         # The lenth of the message should be divisible by 8
    #         coded_msg = request.data_input.encode()
    #     else:
    #         with open(request.input_file, "rb+") as input_file:
    #             coded_msg = input_file.read()
    #
    #     decrypted_output = key0.decrypt(coded_msg, padding=True)
    #     print(f"decrypted output: {decrypted_output}")


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
