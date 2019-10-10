"""
Demonstrate observer pattern through auction simulation.
"""
from random import random


class Auction:
    def __init__(self, item, starting_price, bidders=None):
        """
        Initialise Auction object responsible for setting up auction.
        :param bidders: list of Bidder objects
        :param item: String representing name of item being auctioned
        :param starting_price: float
        """
        self._bidders = bidders
        self._item = item
        self._starting_price = starting_price
        if self._bidders is None:
            self._bidders = []

    @property
    def item(self):
        return self._item

    @property
    def starting_price(self):
        return self._starting_price

    def add(self, bidder):
        self._bidders.append(bidder)

    def item_sold(self):
        return f"{self._item.title()} was sold to {self._bidders}!"


class Auctioneer:
    def __init__(self, bidders, highest_current_bid, highest_current_bidder):
        self._bidders = bidders
        self._highest_current_bid = highest_current_bid
        self._highest_current_bidder = highest_current_bidder


class Bidder:
    """
    Represent bidder as callable object.
    """
    def __init__(self, name, budget, bid_increase_perc, bid_probability=None,
                 highest_bid=0):
        """
        Initialise Bidder object.
        :param name: name of bidder as String
        :param budget: max amount of money bidder will spend, float
        :param bid_probability: probability between 0 and 1, float
        :param bid_increase_perc: float grater than 1. 1.4 = 140%
        :param highest_bid: highest bid made by this bidder, float
        """
        self._name = name
        self._budget = budget
        self._bid_probability = bid_probability
        self._bid_increase_perc = bid_increase_perc
        self._highest_bid = highest_bid
        if self._bid_probability is None:
            self._bid_probability = random()
            # print(self._bid_probability)

    def __call__(self, auctioneer):
        """
        Allow bidder to place a new bid with the Auctioneer.
        :param auctioneer: Auctioneer
        :return:
        """


def main():
    item_name = input("Name of item being auctioned: ")
    starting_price = 0
    while True:
        try:
            starting_price = float(input("Starting price: "))
        except ValueError as e:
            print(f"Input is not a float. Try again.")
            continue
        else:
            break

    auction = Auction(item_name, starting_price)

    num_of_bidders = 0

    while True:
        try:
            num_of_bidders = int(input("Number of bidders: "))
        except ValueError as e:
            print(f"Input is not an integer. Try again.")
            continue
        else:
            break

    while num_of_bidders > 0:
        name = input(f"Enter bidder #{num_of_bidders}'s name: ")
        budget = 0
        inc_per = 1
        while True:
            try:
                budget = float(input("Budget: "))
            except ValueError as e:
                print(f"Input is not a float. Try again.")
                continue
            else:
                break
        while True:
            try:
                inc_perc = float(input("Bid increase %: "))
            except ValueError as e:
                print(f"Input is not a float. Try again.")
                continue
            else:
                break
        auction.add(Bidder(name, budget, inc_per))
        print(f"Bidder {name} added")
        num_of_bidders -= 1

    print(f"Auctioning {auction.item} starting at"
          f" {'${:,.2f}'.format(auction.starting_price)}")


if __name__ == "__main__":
    main()