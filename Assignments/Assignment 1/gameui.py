from pokemon import PokemonCreator
from pokemon import PokemonController
from interaction import Catalogue

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
                PokemonController.set_pet(PokemonCreator.hatch_pet())
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
        all_food = Catalogue.get_food_items()
        all_food_list = Catalogue.food_items
        disliked_food = PokemonController._pet._food_dislikes
        liked_food = PokemonController._pet._food_likes
        print("What do you want to feed your Pokemon?")
        print(all_food)
        user_input = int(input("Select item: "))
        food_selected = all_food_list.get(user_input)
        if food_selected in disliked_food:
            print("Yuck!")
        elif food_selected in liked_food:
            print("Yum!")
        else:
            print("It\'s okay")

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
                print(pet_menu_dict.get(user_input)())
                GameUI.display_pet_menu()
            # print(f"More testing: "
            #       f"{PokemonController.check_status()}")

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