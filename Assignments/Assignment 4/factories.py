"""
Factories in Abtract Factory Pattern.
"""

from abc import ABC, abstractmethod
import garments


class BrandFactory(ABC):

    @abstractmethod
    def create_shirt_men(self, order) -> garments.ShirtMen:
        pass

    @abstractmethod
    def create_shirt_women(self, order) -> garments.ShirtWomen:
        pass

    @abstractmethod
    def create_socks_unisex(self, order) -> garments.SockPairUnisex:
        pass


class LululimeFactory(BrandFactory):
    """
    Creates a family of Lululime products.
    """

    def create_shirt_men(self, details) -> garments.ShirtMen:
        """
        Create a Lululime Men's Shirt.
        :return: ShirtMen
        """
        temp = []
        for _ in range(details["count"]):
            temp.append(garments.ShirtMenLululime(**details))
        return temp

    def create_shirt_women(self, details) -> garments.ShirtWomen:
        """
        Create a Lululime Women's Shirt.
        :return: ShirtWomen
        """
        temp = []
        for _ in range(details["count"]):
            temp.append(garments.ShirtWomenLululime(**details))
        return temp

    def create_socks_unisex(self, details) -> garments.SockPairUnisex:
        """
        Create a pair of Lululime unisex socks.
        :return: SockPairUnisex
        """
        temp = []
        for _ in range(details["count"]):
            temp.append(garments.SockPairUnisexLululime(**details))
        return temp


class PineappleRepublicFactory(BrandFactory):
    """
    Creates a family of Pineapple Republic products.
    """

    def create_shirt_men(self, details) -> garments.ShirtMen:
        """
        Create a Pineapple Republic Men's Shirt.
        :return: ShirtMen
        """
        temp = []
        for _ in range(details["count"]):
            temp.append(garments.ShirtMenPineappleRepublic(**details))
        return temp

    def create_shirt_women(self, details) -> garments.ShirtWomen:
        """
        Create a Pineapple Republic Women's Shirt.
        :return: ShirtWomen
        """
        temp = []
        for _ in range(details["count"]):
            temp.append(garments.ShirtWomenPineappleRepublic(**details))
        return temp

    def create_socks_unisex(self, details) -> garments.SockPairUnisex:
        """
        Create a pair of Pineapple Republic unisex socks.
        :return: SockPairUnisex
        """
        temp = []
        for _ in range(details["count"]):
            temp.append(garments.SockPairUnisexPineappleRepublic(**details))
        return temp


class NikaFactory(BrandFactory):
    """
    Creates a family of Pineapple Republic products.
    """

    def create_shirt_men(self, details) -> garments.ShirtMen:
        """
        Create a Nika Men's Shirt.
        :return: ShirtMen
        """
        temp = []
        for _ in range(details["count"]):
            temp.append(garments.ShirtMenNika(**details))
        return temp

    def create_shirt_women(self, details) -> garments.ShirtWomen:
        """
        Create a Nika Women's Shirt.
        :return: ShirtWomen
        """
        temp = []
        for _ in range(details["count"]):
            temp.append(garments.ShirtWomenNika(**details))
        return temp

    def create_socks_unisex(self, details) -> garments.SockPairUnisex:
        """
        Create a pair of Nika unisex socks.
        :return: SockPairUnisex
        """
        temp = []
        for _ in range(details["count"]):
            temp.append(garments.SockPairUnisexNika(**details))
        return temp