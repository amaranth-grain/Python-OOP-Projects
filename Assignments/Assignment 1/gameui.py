from pokemon import PokemonCreator
from pokemon import PokemonController

class GameUI:
    """
    Print game menu for user interaction and input.
    """

    @staticmethod
    def display_start_menu():
        """
        Display start menu (with no Pokemon hatched).
        :return: None
        """
        user_input = None
        while user_input != 2 or user_input != 1:
            print("=== Pokemon Tamagotchi Game===")
            print("1. Hatch a random Pokemon")
            print("2. Quit")
            user_input = int(input("\nSelect action: "))

            if user_input == 1:
                pet = PokemonCreator.hatch_pet()
                GameUI.display_pet_menu()
            else:
                print("\nInvalid input. Try again.\n")

    # Consumable
    @staticmethod
    def display_food_items():
        """
        Display list of available Food items.
        :return: None
        """
        print("\nFood items go here.\n")

    # Consumable
    @staticmethod
    def display_give_item_menu():
        """
        Display list of item types.
        :return: None
        """
        print("\nWhat would you like to give your pet?")
        print("1. Medicine")
        print("2. Food")
        print("3. Back to pet menu")
        user_input = int(input("\nSelect action: "))

        if user_input == 1:
            PokemonController.give_consumable()
        elif user_input == 2:
            GameUI.display_food_items()
        elif user_input == 3:
            GameUI.display_pet_menu()
        else:
            print("\nInvalid input. Please try again.\n")

    # Pet Controller
    @staticmethod
    def display_pet_menu():
        """
        Display list of possible pet interactions.
        :return: None
        """
        user_input = None
        while user_input != 4:
            print("\n=== Tamagotchi Pet Menu ===")
            print(f"1. Check on your Pokémon")
            print("2. Give your Pokémon an item")
            print("3. Play with your Pokémon")
            print("4. Quit game")
            user_input = int(input("\nSelect action: "))

            pet_menu_dict = {1: PokemonController.check_status,
                             2: GameUI.display_give_item_menu,
                             3: GameUI.display_minigame_menu
                             }
            if user_input in range(1, 4):
                pet_menu_dict.get(user_input, "\nInvalid input. Try "
                                          "again.\n")()

    # Minigame
    @staticmethod
    def display_minigame_menu():
        """
        Display list of minigames.
        :return: None
        """
        user_input = None
        while user_input != 4:
            print("\n=== Pokémon Tamagotchi Minigames ===")
            print("What kind of game would you like to play?")
            print("1. Hide and seek")
            print("2. Guessing numbers")
            print("3. Rock paper scissors")
            print("4. Back to pet menu")
            user_input = int(input("\nSelect action: "))

            if user_input in range(1, 4):
                print("Start minigame")
            elif user_input == 4:
                GameUI.display_pet_menu()
            else:
                print("\nInvalid input. Please try again.\n")


def main():
    """
    Drive the program.
    :return: None
    """
    GameUI.display_start_menu()


if __name__ == "__main__":
    main()