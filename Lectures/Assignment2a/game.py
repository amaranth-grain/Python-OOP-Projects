from datetime import datetime
from peripherals import Catalogue
from pokemon import PokemonCreator


class GameController:
    def __init__(self):
        self.pet = None

    def start(self):
        """
        Display start menu (with no Pokemon hatched).
        :return: None
        """
        user_input = None
        while user_input not in range(1, 3):
            Catalogue.print_menu(Catalogue.start_menu)
            user_input = int(input("\nSelect action: "))

            if user_input == 1:
                self.pet = PokemonCreator.hatch_pet()
                self.display_pet_menu()
            elif user_input == 2:
                print("\nThanks for playing.\n")
            else:
                print("\nInvalid input. Try again.\n")

    def display_pet_menu(self):
        """
        Display list of possible pet interactions.
        :return: None
        """
        user_input = None
        while user_input != 4:
            Catalogue.print_menu(Catalogue.pet_menu)
            user_input = int(input("Select action: "))

            # TODO 3: minigame
            choices = {1: self.check_status,
                       2: self.display_item_menu,
                       3: self.display_item_menu}

            print(choices.get(user_input)())

    def display_item_menu(self):
        print("\nWhich item would you like to give your pet?")
        Catalogue.print_menu(Catalogue.item_menu)
        user_input = int(input("Select action: "))

        # TODO 1: Medicine
        choices = {1: self.display_food_menu,
                   2: self.display_food_menu,
                   3: self.display_pet_menu}

        choices.get(user_input)()

    def display_food_menu(self):
        print("What do you want to feed your Pokemon?")
        Catalogue.print_food()

        user_input = int(input("Select item: "))
        food_selected = Catalogue.food_items.get(user_input)

        if food_selected.name in self.pet._food_dislikes:
            print("\nYUCK! Your pet refuses to eat this.\n")
            print("What do you want to feed your Pokemon?")
            Catalogue.print_food()
        elif food_selected.name in self.pet._food_likes:
            print(f"YUM! Your pet gobbled {food_selected.name}!")
            self.feed_like(food_selected)
        else:
            print("Meh... it's okay, I guess.")
            self.feed_neutral(food_selected)

    def change_bar(self, bar):
        curr_time = datetime.now()
        diff = abs(curr_time - self.pet._timestamp)
        change = bar.rate * diff.total_seconds()
        bar.curr += int(change)
        if bar.curr < 0:
            bar.curr = 0
        elif bar.curr > 100:
            bar.curr = 100

    def check_status(self):
        self.change_bar(self.pet.health)
        self.change_bar(self.pet.happiness)
        self.change_bar(self.pet.hunger)
        self._timestamp = datetime.now()

        if self.pet.health.curr > 0:
            return f"\n{self.pet}"
        else:
            return f"\nYour pet has died. :("

    def feed_like(self, food):
        self.pet.hunger.curr += food._value * food._like_multiplier

    def feed_neutral(self, food):
        self.pet.hunger.curr += food._value




def main():
    game = GameController()
    game.start()


if __name__ == "__main__":
    main()
