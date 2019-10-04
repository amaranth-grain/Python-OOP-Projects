"""
Unit tests for applicable functions in Dictionary class.
"""
from unittest import TestCase
from dictionary import Dictionary


class TestDictionary(TestCase):
    """
    Test functions in Dictionary class.
    """

    def test_is_data_loaded_false(self):
        """
        Test whether is_data_loaded returns false when no data is loaded
        into the dictionary.
        :return: False
        """
        dictionary = Dictionary()
        msg = "FAILED: Data was loaded without callingg load_daa"
        self.assertFalse(dictionary.is_data_loaded(), msg)

    def test_is_data_loaded_true(self):
        """
        Test whether is_data_loaded returns true when data is loaded into
        the dictionary.
        :return: True
        """
        dictionary = Dictionary()
        dictionary.load_dictionary("./data.json")
        msg = "FAILED: Data was not loaded when load_data was called"
        self.assertTrue(dictionary.is_data_loaded(), msg)

    def test__definitions(self):
        """
        Test the formatted output of definitions stored in an array.
        :return: String
        """
        dictionary = Dictionary()
        dictionary.load_dictionary("./data.json")
        output = "\n== sadly ==\n" \
                 "In an unfortunate manner.\n" \
                 "With sadness.\n"
        self.assertEqual(dictionary._definitions("sadly"), output)

    # def test_query_definition(self):
    #     self.fail()
