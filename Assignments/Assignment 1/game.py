from datetime import datetime
import random
from peripherals import Catalogue
from peripherals import Medicine
from peripherals import Minigame
from pokemon import PokemonCreator


class GameUI:
    """
    Display menu items and control the flow of logic for the menu
    itself.
    """

    @classmethod
    def display_start_menu(cls, game):
        """
        Display start menu (with no Pokemon hatched).
        """
        user_input = None

        while user_input != 2:

            print("\n\n=== The Pokemon Tamagotchi Game ===\n")
            print("Hello there! Welcome to the world of POKEMON!\n"
                  "My name is EUCALYPTUS. People call me the \n"
                  "POKEMON PROF!\n")
            print("This world is inhabited by creatures called \n"
                  "POKEMON! For some people, POKEMON are used for \n"
                  "fights. Myself... I raise POKEMON as pets.\n")
            print("Your very own POKEMON legend is about to unfold!\n"
                  "A world of dreams and adventures with POKEMON \n"
                  "awaits! Let's go!\n")

            Catalogue.print_menu(Catalogue.start_menu)
            user_input = input("\nSelect action: ")

            try:
                user_input = int(user_input)
            except ValueError:
                print("\nInvalid input. Try again.\n")

            if type(user_input) == int:
                if user_input == 1:
                    game.pet = PokemonCreator.hatch_pet()
                    game.pet_menu()
                elif user_input == 2:
                    print("\nThanks for playing.\n")
                else:
                    print("\nInvalid input. Try again.\n")

    @classmethod
    def display_pet_menu(cls, game):
        """
        Display list of possible pet interactions.
        """
        user_input = None
        while user_input != 4:
            Catalogue.print_menu(Catalogue.pet_menu)
            user_input = input("Select action: ")

            choices = {1: game.check_status,
                       2: game.item_menu,
                       3: game.minigame_menu}
            try:
                user_input = int(user_input)
            except ValueError:
                print("\nInvalid input. Try again.\n")

            if user_input in range(1, 4):
                choices.get(user_input)()
            elif user_input == 4:
                print("\nThanks for playing.\n")

    @classmethod
    def display_minigame_menu(cls, game):
        """
        Display list of games that your pet can play.
        :param game: as GameController
        :return: None
        """
        user_input = None
        while user_input != 4:
            Catalogue.print_menu(Catalogue.minigame_menu)
            user_input = input("Select action: ")

            try:
                user_input = int(user_input)
            except ValueError:
                print("\nInvalid input. Try again.\n")

            output = ""

            if user_input == 1:
                guess = input("Enter starter Pokemon: ").title()
                output = Minigame.guess(guess)
                game.make_happier()
            elif user_input == 2:
                output = Minigame.elements(random.choice(
                    Catalogue.elements),
                                  random.choice(Catalogue.elements))
                game.make_happier()
            elif user_input == 3:
                output = Minigame.whack(random.randint(2, 10))
                game.make_happier()
            elif user_input == 4:
                pass

            print(output)

    @classmethod
    def display_item_menu(cls, game):
        """
        Display list of items that your pet can interact with.
        :param game: as GameController
        :return: None
        """
        user_input = None

        while user_input not in range(1, 4):
            print("\nWhich item would you like to give your pet?")
            Catalogue.print_menu(Catalogue.item_menu)
            user_input = input("Select action: ")

            try:
                user_input = int(user_input)
            except ValueError:
                print("\nInvalid input. Try again.\n")

            choices = {1: game.give_meds,
                       2: game.food_menu,
                       3: game.pet_menu}

            if user_input == 1:
                choices.get(user_input)(Medicine())
            elif user_input in range(2, 4):
                choices.get(user_input)()

    @classmethod
    def display_food_menu(cls, game):
        """
        Display food items from Catalogue.
        :param game: as GameController
        :return: None
        """
        print("What do you want to feed your Pokemon?")
        Catalogue.print_food()

        user_input = input("Select item: ")

        try:
            user_input = int(user_input)
        except ValueError:
            print("\nInvalid input. Try again.\n")

        food_selected = Catalogue.food_items.get(user_input)

        if food_selected.name in game.pet.food_dislikes:
            print("\nYUCK! Your pet refuses to eat this.\n")

        elif food_selected.name in game.pet.food_likes:
            print(f"\nYUM! Your pet gobbled {food_selected.name}!\n")
            game.feed_like(food_selected)
        else:
            print("\nMeh... it's okay, I guess.\n")
            game.feed_neutral(food_selected)


