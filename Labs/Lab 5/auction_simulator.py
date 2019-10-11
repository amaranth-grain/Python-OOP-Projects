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
        print(f"\nAuctioning {self.item} starting at"
              f" {'${:,.2f}'.format(self.starting_price)}")
        self.register_bidders(auctioneer)
        auctioneer.start_bid(self._starting_price)


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

    @property
    def highest_current_bid(self):
        return self._highest_current_bid

    @highest_current_bid.setter
    def highest_current_bid(self, bid):
        self._highest_current_bid = bid
        self.inform_bidders()

    @property
    def bidders(self):
        return self._bidders

    @property
    def highest_current_bidder(self):
        return self._highest_current_bidder

    def start_bid(self, price):
        self._highest_current_bidder = "Starting price"
        self.highest_current_bid = price

    def add(self, callback):
        """
        Attaches an observer method as to the list of observer callbacks.
        These methods must have the signature
        my_method(self, traffic_light)
        :param callback: a method with signature
        my_method(self, traffic_light)
        """
        self._bidders.append(callback)

    def accept_bid(self, name, price):
        if price > self.highest_current_bid:
            print(f"{name} bid {'${:,.2f}'.format(price)} in response to "
                  f"{self._highest_current_bidder}'s bid of "
                  f"{'${:,.2f}'.format(self._highest_current_bid)}!")
            self._highest_current_bidder = name
            self.highest_current_bid = price

    def inform_bidders(self):
        """
        Notifies all the bidders of the current highest bid.
        """
        for bidder in self._bidders:
            bidder(self)

    def announce_winner(self):
        if self.highest_current_bidder is not "Starting price":
            print(f"\nThe winner of this auction is: "
                  f"{self.highest_current_bidder} at"
                  f" {'${:,.2f}'.format(self._highest_current_bid)}!\n")
        else:
            print(f"No one made any bids!")

    def announce_highest_bids(self):
        highest_bids = {bidder.name: bidder.highest_bid for bidder in
                        self.bidders}
        print("====== Highest Bids per Bidder ======")
        for bidder, bid in highest_bids.items():
            print(f"Bidder: {bidder} Highest bid:"
                  f" {'${:,.2f}'.format(bid)}")


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

    @property
    def name(self):
        return self._name

    @property
    def bid_probability(self):
        return self._bid_probability

    @property
    def highest_bid(self):
        return self._highest_bid

    def _check_bidder(self, auctioneer):
        return auctioneer.highest_current_bidder is not self._name

    def _check_bid(self, auctioneer):
        bid = auctioneer.highest_current_bid * self._bid_increase_perc
        return self._budget > bid > auctioneer.highest_current_bid

    def make_bid(self, auctioneer):
        bid = auctioneer.highest_current_bid * self._bid_increase_perc
        self._highest_bid = bid

    def _check_desire(self):
        likelihood_to_bid = random()
        return self._bid_probability >= likelihood_to_bid

    def __call__(self, auctioneer):
        """
        Allow bidder to place a new bid with the Auctioneer.
        :param auctioneer: Auctioneer
        :return: None
        """
        if self._check_bidder(auctioneer) and self._check_bid(auctioneer) \
                and self._check_desire():
            self.make_bid(auctioneer)
            auctioneer.accept_bid(self._name, self._highest_bid)


def main():

    while True:
        try:
            item_name = input("Name of item being auctioned: ")
            starting_price = float(input("Starting price: "))
            num_of_bidders = int(input("Number of bidders: "))
        except ValueError as e:
            print(f"Invalid input -- {e}")
        else:
            break

    auction = Auction(item_name, starting_price)

    for i in range(num_of_bidders):
        while True:
            try:
                name = input(f"Enter bidder #{i + 1}'s name: ").capitalize()
                budget = float(input("Budget: "))
                inc_perc = float(input("Bid increase factor: "))
                if inc_perc <= 1:
                    raise ValueError("Value must be greater "
                                     "than 1.")
            except ValueError as e:
                print(e)
            else:
                auction.add(Bidder(name, budget, inc_perc))
                print(f"Bidder {name} added")
                break

    auctioneer = Auctioneer()
    auction.start(auctioneer)
    auctioneer.announce_winner()
    auctioneer.announce_highest_bids()
    # For demo purposes, show bidders' bid probability
    print()
    for bidder in auctioneer.bidders:
        print(f"{bidder.name}'s bid prob: "
              f"{'{:,.2f}'.format(bidder.bid_probability)}")


if __name__ == "__main__":
    main()