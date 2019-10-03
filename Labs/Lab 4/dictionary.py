"""
Represent dictionary and search function in the dictionary program.
"""
from file_handler import FileHandler
from file_handler import InvalidFileTypeError
from difflib import get_close_matches
import os


class WordNotFound(Exception):
    """
    When a lowercase word is not found in the data loaded into the dictionary.
    """
    pass


class Dictionary:
    def __init__(self):
        self._data = None
        self._output = "./output.txt"

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
        try:
            self._data = FileHandler.load_data(filepath, ext)
        except FileNotFoundError as e:
            print(f"{e}\nThe filepath you entered was {filepath}")
        except InvalidFileTypeError as e:
            print(f"{e}\nThe filepath you entered was {filepath}")

    def _definitions(self, word):
        """
        Format definitions based on search term.
        :param word: String
        :return: String
        """
        definitions = self._data.get(word)
        output = f"\n== {word} ==\n"
        for definition in definitions:
            output += f"{definition}\n"
        return output

    def query_definition(self, word):
        """
        Look up the definition of a word.
        :param word: String
        :return: String
        """
        lines = ""
        if word in self._data:
            lines = self._definitions(word)
        elif word.lower() in self._data:
            lines = self._definitions(word.lower())
        elif word.capitalize() in self._data:
            lines = self._definitions(word.capitalize())
        else:
            print("Did you mean:")
            matches = get_close_matches(word, list(self._data.keys()))
            for match in matches:
                print(f"* {match}")

        FileHandler.write_lines(self._output, lines)
        return lines


class Controller:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def search(self):
        while True:
            user_input = input("\nEnter search term: ")
            if user_input.lower() == "exitprogram":
                break
            try:
                print(self.dictionary.query_definition(user_input))
            except WordNotFound as e:
                print(e)


def main():
    dictionary = Dictionary()
    dictionary.load_dictionary("./data.json")
    # print(dictionary._data)
    controller = Controller(dictionary)
    controller.search()
    # dictionary.query_definition("accumulator")
    # print(f"Dictionary data after loading: {dictionary._data}")


if __name__ == "__main__":
    main()