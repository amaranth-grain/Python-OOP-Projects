from unittest import TestCase
import driver as d
import mock


class TestGarmentMaker(TestCase):

    def test_gm_start_input(self):
        gm = d.GarmentMaker()
        with mock.patch('builtins.input', return_value="orders.txt"):
            self.assertRaises(d.FileExtensionError, gm.start)

    def test_gm_start_input_valid(self):
        gm = d.GarmentMaker()
        with mock.patch('builtins.input', return_value="orders.xlsx"):
            gm.start()
            self.assertEqual(len(gm.processor.order_list), 10)

    def test_gm_start_input_not_found(self):
        gm = d.GarmentMaker()
        with mock.patch('builtins.input', return_value="what.xlsx"):
            self.assertRaises(FileNotFoundError, gm.start)

