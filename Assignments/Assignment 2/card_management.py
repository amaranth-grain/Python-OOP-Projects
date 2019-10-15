"""
Management side of card management system.  Includes data import / export
and the ability for users to interact with the system.
"""
import json
import sys

import card


class CardManager:
    def __init__(self):
        self._card_list = []

    @property
    def card_list(self):
        return self._card_list

    #     with open("./sample_card_data.txt", "r") as data_file:
    #         self._card_list = json.loads(data_file.read())

    def start(self):
        UserInterface.display_start_menu(self)

    def view_all_cards(self):
        output = ""
        for card in self._card_list:
            output += f"* {card}\n"
        return output

    def view_cards_by_type(self):
        UserInterface.display_view_cards_by_type(self)

    def add_card(self):
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
                self._card_list.append(card)

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
        output = UserInterface.welcome()
        output += Catalogue.get_menu(Catalogue.start_menu)
        print(output)
        user_input = 0
        while user_input > 6 or user_input < 1:
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
                ctype = Catalogue.card_types.get(user_input)
                for card in manager.card_list:
                    if card.__class__.__name__ is ctype:
                        print(card)


class CardCreator:
    """
    Create card of specific subtype for card management system.
    """

    @staticmethod
    def create_loyalty_card():
        reward_list = []
        reward_dict = {}
        val = True
        while val:
            try:
                points = int(input("Enter current loyalty points earned: "))
                num_of_rewards = int(input("Enter number of redeemable rewards: "))

                for i in range(num_of_rewards):
                    reward = input(f"Enter reward #{i + 1}: ")
                    reward_list.append(reward)

                for reward in reward_list:
                    points = int(input(f"Enter points value for {reward}: "))
                    reward_dict[reward] = points
            except ValueError as e:
                print("Invalid input. Try again.")
            else:
                val = False
                address = CardCreator.prompt_address()
                return card.LoyaltyCard(points, reward_dict, address)

    @staticmethod
    def prompt_address():
        try:
            name = input("Enter issuer name: ")
            street = input("Enter street address: ")
            postal = input("Enter postal code: ")
            if len(postal) < 5 or len(postal) > 7:
                raise ValueError("Invalid postal code. Try again.")
            city = input("Enter city: ")
            province = input("Enter province: ")
            country = input("Enter country: ")
        except ValueError as e:
            print(e)
        else:
            return card.Address(name, street, postal, city, province, country)

    @staticmethod
    def create_balance_card(card_no, balance, address):
        return card.BalanceCard(card_no, balance, address)

    @staticmethod
    def create_id_card(name, card_no, expiry_date, address):
        return card.IDCard(name, card_no, expiry_date, address)

    @staticmethod
    def create_money_card(csv, card_type, name, card_no, expiry_date, address):
        return card.MoneyCard(csv, card_type, name, card_no, expiry_date,
                              address)

    @staticmethod
    def create_gov_card(dob, weight, height, sex, eyes, hair, home_address,
                        name, card_no, expiry_date, address):
        return card.GovernmentIDCard(dob, weight, height, sex, eyes, hair,
                                     home_address, name, card_no,
                                     expiry_date, address)


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
        3: "All ID cards",
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

    create_menu = {
        1: CardCreator.create_loyalty_card
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
