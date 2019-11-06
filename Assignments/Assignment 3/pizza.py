"""
Interface, concrete object, and decorators for Pizzas.
"""

from abc import ABC, abstractmethod


class Ingredient:
    """
    Represents an ingredient (stores its name and price).
    """

    def __init__(self, name, price):
        """
        Initialsies an Ingredient object.
        :param name: String
        :param price: float
        """
        self.name = str(name).title()
        if isinstance(price, str):
            raise TypeError("Enter a numeric value for price.")
        elif price <= 0:
            raise ValueError("Price must be at least $0.01")
        else:
            self.price = price

    def __str__(self):
        price = '${:,.2f}'.format(self.price)
        return f"{self.name}: {price}"


class Pizza(ABC):
    """
    Interface for Pizza and PizzaDecorator objects.
    """
    @abstractmethod
    def increase_price(self, ingredient):
        pass

    @abstractmethod
    def get_total_price(self):
        pass

    @abstractmethod
    def add_ingredient(self, ingredient):
        pass

    @abstractmethod
    def get_ingredients(self):
        pass

    @abstractmethod
    def assemble(self):
        """
        Assemble pizza.
        :return: None
        """
        # create an ingredient - depending on the decorator
        # increment price
        # append to the list
        # call super
        pass

    @abstractmethod
    def __str__(self):
        pass


class PlainPizza(Pizza):
    """
    Concrete Pizza with Signature Crust.
    """

    def __init__(self):
        """
        Creates a basic pizza with signature crust.
        :param ingredients: Ingredient []
        :param total_price: float
        """
        self.ingredients = []
        self.total_price = 0

    def increase_price(self, ingredient):
        """
        Takes ingredient and adds its price to total.
        :param ingredient: Ingredient
        :return: None
        """
        self.total_price += ingredient.price

    def get_total_price(self):
        """
        Get total price of pizza.
        :return: float
        """
        return self.total_price

    def add_ingredient(self, ingredient):
        """
        Add ingredient to pizza's ingredient list.
        :param ingredient:
        :return: None
        """
        self.ingredients.append(ingredient)

    def get_ingredients(self):
        """
        Get ingredients from pizza.
        :return: Ingredient list
        """
        return self.ingredients

    def assemble(self):
        """
        Add an ingredient to the pizza.
        :param ingredient: Ingredient
        :return: None
        """
        ingredient = Ingredient("Signature Crust", 4.99)
        self.ingredients.append(ingredient)
        self.increase_price(ingredient)

    def __str__(self):
        """
        String representation of pizza.
        :return: String
        """
        price = '${:,.2f}'.format(self.total_price)
        i_list = [i.name for i in self.ingredients][::-1]
        return f"Ingredient List: {', '.join(i_list)}\n" \
               f"Total Price: {price}\n"


class BasePizzaDecorator(Pizza):

    """
    Base pizza decorator that all decorators inherit from;
    Creates the interface through which decorators access
    wrapee functionality.
    """

    def __init__(self, pizza):
        """
        Initialises BasePizzaDecorator with pizza object.
        :param pizza: object that implements Pizza interface
        """
        self.pizza = pizza

    def increase_price(self, ingredient):
        """
        Get total price of pizza.
        :return: float
        """
        self.pizza.increase_price(ingredient)

    def get_total_price(self):
        """
        Get total price of pizza.
        :return: float
        """
        return self.pizza.get_total_price()

    def add_ingredient(self, ingredient):
        """
        Add ingredient to pizza's ingredient list.
        :param ingredient:
        :return: None
        """
        self.pizza.add_ingredient(ingredient)

    def get_ingredients(self):
        """
        Get ingredients from pizza.
        :return: Ingredient list
        """
        return self.pizza.get_ingredients()

    def assemble(self):
        """
        Add an ingredient to the pizza.
        :param ingredient: Ingredient
        :return: None
        """
        self.pizza.assemble()

    def __str__(self):
        """
        String representation of pizza.
        :return: String
        """
        return self.pizza.__str__()


class ParmigianoPizzaDecorator(BasePizzaDecorator):

    def assemble(self):
        """
        Add an ingredient to the pizza.
        :param ingredient: Ingredient
        :return: None
        """
        ingredient = Ingredient("Parmigiano Reggiano", 4.99)
        super().add_ingredient(ingredient)
        super().increase_price(ingredient)
        super().assemble()


