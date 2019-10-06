"""
Management side of card management system.  Includes data import / export
and the ability for users to interact with the system.
"""
import json
from card import Card

class CardManager:
    def __init__(self):
    # def __init__(self, card_list):
    #     self._card_list = card_list
        with open("./sample_card_data.txt", "r") as data_file:
            self._card_list = json.load(data_file)

    def start(self):
        output = UserInterface.welcome()
        output += UserInterface.display_start_menu()
        print(output)

    def view_all_cards(self):
        return

    def view_cards_by_type(self):
        return

    def add_card(self):
        return

    def search_card(self):
        return

    def backup_data(self):
        return

    def import_data(self):
        return


class UserInterface:

    @staticmethod
    def welcome():
        msg = "\n\n==== One-der Card ====\n" \
              "Your one-stop solution for managing a wallet full of\n" \
              "gift cards, credit cards, business cards, points cards,\n" \
              "and more.\n"
        return msg

    @staticmethod
    def display_start_menu():
        return Catalogue.get_menu(Catalogue.start_menu)


class Catalogue:
    start_menu = {
        1: "View all cards",
        2: "View cards by type",
        3: "Add a card",
        4: "Delete a card",
        5: "Export card data",
        6: "Import card data"
    }

    @classmethod
    def get_menu(cls, menu):
        output = "\n==== Menu ====\n"
        for k, v in menu.items():
            output += f"{k}. {v}\n"
        return output


def main():
    manager = CardManager()
    # card_list = []
    # for card in manager._card_list:
    #     card_list.append(Card(**card))


if __name__ == "__main__":
    main()
