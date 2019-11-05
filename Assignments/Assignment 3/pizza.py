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
        self.ingredients.append(ingredient)

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
        price = '${:,.2f}'.format(self.total_price)
        i_list = [i.name for i in self.ingredients][::-1]
        return f"Ingredient List: {', '.join(i_list)}\n" \
               f"Total Price: {price}\n"


class BasePizzaDecorator(Pizza):

    def __init__(self, pizza):
        self.pizza = pizza

    def increase_price(self, ingredient):
        self.pizza.increase_price(ingredient)

    def get_total_price(self):
        """
        Get total price of pizza.
        :return: float
        """
        print(self.pizza.total_price)
        return self.pizza.total_price

    def add_ingredient(self, ingredient):
        self.pizza.add_ingredient(ingredient)

    def assemble(self):
        """
        Add an ingredient to the pizza.
        :param ingredient: Ingredient
        :return: None
        """
        self.pizza.assemble()

    def __str__(self):
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

    def __str__(self):
        return super().__str__()


class MozzarellaPizzaDecorator(BasePizzaDecorator):

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

    def __str__(self):
        return super().__str__()


class VeganPizzaDecorator(BasePizzaDecorator):

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

    def __str__(self):
        return super().__str__()




def main():
    pizza = PlainPizza()

    pizza = ParmigianoPizzaDecorator(pizza)
    #
    pizza = MozzarellaPizzaDecorator(pizza)

    pizza = MozzarellaPizzaDecorator(pizza)

    pizza.assemble()
    print(pizza)

    # has_parm = input("Has parm? Y/N ")
    # if has_parm.lower() == 'y':
    #     has_parm = True
    # else:
    #     has_parm = False
    #
    # has_mozz = input("Has mozz? Y/N ")
    # if has_mozz.lower() == 'y':
    #     has_mozz = True
    # else:
    #     has_mozz = False
    #
    # if has_parm:
    #     pizza = ParmigianoPizzaDecorator(pizza)
    # if has_mozz:
    #     pizza = MozzarellaPizzaDecorator(pizza)



if __name__ == "__main__":
    main()