class MozzarellaPizzaDecorator(BasePizzaDecorator):

    """
    Adds the Fresh Mozzarella ingredient to the pizza.
    """

    def assemble(self):
        """
        Add an ingredient to the pizza.
        :param ingredient: Ingredient
        :return: None
        """
        ingredient = Ingredient("Fresh Mozzarella", 3.99)
        super().add_ingredient(ingredient)
        super().increase_price(ingredient)
        super().assemble()


class VeganPizzaDecorator(BasePizzaDecorator):
    """
    Adds the Vegan Cheese ingredient to the pizza.
    """

    def assemble(self):
        """
        Add an ingredient to the pizza.
        :param ingredient: Ingredient
        :return: None
        """
        ingredient = Ingredient("Vegan Cheese", 5.99)
        super().add_ingredient(ingredient)
        super().increase_price(ingredient)
        super().assemble()


class PepperPizzaDecorator(BasePizzaDecorator):
    """
    Adds the Peppers ingredient to the pizza.
    """

    def assemble(self):
        """
        Add an ingredient to the pizza.
        :param ingredient: Ingredient
        :return: None
        """
        ingredient = Ingredient("Peppers", 1.5)
        super().add_ingredient(ingredient)
        super().increase_price(ingredient)
        super().assemble()


class PineapplePizzaDecorator(BasePizzaDecorator):
    """
    Adds the Pineapple ingredient to the pizza.
    """

    def assemble(self):
        """
        Add an ingredient to the pizza.
        :param ingredient: Ingredient
        :return: None
        """
        ingredient = Ingredient("Pineapple", 2)
        super().add_ingredient(ingredient)
        super().increase_price(ingredient)
        super().assemble()


class MushroomPizzaDecorator(BasePizzaDecorator):
    """
    Adds the Mushroom ingredient to the pizza.
    """

    def assemble(self):
        """
        Add an ingredient to the pizza.
        :param ingredient: Ingredient
        :return: None
        """
        ingredient = Ingredient("Mushrooms", 1.5)
        super().add_ingredient(ingredient)
        super().increase_price(ingredient)
        super().assemble()


class BasilPizzaDecorator(BasePizzaDecorator):
    """
    Adds the Basil ingredient to the pizza.
    """

    def assemble(self):
        """
        Add an ingredient to the pizza.
        :param ingredient: Ingredient
        :return: None
        """
        ingredient = Ingredient("Fresh Basil", 2)
        super().add_ingredient(ingredient)
        super().increase_price(ingredient)
        super().assemble()


class SpinachPizzaDecorator(BasePizzaDecorator):
    """
    Adds the Spinach ingredient to the pizza.
    """

    def assemble(self):
        """
        Add an ingredient to the pizza.
        :param ingredient: Ingredient
        :return: None
        """
        ingredient = Ingredient("Spinach", 1)
        super().add_ingredient(ingredient)
        super().increase_price(ingredient)
        super().assemble()


class PepperoniPizzaDecorator(BasePizzaDecorator):
    """
    Adds the Pepperoni ingredient to the pizza.
    """

    def assemble(self):
        """
        Add an ingredient to the pizza.
        :param ingredient: Ingredient
        :return: None
        """
        ingredient = Ingredient("Pepperoni", 3)
        super().add_ingredient(ingredient)
        super().increase_price(ingredient)
        super().assemble()


class BeyondPizzaDecorator(BasePizzaDecorator):
    """
    Adds the Beyond Meat ingredient to the pizza.
    """

    def assemble(self):
        """
        Add an ingredient to the pizza.
        :param ingredient: Ingredient
        :return: None
        """
        ingredient = Ingredient("Beyond Meat", 4)
        super().add_ingredient(ingredient)
        super().increase_price(ingredient)
        super().assemble()


def main():
    pizza = PlainPizza()

    pizza = ParmigianoPizzaDecorator(pizza)
    #
    pizza = MozzarellaPizzaDecorator(pizza)

    pizza = MozzarellaPizzaDecorator(pizza)

    pizza.assemble()
    print(pizza)


if __name__ == "__main__":
    main()
