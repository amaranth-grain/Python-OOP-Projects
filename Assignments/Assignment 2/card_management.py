"""
Management side of card management system.  Includes data import / export
and the ability for users to interact with the system.
"""
import sys
from datetime import datetime

from card_creator import CardCreator
from card import Address, Card, LoyaltyCard, BalanceCard, IDCard, MoneyCard, \
    GovernmentIDCard, AccessCard


class CardManager:
    def __init__(self):
        self._card_list = []

    @property
    def card_list(self):
        return self._card_list

    #     with open("./sample_card_data.txt", "r") as data_file:
    #         self._card_list = json.loads(data_file.read())

    def start(self):
        UserInterface.welcome()
        UserInterface.display_start_menu(self)

    def view_all_cards(self):
        output = ""
        for card in self._card_list:
            output += f"{card}\n"
        return output

    def view_cards_by_type(self):
        UserInterface.display_view_cards_by_type(self)

    def add_card(self):
        UserInterface.display_add_card(self)

    def delete_card(self):
        cards = self.search_by_issuer()
        if len(cards) is not 0:
            try:
                i = 0
                output = ""
                for card in cards:
                    output += f"{i + 1}.\n {card}"
                delete_index = int(
                    input("\nWhich card would you like to delete? "))
                card_to_delete = cards[delete_index - 1]
                card_id = card_to_delete.id

                for card in self._card_list:
                    if card.id == card_id:
                        self._card_list.remove(card)
                        print("\nYour card was deleted.")
            except ValueError as e:
                print(f"Invalid input. {str(e).capitalize()}")

    def search_card(self):
        user_input = UserInterface.display_search_menu()
        choices = {
            1: self.search_by_issuer,
            2: sys.exit
        }
        choices.get(user_input)()

    def search_by_issuer(self):
        issuer = input("Enter card issuer name: ")
        cards = []
        for card in self._card_list:
            if card.address.company_name.lower() == issuer.lower():
                cards.append(card)

        if len(cards) == 0:
            print(f"No cards issued by {issuer} were found.")
        else:
            output = ""
            i = 1
            for card in cards:
                output += f"\n#{i}.\n{card}"
                i += 1
            print(output)
        return cards

    def backup_data(self):
        return


class UserInterface:

    @staticmethod
    def welcome():
        msg = "\n\n==== One-der Card ====\n" \
              "One-der Card is your one-stop solution for managing a\n" \
              "wallet full of gift cards, credit cards, business cards,\n" \
              "points cards,and more.\n"
        return msg

    @staticmethod
    def display_start_menu(manager):
        # output = UserInterface.welcome()
        # user_input = 0
        # while user_input > 6 or user_input < 1:
        while True:
            output = Catalogue.get_menu(Catalogue.start_menu)
            print(output)
            try:
                user_input = int(input("Enter selection: "))
                if user_input > len(Catalogue.start_menu):
                    raise ValueError
            except ValueError as e:
                print("Invalid input. Enter the number of your selected "
                      "action.")
            else:
                choices = {
                    1: manager.view_all_cards,
                    2: manager.view_cards_by_type,
                    3: manager.add_card,
                    4: manager.search_card,
                    5: manager.delete_card,
                    6: manager.backup_data,
                    7: sys.exit
                }

                if user_input == 1:
                    print(choices.get(user_input)())

                if 1 < user_input < 8:
                    choices.get(user_input)()

    @staticmethod
    def display_view_cards_by_type(manager):
        print("\nWhich type of card would you like to view?")
        print(Catalogue.get_menu(Catalogue.card_type_menu))
        user_input = 0
        while user_input > 7 or user_input < 1:
            try:
                user_input = int(input("Enter selection: "))
                if user_input == 7:
                    sys.exit()
                if user_input > 7:
                    raise ValueError
            except ValueError as e:
                print("Invalid input. Enter the number of your selected "
                      "action.")
            else:
                count = 0
                ctype = Catalogue.card_types.get(user_input)
                user_card_type = Catalogue.user_card_types.get(user_input)
                for card in manager.card_list:
                    if card.__class__.__name__ is ctype:
                        print(card)
                        count += 1

                if count == 0:
                    print(f"No {user_card_type} cards are stored in One-der "
                          f"Card currently.")

    @staticmethod
    def display_add_card(manager):
        print("\nWhich type of card would you like to add?\n")
        print(Catalogue.get_menu(Catalogue.card_type_menu))
        val = True
        while val:
            try:
                user_input = int(input("Enter selection: "))
                if user_input > len(Catalogue.card_type_menu):
                    raise ValueError
            except ValueError as e:
                print("Invalid input. Enter the number of your selected "
                      "action.")
            else:
                val = False
                # choice = Catalogue.card_types.get(user_input)
                card = Catalogue.create_menu.get(user_input)()
                manager._card_list.append(card)
                # UserInterface.display_start_menu(self)

    @staticmethod
    def display_search_menu():
        print("\nHow would you like to search for a card?\n")
        print(Catalogue.get_menu(Catalogue.search_menu))
        val = True
        while val:
            try:
                user_input = int(input("Enter selection: "))
                if user_input > len(Catalogue.search_menu):
                    raise ValueError
            except ValueError as e:
                print("Invalid input. Enter the number of your selected "
                      "action.")
            else:
                val = False
                return user_input