class GameController:
    """
    Control the logic for the Tamagotchi pet.
    """
    def __init__(self):
        self.pet = None

    def start(self):
        GameUI.display_start_menu(self)

    def pet_menu(self):
        GameUI.display_pet_menu(self)

    def item_menu(self):
        GameUI.display_item_menu(self)

    def minigame_menu(self):
        GameUI.display_minigame_menu(self)

    def food_menu(self):
        GameUI.display_food_menu(self)

    def change_bar(self, bar):
        """
        Calculate the time difference between now and last
        status check, and modifies the value of the given
        StatusBar (bar) based on an inherent bar rate.
        :param bar: as StatusBar, through instance variable "pet"
        (type Pokemon)
        :return: None
        """
        curr_time = datetime.now()
        diff = abs(curr_time - self.pet.timestamp)
        change = bar.rate * diff.total_seconds()
        bar.curr += int(change)
        if bar.curr < 0:
            bar.curr = 0
        elif bar.curr > 100:
            bar.curr = 100

    def make_happier(self):
        """
        Make pet happier after playing a game. Happiness
        value is controlled by Pokemon subclass defined value
        (e.g. All Scorbunnies have the same value.)
        :return: None
        """
        bar = self.pet.happiness
        bar.curr += self.pet.game_happiness
        if bar.curr < 0:
            bar.curr = 0
        elif bar.curr > 100:
            bar.curr = 100

    def check_status(self):
        """
        Use change_bar(bar) as a helper to update all pet StatusBars
        and perform checks on special behaviour dependent on current
        values. (e.g. When famished, pets' health decreases twice as
        fast.)
        :return: None
        """
        curr_time = datetime.now()
        self.change_bar(self.pet.health)
        self.change_bar(self.pet.happiness)
        self.change_bar(self.pet.hunger)
        self.check_sickness()
        self.pet.timestamp = curr_time

        if self.pet.hunger.curr > 99:
            self.pet.health.rate = self.pet.HUNGRY_HEALTH_RATE
        else:
            self.pet.health.rate = self.pet.HEALTH_RATE

        if self.pet.health.curr > 0:
            print(f"\n{self.pet}")
        else:
            print("Your pet has died :(\n"
                  "Create a new one now.")
            self.pet = None
            self.pet = PokemonCreator.hatch_pet()

    def feed_like(self, food):
        """
        Give pet one of its liked foods.
        :param food: as Food
        :return: None
        """
        self.pet.hunger.curr += food.value * food.like_multiplier

    def feed_neutral(self, food):
        """
        Give pet one of the foods it feels neutral about.
        :param food: as Food
        :return: None
        """
        self.pet.hunger.curr += food.value

    def give_meds(self, meds):
        """
        Determine logic for giving Medicine.  Pet will refuse
        Medicine if Healthy.  When sick, Medicine will cure its
        ailment.
        :param meds: as Medicine
        :return: None
        """
        if self.pet.is_sick:
            self.pet.health.curr += meds.value
            self.pet.is_sick = False
            print(f"\n{self.pet.name} took {meds.name} and feels a "
                  f"lot better!")
        else:
            print(f"\nYUCK! I'm not sick. I don't want any"
                  f" {meds.name}.\n")

    def check_sickness(self):
        """
        Check to see if pet is sick, based on its instance variable,
        sick_threshold.
        :return: None
        """
        if self.pet.health.curr < self.pet.sick_threshold:
            self.pet.is_sick = True


def main():
    """
    Drive the program.
    :return: None
    """
    game = GameController()
    game.start()


if __name__ == "__main__":
    main()
