"""
Management side of card management system.  Includes data import / export
and the ability for users to interact with the system.
"""
import sys
from card_creator import CardCreator


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
        return

    def search_card(self):
        return

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
                    4: manager.delete_card,
                    5: manager.backup_data,
                    6: sys.exit
                }

                if user_input == 1:
                    print(choices.get(user_input)())

                if user_input == 3 or user_input == 2:
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


class Catalogue:
    start_menu = {
        1: "View all cards",
        2: "View cards by type",
        3: "Add a card",
        4: "Delete a card",
        5: "Export card data",
        6: "Close program"
    }

    card_type_menu = {
        1: "Loyalty cards (e.g. stamp cards)",
        2: "Cards with balances (e.g. transit fare, gift card)",
        3: "Basic ID cards",
        4: "Credit / debit cards",
        5: "Government ID cards",
        6: "Basic membership cards (e.g. library or gym card)",
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
        3: "ID",
        4: "credit or debit",
        5: "government ID",
        6: "basic membership"
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
    manager.start()
    # manager.view_cards_by_type()


#     object.__class__.__name__
if __name__ == "__main__":
    main()
