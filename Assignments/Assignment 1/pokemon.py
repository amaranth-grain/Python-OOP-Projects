from abc import ABC
from datetime import datetime



class Pokemon(ABC):
    def __init__(self, health, happiness, hunger,
                 is_sick, timestamp, food_likes,
                 food_dislikes, pet_msgs):
        self._health = health
        self._happiness = happiness
        self._hunger = hunger
        self._is_sick = is_sick
        self._timestamp = timestamp
        self._food_likes = food_likes
        self._food_dislikes = food_dislikes
        self._pet_msgs = pet_msgs


class StatusBar():
    def __init__(self, max_value, rate, multiplier):
        self._max_value = max_value
        self._rate = rate
        self._multiplier = multiplier


class PokemonController:

    @staticmethod
    def hatch_pet():
        print("\nYour Pokémon has hatched!\n")

    @staticmethod
    def give_consumable():
        print("\nGive consumable\n")

    @staticmethod
    def check_status():
        print("\nCheck pet status\n")