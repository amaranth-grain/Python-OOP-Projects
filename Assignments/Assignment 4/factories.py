from abc import ABC, abstractmethod
import garments


class BrandFactory(ABC):

    @abstractmethod
    def create_shirt_men(self) -> garments.ShirtMen:
        pass

    @abstractmethod
    def create_shirt_women(self) -> garments.ShirtWomen:
        pass

    @abstractmethod
    def create_socks_unisex(self) -> garments.SockPairUnisex:
        pass


class LululimeFactory(BrandFactory):
    """
    Creates a family of Lululime products.
    """

    def create_shirt_men(self) -> garments.ShirtMen:
        """
        Create a Lululime Men's Shirt.
        :return: ShirtMen
        """
        print("I'm a Lululime shirt men")
        return garments.ShirtMenLululime

    def create_shirt_women(self) -> garments.ShirtWomen:
        """
        Create a Lululime Women's Shirt.
        :return: ShirtWomen
        """
        print("I'm a Lululime shirt women")
        return garments.ShirtWomenLululime

    def create_socks_unisex(self) -> garments.SockPairUnisex:
        """
        Create a pair of Lululime unisex socks.
        :return: SockPairUnisex
        """
        print("I'm a Lululime sock pair")
        return garments.SockPairUnisexLululime


class PineappleRepublicFactory(BrandFactory):
    """
    Creates a family of Pineapple Republic products.
    """

    def create_shirt_men(self) -> garments.ShirtMen:
        """
        Create a Pineapple Republic Men's Shirt.
        :return: ShirtMen
        """
        print("I'm a PR shirt men")
        return garments.ShirtMenPineappleRepublic

    def create_shirt_women(self) -> garments.ShirtWomen:
        """
        Create a Pineapple Republic Women's Shirt.
        :return: ShirtWomen
        """
        print("I'm a PR shirt women")
        return garments.ShirtWomenPineappleRepublic

    def create_socks_unisex(self) -> garments.SockPairUnisex:
        """
        Create a pair of Pineapple Republic unisex socks.
        :return: SockPairUnisex
        """
        print("I'm a PR sock pair")
        return garments.SockPairUnisexPineappleRepublic


class NikaFactory(BrandFactory):
    """
    Creates a family of Pineapple Republic products.
    """

    def create_shirt_men(self) -> garments.ShirtMen:
        """
        Create a Nika Men's Shirt.
        :return: ShirtMen
        """
        print("I'm a Nika shirt men")
        return garments.ShirtMenNika

    def create_shirt_women(self) -> garments.ShirtWomen:
        """
        Create a Nika Women's Shirt.
        :return: ShirtWomen
        """
        print("I'm a Nika shirt women")
        return garments.ShirtWomenNika

    def create_socks_unisex(self) -> garments.SockPairUnisex:
        """
        Create a pair of Nika unisex socks.
        :return: SockPairUnisex
        """
        print("I'm a Nika sock pair")
        return garments.SockPairUnisexNika