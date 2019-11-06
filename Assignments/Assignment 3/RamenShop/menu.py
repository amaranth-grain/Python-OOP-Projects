

class Ingredient:
    def __init__(self, name, price):
        self._name = str(name).title()
        if isinstance(price, str):
            raise TypeError("Enter a numeric value for price.")
        elif price <= 0:
            raise ValueError("Price must be at least $0.01")
        else:
            self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price


class Menu:

    start = {
        "Customise your ramen": Ingredient("Marutama Ramen", 4.99),
        "Quit": exit
    }

    broth = {
        "Marutama Ramen" : Ingredient("Marutama Ramen", 4.99),
        "Chicken Broth": Ingredient("Chicken Broth", 2.99),
        "Spicy Broth": Ingredient("Spicy Broth", 2.99),
        "Creamy Broth": Ingredient("Creamy Broth", 2.99)
    }

    toppings = {
        "Ajitsuke Tamago": Ingredient("Ajitsuke Tamago", 1.5),
        "Fatty Chashu": Ingredient("Fatty Chashu", 2),
        "Black Fungus": Ingredient("Black Fungus", 1.5),
        "Spring Onion": Ingredient("Spring Onion", 2),
        "Mung Bean Sprout": Ingredient("Mung Bean Sprout", 1),
        "Fish Cake": Ingredient("Fish Cake", 3),
        "Aosa Seaweed": Ingredient("Seaweed", 4)
    }

    @staticmethod
    def get_broth_from_dec(dec):
        return Menu.broth.get(dec)

    @staticmethod
    def get_toppings_from_dec(dec):
        return Menu.toppings.get(dec)

    @staticmethod
    def print(menu):
        i = 1
        for v in menu.keys():
            print(f"{i}. {v}")
            i += 1