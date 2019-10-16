"""
Management side of card management system.  Includes data import / export
and the ability for users to interact with the system.
"""
import sys
from datetime import datetime
from enum import Enum

from card_creator import CardCreator
from card import Address, Card, LoyaltyCard, BalanceCard, IDCard, MoneyCard, \
    GovernmentIDCard, AccessCard
from card_data_handler import DataHandler


class CardManager:
    """
    Main control for card management app.  Stores and manages list of cards
    within app.
    """
    def __init__(self):
        """
        Initialise CardManager.
        """
        self._card_list = []
        self._card_list_json = ""

    @property
    def card_list(self):
        return self._card_list

    @property
    def card_list_json(self):
        return self._card_list_json

    def start(self):
        """
        Start app by welcoming user and offering options menu.
        :return: None
        """
        UserInterface.welcome()
        UserInterface.display_start_menu(self)

    def view_all_cards(self):
        """
        Prints all cards stored in card management app.
        :return: None
        """
        output = ""
        for card in self._card_list:
            output += f"{card}\n"
        print(output)

    def view_cards_by_type(self):
        """
        See cards in app by type (determined by card subclasses).
        :return: None
        """
        UserInterface.display_view_cards_by_type(self)

    def add_card(self):
        """
        Add card to app.
        :return: None
        """
        UserInterface.display_add_card(self)

    def delete_card(self):
        """
        Delete a specific card from the app.
        :return: None
        """
        cards = self.search_by_issuer()
        if len(cards) is not 0:
            try:
                i = 0
                output = ""
                for card in cards:
                    output += f"{i + 1}.\n {card}"
                delete_index = int(
                    input("\nWhich card would you like to delete?\n"
                          "Enter X for Card #X: "))
                card_to_delete = cards[delete_index - 1]
                card_id = card_to_delete.id

                for card in self._card_list:
                    if card.id == card_id:
                        self._card_list.remove(card)
                        print("\nYour card was deleted successfully.")
            except ValueError as e:
                print(f"Invalid input. Enter the number associated "
                      f"with the card you would like to delete.")

    def search_card(self):
        """
        Search through stored cards.
        :return: None
        """
        user_input = UserInterface.display_search_menu()
        choices = {
            1: self.search_by_issuer,
            2: self.search_by_id,
            3: sys.exit
        }
        choices.get(user_input)()

    def search_by_issuer(self):
        """
        Prompts user to search for card by specifying card issuer.
        :return: None
        """
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
                output += f"\n*********** CARD #{i} ***********{card}"
                i += 1
            print(output)
        return cards

    def search_by_id(self):
        """
        Prompts user for ID of card they want to search.
        :return: None
        """
        try:
            card_id = int(input("Enter internal card id: "))
        except ValueError as e:
            print(f"Invalid input. {str(e).capitalize()}")
        else:
            found = False
            for card in self._card_list:
                if card.id == card_id:
                    found = True
                    print(card)
            if not found:
                print(f"No card with ID #{card_id} was found in the system.")

    def backup_data(self):
        """
        Back up cards in JSON format.
        :return: None
        """
        json_list = []
        json = "{\n\t"
        for card in self._card_list:
            json_list.append(card.jsonfy())
        json += ",\n".join(json_list)
        json += "\n}"
        self._card_list_json = json

        DataHandler.backup_data(self)


class UserInterface:
    """
    UserInterface allows user to interact with the program and provide inputs.
    """

    @staticmethod
    def welcome():
        """
        Welcome message displayed when program is first started.
        :return:
        """
        msg = "\n\n==== One-der Card ====\n" \
              "One-der Card is your one-stop solution for managing a\n" \
              "wallet full of gift cards, credit cards, business cards,\n" \
              "points cards,and more.\n"
        print(msg)

    @staticmethod
    def display_start_menu(manager):
        """
        Displays the options in the app.
        :param manager: CardManager
        :return: None
        """
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

                if 0 < user_input < 8:
                    choices.get(user_input)()

    @staticmethod
    def display_view_cards_by_type(manager):
        """
        Prompts the user to select which type they would like to view.
        :param manager: CardManager
        :return: None
        """
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
                card_type = CardType(user_input).name
                for card in manager.card_list:
                    if card.__class__.__name__.upper() == card_type:
                        print(card)
                        count += 1
                user_card_type = Catalogue.user_card_types.get(user_input)

                if count == 0:
                    print(f"No {user_card_type} cards are stored in One-der "
                          f"Card currently.")
                elif count == 1:
                    print(f"There is {count} card that matches your search "
                          f"criteria.")
                else:
                    print(f"There are {count} cards that match your search "
                          f"criteria.")

    @staticmethod
    def display_add_card(manager):
        """
        Prompts user with inputs on which card type they would like to add.
        :param manager: CardManager
        :return: None
        """
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
                card = Catalogue.create_menu.get(user_input)()
                manager.card_list.append(card)

    @staticmethod
    def display_search_menu():
        """
        Prompts the user on how they would like to search for a card.
        :return: None
        """
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
    """
    Represent a catalogue of items / data that is used in the app.
    """

    start_menu = {
        1: "View all cards",
        2: "View cards by type",
        3: "Add a card",
        4: "Search for a card",
        5: "Delete a card",
        6: "Back-up card data",
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
    # card_types = {
    #     1: "LoyaltyCard",
    #     2: "BalanceCard",
    #     3: "IDCard",
    #     4: "MoneyCard",
    #     5: "GovernmentIDCard",
    #     6: "AccessCard"
    # }

    card_types = {}
    card_type_list = []
    for child in Card.__subclasses__():
        card_type_list.append(child.__name__)
        for grandchild in child.__subclasses__():
            card_type_list.append(grandchild.__name__)
    i = 1
    for ctype in card_type_list:
        card_types[i] = ctype
        i += 1

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
        2: "Search by ID",
        3: "Close program"
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
        """
        Return a formatted output for menu.
        :param menu: {int: String} dictionary
        :return: String
        """
        output = "\n==== Menu ====\n"
        for k, v in menu.items():
            output += f"{k}. {v}\n"
        return output


class CardType(Enum):
    """
    Specifies accepted Card types.
    """
    LOYALTYCARD = 1
    BALANCECARD = 2
    IDCARD = 3
    MONEYCARD = 4
    GOVERNMENTIDCARD = 5
    ACCESSCARD = 6


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

    # Manually pre-loading with cards
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
