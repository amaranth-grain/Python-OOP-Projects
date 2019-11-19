"""
Client side of abstract factory pattern.
"""
import pandas as pd


class FileExtensionError(Exception):
    def __init__(self):
        super().__init__("\nIncorrect file extension. Only .xlsx accepted.\n")


class Order:
    """
    Represent the garment Order, which is read in from Excel row.
    """
    def __init__(self, brand, garment, details):
        self._brand = brand.capitalize()
        self._garment = garment.capitalize()
        self._details = details

    def __str__(self):
        output = ""
        for detail in [f"{k.capitalize()}: {v.capitalize()}"
                       for k, v in self._details.items()]:
            output += f"{detail}\n"
        return f"Brand: {self._brand}\n" \
               f"Garment: {self._garment}\n" \
               f"{output}\n"


class OrderProcessor:
    def __init__(self):
        self._data_frame = None

    def open_excel_file(self, path):
        if not path.endswith(".xlsx"):
            raise FileExtensionError
        else:
            self._data_frame = pd.read_excel(path)
            # for index, row in df.iterrows():
            #     print(f"Index: {index}\nRow: {row}\n******************")

    def process_next_order(self):
        # TODO debug the generator
        yield from [row for index, row in self._data_frame.iterrows()]


class GarmentMaker:
    def __init__(self):
        self._shirts_men = []
        self._shirts_women = []
        self._socks_unisex = []
        self._processor = OrderProcessor()

    def start(self):
        """
        Starts the garment making program.
        :return: None
        """
        print("=== Christy's Garment-Making Factory ===\n")
        path = input("Enter excel file path: ")
        self._processor.open_excel_file(path)
        test = self._processor.process_next_order()


def main():
    file_opened = False
    while not file_opened:
        try:
            maker = GarmentMaker()
            maker.start()
        except ValueError as e:
            print(f"\n{e}\n")
        else:
            file_opened = True


if __name__ == "__main__":
    main()












# df = pd.read_excel('orders.xlsx')

# for index, row in df.iterrows():
#     print(f"Index: {index}\nRow: {row}\n******************")

# for index, row in df.iterrows():
#     if row["Garment"] == "ShirtMen":
#         print(f"Row: {row}\n******************")

# print("Column headings:")
# print(df.columns)
# print(df['Date'])
# print([item for item in df[0:1]])
# print(df[0:2]['Brand'])

# print(df.loc[2])
# print("*" * 100)
# print(df.loc[2]["Brand"])

# for item in df.items():
#     print(item)