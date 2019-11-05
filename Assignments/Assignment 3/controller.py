from menu import Menu
from pizza import PlainPizza
from sys import exit
import texttable as tt


class Controller:

    def __init__(self):
        self.pizza = None
        self.pending_order = "Signature Crust"

    def get_pending_order(self):
        return f"\nPending Order: {self.pending_order}"

    def add_to_pending_order(self, ingredient):
        self.pending_order += f", {ingredient}"

    def update_pending_order(self, ingredient):
        self.add_to_pending_order(ingredient)
        print(self.get_pending_order())

    @classmethod
    def get_user_choice(cls, menu):
        """
        Solicit user input with error validation in place.
        :param menu: Menu dictionary
        :return: choice as int
        """
        Menu.print(menu)
        try:
            user_input = int(input("Enter menu number: "))
            if user_input not in range(1, len(menu) + 1):
                raise ValueError
        except TypeError as e:
            print("\nException: Only integers are accepted.\n")
        except ValueError as e:
            print(f"\nException: Enter valid integer.")
        else:
            return user_input

    def start(self):
        user_input = None
        while user_input is None:
            user_input = Controller.get_user_choice(Menu.start_menu)

        choices = {
            1: PlainPizza,
            2: exit
        }
        # Create base concrete pizza
        self.pizza = choices.get(user_input)()
        print(self.get_pending_order())

        # Select cheese toppings
        self.cheese_menu()

    def add_topping(self, menu, dec_menu):
        user_input = Controller.get_user_choice(menu)

        if user_input in range(1, len(dec_menu) + 1):
            topping = menu.get(user_input)
            self.pizza = dec_menu.get(user_input)(self.pizza)
            self.update_pending_order(topping.name)
        return user_input

    def check_out(self):
        print("\nCHECKING OUT...\n")
        print("Please confirm your order below.\n")
        self.pizza.assemble()

        tab = tt.Texttable()
        headings = ['Ingredient', 'Unit Price']
        tab.header(headings)

        ingredients = [i.name for i in self.pizza.get_ingredients()][::-1]

        prices = [i.price for i in self.pizza.get_ingredients()][::-1]
        prices = ['${:,.2f}'.format(price) for price in prices]

        for row in zip(ingredients, prices):
            tab.add_row(row)

        # Grab total price of pizza
        total_price = self.pizza.get_total_price()
        # Format total price
        total_price = '${:,.2f}'.format(total_price)
        # Add total price to texttable
        tab.add_row(["Total", total_price])

        s = tab.draw()
        print(s)

    def cheese_menu(self):
        render_menu = True
        num_cheese = len(Menu.cheese_dec)
        while render_menu:
            user_input = self.add_topping(Menu.cheese_menu, Menu.cheese_dec)

            if user_input in range(4, 7):
                render_menu = False

            if not self.has_cheese():
                render_menu = True

            if user_input is 4:
                self.toppings_menu()
            elif user_input is 5 and self.has_cheese():
                self.check_out()
            elif user_input is 5 and not self.has_cheese():
                print("Pizzas must have at least one cheese topping.")
            elif user_input is 6:
                exit()

    def has_cheese(self):
        order = self.pending_order
        cheeses = ["Parmigiano Reggiano", "Fresh Mozzarella", "Vegan Cheese"]
        for cheese in cheeses:
            if cheese in order:
                return True
        return False

    def toppings_menu(self):
        user_input = None
        while user_input is not 9:
            user_input = self.add_topping(Menu.toppings_menu,
                                          Menu.toppings_dec)

            if user_input is 8:
                self.cheese_menu()
            elif user_input is 9 and self.has_cheese():
                self.check_out()
            elif user_input is 10:
                exit()


def main():
    con = Controller()
    con.start()


if __name__ == "__main__":
    main()