"""
Client side of the abstract factory pattern.
"""

import pandas as pd
from garments import GarmentType
from factories import NikaFactory, LululimeFactory, PineappleRepublicFactory


class FileExtensionError(Exception):
    """
    Error raised when Pandas attempts to read a non-xlsx file.
    """

    def __init__(self):
        super().__init__("File must end with .xlsx extension.")


class CorruptedFileError(Exception):
    """
    Error raised when the correct headings could not be read.
    """

    def __init__(self):
        super().__init__("File is corrupted. Make sure column headings "
                         "match the template.")


class GarmentMaker:
    """
    Produce garments based on order quanity and attributes.
    Decoupled from concrete garments that Garment Maker makes.
    """

    def __init__(self):
        """
        Initialise garment maker to process orders.
        """
        self.inventory = []
        self.processor = OrderProcessor()
        self.garment_maker_dict = {
            "SHIRT_MEN": self.shirt_men_maker,
            "SHIRT_WOMEN": self.shirt_women_maker,
            "SOCK_PAIR_UNISEX": self.socks_unisex_maker
        }

    def start(self):
        """
        Start the Garment Maker by asking the user to load data from Excel.
        Which then processes and formats orders and prints a summary report.
        :return: None
        """
        path = input("Enter the file path of the Excel file: ")
        self.processor.import_data(path)
        self.processor.format_data()
        self.processor.check_data_integrity()
        self.processor.create_orders()

        orders = self.processor.process_next_order()

        # For every order, call the appropriate garment maker method
        for o in orders:
            self.garment_maker_dict[o.garment.name](o)

        self.write_report()

    def shirt_men_maker(self, order):
        """
        Make an order of men's shirts based on given order.
        :param order: Order
        :return: None
        """
        shirt_m_order = order.factory.create_shirt_men(order.details)
        self.inventory.append(shirt_m_order)

    def shirt_women_maker(self, order):
        """
        Make an order of women's shirts based on given order.
        :param order: Order
        :return: None
        """
        shirt_w_order = order.factory.create_shirt_women(order.details)
        self.inventory.append(shirt_w_order)

    def socks_unisex_maker(self, order):
        """
        Make an order of socks based on given order.
        :param order: Order
        :return: None
        """
        socks_order = order.factory.create_socks_unisex(order.details)
        self.inventory.append(socks_order)

    def write_report(self):
        """
        Prints a summary of the order report.
        :return: None
        """
        for order in self.inventory:
            print(f"Order #{order[0].order_number} {order[0].brand}"
                  f" {order[0].garment}")
            for garment in order:
                print(garment)
            print()


class OrderProcessor:
    """
    Process orders from Excel sheet by formatting the data to work with
    Garment classes.
    """

    brand_dict = {
        "lululime": LululimeFactory(),
        "pineapplerepublic": PineappleRepublicFactory(),
        "nika": NikaFactory()
    }

    def __init__(self):
        """
        Initialises Order Processor object by loading dataframe and setting
        basic pandas options.
        """
        pd.set_option("display.max_rows", 200)
        pd.set_option('display.max_columns', 200)
        pd.set_option('display.width', 1000)
        self.valid_headings = {"date", "order_number", "brand", "garment",
                               "count", "style_name", "size", "colour",
                               "textile", "sport", "hidden_zipper_pockets",
                               "dry_cleaning", "indoor_or_outdoor",
                               "requires_ironing", "buttons", "articulated",
                               "length", "silver", "stripe"}
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
        self.df = self.df.where((pd.notnull(self.df)), "n")
        self.df = self.df.to_dict("records")

    def create_orders(self):
        """
        Based on the data frame, create orders and store in self.order_list.
        :return: None
        """
        for details in self.df:
            brand = details.get('brand').lower()
            g_type = details.get('garment').lower()
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

    def check_data_integrity(self):
        """
        Check if column headings in Excel file are corrupted.
        Select the first dict (representing Order details) in self.df and
        compare its keys with the list of valid headings.
        :return: None
        """
        if not self.df[0].keys() >= self.valid_headings:
            raise CorruptedFileError


class Order:
    """
    Represent an individual garment order.
    """

    def __init__(self, details, factory, garment):
        """
        Initialises an Order
        :param details: dict
        :param factory: Factory
        :param garment: GarmentType
        """
        self.details = details
        self.factory = factory
        self.garment = garment

    def __str__(self) -> str:
        """
        Formatted string for Order object
        :return: str
        """
        return f"Details: {self.details}\n" \
               f"Factory: {self.factory}\n" \
               f"Garment: {self.garment.name}\n"


def main():
    # COMP_3522_A4_orders.xlsx for full order
    # orders.xlsx for test order
    file_imported = False
    while not file_imported:
        try:
            gm = GarmentMaker()
            gm.start()
        except Exception as e:
            print(e)
        else:
            file_imported = True


if __name__ == "__main__":
    main()
