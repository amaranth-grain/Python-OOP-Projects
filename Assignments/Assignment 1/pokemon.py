from abc import ABC
from datetime import datetime, timedelta
import random


class StatusBar():
    def __init__(self, rate=-1.0, curr_value=100, max_value=100,
                 multiplier=1.0):
        self.rate = rate
        self.curr_value = int(curr_value)
        self.max_value = max_value
        self.multiplier = multiplier

class Pokemon(ABC):
    def __init__(self, name, species, food_likes, food_dislikes, moods,
                 health, happiness, hunger, is_sick, is_alive,
                 timestamp):
        self._name = name
        self._species = species
        self._food_likes = food_likes
        self._food_dislikes = food_dislikes
        self._moods = moods
        self._health = health
        self._happiness = happiness
        self._hunger = hunger
        self._is_sick = is_sick
        self._is_alive = is_alive
        self._timestamp = timestamp

    def get_name(self):
        return self._name

    def die(self):
        if self._health.curr_value <= 0:
            self._is_alive = False

    def __str__(self):
        feel = "Sick" if self._is_sick else "Healthy"
        likes = "\n".join(self._food_likes)
        dislikes = "\n".join(self._food_dislikes)

        return f"=== {self._name} the {self._species}'s Stats ===\n" \
               f"Health rate: \t{self._health.rate} per second\n" \
               f"Health: \t\t{self._health.curr_value} / " \
               f"{self._health.max_value}\n" \
               f"Happiness: \t\t{self._happiness.curr_value} / " \
               f"{self._happiness.max_value}\n" \
               f"Hunger: \t\t{self._hunger.curr_value} / " \
               f"{self._hunger.max_value}\n" \
               f"Feeling: \t\t{feel}\n" \
               f"===Food Likes ===\n {likes}\n" \
               f"===Food Dislikes ===\n {dislikes}\n" \
               f"Timestamp: {self._timestamp}"


class Scorbunny(Pokemon):
    likes = ('Spicy Szechuan Carrots', 'Carrot Cake',
             'Spaghetti Bolognese', 'Red Velvet Cake')

    dislikes = ('Bloody Mary', 'Pig Blood Curd', 'Rabbit Cacciatore')

    moods = {"sick": "／(˃ᆺ˂)＼", "happy": "／(^ᆺ^)＼ ~♡",
             "frustrated": "／(≧ x ≦)＼", "neutral": "／(･ᆺ･)＼",
             "angry": "／(＞×＜#)＼"}

    def __init__(self, name,
                 species="Scorbunny",
                 food_likes=likes,
                 food_dislikes=dislikes,
                 moods=moods,
                 health=StatusBar(),
                 happiness=StatusBar(),
                 hunger=StatusBar(),
                 is_sick=False,
                 is_alive=True,
                 timestamp=datetime.now()):
        super().__init__(name, species,
                         food_likes, food_dislikes, moods,
                         health, happiness, hunger, is_sick,
                         is_alive, timestamp)
        self._species = species


class Crobat(Pokemon):
    likes = ('Bloody Mary', 'Pig Blood Curd', 'Rabbit Cacciatore')

    dislikes = ('Carrot Cake', 'Leek and Potato Cake',
                'Buttered Leeks', 'Garlic Chicken')

    moods = {"sick": "/|\(＋_＋)/|\\", "happy": "/|\(≧◡≦)/|\\ ~♡",
             "frustrated": "/|\( ;,;)/|\\", "neutral": "/|\(￣～￣)/|\\",
             "angry": "/|\(╬◣﹏◢)/|\\"}

    def __init__(self, name,
                 species="Crobat",
                 food_likes=likes,
                 food_dislikes=dislikes,
                 moods=moods,
                 health=StatusBar(),
                 happiness=StatusBar(),
                 hunger=StatusBar(),
                 is_sick=False,
                 is_alive=True,
                 timestamp=datetime.now()):
        super().__init__(name, species, food_likes, food_dislikes,
                         moods, health, happiness, hunger, is_sick,
                         is_alive, timestamp)
        self._species = species


class Sirfetchd(Pokemon):
    likes = ('Leek and Potato Cake', 'Buttered Leeks',
             'Spring Onion Oil Noodles')

    dislikes = ('Pig Blood Curd', 'Rabbit Cacciatore',
                'Garlic Chicken', 'Duck a l\'Orange')

    moods = {"sick": "/|\(＋_＋)/|\\", "happy": "/|\(≧◡≦)/|\\ ~♡",
             "frustrated": "/|\( ;,;)/|\\", "neutral": "/|\(￣～￣)/|\\",
             "angry": "/|\(╬◣﹏◢)/|\\"}

    def __init__(self, name,
                 species="Sirfetchd",
                 food_likes=likes,
                 food_dislikes=dislikes,
                 moods=moods,
                 health=StatusBar(),
                 happiness=StatusBar(),
                 hunger=StatusBar(),
                 is_sick=False,
                 is_alive=True,
                 timestamp=datetime.now()):
        super().__init__(name, species, food_likes, food_dislikes,
                         moods, health, happiness, hunger, is_sick,
                         is_alive, timestamp)
        self._species = species

class PokemonCreator:
    @classmethod
    def hatch_pet(cls):
        pets = {1: Scorbunny,
                2: Crobat,
                3: Sirfetchd}
        name = input("\nGive a name to your Pokemon: ")

        type_of_pokemon = pets.get(random.choice(list(pets)))
        pet = type_of_pokemon(name)

        return pet


class PokemonController:

    _pet = None

    @classmethod
    def set_pet(cls, pet):
        cls._pet = pet

    @classmethod
    def get_name(cls):
        return cls._pet.get_name()

    @classmethod
    def get_pet(cls):
        return cls._pet

    @classmethod
    def check_status(cls):
        PokemonController.change_bar(cls._pet._health.rate)
        PokemonController.change_bar(cls._pet._happiness.rate)
        PokemonController.change_bar(cls._pet._hunger.rate)
        return f"\n{cls._pet}"

    @classmethod
    def change_bar(cls, bar):
        curr_time = datetime.now()
        diff = abs(curr_time - cls._pet._timestamp)
        decrement = bar * diff.total_seconds()
        cls._pet._health.curr_value += int(decrement)
        cls._pet._timestamp = curr_time

    @classmethod
    def give_consumable(cls):
        print("\nGive consumable\n")


def main():
    scorbunny = Scorbunny("Bun bun")
    crobat = Crobat("Batty")
    sirfetchd = Sirfetchd("Ducky")
    print(crobat)
    print(sirfetchd)

    # test = PokemonController(PokemonCreator.hatch_pet())
    # print(test)
    # print(test.check_status())


if __name__ == "__main__":
    main()