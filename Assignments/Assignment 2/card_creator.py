"""
Module for creating all card types.
"""

from datetime import datetime
import card


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
                num_of_rewards = int(
                    input("Enter number of redeemable rewards: "))
                reward = ""
                for i in range(num_of_rewards):
                    reward = input(f"Enter reward #{i + 1}: ")
                    if len(reward.strip()) == 0:
                        raise ValueError("No fields can be left blank.")
                    reward_list.append(reward)

                for reward in reward_list:
                    points = int(input(f"Enter points value for {reward}: "))
                    reward_dict[reward] = points
                    raise ValueError("No fields can be left blank.")
            except ValueError as e:
                print("Invalid input. Try again.")
            else:
                val = False
                address = CardCreator.prompt_address("issuer")
                return card.LoyaltyCard(points, reward_dict, address)

    @staticmethod
    def prompt_address(address_type):
        try:
            name = input(f"Enter {address_type} name: ")
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
    def create_balance_card():
        try:
            card_no = input("Enter card number: ")
            balance = float(input("Enter card balance: "))
            if not isinstance(balance, float):
                raise ValueError
            address = CardCreator.prompt_address("issuer")
        except ValueError as e:
            print("Balance must be numerical.")
        else:
            return card.BalanceCard(card_no, balance, address)

    @staticmethod
    def create_id_card():
        card_no = None
        expiry_date = None
        address = None
        try:
            name = input("Enter your full name: ")
            ans = input("Are you adding a business card? (Y/N) ")
            if ans.upper() == "N":
                card_no = input("Enter card number: ")
                expiry_list = input("Enter expiry date as dd/mm/yy: ")
                expiry_list = expiry_list.split("/")
                if len(expiry_list) is not 3:
                    raise ValueError("Date was not formatted properly.")
                expiry_date = datetime(int(expiry_list[2]), int(expiry_list[1]),
                                       int(expiry_list[0]))
                address = CardCreator.prompt_address("issuer")
            elif ans.upper() == "Y":
                address = CardCreator.prompt_address("business")
        except ValueError as e:
            print(f"Invalid input. {str(e).capitalize()}")
        else:

            return card.IDCard(name, card_no, expiry_date, address)

    @staticmethod
    def create_money_card():
        expiry_date = None
        try:
            csv = int(input("Enter CSV code: "))
            if not isinstance(csv, int):
                raise TypeError("Your CSV code should be numerical.")
            card_type = input("Which type of card do you have?\n"
                              "1. Debit\n"
                              "2. Credit\n")
            if card_type == "1" or card_type.lower() == "debit":
                card_type = "DEBIT"
            elif card_type == "2" or card_type.lower() == "credit":
                card_type = "CREDIT"
                month = int(input("Enter expiry month: "))
                day = int(input("Enter expiry day: "))
                year = int(input("Enter expiry year (yyyy): "))
                expiry_date = datetime(year, month, day)
            else:
                raise ValueError("Invalid input. Select debit or credit.")
            name = input("Enter your full name: ")
            card_no = input("Enter card number: ")
        except ValueError as e:
            print(f"Invalid input -- {e}")
        except TypeError as e:
            print(f"Invalid type -- {e}")
        else:
            address = CardCreator.prompt_address("issuer")
            return card.MoneyCard(csv, card_type, name, card_no,
                                  expiry_date, address)

    @staticmethod
    def create_gov_card():
        try:
            dob_list = input("Enter date of birth as dd/mm/yy: ")
            dob_list = dob_list.split("/")
            if len(dob_list) is not 3:
                raise ValueError("Date was not formatted properly.")
            dob = datetime(int(dob_list[2]), int(dob_list[1]),
                           int(dob_list[0]))
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (cm): "))
            sex = input("Your sex (F/M/X): ")
            if sex not in ("F", "M", "X"):
                raise ValueError("Invalid input. Try again.")
            eyes = input("Eye colour: ")
            hair = input("Hair colour: ")
            home_address = CardCreator.prompt_address("home")
            full_name = input("Enter your full name: ")
            card_no = input("Enter card number: ")
            expiry_list = input("Enter expiry date as dd/mm/yy: ")
            expiry_list = expiry_list.split("/")
            if len(expiry_list) is not 3:
                raise ValueError("Date was not formatted properly.")
            expiry_date = datetime(int(expiry_list[2]), int(expiry_list[1]),
                                   int(expiry_list[0]))
        except ValueError as e:
            print(f"Invalid input. {str(e).capitalize()}")
        except IndexError as e:
            print(f"Invalid input. {str(e).capitalize()}")
        else:
            address = CardCreator.prompt_address("issuer")
            return card.GovernmentIDCard(dob, weight, height, sex, eyes,
                                         hair, home_address, full_name,
                                         card_no, expiry_date, address)

    @staticmethod
    def create_access_card():
        try:
            detail = None
            card_no = input("Enter card number: ")
            expiry_list = input("Enter expiry date as dd/mm/yy: ")
            expiry_list = expiry_list.split("/")
            if len(expiry_list) is not 3:
                raise ValueError("Date was not formatted properly.")
            expiry_date = datetime(int(expiry_list[2]), int(expiry_list[1]),
                                   int(expiry_list[0]))
            ans = input("Are there additional details you would "
                        "like to record? (Y/N) ")
            if ans.upper() == "Y":
                detail = input("Enter card details: ")
            if len(card_no.strip()) == 0:
                raise ValueError("No fields can be left blank.")
        except ValueError as e:
            print(f"Invalid input. {str(e).capitalize()}")
        else:
            address = CardCreator.prompt_address("issuer")
            return card.AccessCard(card_no, expiry_date, detail, address)

