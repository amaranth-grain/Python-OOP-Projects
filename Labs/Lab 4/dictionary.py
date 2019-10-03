"""
Represent dictionary and search function in the dictionary program.
"""
from file_handler import FileHandler
import os


class Dictionary:
    def __init__(self):
        self._data = None

    # @property
    # def data(self):
    #     return self._data
    #
    # @data.setter
    # def data(self, data):
    #     self._data = data

    def is_data_loaded(self):
        """
        Track whether dictionary has been loaded with data or not.
        :return:
        """
        return self.data is not None

    def load_dictionary(self, filepath):
        """
        Load the dictionary with words and definitions.
        :param filepath: String
        :return: None
        """
        name, ext = os.path.splitext(filepath)
        print(f"File Extension: {ext}")
        self._data = FileHandler.load_data(filepath, ext)

    def query_definition(self, word):
        """
        Look up the definition of a word.
        :param word: String
        :return: String
        """
        return


def main():
    dictionary = Dictionary()
    dictionary.load_dictionary("./test.json")


if __name__ == "__main__":
    main()