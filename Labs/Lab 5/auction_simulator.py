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
        """
        Add bidders to auction registry.
        :param bidder: Bidder
        :return: None
        """
        self._bidders.append(bidder)

    def register_bidders(self, auctioneer):
        """
        Register Bidders to a given auctioneer.
        :param auctioneer: Auctioneer
        :return: None
        """
        for bidder in self._bidders:
            auctioneer.add(bidder)

    def start(self, auctioneer):
        """
        Start the auction process
        :param auctioneer: Auctioneer
        :return: None
        """
        print(f"Auctioning {self.item} starting at"
              f" {'${:,.2f}'.format(self.starting_price)}")
        self.register_bidders(auctioneer)
        auctioneer.start_bid(self._starting_price)


        # start = Bidder("Starting price", 0, 0, 0, 0)
        # auctioneer._highest_current_bid = self._starting_price
        # auctioneer._highest_current_bidder = "Starting price"
        # auctioneer.inform_bidders()


class Auctioneer:
    """
    Auctioneer is responsible for keeping track of bidders, their highest
    bids, and the highest bid on the item being auctioned.
    """
    def __init__(self, bidders=[], highest_current_bid=0,
                 highest_current_bidder=0):
        self._bidders = bidders
        self._highest_current_bid = highest_current_bid
        self._highest_current_bidder = highest_current_bidder
    #
    # @traffic_light.setter
    # def traffic_light(self, value):
    #     """
    #     Allows the system to assign a new state to the traffic light
    #     state. This will cause all the observers to be called.
    #     :param value: TrafficLightState enum.
    #     """
    #     self._light = value
    #     self.execute_callbacks()]

    @property
    def highest_current_bid(self):
        return self._highest_current_bid

    @highest_current_bid.setter
    def highest_current_bid(self, bid):
        self._highest_current_bid = bid
        self.inform_bidders()

    @property
    def highest_current_bidder(self):
        return self._highest_current_bidder

    def start_bid(self, price):
        self.highest_current_bid = price
        self._highest_current_bidder = "Starting price"

    def add(self, callback):
        """
        Attaches an observer method as to the list of observer callbacks.
        These methods must have the signature
        my_method(self, traffic_light)
        :param callback: a method with signature
        my_method(self, traffic_light)
        """
        self._bidders.append(callback)

    def inform_bidders(self):
        """
        Notifies all the bidders of the current highest bid.
        """
        for bidder in self._bidders:
            bidder(self)


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

    def _check_bidder(self, auctioneer):
        return auctioneer.highest_current_bidder is not self._name

    def _check_budget(self, auctioneer):
        bid = auctioneer.highest_current_bid * self._bid_increase_perc
        return self._budget > bid

    def _check_desire(self):
        likelihood_to_bid = random()
        return self._bid_probability >= likelihood_to_bid

    def __call__(self, auctioneer):
        """
        Allow bidder to place a new bid with the Auctioneer.
        :param auctioneer: Auctioneer
        :return: None
        """
        if self._check_bidder(auctioneer) and self._check_budget(auctioneer) \
                and self._check_desire():
            print(f"{self._name} would like to place a bid")
            # auctioneer.accept_bid()


def main():
    item_name = ""
    starting_price = 0
    num_of_bidders = 0
    name = ""
    budget = 0
    inc_per = 1

    while True:
        try:
            item_name = input("Name of item being auctioned: ")
            starting_price = float(input("Starting price: "))
            num_of_bidders = int(input("Number of bidders: "))
        except ValueError as e:
            print(e)
        else:
            break

    auction = Auction(item_name, starting_price)

    for i in range(num_of_bidders):
        try:
            name = input(f"Enter bidder #{num_of_bidders}'s name: ")
            budget = float(input("Budget: "))
            inc_perc = float(input("Bid increase %: "))
        except ValueError as e:
            print(e)
        auction.add(Bidder(name, budget, inc_per))
        print(f"Bidder {name} added")

    auctioneer = Auctioneer()
    print(auction.start(auctioneer))

    print(f"Auctioneer highest current bidder:"
          f" {auctioneer._highest_current_bidder}")
    print(f"Auctioneer starting price: {auctioneer._highest_current_bid}")


    # while num_of_bidders > 0:
    #     name = input(f"Enter bidder #{num_of_bidders}'s name: ")
    #     budget = 0
    #     inc_per = 1
    #     while True:
    #         try:
    #             budget = float(input("Budget: "))
    #         except ValueError as e:
    #             print(f"Input is not a float. Try again.")
    #             continue
    #         else:
    #             break
    #     while True:
    #         try:
    #             inc_perc = float(input("Bid increase %: "))
    #         except ValueError as e:
    #             print(f"Input is not a float. Try again.")
    #             continue
    #         else:
    #             break
    #     auction.add(Bidder(name, budget, inc_per))
    #     print(f"Bidder {name} added")
    #     num_of_bidders -= 1

    # item_name = input("Name of item being auctioned: ")
    # starting_price = 0
    #
    # while True:
    #     try:
    #         starting_price = float(input("Starting price: "))
    #     except ValueError as e:
    #         print(f"Input is not a float. Try again.")
    #         continue
    #     else:
    #         break
    #
    # auction = Auction(item_name, starting_price)
    #
    # num_of_bidders = 0
    #
    # while True:
    #     try:
    #         num_of_bidders = int(input("Number of bidders: "))
    #     except ValueError as e:
    #         print(f"Input is not an integer. Try again.")
    #         continue
    #     else:
    #         break
    #
    # while num_of_bidders > 0:
    #     name = input(f"Enter bidder #{num_of_bidders}'s name: ")
    #     budget = 0
    #     inc_per = 1
    #     while True:
    #         try:
    #             budget = float(input("Budget: "))
    #         except ValueError as e:
    #             print(f"Input is not a float. Try again.")
    #             continue
    #         else:
    #             break
    #     while True:
    #         try:
    #             inc_perc = float(input("Bid increase %: "))
    #         except ValueError as e:
    #             print(f"Input is not a float. Try again.")
    #             continue
    #         else:
    #             break
    #     auction.add(Bidder(name, budget, inc_per))
    #     print(f"Bidder {name} added")
    #     num_of_bidders -= 1
    #
    # auctioneer = Auctioneer()
    # # auction.register_bidders(auctioneer)
    # print(f"Bidders registered to auctioneer.")
    #
    # print(auction.start(auctioneer))


if __name__ == "__main__":
    main()