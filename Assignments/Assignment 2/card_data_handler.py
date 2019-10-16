import os
from enum import Enum
from datetime import datetime
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
    @staticmethod
    def backup_data(manager):
        time = datetime.now().strftime("%m%d%Y_%H%M")
        path = f"./OnederCard_Export_{time}.txt"
        with open(path, mode="w", encoding="utf-8") as backup:
            backup.write(manager.card_list_json)
        print("Backed up data successfully.")