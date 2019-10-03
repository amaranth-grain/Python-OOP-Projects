"""
FileHandler class responsible for classes related to reading and / or
writing files for dictionary program.
"""
from enum import Enum
import json


class FileExtensions(Enum):
    """
    Specifies accepted file extensions for dictionary program.
    """
    TXT = ".txt"
    JSON = ".json"


class InvalidFileTypeError:
    """
    Exception that is raised if user attempts to load a file that is
    not an accepted format (see FileExtensions).
    """
    def __init__(self):
        return


class FileHandler:
    """
    Handle all file reading and file writing functions.
    """

    @staticmethod
    def load_data(path, file_extension):
        """
        Check if file extension is correct.
        If correct, read data from file.
        :param path: String
        :param file_extension: FileExtensions
        :return: None
        """
        ext = FileExtensions(file_extension)
        if isinstance(ext, FileExtensions):
            with open(path, 'r+') as data_file, open('./output.txt',
                                                     'r+') as output_file:
                data = data_file.read()
                return json.loads(data)
                # decoded = json.loads(data)
                # output_file.write(json.dumps(decoded))
        else:
            print("Incorrect file type D:")

    @staticmethod
    def write_lines(path, lines):
        """
        Write queried lines to text file by appending.
        :param path: String
        :param lines: ???
        :return: None
        """
        return

