"""
Structure of abstract factory pattern that decouples GarmentMaker from
concrete products.
"""

from enum import Enum
from abc import ABC, abstractmethod


class SizeW(Enum):
    """
    Valid sizes for Women's Garments.
    """
    XS = "xs"
    S = "s"
    M = "m"
    L = "l"
    XL = "xl"
    XXL = "xxl"


class SizeM(Enum):
    """
    Valid sizes for Men's Garments.
    """
    S = "s"
    M = "m"
    L = "l"
    XL = "xl"
    XXL = "xxl"


class SizeSock(Enum):
    """
    Valid sizes for unisex Socks.
    """
    S = "s"
    M = "m"
    L = "l"


class LululimeShirtSportType(Enum):
    """
    Valid sport types for Lululime shirts.
    """
    YOGA = "yoga"
    RUNNING = "running"


class SockLength(Enum):
    """
    Valid sock lengths.
    """
    ANKLE = "ankle"
    CALF = "calf"
    KNEE = "knee"


class ShirtMen(ABC):
    """
    Abstract men's shirt class. Member in product family.
    """
    def __init__(self, style, colour, textile, size):
        self._style = str(style)
        self._colour = str(colour)
        self._textile = str(textile)
        size = size.upper()
        if size in SizeM.__members__:
            self._size = size
        else:
            raise ValueError(f"The size {size} is not valid for Men's "
                             f"Shirts.")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        size = size.upper()
        if size in SizeM.__members__:
            self._size = size
        else:
            raise ValueError(f"The size {size} is not valid for Men's Shirts.")

    @abstractmethod
    def __str__(self):
        return f"Style: {self._style}\n" \
               f"Size: {self._size}\n" \
               f"Colour: {self._colour}\n" \
               f"Textile: {self._textile}\n"


class ShirtWomen(ABC):
    """
    Abstract women's shirt class. Member in product family.
    """

    def __init__(self, style, colour, textile, size):
        self._style = style
        self._colour = colour
        self._textile = textile
        size = size.upper()
        if size in SizeW.__members__:
            self._size = size
        else:
            raise ValueError(f"The size {size} is not valid for Women's "
                             f"Shirts.")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        size = size.upper()
        if size in SizeW.__members__:
            self._size = size
        else:
            raise ValueError(f"The size {size} is not valid for Women's "
                             f"Shirts.")

    @abstractmethod
    def __str__(self):
        return f"Style: {self._style}\n" \
               f"Size: {self._size}\n" \
               f"Colour: {self._colour}\n" \
               f"Textile: {self._textile}\n"


class SockPairUnisex(ABC):
    """
    Abstract unisex socks class. Member in product family.
    """

    def __init__(self, style, colour, textile, size):
        self._style = style
        self._colour = colour
        self._textile = textile
        size = size.upper()
        if size in SizeSock.__members__:
            self._size = size
        else:
            raise ValueError(f"The size {size} is not valid for Socks.")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        size = size.upper()
        if size in SizeSock.__members__:
            self._size = size
        else:
            raise ValueError(f"The size {size} is not valid for Socks.")

    @abstractmethod
    def __str__(self):
        return f"Style: {self._style}\n" \
               f"Size: {self._size}\n" \
               f"Colour: {self._colour}\n" \
               f"Textile: {self._textile}\n"


class ShirtMenLuluLime(ShirtMen):
    """
    Lululime Men's Shirt.  Concrete product in abstract factory pattern.
    """
    def __init__(self, style, colour, textile, size, sport_type,
                 num_zip_pockets):
        super().__init__(style, colour, textile, size)
        sport_type = sport_type.upper()
        if sport_type in LululimeShirtSportType.__members__:
            self._sport_type = sport_type
        else:
            raise ValueError(f"The type {sport_type} is not valid for "
                             f"Lululime shirts.")
        if isinstance(num_zip_pockets, int):
            self._num_zip_pockets = num_zip_pockets
        else:
            raise ValueError(f"Only integer values accepted for the number "
                             f"of zippered pockets.")

    def __str__(self):
        return f"=== Lululime Men's Shirts ===\n" \
               f"{super().__str__()}"


