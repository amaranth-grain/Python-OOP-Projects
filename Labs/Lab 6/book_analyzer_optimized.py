"""
This module is responsible for holding a BookAnalyzer class that has been
reworked and optimised.
"""
from collections import Counter
import string


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    def __init__(self):
        self.text = None
        self.text_lower = None
        self.unique_words = None

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        # read lines
        with open(src, mode='r', encoding='utf-8') as book_file:
            data = book_file.read().replace("\ufeff", "")
            translator = str.maketrans('', '', string.punctuation)
            # Strip data of punctuation and create word list
            stripped_text = data.translate(translator).split()
            self.text = stripped_text
            self.text_lower = [w.lower() for w in stripped_text]

    @staticmethod
    def is_unique(word, word_list):
        """
        Checks to see if the given word appears in the provided sequence.
        This check is case in-sensitive.
        :param word: a string
        :param word_list: a sequence of words
        :return: True if not found, false otherwise
        """
        return word_list.count(word) == 1

    def find_unique_words(self):
        """
        Filters out all the words that only appear once in the text.
        :return: a list of all the unique words.
        """
        counter = Counter(self.text_lower)
        if self.unique_words is None:
            self.unique_words = [k for k, v in counter.items() if v == 1]
        return self.unique_words


def main():
    book_analyzer = BookAnalyzer()
    book_analyzer.read_data()
    unique_words = book_analyzer.find_unique_words()
    print("-" * 50)
    print(f"List of unique words (Count: {len(unique_words)})")
    print("-" * 50)
    for w in unique_words:
        print(w)
    print("-" * 50)


if __name__ == '__main__':
    main()
