"""
Module captures and represents most common card types for card management
system.
"""
import json
from abc import ABC


class Address:
    """
    Represent mailing address.
    """
    def __init__(self, company_name, street, postal_code, city, province,
                 country):
        self.company_name = company_name
        self.street = street
        self.postal_code = postal_code
        self.city = city
        self.province = province
        self.country = country

    def __str__(self):
        return f"{self.company_name}\n" \
               f"{self.street}\n" \
               f"{self.postal_code}\n" \
               f"{self.city} {self.province} {self.country}"


class Card(ABC):
    """
    Represent basic card information issued by companies.
    """
    def __init__(self, address):
        self._address = address

    def jsonfy(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          indent=4)

    def __str__(self):
        return f"{self._address}\n"


class LoyaltyCard(Card):
    def __init__(self, points, rewards, address):
        super().__init__(address)
        self._points = points
        self._rewards = rewards

    def __str__(self):
        rewards = ""
        for reward, points in self._rewards.items():
            rewards += f"{reward} >>> {points} PTS\n"
        return f"====== {self._address.company_name.upper()} LOYALTY CARD ======\n" \
               f"Current Points: {self._points}\n" \
               f"Redeemable Rewards\n" \
               f"{rewards}\n" \
               f"{super().__str__()}"


class BalanceCard(Card):
    """
    Represent a card with a balance that can be used at a specific company.
    e.g. gift card, transit fare card
    """
    def __init__(self, card_no, balance, address):
        super().__init__(address)
        self._card_no = card_no
        self._balance = balance

    def __str__(self):
        return f"====== {self._address.company_name.upper()} CARD ======\n" \
               f"Barcode: {self._card_no}\n" \
               f"{'${:,.2f}'.format(self._balance)} credit left\n" \
               f"{super().__str__()}"


class IDCard(Card):
    """
    Represent identification card.
    """
    def __init__(self, name, card_no, expiry_date, address):
        """
        Initialise IDCard.
        :param name: String
        :param card_no: String
        :param expiry_date: Date
        :param address: Address
        """
        super().__init__(address)
        self._name = name
        self._card_no = card_no
        self._expiry_date = expiry_date

    def __str__(self):
        expiry = ""
        if self._expiry_date is not None:
            expiry = f"Expires on {self._expiry_date.strftime('%Y-%m-%d')}\n"
        return f"====== {self._address.company_name.upper()} ID CARD ======\n" \
               f"{self._name}\n" \
               f"{self._card_no}\n" \
               f"{expiry}\n" \
               f"{super().__str__()}"


class AccessCard(Card):
    def __init__(self, card_no, expiry_date, detail, address):
        """
        Initialise a card that grants access.
        If card does not expire, set expiry_date to None
        e.g. novelty ticket, library card, gym membership
        :param card_no: String
        :param expiry_date: Date
        :param detail: String
        :param address: Address
        """
        super().__init__(address)
        self._card_no = card_no
        self._expiry_date = expiry_date
        self._detail = detail

    def __str__(self):
        expiry = ""
        if self._expiry_date is not None:
            expiry = f"Expires on {self._expiry_date.strftime('%Y-%m-%d')}\n"
        return f"======{self._address.company_name.upper()} ACCESS CARD " \
               f"======\n" \
               f"{self._card_no}\n" \
               f"{expiry}" \
               f"{'' if self._detail is None else self._detail}\n" \
               f"{self._address}"


class MoneyCard(IDCard):
    def __init__(self, csv, card_type, name, card_no, expiry_date, address):
        super().__init__(name, card_no, expiry_date, address)
        self._csv = csv
        self._card_type = card_type

    def __str__(self):
        expiry = ""
        if self._expiry_date is not None:
            expiry = f"Expires on {self._expiry_date.strftime('%Y-%m-%d')}\n"
        return f"====== {self._card_type.upper()} CARD ======\n" \
               f"{self._name}\n" \
               f"{self._card_no}\n" \
               f"CSV: {self._csv}\n" \
               f"{expiry}" \
                f"{self._address}"


class GovernmentIDCard(IDCard):
    def __init__(self, dob, weight, height, sex, eyes, hair, home_address,
                 name, card_no, expiry_date, address):
        super().__init__(name, card_no, expiry_date, address)
        self._dob = dob
        self._weight = weight
        self._height = height
        self._sex = sex
        self._eyes = eyes
        self._hair = hair
        self._home_address = home_address

    def __str__(self):
        return f"====== {self._address.company_name.upper()} CARD ======\n" \
               f"{self._name}\n" \
               f"ID: {self._card_no}\n" \
               f"Wt: {self._weight} kg\tHt: {self._height} cm\n" \
               f"Sex: {self._sex.upper()} \tEyes: " \
               f"{self._eyes.upper()}\tHair: " \
               f":{self._hair.upper()}\n" \
               f"{self._home_address}\n" \
               f"{self._address}"


def main():
    address = Address("BCIT", "555 Seymour Street", "V2F 9K1", "Vancouver",
                      "BC", "Canada")

    g_address = Address("Ghibli Museum", "1 Chome-1-83 Shimorenjaku", "181-0013",
                        "Mitaka", "Tokyo", "Japan")

    h_address = Address("Home address", "123 Main Street", "V8K 1P3",
                        "Vancouver",
                        "BC", "Canada")

    i_address = Address("ICBC", "999 Robson Street", "V2B 2N9", "Vancouver",
                        "BC", "Canada")
    # CARD
    # card = Card(address)

    # LOYALTY CARD
    # rewards = {"Bubble Waffles" : 5, "Brown Sugar BBT": 10}
    # card = LoyaltyCard(9, rewards, address)

    # BALANCE CARD
    # card = BalanceCard("2383 1239 9101", 438.2, address)

    # ID Card
    # card = IDCard(("Ms", "Christy C Yau"), "3492 9384 2342", "10/22", address)

    # Access Card
    # card = AccessCard("3428 2398 3021", None, "Ghibili Museum Ticket",
    #                   g_address)

    # Money Card
    # card = MoneyCard("281", CardType.VISA, ("Ms", "Christy C Yau"),
    #                  "3249 9845 2911", "01/22", address)
    # card = MoneyCard("564", "VISA", ("Ms", "Christy C Yau"),
    #                  "8673 1214 6563", "02/22", address)

    # Government ID Card
    card = GovernmentIDCard("10/09/1989", 61.1, 164, "F", "Brown", "Brown",
                            h_address, ("Ms", "Christy C Yau"), "2847 6951 3241",
                            "12/23", i_address)

    # print(card.jsonfy())
    # print(card)
    print(card.__class__.__name__)

if __name__ == "__main__":
    main()