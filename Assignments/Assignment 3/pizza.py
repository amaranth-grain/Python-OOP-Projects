from abc import ABC, abstractmethod
from enum import Enum


class Pizza(ABC):

    @abstractmethod
    def get_ingredients_str(self):
        pass

    @abstractmethod
    def add_ingredient(self, ingredient):
        pass

    @property
    @abstractmethod
    def ingredients(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @property
    @abstractmethod
    def total_price(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class SignatureCrustPizza(Pizza):

    def __init__(self, name, ingredients, price, total_price):
        """
        Initialises a Pizza object.
        :param name: String name of component
        :param ingredients: list of ingredients (String)
        :param price: float
        :param total_price: float
        """
        self._name = name.title()
        self._ingredients = [i.title() for i in ingredients]
        self._price = '${:,.2f}'.format(price)
        self._total_price = '${:,.2f}'.format(total_price)

    def get_ingredients_str(self):
        ing = "Ingredients: "
        ing += ", ".join(self._ingredients)
        return ing

    def add_ingredient(self, ingredient):
        self._ingredients.append(ingredient)
        self._total_price += ingredient.price

    @property
    def ingredients(self):
        return self._ingredients

    @property
    def price(self):
        return self._price

    @property
    def total_price(self):
        return self._total_price

    def __str__(self):
        return f"{self.get_ingredients_str()}\n" \
               f"Total Price: {self.total_price}"


class BasePizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_ingredients_str(self):
        self.pizza.get_ingredients_str()

    def add_ingredient(self, ingredient):
        self.pizza.add_ingredient(ingredient)

    @property
    def ingredients(self):
        return self.pizza.ingredients

    @property
    def price(self):
        return self.pizza.price

    @property
    def total_price(self):
        return self.pizza.total_price

    def __str__(self):
        return f"{self.get_ingredients_str()}\n" \
               f"Total Price: {self.total_price}"


class PizzaCreator:
    pizza_dict = {
        1: SignatureCrustPizza
    }


def main():
    plain = SignatureCrustPizza("sigNATURE Crust", ["sIgnaTURE Crust"], 234,
                                454)
    print(plain)


if __name__ == "__main__":
    main()
