from menu import Menu
from pizza import SignatureCrustPizza


class Controller:

    @staticmethod
    def start():
        Menu.print_menu(Menu.start_menu)
        choice_selected = False
        while not choice_selected:
            try:
                user_input = int(input("Enter menu number: "))
                if user_input > len(Menu.start_menu) or user_input < 1:
                    raise ValueError
            except ValueError as e:
                print(f"\nEnter a valid integer.\n")
            else:
                choice_selected = True


def main():
    con = Controller()
    con.start()


if __name__ == "__main__":
    main()