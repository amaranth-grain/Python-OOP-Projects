import random
from abc import ABC
from datetime import datetime
from peripherals import StatusBar
from peripherals import Catalogue


class Pokemon(ABC):
    """
    Skeleton for individual subclass Pokemon species.
    """

    def __init__(self, name):
        self.name = name
        self.timestamp = datetime.now()
        self.species = None
        self.game_happiness = None
        self.health = None
        self.happiness = None
        self.hunger = None
        self.sick_threshold = None
        self.is_sick = False

    def __str__(self):
        """
        Format string for displaying Pokemon status.
        :return: as String
        """
        feel = "Sick" if self.is_sick else "Healthy"
        kaomoji = self.moods.get(random.choice(list(self.moods)))

        return f"== {self.name} the {self.species}'s Stats ===\n" \
               f"Health rate: \t {self.health.rate} / s\n" \
               f"Happiness rate: {self.happiness.rate} / s \n" \
               f"Hunger rate: \t {self.hunger.rate} / s \n" \
               f"Health: \t\t {self.health.curr} / " \
               f"{self.health.max}\n" \
               f"Happiness: \t\t " \
               f"{self.happiness.curr} / {self.happiness.max} \n" \
               f"Hunger: \t\t {self.hunger.curr} / {self.hunger.max}" \
               f"\n" \
               f"Feeling: \t\t{feel}\n" \
               f"Mood: \n" \
               f"I'm feeling " \
               f"{kaomoji}\n\n"


class Scorbunny(Pokemon):
    """
    All Scorbunnies have the same traits.
    To add variance, set class variables with a range using
    random.randint() instead of specific values.
    """
    GAME_HAPPINESS = 50
    HEALTH_RATE = -1
    HAPPINESS_RATE = -1.5
    HUNGER_RATE = 2.1
    HUNGER_START_VAL = 0
    SICK_THRESHOLD = 85

    def __init__(self, name):
        super().__init__(name)
        self.species = "Scorbunny"
        self.game_happiness = Scorbunny.GAME_HAPPINESS
        self.health = StatusBar(Scorbunny.HEALTH_RATE)
        self.happiness = StatusBar(Scorbunny.HAPPINESS_RATE)
        self.hunger = StatusBar(Scorbunny.HUNGER_RATE,
                                Scorbunny.HUNGER_START_VAL)
        self.sick_threshold = Scorbunny.SICK_THRESHOLD
        self.is_sick = False
        self.food_likes = Catalogue.scorbunny_likes
        self.food_dislikes = Catalogue.scorbunny_dislikes
        self.moods = Catalogue.scorbunny_moods

    def __str__(self):
        """
        Format string for displaying Pokemon status.
        :return: as String
        """
        return f"{super().__str__()}\n" \
               f"=== Food Likes ===\n" \
               f"{Catalogue.str_preferences(self.food_likes)} \n" \
               f"== Food Disikes ===\n" \
               f"{Catalogue.str_preferences(self.food_dislikes)} \n"


class Crobat(Pokemon):
    """
    All Crobats have the same traits.
    To add variance, set class variables with a range using
    random.randint() instead of specific values.
    """
    GAME_HAPPINESS = 60
    HEALTH_RATE = -1.1
    HAPPINESS_RATE = -1.2
    HUNGER_RATE = 1.3
    HUNGER_START_VAL = 0
    SICK_THRESHOLD = 78

    def __init__(self, name):
        super().__init__(name)
        self.species = "Crobat"
        self.game_happiness = Crobat.GAME_HAPPINESS
        self.health = StatusBar(Crobat.HEALTH_RATE)
        self.happiness = StatusBar(Crobat.HAPPINESS_RATE)
        self.hunger = StatusBar(Crobat.HUNGER_RATE,
                                Crobat.HUNGER_START_VAL)
        self.sick_threshold = Crobat.SICK_THRESHOLD
        self.is_sick = False
        self.food_likes = Catalogue.crobat_likes
        self.food_dislikes = Catalogue.crobat_dislikes
        self.moods = Catalogue.crobat_moods

    def __str__(self):
        """
        Format string for displaying Pokemon status.
        :return: as String
        """
        return f"{super().__str__()}" \
               f"=== Food Likes ===\n" \
               f"{Catalogue.str_preferences(self.food_likes)} " \
               f"\n" \
               f"== Food Disikes ===\n" \
               f"{Catalogue.str_preferences(self.food_dislikes)} " \
               f"\n"


class Sirfetchd(Pokemon):
    """
    All Sirfetchd have the same traits.
    To add variance, set class variables with a range using
    random.randint() instead of specific values.
    """
    GAME_HAPPINESS = 62
    HEALTH_RATE = -1.2
    HAPPINESS_RATE = -1.3
    HUNGER_RATE = 1.4
    HUNGER_START_VAL = 0
    SICK_THRESHOLD = 76

    def __init__(self, name):
        super().__init__(name)
        self.species = "Sirfetchd"
        self.game_happiness = Sirfetchd.GAME_HAPPINESS
        self.health = StatusBar(Sirfetchd.HEALTH_RATE)
        self.happiness = StatusBar(Sirfetchd.HAPPINESS_RATE)
        self.hunger = StatusBar(Sirfetchd.HUNGER_RATE,
                                Sirfetchd.HUNGER_START_VAL)
        self.sick_threshold = Sirfetchd.SICK_THRESHOLD
        self.is_sick = False
        self.food_likes = Catalogue.sirfetchd_likes
        self.food_dislikes = Catalogue.sirfetchd_dislikes
        self.moods = Catalogue.sirfetchd_moods

    def __str__(self):
        """
        Format string for displaying Pokemon status.
        :return: as String
        """
        return f"{super().__str__()}" \
               f"=== Food Likes ===\n" \
               f"{Catalogue.str_preferences(self.food_likes)} " \
               f"\n" \
               f"== Food Disikes ===\n" \
               f"{Catalogue.str_preferences(self.food_dislikes)} " \
               f"\n"


class PokemonCreator:
    """
    Create a new Pokemon object randomly based on class variable pets.
    """
    pets = {1: Scorbunny,
            2: Crobat,
            3: Sirfetchd}

    @classmethod
    def hatch_pet(cls):
        """
        Hatch a random, pre-defined Pokemon type.
        :return: as Pokemon
        """
        name = input("\nGive a name to your Pokemon: ")
        pokemon = cls.pets.get(random.choice(list(cls.pets)))
        pet = pokemon(name)

        return pet


def main():
    duck = Sirfetchd("Ducky")
    print(duck)


if __name__ == "__main__":
    main()
