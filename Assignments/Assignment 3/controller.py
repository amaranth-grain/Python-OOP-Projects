from menu import Menu
from pizza import PlainPizza
from sys import exit


class Controller:

    def __init__(self):
        self.pizza = None
        self.pending_order = "Signature Crust"

    def get_pending_order(self):
        return f"\nPending Order: {self.pending_order}\n"

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

            self.pizza.assemble()
            print(self.pizza)

    def add_topping(self, menu, dec_menu):
        user_input = Controller.get_user_choice(menu)

        if user_input in range(1, len(dec_menu)):
            topping = menu.get(user_input)
            self.pizza = dec_menu.get(user_input)(self.pizza)
            self.update_pending_order(topping.name)
        return user_input

    def check_out(self):
        print("Check out pizza")

    def cheese_menu(self):
        user_input = None
        while user_input is not 5:
            user_input = self.add_topping(Menu.cheese_menu, Menu.cheese_dec)

            if user_input in range(len(Menu.cheese_dec),
                                   len(Menu.cheese_menu)):
                choices = {
                    4: self.toppings_menu,
                    5: self.check_out,
                    6: exit
                }
                choices.get(user_input)()


    def toppings_menu(self):
        user_input = None
        while user_input is not 9:
            self.add_topping(Menu.toppings_menu, Menu.toppings_dec)

    # def start(self):
    #     """
    #     Present start menu for Pizza shop.
    #     :return: None
    #     """
    #     user_input = Controller.get_user_choice(Menu.start_menu)
    #     choices = {
    #         1: PlainPizza,
    #         2: exit
    #     }
    #     # Create basic pizza with Signature Crust
    #     self.pizza = choices.get(user_input)()
    #     print(self.pizza)
    #
    #     # Render cheese menu
    #     self.cheese_menu()
    #
    # def cheese_menu(self):
    #     user_input = ""
    #     while user_input != 4:
    #         user_input = Controller.get_user_choice(Menu.cheese_menu)
    #         try:
    #             self.pizza = Menu.cheese_menu_create.get(user_input)(self.pizza)
    #         except TypeError as e:
    #             print(e)
    #
    #     self.pizza.add_ingredient()
    #     print(self.pizza)

    # tabulate and zip for bill formatting

    # @staticmethod
    # def start():
    #     Menu.print_menu(Menu.start_menu)
    #     choice_selected = False
    #     while not choice_selected:
    #         try:
    #             user_input = int(input("Enter menu number: "))
    #             if user_input > len(Menu.start_menu) or user_input < 1:
    #                 raise ValueError
    #         except ValueError as e:
    #             print(f"\nEnter a valid integer.\n")
    #         else:
    #             choice_selected = True
    #             base_pizza = SignatureCrustPizza()


def main():
    con = Controller()
    con.start()


if __name__ == "__main__":
    main()