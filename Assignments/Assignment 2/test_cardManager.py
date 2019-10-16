import os
from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock, patch
import card_management
import card


class TestCardManager(TestCase):
    # Cannot get patch to work beyond first mock_input.side_effect input for
    # all unit tests that require mock user inputs.
    @patch('card_management.input', create=True)
    def test_add_card(self, m):
        m.side_effect = ["3", "Christy", "N", "1234", "01/01/20",
                                  "BCIT", "123 Main St", "V2K3L3",
                                  "Vancouver", "BC", "Canada"]
        manager = card_management.CardManager()
        manager.add_card()
        self.assertEqual(1, len(manager.card_list))

    # Cannot get patch to work beyond first mock_input.side_effect input for
    # all unit tests that require mock user inputs.
    @patch('card_management.input', create=True)
    def test_delete_card(self, mock_input):
        address = card.Address("Company", "123 Main St", "V2O 3J0",
                               "Vancouver", "BC", "Canada")
        loyal = card.LoyaltyCard(100, {"Book": 100}, address)

        mock_input.side_effect = ["2", "1"]

        manager = card_management.CardManager()
        manager.card_list.append(loyal)
        manager.card_list.append(loyal)
        print(len(manager.card_list))
        manager.delete_card()
        self.assertEqual(1, len(manager.card_list))

    # This unit test works
    @patch('card_management.input', create=True)
    def test_search_card(self, m):
        address = card.Address("Company", "123 Main St", "V2O 3J0",
                               "Vancouver", "BC", "Canada")
        loyal = card.LoyaltyCard(100, {"Book": 100}, address)

        m.side_effect = ["2", "1"]
        manager = card_management.CardManager()
        manager.card_list.append(loyal)
        self.assertTrue(1, manager.card_list[0].id)

    # This unit test works
    def test_backup_data(self):
        manager = card_management.CardManager()
        manager.backup_data()
        time = datetime.now().strftime("%m%d%Y_%H%M")
        path = f"./OnederCard_Export_{time}.txt"
        self.assertTrue(os.path.exists(path))
