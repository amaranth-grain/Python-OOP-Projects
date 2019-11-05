from menu import Menu
from pizza import PlainPizza
from sys import exit


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
                raise ValueError("Enter valid integer.")
        except ValueError as e:
            print(f"\nException: {e}\n")
        except TypeError as e:
            print("\nException: Only integers are accepted.\n")
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
        return self.pizza

    def cheese_menu(self):
        render_menu = True
        while render_menu:
            user_input = self.add_topping(Menu.cheese_menu, Menu.cheese_dec)

            if user_input in range(4, 7):
                render_menu = False

            if user_input is 4:
                self.toppings_menu()
            elif user_input is 5:
                print(self.check_out())
            elif user_input is 6:
                exit()

    def toppings_menu(self):
        user_input = None
        while user_input is not 9:
            user_input = self.add_topping(Menu.toppings_menu,
                                          Menu.toppings_dec)

            if user_input is 8:
                self.cheese_menu()
            elif user_input is 9:
                result = self.check_out()
                print(result)
            elif user_input is 10:
                exit()


def main():
    con = Controller()
    con.start()


if __name__ == "__main__":
    main()