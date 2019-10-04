"""
Represent dictionary and search function in the dictionary program.
"""
import json

from file_handler import FileHandler
from file_handler import InvalidFileTypeError
from difflib import get_close_matches
import os


class WordNotFound(Exception):
    """
    When a word is not found in the data loaded into the dictionary.
    """
    pass


class Dictionary:
    """
    Represent a dictionary with data stored in JSON format.
    """
    def __init__(self):
        """
        Initialise dictionary by loading it with data.
        Output attribute determines the name of the file where search
        history is written to.
        """
        self._data = None
        self._output = "./output.txt"

    @property
    def output(self):
        return self._output

    def is_data_loaded(self):
        """
        Track whether dictionary has been loaded with data or not.
        :return:
        """
        return self._data is not None

    def load_dictionary(self, filepath):
        """
        Load the dictionary with words and definitions.
        :param filepath: String
        :return: None
        """
        name, ext = os.path.splitext(filepath)
        string_data = FileHandler.load_data(filepath, ext)
        try:
            self._data = json.loads(string_data)
        except FileNotFoundError as e:
            print(f"{e}\nThe filepath you entered was {filepath}")
        except InvalidFileTypeError as e:
            print(f"{e}\nThe filepath you entered was {filepath}")
        except json.decoder.JSONDecodeError as e:
            print(f"Your file has the correct extension, but file contents"
                  f" are not in JSON.\n{e}")
        except Exception as e:
            print("Exception has occurred")

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
        elif word.title() in self._data:
            lines = self._definitions(word.title())
        else:
            matches = get_close_matches(word, list(self._data.keys()))
            if len(matches) > 0:
                print("Did you mean:")
                for match in matches:
                    print(f"* {match}")
            else:
                raise WordNotFound(f"{word.capitalize()} was not found "
                                   f"in the dictionary.")
        return lines


class Controller:
    """
    Drive the dictionary program.
    """
    def __init__(self, dictionary):
        """
        Initialises Controller with a Dictionary.
        :param dictionary: Dictionary
        """
        self.dictionary = dictionary

    def search(self):
        """
        Prompt user for search term as input
        :return: None
        """
        if not self.dictionary.is_data_loaded():
            return

        while True:
            user_input = input("\nEnter search term: ")
            if user_input.lower() == "exitprogram":
                break
            try:
                results = self.dictionary.query_definition(user_input)
                print(f"Results: {results}")
            except WordNotFound as e:
                print(e)
            else:
                self.write_search_history(results)

    def write_search_history(self, lines):
        """
        Write the results of successful searches into output file.
        :param lines: String
        :return: None
        """
        FileHandler.write_lines(self.dictionary.output, lines)


def main():
    dictionary = Dictionary()
    dictionary.load_dictionary("./data.json")
    controller = Controller(dictionary)
    controller.search()


if __name__ == "__main__":
    main()