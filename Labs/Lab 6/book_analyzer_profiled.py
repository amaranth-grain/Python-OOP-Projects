"""
This module is responsible for holding a profiled BookAnalyzer class (
without redesigning the architecture).
"""
from collections import Counter
import string


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation.
    COMMON_PUNCTUATION = [",", "*", ";", ".", ":", "(", "[", "]", ")"]

    def __init__(self):
        """
        Initialise BookAnalyzer object.
        """
        self.text = None
        self.text_lower = []

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        # read lines
        with open(src, mode='r', encoding='utf-8') as book_file:
            self.text = book_file.readlines()

        # strip out empty lines
        stripped_text = []
        for line in self.text:
            if line != "\n":
                stripped_text.append(line)
        self.text = stripped_text
        print(f"Stripped length: {len(self.text)}")

        # convert list of lines to list of words
        words = []
        for line in self.text:
            words += line.split()
        self.text = words

        # remove common punctuation from words
        temp_text = []
        for word in self.text:
            temp_word = word
            for punctuation in string.punctuation:
                temp_word = temp_word.replace(punctuation, '')
            temp_text.append(temp_word)
            self.text_lower.append(temp_word.lower())
        self.text = temp_text
        print(f"Punctuation removed length: {len(self.text)}")

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
        unique_words = []
        for k, v in counter.items():
            if v == 1:
                unique_words.append(k)
        return unique_words


def main():
    book_analyzer = BookAnalyzer()
    book_analyzer.read_data()
    unique_words = book_analyzer.find_unique_words()
    print("-" * 50)
    print(f"List of unique words (Count: {len(unique_words)})")
    print("-" * 50)
    # for word in unique_words:
    #     print(word)
    print(len(book_analyzer.text_lower))
    print("-" * 50)
    print(f"List of unique words (Count: {len(unique_words)})")


if __name__ == '__main__':
    main()
