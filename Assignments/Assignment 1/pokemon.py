from abc import ABC
import random
from datetime import datetime


class StatusBar():
    def __init__(self, rate=1.0, curr_value=100, max_value=100,
                 multiplier=1.0):
        self.rate = rate
        self.curr_value = curr_value
        self.max_value = max_value
        self.multiplier = multiplier


class Pokemon(ABC):
    def __init__(self, name, food_likes, food_dislikes, moods,
                 health=StatusBar(),
                 happiness=StatusBar(),
                 hunger=StatusBar(),
                 is_sick=False,
                 is_alive=True,
                 timestamp=datetime.now()):
        self._name = name
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
        feel = "Healthy" if self._is_sick else "Sick"
        print(f"=== {name}'s Stats ===\n"
              f"Health rate: {self._health.rate}\n"
              f"Health: {self._health.max_value}"
              f"Happiness: {self._happiness.rate}\n"
              f"Hunger: {self._hunger.rate}\n"
              f"Feeling: {feel}"
              f"Food likes: {self._food_likes}\n"
              f"Food dislikes: {self._food_dislikes}\n")


class Scorbunny(Pokemon):
    likes = ['Spicy Szechuan Carrots',
             'Carrot Cake',
             'Spaghetti Bolognese',
             'Red Velvet Cake']

    dislikes = ['Bloody Mary',
                'Pig Blood Curd',
                'Rabbit Cacciatore']

    moods = {"sick": "／(˃ᆺ˂)＼",
             "happy": "／(^ᆺ^)＼ ~♡",
             "frustrated": "／(≧ x ≦)＼",
             "neutral": "／(･ᆺ･)＼",
             "angry": "／(＞×＜#)＼"}

    def __init__(self, name,
                 food_likes=likes,
                 food_dislikes=dislikes,
                 moods=moods,
                 health=StatusBar(),
                 happiness=StatusBar(),
                 hunger=StatusBar(),
                 is_sick=False,
                 is_alive=True,
                 timestamp=datetime.now()):
        self._name = name
        self._food_likes = food_likes
        self._food_dislikes = food_dislikes
        self._moods = moods
        super().__init__(health, happiness, hunger,
                         is_sick, is_alive, timestamp)


class Crobat(Pokemon):
    likes = ('Bloody Mary',
             'Pig Blood Curd',
             'Rabbit Cacciatore')

    dislikes = ('Carrot Cake',
                'Leek and Potato Cake',
                'Buttered Leeks',
                'Garlic Chicken')

    moods = {"sick": "/|\(＋_＋)/|\\",
             "happy": "/|\(≧◡≦)/|\\ ~♡",
             "frustrated": "/|\( ;,;)/|\\",
             "neutral": "/|\(￣～￣)/|\\",
             "angry": "/|\(╬◣﹏◢)/|\\"}

    def __init__(self, name,
                 food_likes=likes,
                 food_dislikes=dislikes,
                 moods=moods,
                 health=StatusBar(),
                 happiness=StatusBar(),
                 hunger=StatusBar(),
                 is_sick=False,
                 is_alive=True,
                 timestamp=datetime.now()):
        self._name = name
        self._food_likes = food_likes
        self._food_dislikes = food_dislikes
        self._moods = moods
        super().__init__(health, happiness, hunger,
                         is_sick, is_alive, timestamp)


class Sirfetchd(Pokemon):
    likes = ('Leek and Potato Cake',
             'Buttered Leeks',
             'Spring Onion Oil Noodles')

    dislikes = ('Pig Blood Curd',
                'Rabbit Cacciatore'
                'Garlic Chicken',
                'Duck a l\'Orange')

    moods = {"sick": "/|\(＋_＋)/|\\",
             "happy": "/|\(≧◡≦)/|\\ ~♡",
             "frustrated": "/|\( ;,;)/|\\",
             "neutral": "/|\(￣～￣)/|\\",
             "angry": "/|\(╬◣﹏◢)/|\\"}

    def __init__(self, name,
                 food_likes=likes,
                 food_dislikes=dislikes,
                 moods=moods,
                 health=StatusBar(),
                 happiness=StatusBar(),
                 hunger=StatusBar(),
                 is_sick=False,
                 is_alive=True,
                 timestamp=datetime.now()):
        self._name = name
        self._food_likes = food_likes
        self._food_dislikes = food_dislikes
        self._moods = moods
        super().__init__(health, happiness, hunger,
                         is_sick, is_alive, timestamp)


class PokemonCreator:
    @staticmethod
    def hatch_pet():
        pets = {1: Scorbunny,
                2: Crobat,
                3: Sirfetchd}
        name = input("\nGive a name to your Pokemon: ")

        type_of_pokemon = pets.get(random.choice(list(pets)))
        pet = type_of_pokemon(name,
                              ["Poutine", "Marutama ramen"],
                              ["Durian", "Hawaiian Pizza"],
                              ["Feeling uwu", "Feeling pissed"])
        PokemonController(pet)


class PokemonController:
    def __init__(self, pet):
        self._pet = pet
        print(f"\n{self.get_name()} is in PetController\n")

    def get_name(self):
        return self._pet.get_name()

    @staticmethod
    def give_consumable():
        print("\nGive consumable\n")

    @staticmethod
    def check_status():
        print("\nCheck pet status\n")
