"""
Structure of abstract factory pattern that decouples GarmentMaker from
concrete products.
"""

from enum import Enum
from abc import ABC, abstractmethod


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
    Abstract garment class.
    """
    def __init__(self, style, colour, textile):
        self._style = style
        self._colour = colour
        self._textile = textile

    @abstractmethod
    def __str__(self):
        """
        Formatted string for Garment.
        :return: str
        """
        return f"Style: {self._style}\n" \
               f"Colour: {self._colour}\n" \
               f"Textile: {self._textile}\n"


class ShirtMen(Garment):
    """
    Abstract men's shirt class. Member in product family.
    """
    def __init__(self, style, colour, textile, size):
        super().__init__(style, colour, textile)
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
    def __init__(self, style, colour, textile, size):
        super().__init__(style, colour, textile)
        size = size.lower()
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
    def __init__(self, style, colour, textile, size):
        super().__init__(style, colour, textile)
        self._accepted_sizes = ["S", "M", "L"]
        size = size.upper()
        if size in self._accepted_sizes:
            self._size = Size(size)
        else:
            raise ValueError(f"The size {size} is not valid for Socks.")

    @abstractmethod
    def __str__(self):
        """
        Formatted string for Unisex Socks.
        :return: str
        """
        return f"{super().__str__()}" \
               f"Size: {self._size.name}\n"


class ShirtMenLuluLime(ShirtMen):
    """
    Lululime Men's Shirt.  Concrete product in abstract factory pattern.
    """
    def __init__(self, style, colour, textile, size, sport_type,
                 num_zip_pockets):
        super().__init__(style, colour, textile, size)
        sport_type = sport_type.upper()
        self._sport_type = SportType(sport_type)
        self._num_zip_pockets = int(num_zip_pockets)

    def __str__(self):
        return f"=== Lululime Men's Shirts ===\n" \
               f"{super().__str__()}" \
               f"Sport Type: {self._sport_type.name}\n" \
               f"Number of zippered pockets: {self._num_zip_pockets}\n"


class ShirtMenPineappleRepublic(ShirtMen):
    """
    Pineapple Republic Men's Shirt.  Concrete product in abstract factory
    pattern.
    """
    def __init__(self, style, colour, textile, size, needs_ironing: bool,
                 num_buttons):
        super().__init__(style, colour, textile, size)
        if isinstance(needs_ironing, bool):
            self._needs_ironing = needs_ironing
        else:
            raise TypeError(f"The value '{needs_ironing}' is not a boolean "
                            f"value.")
        self._num_buttons = int(num_buttons)

    def __str__(self):
        return f"=== Pineapple Republic Men's Shirts ===\n" \
               f"{super().__str__()}" \
               f"Needs Ironing: {self._needs_ironing}\n" \
               f"Number of Buttons: {self._num_buttons}\n"


class ShirtMenNika(ShirtMen):
    """
    Nika Men's Shirt.  Concrete product in abstract factory
    pattern.
    """
    def __init__(self, style, colour, textile, size, is_indoor):
        super().__init__(style, colour, textile, size)
        if isinstance(is_indoor, bool):
            self._is_indoor = is_indoor
        else:
            raise TypeError(f"The value '{is_indoor}' is not a boolean "
                            f"value.")

    def __str__(self):
        return f"=== Nika Men's Shirts ===\n" \
               f"{super().__str__()}" \
               f"Indoor: {self._is_indoor}\n"


class ShirtWomenLuluLime(ShirtWomen):
    """
    Lululime Women's Shirt.  Concrete product in abstract factory pattern.
    """
    def __init__(self, style, colour, textile, size, sport_type,
                 num_zip_pockets):
        super().__init__(style, colour, textile, size)
        sport_type = sport_type.upper()
        self._sport_type = SportType(sport_type)
        self._num_zip_pockets = int(num_zip_pockets)

    def __str__(self):
        return f"=== Lululime Women's Shirts ===\n" \
               f"{super().__str__()}" \
               f"Sport Type: {self._sport_type.name}\n" \
               f"Number of zippered pockets: {self._num_zip_pockets}\n"


class ShirtWomenPineappleRepublic(ShirtWomen):
    """
    Pineapple Republic Women's Shirt.  Concrete product in abstract factory
    pattern.
    """
    def __init__(self, style, colour, textile, size, needs_ironing: bool,
                 num_buttons):
        super().__init__(style, colour, textile, size)
        if isinstance(needs_ironing, bool):
            self._needs_ironing = needs_ironing
        else:
            raise TypeError(f"The value '{needs_ironing}' is not a boolean "
                            f"value.")
        self._num_buttons = int(num_buttons)

    def __str__(self):
        return f"=== Pineapple Republic Women's Shirts ===\n" \
               f"{super().__str__()}" \
               f"Needs Ironing: {self._needs_ironing}\n" \
               f"Number of Buttons: {self._num_buttons}\n"


class ShirtWomenNika(ShirtWomen):
    """
    Nika Women's Shirt.  Concrete product in abstract factory
    pattern.
    """
    def __init__(self, style, colour, textile, size, is_indoor):
        super().__init__(style, colour, textile, size)
        if isinstance(is_indoor, bool):
            self._is_indoor = is_indoor
        else:
            raise TypeError(f"The value '{is_indoor}' is not a boolean "
                            f"value.")

    def __str__(self):
        return f"=== Nika Women's Shirts ===\n" \
               f"{super().__str__()}" \
               f"Indoor: {self._is_indoor}\n"


class SockPairUnisexLululime(SockPairUnisex):
    """
    Lululime unisex socks. Concrete product in abstract factory pattern.
    """
    def __init__(self, style, colour, textile, size, has_silver):
        super().__init__(style, colour, textile, size)
        if isinstance(has_silver, bool):
            self._has_silver = has_silver
        else:
            raise TypeError(f"The value '{has_silver}' is not a boolean "
                            f"value.")

    def __str__(self):
        return f"=== Lululime Socks ===\n" \
               f"{super().__str__()}" \
               f"Has Silver: {self._has_silver}\n"


class SockPairUnisexPineappleRepublic(SockPairUnisex):
    """
    Lululime unisex socks. Concrete product in abstract factory pattern.
    """
    def __init__(self, style, colour, textile, size, needs_drycleaning):
        super().__init__(style, colour, textile, size)
        if isinstance(needs_drycleaning, bool):
            self._needs_drycleaning = needs_drycleaning
        else:
            raise TypeError(f"The value '{needs_drycleaning}' is not a "
                            f"boolean value.")

    def __str__(self):
        return f"=== Pineapple Republic Socks ===\n" \
               f"{super().__str__()}" \
               f"Requires Drycleaning: {self._needs_drycleaning}\n"


class SockPairUnisexNika(SockPairUnisex):
    """
    Lululime unisex socks. Concrete product in abstract factory pattern.
    """
    def __init__(self, style, colour, textile, size, is_articulated,
                 sock_length):
        super().__init__(style, colour, textile, size)
        if isinstance(is_articulated, bool):
            self._is_articulated = is_articulated
        else:
            raise TypeError(f"The value '{is_articulated}' is not a boolean "
                            f"value.")
        self._sock_length = SockLength(sock_length.upper())

    def __str__(self):
        return f"=== Nika Socks ===\n" \
               f"{super().__str__()}" \
               f"Articulated: {self._is_articulated}\n" \
               f"Sock Length: {self._sock_length.name}\n"


def main():
    # print('s'.upper() in SizeW.__members__)
    try:
        n_socks = SockPairUnisexPineappleRepublic("style b", "Grey", "Merino",
                                                  "M", True)
        print(n_socks)
    except Exception as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
