"""
Structure of abstract factory pattern that decouples GarmentMaker from
concrete products.
"""

from enum import Enum
from abc import ABC, abstractmethod


def convert(self, a):
    return int(a)

class Size(Enum):
    """
    Valid sizes for all garments.
    """
    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"
    XXL = "XXL"


class SportType(Enum):
    """
    Valid sport types for Lululime garments.
    """
    YOGA = "YOGA"
    RUNNING = "RUNNING"


class SockLength(Enum):
    """
    Valid sock lengths.
    """
    ANKLE = "ANKLE"
    CALF = "CALF"
    KNEE = "KNEE"


class Garment(ABC):
    """
    Abstract Garment class.
    """

    def __init__(self, style_name="", colour="", textile="", **kwargs):
        """
        Initialises abstract garment.
        :param kwargs: dictionary of garment values
        """
        # self.__dict__.update(kwargs)
        self._style_name = style_name
        self._colour = colour
        self._textile = textile

    @abstractmethod
    def __str__(self):
        """
        Formatted string for Garment.
        :return: str
        """
        return f"Style: {self._style_name.upper()}\n" \
               f"Colour: {self._colour.upper()}\n" \
               f"Textile: {self._textile.upper()}\n"
        # output = ""
        # for k, v in self.__dict__.items():
        #     output += f"{k.title()}: {v.upper()}\n"
        # return output


class ShirtMen(Garment):
    """
    Abstract men's shirt class. Member in product family.
    """

    def __init__(self, size=None, **kwargs):
        super().__init__(**kwargs)
        self._accepted_sizes = ["S", "M", "L", "XL", "XXL"]
        size = size.upper()
        if size in self._accepted_sizes:
            self._size = Size(size)
        else:
            raise ValueError(f"The size {size} is not accepted for men's "
                             f"shirts.")

    @abstractmethod
    def __str__(self):
        """
        Formatted string for Men's Shirt
        :return: str
        """
        return f"{super().__str__()}" \
               f"Size: {self._size.name}\n"


class ShirtWomen(Garment):
    """
    Abstract women's shirt class. Member in product family.
    """

    def __init__(self, size=None, **kwargs):
        super().__init__(**kwargs)
        size = size.upper()
        try:
            self._size = Size(size)
        except ValueError:
            print(f"The size {size} is not accepted for women's shirts.")

    @abstractmethod
    def __str__(self):
        """
        Formatted string for Women's Shirt
        :return: str
        """
        return f"{super().__str__()}" \
               f"Size: {self._size.name}\n"


class SockPairUnisex(Garment):
    """
    Abstract unisex socks class. Member in product family.
    """

    def __init__(self, size=None, **kwargs):
        super().__init__(**kwargs)
        self._accepted_sizes = ["S", "M", "L"]
        size = size.upper()
        if size in self._accepted_sizes:
            self._size = Size(size)
        else:
            raise ValueError(f"The size {size} is not valid for Socks.")

    @abstractmethod
    def __str__(self):
        """
        Formatted string for Women's Shirt
        :return: str
        """
        return f"{super().__str__()}" \
               f"Size: {self._size.name}\n"


class ShirtMenLululime(ShirtMen):
    """
    Lululime Men's Shirt.  Concrete product in abstract factory pattern.
    """

    def __init__(self, sport, hidden_zipper_pockets, **kwargs):
        super().__init__(**kwargs)
        sport = sport.upper()
        self._sport = SportType(sport)
        self._hidden_zipper_pockets = int(hidden_zipper_pockets)

    def __str__(self):
        """
        Formatted string for ShirtMenLuluLime
        :return: str
        """
        return f"=== Lululime Men's Shirts ===\n" \
               f"{super().__str__()}" \
               f"Sport Type: {self._sport.name}\n" \
               f"Number of Zippered Pockets: {self._hidden_zipper_pockets}\n"


class ShirtMenPineappleRepublic(ShirtMen):
    """
    Pineapple Republic Men's Shirt.  Concrete product in abstract factory
    pattern.
    """

    def __init__(self, requires_ironing, buttons, **kwargs):
        super().__init__(**kwargs)
        requires_ironing = requires_ironing.lower()
        self._buttons = int(buttons)
        if requires_ironing == "y":
            self._requires_ironing = True
        elif requires_ironing == "n":
            self._requires_ironing = False
        else:
            raise ValueError(f"The requires_ironing field must either be Y"
                             f" or N. You provided '{requires_ironing}'.")

    def __str__(self):
        """
        Formatted string for ShirtMenPineappleRepublic
        :return: str
        """
        return f"=== Pineapple Republic Men's Shirts ===\n" \
               f"{super().__str__()}" \
               f"Requires Ironing: {self._requires_ironing}\n" \
               f"Number of Buttons: {self._buttons}\n"


class ShirtMenNika(ShirtMen):
    """
    Nika Men's Shirt.  Concrete product in abstract factory
    pattern.
    """

    def __init__(self, indoor_or_outdoor, **kwargs):
        super().__init__(**kwargs)
        indoor_or_outdoor = indoor_or_outdoor.upper()
        if indoor_or_outdoor == "INDOOR" or indoor_or_outdoor == "OUTDOOR":
            self._indoor_or_outdoor = indoor_or_outdoor
        else:
            raise ValueError(f"The indoor_or_outdoor field must either be"
                             f"'INDOOR' or 'OUTDOOR'.  You provided "
                             f"{indoor_or_outdoor}.")

    def __str__(self):
        """
        Formatted string for ShirtMenNika
        :return: str
        """
        return f"=== Nika Men's Shirts ===\n" \
               f"{super().__str__()}" \
               f"Indoor: {self._indoor_or_outdoor}\n"


