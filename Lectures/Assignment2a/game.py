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
            user_input = int(input("\nSelect action: "))

            choices = {1: self.check_status(),
                       2: "give item",
                       3: "mini game"}

            print(choices.get(user_input))

    def change_bar(self, bar):
        curr_time = datetime.now()
        diff = abs(curr_time - self.pet._timestamp)
        change = bar.rate * diff.total_seconds()
        bar.curr += int(change)

    def check_status(self):
        self.change_bar(self.pet.health)
        self.change_bar(self.pet.happiness)
        self.change_bar(self.pet.hunger)
        self._timestamp = datetime.now()

        if self.pet.health.curr > 0:
            return f"\n{self.pet}"
        else:
            return ""


def main():
    game = GameController()
    game.start()


if __name__ == "__main__":
    main()
