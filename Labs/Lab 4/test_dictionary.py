import json
from unittest import TestCase
from dictionary import Dictionary


class TestDictionary(TestCase):
    def test_is_data_loaded_false(self):
        dictionary = Dictionary()
        msg = "FAILED: Data was laoded "
        self.assertFalse(dictionary.is_data_loaded(), "FAILED: Data was "
                                                      "loaded without "
                                                      "calling load_data")

    def test_is_data_loaded_true(self):
        dictionary = Dictionary()
        dictionary.load_dictionary("./data.json")
        msg = "FAILED: Data was not loaded when load_data was called"
        self.assertTrue(dictionary.is_data_loaded(), msg)

    def test_load_dictionary_filenotfound(self):
        dictionary = Dictionary()
        # self.assertRaises(TypeError, test_function, args)
        self.assertRaises(FileNotFoundError,
                          dictionary.load_dictionary(
                              "./data.pdf"))

    def test_load_dictionary_notJSONcontent(self):
        dictionary = Dictionary()
        self.assertRaises(json.decoder.JSONDecodeError,
                          dictionary.load_dictionary(
                              "./test.json"))

    # def test__definitions(self):
    #     self.fail()
    #
    # def test_query_definition(self):
    #     self.fail()