class ShirtWomenLululime(ShirtWomen):
    """
    Lululime Women's Shirt.  Concrete product in abstract factory pattern.
    """

    def __init__(self, sport, hidden_zipper_pockets, **kwargs):
        super().__init__(**kwargs)
        sport = sport.upper()
        self._sport = SportType(sport)
        self._hidden_zipper_pockets = int(hidden_zipper_pockets)

    def __str__(self):
        """
        Formatted string for ShirtWomenLuluLime
        :return: str
        """
        return f"=== Lululime Women's Shirts ===\n" \
               f"{super().__str__()}" \
               f"Sport Type: {self._sport.name}\n" \
               f"Number of Zippered Pockets: {self._hidden_zipper_pockets}\n"


class ShirtWomenPineappleRepublic(ShirtWomen):
    """
    Pineapple Republic Women's Shirt.  Concrete product in abstract factory
    pattern.
    """

    def __init__(self, requires_ironing, buttons, **kwargs):
        super().__init__(**kwargs)
        self._buttons = int(buttons)
        requires_ironing = requires_ironing.lower()
        if requires_ironing == "y":
            self._requires_ironing = True
        elif requires_ironing == "n":
            self._requires_ironing = False
        else:
            raise ValueError(f"The requires_ironing field must either be Y"
                             f" or N. You provided '{requires_ironing}'.")

    def __str__(self):
        """
        Formatted string for ShirtWomenPineappleRepublic
        :return: str
        """
        return f"=== Pineapple Republic Women's Shirts ===\n" \
               f"{super().__str__()}" \
               f"Requires Ironing: {self._requires_ironing}\n" \
               f"Number of Buttons: {self._buttons}\n"


class ShirtWomenNika(ShirtWomen):
    """
    Nika Women's Shirt.  Concrete product in abstract factory
    pattern.
    """

    def __init__(self, indoor_or_outdoor, **kwargs):
        super().__init__(**kwargs)
        indoor_or_outdoor = indoor_or_outdoor.upper()
        if indoor_or_outdoor == "INDOOR" or indoor_or_outdoor == "OUTDOOR":
            self._indoor_or_outdoor = indoor_or_outdoor
        else:
            raise ValueError(f"The indoor_or_outdoor field must either be"
                             f"'INDOOR' or 'OUTDOOR'.  You provided "
                             f"{indoor_or_outdoor}.")

    def __str__(self):
        """
        Formatted string for ShirtWomenNika
        :return: str
        """
        return f"=== Nika Men's Shirts ===\n" \
               f"{super().__str__()}" \
               f"Indoor: {self._indoor_or_outdoor}\n"


class SockPairUnisexLululime(SockPairUnisex):
    """
    Lululime unisex socks. Concrete product in abstract factory pattern.
    """

    def __init__(self, silver, **kwargs):
        super().__init__(**kwargs)
        silver = silver.lower()
        if silver == "y":
            self._silver = True
        elif silver == "n":
            self._silver = False
        else:
            raise ValueError(f"The silver field must either be Y"
                             f" or N. You provided '{silver}'.")

    def __str__(self):
        return f"=== Lululime Socks ===\n" \
               f"{super().__str__()}" \
               f"Has Silver: {self._silver}\n"


class SockPairUnisexPineappleRepublic(SockPairUnisex):
    """
    Lululime unisex socks. Concrete product in abstract factory pattern.
    """

    def __init__(self, dry_cleaning, **kwargs):
        super().__init__(**kwargs)
        dry_cleaning = dry_cleaning.lower()
        if dry_cleaning == "y":
            self._dry_cleaning = True
        elif dry_cleaning == "n":
            self._dry_cleaning = False
        else:
            raise ValueError(f"The dry_cleaning field must either be Y"
                             f" or N. You provided '{dry_cleaning}'.")

    def __str__(self):
        return f"=== Pineapple Republic Socks ===\n" \
               f"{super().__str__()}" \
               f"Requires Drycleaning: {self._dry_cleaning}\n"


class SockPairUnisexNika(SockPairUnisex):
    """
    Lululime unisex socks. Concrete product in abstract factory pattern.
    """

    def __init__(self, articulated, length, **kwargs):
        super().__init__(**kwargs)
        articulated = articulated.lower()
        if articulated == "y":
            self._articulated = True
        elif articulated == "n":
            self._articulated = False
        else:
            raise ValueError(f"The articulated field must either be Y"
                             f" or N. You provided '{articulated}'.")
        self._length = SockLength(length.upper())

    def __str__(self):
        return f"=== Nika Socks ===\n" \
               f"{super().__str__()}" \
               f"Articulated: {self._articulated}\n" \
               f"Sock Length: {self._length.name}\n"


def main():
    try:
        d = {'date': 'Friday November 16 2019', 'order_number': 1,
             'count': 300, 'style_name': 'Bowen', 'size': 'M',
             'colour': 'Grey', 'textile': 'Merino wool',
             'sport': 'Yoga', 'hidden_zipper_pockets': 1.0,
             'dry_cleaning': 'n', 'indoor_or_outdoor': 'n',
             'requires_ironing': 'n', 'buttons': 'n', 'articulated': 'n',
             'length': 'n', 'silver': 'n', 'stripe': 'n'}
        shirt_men = ShirtMenLululime(**d)
        print(shirt_men)
    except Exception as e:
        print(e)


# def main():
#     # print('s'.upper() in SizeW.__members__)
#     # try:
#     #     n_socks = SockPairUnisexPineappleRepublic("style b", "Grey", "Merino",
#     #                                               "M", True)
#     #     print(n_socks)
#     # except Exception as e:
#     #     print(f"Invalid input: {e}")
#     pass


if __name__ == "__main__":
    main()
