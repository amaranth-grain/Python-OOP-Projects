"""
FileHandler class responsible for classes related to reading and / or
writing files for dictionary program.
"""
from enum import Enum
import json
# library


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
    # open(filename, mode)

    @staticmethod
    def load_data(path, file_extension):
        """
        Check if file extension is correct.
        If correct, read data from file.
        :param path: String
        :param file_extension: FileExtensions
        :return: None
        """



    @staticmethod
    def write_lines(path, lines):
        """
        Write queried lines to text file by appending.
        :param path: String
        :param lines: ???
        :return: None
        """
        return

