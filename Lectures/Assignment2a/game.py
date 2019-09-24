from datetime import datetime
from peripherals import Catalogue
from peripherals import Medicine
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
                self.pet_menu()
            elif user_input == 2:
                print("\nThanks for playing.\n")
            else:
                print("\nInvalid input. Try again.\n")

    def pet_menu(self):
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
                       2: self.item_menu,
                       3: self.item_menu}

            if user_input in range(1, 4):
                print(choices.get(user_input)())
            elif user_input == 4:
                print("\nThanks for playing.\n")
            else:
                print("\nInvalid input. Try again.\n")

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
        self.check_sickness()

        if self.pet.hunger.curr > 99:
            self.pet.health.rate *= 2
            print("\nI'm so hungry...\n")

        if self.pet.health.curr > 0:
            return f"\n{self.pet}"
        else:
            print("Your pet has died :(\n"
                  "Create a new one now.")
            self.pet = None
            self.pet = PokemonCreator.hatch_pet()
            # return f"\nYour pet has died. :(\n Create a new one " \
            #        f"now.\n" \
            #        f"{PokemonCreator.hatch_pet()}"

    def feed_like(self, food):
        self.pet.hunger.curr += food._value * food._like_multiplier

    def feed_neutral(self, food):
        self.pet.hunger.curr += food._value

    def give_meds(self, meds):
        if self.pet._is_sick:
            self.pet.health.curr += meds._value
            self.pet._is_sick = False
            print(f"\n{self.pet.name} took {meds._name} and feels a lot " \
                  f"better!\n")
        else:
            print(f"YUCK! I'm not sick. I don't want any {meds._name}.")

    def check_sickness(self):
        if self.pet.health.curr < self.pet.sick_threshold:
            self.pet._is_sick = True


def main():
    game = GameController()
    game.start()


if __name__ == "__main__":
    main()
