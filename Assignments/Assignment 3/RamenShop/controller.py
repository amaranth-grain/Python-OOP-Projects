"""
Controls the flow of logic in Pizza shop order form.
"""
from menu import Menu
from ramen import ConcreteRamen
from sys import exit


class Controller:
    """
    Controls the flow of logic for Pizza shop.
    """

    def __init__(self):
        """
        Initialises Controller object.
        """
        self.ramen = None
        self.pending_order = "Marutama Ramen"

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
        """
        Start the Ramen shop program.
        :return: None
        """
        user_input = None
        while user_input is None:
            user_input = Controller.get_user_choice(Menu.start)

        if user_input == 1:
            self.ramen = ConcreteRamen()
        else:
            exit()

        # Select cheese toppings
        self.broth_menu()

    def broth_menu(self):
        """
        Control the cheese menu logic.
        :return: None
        """
        render_menu = True



def main():
    con = Controller()
    con.start()


if __name__ == "__main__":
    main()