class ShirtMenPineappleRepublic(ShirtMen):
    """
    Pineapple Republic Men's Shirt.  Concrete product in abstract factory
    pattern.
    """
    def __init__(self, style, colour, textile, size, needs_ironing,
                 num_buttons):
        super().__init__(style, colour, textile, size)
        if isinstance(needs_ironing, bool):
            self._needs_ironing = needs_ironing
        else:
            raise TypeError("Only boolean values accepted for whether the "
                            "shirt requires ironing or not.")
        if isinstance(num_buttons, int):
            self._num_buttons = num_buttons
        else:
            raise TypeError("Only integer values accepted for the number of "
                            "buttons on the shirt.")

    def __str__(self):
        return f"=== Pineapple Republic Men's Shirts ===\n" \
               f"{super().__str__()}"


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
            raise TypeError("Only boolean values accepted for whether the "
                            "shirt is designed for indoors or not.")

    def __str__(self):
        return f"=== Nika Men's Shirts ===\n" \
               f"{super().__str__()}"


class ShirtWomenLululime(ShirtWomen):
    """
    Lululime Women's Shirt. Concrete product in abstract factory pattern.
    """
    def __init__(self, style, colour, textile, size, sport_type,
                 num_zip_pockets):
        super().__init__(style, colour, textile, size)
        sport_type = sport_type.upper()
        if sport_type in LululimeShirtSportType.__members__:
            self._sport_type = sport_type
        else:
            raise ValueError(f"The type {sport_type} is not valid for "
                             f"Lululime shirts.")
        if isinstance(num_zip_pockets, int):
            self._num_zip_pockets = num_zip_pockets
        else:
            raise ValueError(f"Only integer values accepted for the number "
                             f"of zippered pockets.")

    def __str__(self):
        return f"=== Lululime Women's Shirts ===\n" \
               f"{super().__str__()}"


class ShirtWomenPineappleRepublic(ShirtWomen):
    """
        Pineapple Republic Women's Shirt.  Concrete product in abstract factory
        pattern.
        """
    def __init__(self, style, colour, textile, size, needs_ironing,
                 num_buttons):
        super().__init__(style, colour, textile, size)
        if isinstance(needs_ironing, bool):
            self._needs_ironing = needs_ironing
        else:
            raise TypeError("Only boolean values accepted for whether the "
                            "shirt requires ironing or not.")
        if isinstance(num_buttons, int):
            self._num_buttons = num_buttons
        else:
            raise TypeError("Only integer values accepted for the number of "
                            "buttons.")

    def __str__(self):
        return f"=== Pineapple Republic Women's Shirts ===\n" \
               f"{super().__str__()}"


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
            raise TypeError("Only boolean values accepted for whether the "
                            "shirts are designed for indoors or not.")

    def __str__(self):
        return f"=== Nika Women's Shirts ===\n" \
               f"{super().__str__()}"


class SockPairUnisexLululime(SockPairUnisex):
    """
    Lululime unisex socks. Concrete product in abstract factory pattern.
    """
    def __init__(self, style, colour, textile, size, has_silver):
        super().__init__(style, colour, textile, size)
        if isinstance(has_silver, bool):
            self._has_silver = has_silver
        else:
            raise TypeError("Only boolean values accepted for whether socks "
                            "have silver to control odour.")

    def __str__(self):
        return f"=== Lululime Socks ===\n" \
               f"{super().__str__()}"


class SockPairUnisexPineappleRepublic(SockPairUnisex):
    """
    Lululime unisex socks. Concrete product in abstract factory pattern.
    """
    def __init__(self, style, colour, textile, size, needs_drycleaning):
        super().__init__(style, colour, textile, size)
        if isinstance(needs_drycleaning, bool):
            self._needs_drycleaning = needs_drycleaning
        else:
            raise TypeError("Only boolean values accepted for whether socks "
                            "require drycleaning or not.")

    def __str__(self):
        return f"=== Pineapple Republic Socks ===\n" \
               f"{super().__str__()}"


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
            raise TypeError("Only boolean values accepted for whether socks "
                            "are articulated or not.")
        sock_length = sock_length.upper()
        if sock_length in SockLength.__members__:
            self._sock_length = sock_length
        else:
            raise ValueError(f"The sock length {sock_length} is invalid.")

    def __str__(self):
        return f"=== Nika Socks ===\n" \
               f"{super().__str__()}"


def main():
    # print('s'.upper() in SizeW.__members__)
    try:
        l_socks = SockPairUnisexLululime(123, "blue", "Cotton", "m",
                                         True)
        l_socks.size = "m"
        print(l_socks)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