class Catalogue:
    start_menu = {
        1: "View all cards",
        2: "View cards by type",
        3: "Add a card",
        4: "Search for a card",
        5: "Delete a card",
        6: "Export card data",
        7: "Close program"
    }

    card_type_menu = {
        1: "Loyalty cards (e.g. stamp cards)",
        2: "Cards with balances (e.g. transit fare, gift card)",
        3: "Basic ID cards / business cards",
        4: "Credit / debit cards",
        5: "Government ID cards",
        6: "Tickets / basic membership cards (e.g. library or gym card)",
        7: "Close program"
    }

    # For internal use
    card_types = {
        1: "LoyaltyCard",
        2: "BalanceCard",
        3: "IDCard",
        4: "MoneyCard",
        5: "GovernmentIDCard",
        6: "AccessCard"
    }

    # For end user
    user_card_types = {
        1: "loyalty",
        2: "gift / transit fare",
        3: "ID / business",
        4: "credit or debit",
        5: "government ID",
        6: "ticket or basic membership"
    }

    search_menu = {
        1: "Search by issuer",
        2: "Close program"
    }

    create_menu = {
        1: CardCreator.create_loyalty_card,
        2: CardCreator.create_balance_card,
        3: CardCreator.create_id_card,
        4: CardCreator.create_money_card,
        5: CardCreator.create_gov_card,
        6: CardCreator.create_access_card
    }

    @classmethod
    def get_menu(cls, menu):
        output = "\n==== Menu ====\n"
        for k, v in menu.items():
            output += f"{k}. {v}\n"
        return output


def main():
    manager = CardManager()
    expiry_date = datetime(2025, 1, 1)
    dob = datetime(1900, 5, 6)

    # CAN BE DELETED IF YOU WOULD PREFER TO ADD ALL CARDS YOURSELF
    # App is pre-loaded with cards for easier testing
    address = Address("BCIT", "555 Seymour Street", "V2F 9K1", "Vancouver",
                      "BC", "Canada")

    g_address = Address("Ghibli Museum", "1 Chome-1-83 Shimorenjaku",
                        "181-0013",
                        "Mitaka", "Tokyo", "Japan")

    h_address = Address("Home address", "123 Main Street", "V8K 1P3",
                        "Vancouver",
                        "BC", "Canada")

    i_address = Address("ICBC", "999 Robson Street", "V2B 2N9", "Vancouver",
                        "BC", "Canada")

    # LOYALTY CARD
    rewards = {"Bubble Waffles": 5, "Brown Sugar BBT": 10}
    loyalty_card = LoyaltyCard(9, rewards, address)

    # BALANCE CARD
    balance_card = BalanceCard("123456789", 438.2, address)

    # ID Card
    id_card = IDCard("Amy Acker", "3492 9384 2342", expiry_date,
                     address)

    # Access Card
    access_card = AccessCard("3428 2398 3021", None, "Ghibili Museum Ticket",
                             g_address)

    # Money Card
    credit_card = MoneyCard("564", "Credit", "Xena Warrior Princess",
                            "8673 1214 6563", expiry_date, address)

    # Government ID Card
    driver_card = GovernmentIDCard(dob, 61.1, 184, "F", "Brown",
                                   "Brown",
                                   h_address, "Delle Seyah",
                                   "2847 6951 3241",
                                   expiry_date, i_address)

    manager.card_list.append(loyalty_card)
    manager.card_list.append(balance_card)
    manager.card_list.append(id_card)
    manager.card_list.append(access_card)
    manager.card_list.append(credit_card)
    manager.card_list.append(driver_card)
    # CAN BE DELETED IF YOU WOULD PREFER TO ADD ALL CARDS YOURSELF

    manager.start()


if __name__ == "__main__":
    main()
