from datetime import datetime
import random
from peripherals import Catalogue
from peripherals import Medicine
from peripherals import Minigame
from pokemon import PokemonCreator


class GameController:
    """
    Control Tamagotchi pet and control flow of logic in game.
    """

    def __init__(self):
        self.pet = None

    def start(self):
        """
        Display start menu (with no Pokemon hatched).
        """
        user_input = None
        while user_input not in range(1, 3):
            Catalogue.print_menu(Catalogue.start_menu)
            user_input = int(input("\nSelect action: "))

            if user_input == 1:
                self.pet = PokemonCreator.hatch_pet()
                self.pet_menu()
            elif user_input == 2:
                print("\nThanks for playing.\n")
            else:
                print("\nInvalid input. Try again.\n")

    def pet_menu(self):
        """
        Display list of possible pet interactions.
        """
        user_input = None
        while user_input != 4:
            Catalogue.print_menu(Catalogue.pet_menu)
            user_input = int(input("Select action: "))

            choices = {1: self.check_status,
                       2: self.item_menu,
                       3: self.minigame_menu}

            if user_input in range(1, 4):
                choices.get(user_input)()
            elif user_input == 4:
                print("\nThanks for playing.\n")
            else:
                print("\nInvalid input. Try again.\n")

    def minigame_menu(self):
        user_input = None
        while user_input != 4:
            Catalogue.print_menu(Catalogue.minigame_menu)
            user_input = int(input("Select action: "))

            output = ""

            if user_input == 1:
                guess = input("Enter starter Pokemon: ").title()
                output = Minigame.guess(guess)
            elif user_input == 2:
                output = Minigame.elements(random.choice(
                    Catalogue.elements),
                                  random.choice(Catalogue.elements))
            elif user_input == 3:
                output = Minigame.whack(random.randint(2, 10))
            elif user_input == 4:
                pass
            else:
                print("\nInvalid input. Try again.\n")

            print(output)

    def item_menu(self):
        user_input = None

        while user_input not in range(1, 4):
            print("\nWhich item would you like to give your pet?")
            Catalogue.print_menu(Catalogue.item_menu)
            user_input = int(input("Select action: "))

            choices = {1: self.give_meds,
                       2: self.food_menu,
                       3: self.pet_menu}

            if user_input == 1:
                choices.get(user_input)(Medicine())
            elif user_input in range(2, 4):
                choices.get(user_input)()
            else:
                print("\nInvalid input. Try again.\n")

    def food_menu(self):
        print("What do you want to feed your Pokemon?")
        Catalogue.print_food()

        user_input = int(input("Select item: "))
        food_selected = Catalogue.food_items.get(user_input)

        if food_selected.name in self.pet.food_dislikes:
            print("\nYUCK! Your pet refuses to eat this.\n")

        elif food_selected.name in self.pet.food_likes:
            print(f"\nYUM! Your pet gobbled {food_selected.name}!\n")
        else:
            print("\nMeh... it's okay, I guess.\n")
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
        self.check_sickness()

        if self.pet.hunger.curr > 99:
            self.pet.health.rate *= self.pet.health.multiplier
            print("\nI'm so hungry...\n")

        if self.pet.health.curr > 0:
            print(f"\n{self.pet}")
        else:
            print("Your pet has died :(\n"
                  "Create a new one now.")
            self.pet = None
            self.pet = PokemonCreator.hatch_pet()

    def feed_like(self, food):
        self.pet.hunger.curr += food._value * food._like_multiplier
        return None

    def feed_neutral(self, food):
        self.pet.hunger.curr += food._value

    def give_meds(self, meds):
        if self.pet._is_sick:
            self.pet.health.curr += meds._value
            self.pet._is_sick = False
            self.pet.health.rate = self.pet.health.original_rate
            print(f"\n{self.pet.name} took {meds._name} and feels a lot " \
                  f"better!\n")
        else:
            print(f"\nYUCK! I'm not sick. I don't want any"
                  f" {meds._name}.\n")

    def check_sickness(self):
        if self.pet.health.curr < self.pet.sick_threshold:
            self.pet._is_sick = True


def main():
    game = GameController()
    game.start()


if __name__ == "__main__":
    main()
