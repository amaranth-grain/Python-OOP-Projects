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

    def create_shirt_men(self, order) -> garments.ShirtMen:
        """
        Create a Lululime Men's Shirt.
        :return: ShirtMen
        """
        print("I'm a Lululime shirt men")
        return garments.ShirtMenLululime(**order)

    def create_shirt_women(self, order) -> garments.ShirtWomen:
        """
        Create a Lululime Women's Shirt.
        :return: ShirtWomen
        """
        print("I'm a Lululime shirt women")
        return garments.ShirtWomenLululime(**order)

    def create_socks_unisex(self, order) -> garments.SockPairUnisex:
        """
        Create a pair of Lululime unisex socks.
        :return: SockPairUnisex
        """
        print("I'm a Lululime sock pair")
        return garments.SockPairUnisexLululime(**order)


class PineappleRepublicFactory(BrandFactory):
    """
    Creates a family of Pineapple Republic products.
    """

    def create_shirt_men(self, order) -> garments.ShirtMen:
        """
        Create a Pineapple Republic Men's Shirt.
        :return: ShirtMen
        """
        print("I'm a PR shirt men")
        return garments.ShirtMenPineappleRepublic(**order)

    def create_shirt_women(self, order) -> garments.ShirtWomen:
        """
        Create a Pineapple Republic Women's Shirt.
        :return: ShirtWomen
        """
        print("I'm a PR shirt women")
        return garments.ShirtWomenPineappleRepublic(**order)

    def create_socks_unisex(self, order) -> garments.SockPairUnisex:
        """
        Create a pair of Pineapple Republic unisex socks.
        :return: SockPairUnisex
        """
        print("I'm a PR sock pair")
        return garments.SockPairUnisexPineappleRepublic(**order)


class NikaFactory(BrandFactory):
    """
    Creates a family of Pineapple Republic products.
    """

    def create_shirt_men(self, order) -> garments.ShirtMen:
        """
        Create a Nika Men's Shirt.
        :return: ShirtMen
        """
        print("I'm a Nika shirt men")
        return garments.ShirtMenNika(**order)

    def create_shirt_women(self, order) -> garments.ShirtWomen:
        """
        Create a Nika Women's Shirt.
        :return: ShirtWomen
        """
        print("I'm a Nika shirt women")
        return garments.ShirtWomenNika(**order)

    def create_socks_unisex(self, order) -> garments.SockPairUnisex:
        """
        Create a pair of Nika unisex socks.
        :return: SockPairUnisex
        """
        print("I'm a Nika sock pair")
        return garments.SockPairUnisexNika(**order)