"""
Module captures and represents most common card types for card management
system.
"""
import json
from datetime import datetime
from abc import ABC
from enum import Enum


class Address:
    """
    Represent mailing address.
    """

    def __init__(self, street, postal_code, city, province, country):
        self.street = street
        self.postal_code = postal_code
        self.city = city
        self.province = province
        self.country = country

    def __str__(self):
        return f"{self.street}\n" \
               f"{self.postal_code}\n" \
               f"{self.city} {self.province} {self.country}"


class CardType(Enum):
    """
    Accepted money card types.
    """
    DEBIT = 1
    VISA = 2
    MASTERCARD = 3
    AMEX = 4


class Card(ABC):
    """
    Basic information for company-issued cards.
    """

    def __init__(self, company_name, company_phone, company_site,
                 company_address):
        """
        Initialise Card with basic company information
        :param name: String
        :param phone: String
        :param site: String
        :param company_address: Address
        """
        self._company_name = company_name
        self._company_phone = company_phone
        self._company_site = company_site
        self._company_address = company_address

    def jsonfy(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          indent=4)

    def __str__(self):
        return f"* {self._company_name.upper()} *\n" \
               f"{self._company_address}\n" \
               f"Tel: {self._company_phone}\n" \
               f"Website: {self._company_site}"


class BusinessCard(Card):
    """
    An individual's business card.
    """

    def __init__(self, company_name, company_phone, company_site,
                 company_address, fname, lname, title,
                 job_title, email, phone):
        super().__init__(company_name, company_phone, company_site,
                         company_address)
        self._fname = fname
        self._lname = lname
        self._title = title
        self._job_title = job_title
        self._email = email
        self._phone = phone

    def format_json_card(self):
        return

    def __str__(self):
        return f"===== {self._fname} {self._lname}, {self._title} =====\n" \
               f"{self._job_title}\n" \
               f"E-mail: {self._email}\n" \
               f"Tel: {self._phone}\n" \
               f"{super().__str__()}\n" \
               f"============================="


class TicketCard(Card):
    """
    Novelty ticket cards issued by companies.
    """

    def __init__(self, company_name, company_phone, company_site,
                 company_address, event_date, event_time, dress_code):
        super().__init__(company_name, company_phone, company_site,
                         company_address)
        self._event_date = event_date
        self._event_time = event_time
        self._dress_code = dress_code

    def format_json_card(self):
        return

    def __str__(self):
        return f"\n======== TICKET ========\n" \
               f"EVENT: {self._event_date} @ {self._event_time}\n" \
               f"DRESS CODE: {self._dress_code}\n" \
               f"{super().__str__()}\n" \
               f"============================"


class RewardCard(Card):
    """
    Reward card where rewards are redeemed through a type of points system
    or are of the "Buy X get Y free" stamp card format.
    """

    def __init__(self, company_name, company_phone, company_site,
                 company_address, curr_points,
                 reward_list):
        super().__init__(company_name, company_phone, company_site,
                         company_address)
        self._curr_points = curr_points
        self._reward_list = reward_list

    def format_json_card(self):
        return

    def __str__(self):
        return


class BalanceCard(Card):
    """
    For any low-security card that involves a balance, such as gift
    card or transit fare card.
    """

    def __init__(self, company_name, company_phone, company_site,
                 company_address, card_no, curr_balance):
        super().__init__(company_name, company_phone, company_site,
                         company_address)
        self._card_no = card_no
        self._curr_balance = curr_balance

    def format_json_card(self):
        return

    def __str__(self):
        return


class MemberCard(Card):
    """
    Any card that is primarily used by issuing a member ID to cardholder.
    Encompasses bank cards, SIN cards, student cards, etc.
    """

    def __init__(self, company_name, company_phone, company_site,
                 company_address, card_no, expiry_date):
        super().__init__(company_name, company_phone, company_site,
                         company_address)
        self._card_no = card_no
        self._expiry_date = expiry_date

    def format_json_card(self):
        return

    def __str__(self):
        return


class MoneyCard(MemberCard):
    """
    For debit and credit cards.
    """

    def __init__(self, company_name, company_phone, company_site,
                 company_address, card_no, expiry_date,
                 csv, card_type, chip_enabled, billing_address):
        super().__init__(company_name, company_phone, company_site,
                         company_address, card_no, expiry_date)
        self._csv = csv
        self._card_type = card_type
        self._chip_enabled = chip_enabled
        self._billing_address = billing_address

    def format_json_card(self):
        return

    def __str__(self):
        return


class MemberRewardCard(RewardCard, MemberCard):
    """
    For more complex reward systems that issue membership IDs to cardholders.
    Includes cards such as Air Miles or Scene cards.
    """

    def __init__(self, company_name, company_phone, company_site,
                 company_address, curr_points,
                 reward_list, card_no, expiry_date):
        RewardCard.__init__(curr_points, reward_list)
        MemberCard.__init__(company_name, company_phone, company_site,
                            company_address, card_no, expiry_date)

    def format_json_card(self):
        return

    def __str__(self):
        return


def main():
    add = Address("555 Seymour Street", "V3K 2H1", "Vancouver", "BC", "Canada")
    add_ghib = Address("1 Chome-1-83 Shimorenjaku", "181-0013",
                       "Mitaka", "Tokyo", "Japan")
    # card = Card("BCIT Downtown Campus", "604-555-2143", "www.bcit.ca", add)
    # business_card = BusinessCard("BCIT Downtown Campus", "604-555-7890",
    #                              "www.bcit.ca", add, "Rahul", "Kukreja",
    #                              "Mr", "Programming Instructor",
    #                              "rkukreja@bcit.ca", "778-555-8989")
    ticket = TicketCard("Ghibli Museum, Mitaka", "81 570-055-777",
                        "www.ghibli-museum.jp", add_ghib,
                        "5/24/2020",
                        "11:00 AM", "Casual")
    print(ticket.jsonfy())
    print(ticket)

if __name__ == "__main__":
    main()
