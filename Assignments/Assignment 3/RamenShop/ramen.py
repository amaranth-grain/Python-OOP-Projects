"""
Decorator pattern for Ramen.
"""
from abc import abstractmethod, ABC
from menu import Menu


class RamenInterface(ABC):

    """
    Interface that decorators and concrete ramen must adhere to.
    Basis of decorator pattern.
    """

    @abstractmethod
    def get_ingredient_list(self):
        pass

    @abstractmethod
    def update_ingredient_list(self, ingredient):
        pass

    @abstractmethod
    def get_total_price(self):
        pass

    @abstractmethod
    def update_total_price(self, ingredient):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ConcreteRamen(RamenInterface):

    def __init__(self):
        """
        Initialises basic Ramen object.
        """
        self.ingredient_list = []
        self.total_price = 0

    def get_ingredient_list(self):
        """
        Get ingredients in customised ramen.
        :return: String
        """
        return ", ".join([i.name for i in self.ingredient_list][::-1])

    def update_ingredient_list(self, ingredient):
        """
        Update bowl of ramen with new ingredient.
        :param ingredient: Ingredient
        :return: None
        """
        self.ingredient_list.append(ingredient)

    def get_total_price(self):
        """
        Get total price of Ramen with customisation.
        :return: float
        """
        return self.total_price

    def update_total_price(self, ingredient):
        """
        Update Ramen with new total price.
        :param ingredient: float
        :return: None
        """
        self.total_price += ingredient.price

    def cook(self):
        """
        Assemble the concrete Ramen and its decorators together.
        :return: None
        """
        ing = Menu.get_broth_from_dec("Marutama Ramen")
        self.update_ingredient_list(ing)
        self.update_total_price(ing)

    def __str__(self):
        """
        String representation of Ramen
        :return: String
        """
        price = '${:,.2f}'.format(self.get_total_price())
        return f"\nIngredients: {self.get_ingredient_list()}\n" \
               f"Total price: {price}\n"


class BaseRamenDecorator(RamenInterface):

    def __init__(self, ramen):
        """
        Initialises basic Ramen object.
        """
        self.ramen = ramen

    def get_ingredient_list(self):
        """
        Get ingredients in customised ramen.
        :return: String
        """
        return self.ramen.get_ingredient_list()

    def update_ingredient_list(self, ingredient):
        """
        Update bowl of ramen with new ingredient.
        :param ingredient: Ingredient
        :return: None
        """
        self.ramen.update_ingredient_list(ingredient)

    def get_total_price(self):
        """
        Get total price of Ramen with customisation.
        :return: float
        """
        return self.ramen.get_total_price()

    def update_total_price(self, ingredient):
        """
        Update Ramen with new total price.
        :param ingredient: float
        :return: None
        """
        self.ramen.update_total_price(ingredient)

    def cook(self):
        """
        Assemble the concrete Ramen and its decorators together.
        :return: None
        """
        self.ramen.cook()

    def __str__(self):
        """
        String representation of Ramen
        :return: String
        """
        price = '${:,.2f}'.format(self.get_total_price())
        return f"\nIngredients: {self.get_ingredient_list()}\n" \
               f"Total price: {price}\n"


class BrothDecorator(BaseRamenDecorator):
    """
    Represent broth customisations for ramen.
    """

    def __init__(self, ramen, decorator_string):
        """
        Initialise BrothDecorator object.
        :param ramen: object with RamenInterface implemented
        :param decorator: String
        """
        super().__init__(ramen)
        self.dec = decorator_string

    def cook(self):
        """
        Assemble the concrete Ramen and its decorators together.
        :return: None
        """
        ing = Menu.get_broth_from_dec(self.dec)
        super().update_ingredient_list(ing)
        super().update_total_price(ing)
        super().cook()


class ToppingsDecorator(BaseRamenDecorator):

    """
    Represent topping customisation for ramen.
    """

    def __init__(self, ramen, decorator_string):
        """
        Initialise BrothDecorator object.
        :param ramen: object with RamenInterface implemented
        :param decorator: String
        """
        super().__init__(ramen)
        self.dec = decorator_string

    def cook(self):
        """
        Assemble the concrete Ramen and its decorators together.
        :return: None
        """
        ing = Menu.get_toppings_from_dec(self.dec)
        super().update_ingredient_list(ing)
        super().update_total_price(ing)
        super().cook()


def main():
    print("\nWelcome to Marutama.\n")
    ramen = ConcreteRamen()

    ramen = BrothDecorator(ramen, "Chicken Broth")
    ramen = BrothDecorator(ramen, "Spicy Broth")
    ramen = BrothDecorator(ramen, "Creamy Broth")
    ramen = ToppingsDecorator(ramen, "Fatty Chashu")

    print("Sample menu generated.")
    Menu.print(Menu.broth)



    ramen.cook()
    print(ramen)


if __name__ == "__main__":
    main()