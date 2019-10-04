"""
Unit testing for FileHandler methods.
"""

from unittest import TestCase
from file_handler import FileHandler
from file_handler import InvalidFileTypeError


class TestFileHandler(TestCase):
    """
    Test functions associated with FileHandler class.
    """
    def test_load_data_file_not_found(self):
        self.assertRaises(FileNotFoundError, FileHandler.load_data,
                          "./asdf.exe", ".exe")

    def test_load_data_ext_mismatch(self):
        self.assertRaises(ValueError, FileHandler.load_data,
                          "./data.json", ".txt")

    def test_load_data_wrong_ext(self):
        self.assertRaises(InvalidFileTypeError, FileHandler.load_data,
                          "./dictionary.py", ".py")
