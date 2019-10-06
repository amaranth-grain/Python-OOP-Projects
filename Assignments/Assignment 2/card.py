"""
Module captures and represents most common card types for card management
system.
"""
from abc import ABC
from enum import Enum


class CardType(Enum):
    """
    Accepted money card types.
    """
    DEBIT = 1
    VISA = 2
    MASTERCARD = 3
    AMEX = 4


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


class Card(ABC):

    _card_system_no = 1

    """
    Basic information for company-issued cards.
    """
    def __init__(self, company_address, company_data):
        self._company_address = company_address
        self._company_data = company_data

    @property
    def company_data(self):
        return self._company_data

    @company_data.setter
    def company_data(self, data):
        self._company_data = data

    @classmethod
    def increment_id(cls):
        cls._card_system_no += 1
        return cls._card_system_no

    def format_json_card(self):
        return

    def __str__(self):
        return


class BusinessCard(Card):
    """
    An individual's business card.
    """
    def __init__(self, company_address, company_data, fname, lname, title,
                 job_title, email, phone):
        super().__init__(company_address, company_data)
        self._fname = fname
        self._lname = lname
        self._title = title
        self._job_title = job_title
        self._email = email
        self._phone = phone

    def format_json_card(self):
        return

    def __str__(self):
        return


class TicketCard(Card):
    """
    Novelty ticket cards issued by companies.
    """
    def __init__(self, company_address, company_data, event_date,
                 event_time, dress_code):
        super().__init__(company_address, company_data)
        self._event_date = event_date
        self._event_time = event_time
        self._dress_code = dress_code

    def format_json_card(self):
        return

    def __str__(self):
        return


class RewardCard(Card):
    """
    Reward card where rewards are redeemed through a type of points system
    or are of the "Buy X get Y free" stamp card format.
    """
    def __init__(self, company_address, company_data, curr_points,
                 reward_list):
        super().__init__(company_address, company_data)
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
    def __init__(self, company_address, company_data, card_no, curr_balance):
        super().__init__(company_address, company_data)
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
    def __init__(self, company_address, company_data, card_no, expiry_date):
        super().__init__(company_address, company_data)
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
    def __init__(self, company_address, company_data, card_no, expiry_date,
                 csv, card_type, chip_enabled, billing_address):
        super().__init__(company_address, company_data, card_no, expiry_date)
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
    def __init__(self, company_address, company_data, curr_points,
                 reward_list, card_no, expiry_date):
        RewardCard.__init__(curr_points, reward_list)
        MemberCard.__init__(company_address, company_data, card_no, expiry_date)

    def format_json_card(self):
        return

    def __str__(self):
        return


