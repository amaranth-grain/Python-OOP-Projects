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


class DataHandler:
    """
    Handle all file reading and file writing functions.
    """

    @staticmethod
    def import_data(path, file_extension):
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
    def export_data(path, lines):
        """
        Write card info (in JSON format) to json file.
        :param path: String
        :param lines: String
        :return: None
        """
        with open(path, mode='r+', encoding="utf-8") as output:
            for line in lines:
                output.write(line)