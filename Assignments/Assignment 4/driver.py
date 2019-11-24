import pandas as pd
import numpy as np
from enum import Enum
from factories import NikaFactory, LululimeFactory, PineappleRepublicFactory


class FileExtensionError(Exception):
    def __init__(self):
        super().__init__("File must end with .xlsx extension.")


class GarmentType(Enum):
    SHIRT_MEN = "shirtmen"
    SHIRT_WOMEN = "shirtwomen"
    SOCK_PAIR_UNISEX = "sockpairunisex"


class GarmentMaker:

    def __init__(self):
        self.shirts_men = []
        self.shirts_women = []
        self.socks_unisex = []
        self.processor = OrderProcessor()
        self.garment_dict = {
            "SHIRT_MEN": self.shirt_men_maker,
            "SHIRT_WOMEN": self.shirt_women_maker,
            "SOCK_PAIR_UNISEX": self.socks_unisex_maker
        }

    def start(self):
        path = input("Enter the file path of the Excel file: ")
        self.processor.import_data(path)
        self.processor.format_data()
        self.processor.create_orders()
        orders = self.processor.process_next_order()
        for o in orders:
            self.garment_dict[o.garment.name](o)

    # invokes the correct method on the brandfactory passed to it
    # to create the correct number of the correct type of clothing
    def shirt_men_maker(self, shirt_men_order):
        shirt_men_order.factory.create_shirt_men()

    def shirt_women_maker(self, shirt_women_order):
        print("I'm shirt women maker")

    def socks_unisex_maker(self, socks_unisex_order):
        print("I'm socks unisex maker")

    def write_report(self):
        pass


class OrderProcessor:

    brand_dict = {
        "lululime": LululimeFactory(),
        "pineapplerepublic": PineappleRepublicFactory(),
        "nika": NikaFactory()
    }

    def __init__(self):
        pd.set_option("display.max_rows", 200)
        pd.set_option('display.max_columns', 200)
        pd.set_option('display.width', 1000)
        self.df = None
        self.order_list = []

    def import_data(self, path):
        """
        Import data from the specified path as a dataframe.
        :param path: str
        :return: None
        """
        if not path.endswith(".xlsx"):
            raise FileExtensionError
        else:
            self.df = pd.read_excel(path)

    def format_data(self):
        """
        Format data such that Order details can be passed to Garments
        easily.  Data is stored as a list of dictionary Order objects.
        :return: None
        """
        self.df.columns = map(str.lower, self.df.columns)
        self.df.columns = self.df.columns.str.replace(' ', '_')
        self.df.columns = self.df.columns.str.replace('/', '_or_')
        self.df = self.df.to_dict("records")

    def create_orders(self):
        for details in self.df:
            brand = details.pop('brand').lower()
            g_type = details.pop('garment').lower()
            # Determine Factory based on Order brand name
            factory = OrderProcessor.brand_dict[brand]
            # Determine type of Garment based on garment attribute
            garment = GarmentType(g_type)
            # Add order to order list
            self.order_list.append(Order(details, factory, garment))

    def process_next_order(self):
        """
        Yield an Order object
        :return: Order
        """
        yield from (order for order in self.order_list)


class Order:

    def __init__(self, details, factory, garment):
        self.details = details
        self.factory = factory
        self.garment = garment

    def __str__(self):
        return f"Details: {self.details}\n" \
               f"Factory: {self.factory}\n" \
               f"Garment: {self.garment.name}\n"


def main():
    gm = GarmentMaker()
    gm.start()


if __name__ == "__main__":
    main()