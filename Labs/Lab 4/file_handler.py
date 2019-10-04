"""
FileHandler class responsible for classes related to reading and / or
writing files for dictionary program.
"""
import os
from enum import Enum
from pathlib import Path


class FileExtensions(Enum):
    """
    Specifies accepted file extensions for dictionary program.
    """
    TXT = ".txt"
    JSON = ".json"


class InvalidFileTypeError(Exception):
    """
    Exception that is raised if user attempts to load a file that is
    not an accepted format (see FileExtensions for accepted formats).
    """
    pass


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
        if not Path(path).exists():
            raise FileNotFoundError("Error: File was not found.")

        values = set(file_type.value for file_type in FileExtensions)

        if file_extension not in values:
            raise InvalidFileTypeError("Error: Invalid file extension. Only "
                                       ".json and .txt are accepted.")

        name, ext = os.path.splitext(path)

        if file_extension != ext:
            raise ValueError("File extension does not match path's file "
                             "extension.")

        file = open(path, mode="r", encoding="utf-8")
        data = file.read()
        file.close()
        return data

    @staticmethod
    def write_lines(path, lines):
        """
        Write queried lines to text file by appending to output file.
        :param path: String
        :param lines: String
        :return: None
        """
        with open(path, mode='a', encoding="utf-8") as output:
            for line in lines:
                output.write(line)

