from abc import ABC
from datetime import datetime, timedelta
import random


class StatusBar():
    """
    Represent a Pokemon status with ongoing changing values.
    """
    def __init__(self, rate=-1.0, curr_value=100, max_value=100,
                 multiplier=1.0):
        self.rate = rate
        self.curr_value = int(curr_value)
        self.max_value = max_value
        self.multiplier = multiplier


class Pokemon(ABC):
    """
    Represent a Pokemon Tamagotchi pet.
    """
    def __init__(self, name, species, food_likes, food_dislikes, moods,
                 health, happiness, hunger, is_sick, is_alive,
                 timestamp):
        """
        ABC for Pokemon
        :param name: as String
        :param species: as String
        :param food_likes: as String tuple
        :param food_dislikes: as String tuple
        :param moods: as dictionary
        :param health: as StatusBar
        :param happiness: as StatusBar
        :param hunger: as StatusBar
        :param is_sick: as boolean
        :param is_alive: as boolean
        :param timestamp: as datetime
        """
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
        """
        Return Pokemon name
        :return: as String
        """
        return self._name

    def die(self):
        """
        Pet dies when health reaches zero.
        :return: None
        """
        if self._health.curr_value <= 0:
            self._is_alive = False

    def __str__(self):
        """
        Format string for displaying Pokemon status.
        :return: as String
        """
        feel = "Sick" if self._is_sick else "Healthy"
        likes = "\n".join(self._food_likes)
        dislikes = "\n".join(self._food_dislikes)

        return f"=== {self._name} the {self._species}'s Stats ===\n" \
               f"Health rate: \t{self._health.rate} per second\n" \
               f"Happiness rate: \t{self._happiness.rate} per sec\n" \
               f"Hunger rate: \t{self._hunger.rate} per second\n" \
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
    """
    Represent Scorbunny pokemon.
    """

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
                 health=StatusBar(-2),
                 happiness=StatusBar(-3),
                 hunger=StatusBar(4, 0),
                 is_sick=False,
                 is_alive=True,
                 timestamp=datetime.now()):
        """
        Initialiser for Scorbunny
        :param name: as String
        :param species: as String
        :param food_likes: as String tuple
        :param food_dislikes: as String tuple
        :param moods: as dictionary
        :param health: as StatusBar
        :param happiness: as StatusBar
        :param hunger: as StatusBar
        :param is_sick: as boolean
        :param is_alive: as boolean
        :param timestamp: as datetime
        """
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
                 health=StatusBar(-3),
                 happiness=StatusBar(-2),
                 hunger=StatusBar(3, 0),
                 is_sick=False,
                 is_alive=True,
                 timestamp=datetime.now()):
        """
        Initialiser for Crobat
        :param name: as String
        :param species: as String
        :param food_likes: as String tuple
        :param food_dislikes: as String tuple
        :param moods: as dictionary
        :param health: as StatusBar
        :param happiness: as StatusBar
        :param hunger: as StatusBar
        :param is_sick: as boolean
        :param is_alive: as boolean
        :param timestamp: as datetime
        """
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
                 health=StatusBar(-1),
                 happiness=StatusBar(-3),
                 hunger=StatusBar(2, 0),
                 is_sick=False,
                 is_alive=True,
                 timestamp=datetime.now()):
        """
        Initialiser for Scorbunny
        :param name: as String
        :param species: as String
        :param food_likes: as String tuple
        :param food_dislikes: as String tuple
        :param moods: as dictionary
        :param health: as StatusBar
        :param happiness: as StatusBar
        :param hunger: as StatusBar
        :param is_sick: as boolean
        :param is_alive: as boolean
        :param timestamp: as datetime
        """
        super().__init__(name, species, food_likes, food_dislikes,
                         moods, health, happiness, hunger, is_sick,
                         is_alive, timestamp)
        self._species = species

class PokemonCreator:
    """
    Create a random Pokemon.
    """
    @classmethod
    def hatch_pet(cls):
        """
        Hatch a random, pre-defined Pokemon type.
        :return: as Pokemon
        """
        pets = {1: Scorbunny,
                2: Crobat,
                3: Sirfetchd}
        name = input("\nGive a name to your Pokemon: ")

        type_of_pokemon = pets.get(random.choice(list(pets)))
        pet = type_of_pokemon(name)

        return pet


class PokemonController:
    """
    Controller for hatched Pokemon.  Only one instance per game.
    """

    _pet = None

    @classmethod
    def set_pet(cls, pet):
        """
        Set Pokemon as provided param.
        :param pet: Pokemon
        :return: None
        """
        cls._pet = pet
    #
    # @classmethod
    # def get_name(cls):
    #     """
    #     Get user-defined Pokemon name.
    #     :return: as String
    #     """
    #     return cls._pet.get_name()

    @classmethod
    def check_status(cls):
        """
        Update pet's stats
        :return: as String
        """
        cls.change_bar(cls._pet._health)
        cls.change_bar(cls._pet._happiness)
        cls.change_bar(cls._pet._hunger)
        # Update pet timestamp after calculating StatusBars
        cls._pet._timestamp = datetime.now()
        if cls._pet._health.curr_value > 0:
            return f"\n{cls._pet}"
        else:
            cls._pet._is_alive = False
            return ""

    @classmethod
    def change_bar(cls, bar):
        curr_time = datetime.now()
        diff = abs(curr_time - cls._pet._timestamp)
        decrement = bar.rate * diff.total_seconds()
        bar.curr_value += int(decrement)

    @classmethod
    def change_like_hunger(cls, food):
        val = food._value * food._like_multiplier
        cls._pet._hunger.curr_value += int(val)

    @classmethod
    def change_basic_hunger(cls, food):

        cls._pet._hunger.curr_value += int(food._value)

    @classmethod
    def give_consumable(cls):
        print("\nGive consumable\n")


def main():
    scorbunny = Scorbunny("Bun bun")
    crobat = Crobat("Batty")
    sirfetchd = Sirfetchd("Ducky")
    print(crobat)
    print(sirfetchd)

if __name__ == "__main__":
    main()