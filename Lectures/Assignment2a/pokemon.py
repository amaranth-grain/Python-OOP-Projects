import random
from abc import ABC
from datetime import datetime
from peripherals import StatusBar
from peripherals import Catalogue


class Pokemon(ABC):

    def __init__(self, name, species, health, happiness, hunger):
        self._name = name
        self._species = species
        self._health = health
        self._happiness = happiness
        self._hunger = hunger
        self._is_alive = True
        self._is_sick = False
        self._timestamp = datetime.now()

    @property
    def name(self):
        return self._name

    @property
    def species(self):
        return self._species

    @property
    def health(self):
        return self._health

    @property
    def happiness(self):
        return self._happiness

    @property
    def hunger(self):
        return self._hunger

    def die(self):
        self._is_alive = False

    def __str__(self):
        """
        Format string for displaying Pokemon status.
        :return: as String
        """
        feel = "Sick" if self._is_sick else "Healthy"
        kaomoji = self._moods.get(random.choice(list(self._moods)))

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
    def __init__(self, name,
                 species="Scorbunny",
                 health=StatusBar(-1),
                 happiness=StatusBar(-1.5),
                 hunger=StatusBar(2.1, 0),
                 food_likes=Catalogue.scorbunny_likes,
                 food_dislikes=Catalogue.scorbunny_dislikes,
                 moods=Catalogue.scorbunny_moods):
        super().__init__(name, species, health, happiness, hunger)
        self._species = species
        self._health = health
        self._happiness = happiness
        self._hunger = hunger
        self._food_likes = food_likes
        self._food_dislikes = food_dislikes
        self._moods = moods

    def __str__(self):
        """
        Format string for displaying Pokemon status.
        :return: as String
        """
        feel = "Sick" if self._is_sick else "Healthy"

        return f"{super().__str__()}" \
               f"=== Food Likes ===\n" \
               f"{Catalogue.str_preferences(Catalogue.scorbunny_likes)} \n" \
               f"== Food Disikes ===\n" \
               f"{Catalogue.str_preferences(Catalogue.scorbunny_dislikes)} \n" \
               f"Timestamp: {self._timestamp}\n"


class Crobat(Pokemon):
    def __init__(self, name,
                 species="Crobat",
                 health=StatusBar(-1.8),
                 happiness=StatusBar(-1.2),
                 hunger=StatusBar(1.5, 0),
                 food_likes=Catalogue.crobat_likes,
                 food_dislikes=Catalogue.crobat_dislikes,
                 moods=Catalogue.crobat_moods):
        super().__init__(name, species, health, happiness, hunger)
        self._species = species
        self._health = health
        self._happiness = happiness
        self._hunger = hunger
        self._food_likes = food_likes
        self._food_dislikes = food_dislikes
        self._moods = moods

    def __str__(self):
        """
        Format string for displaying Pokemon status.
        :return: as String
        """
        feel = "Sick" if self._is_sick else "Healthy"

        return f"{super().__str__()}" \
               f"=== Food Likes ===\n" \
               f"{Catalogue.str_preferences(Catalogue.crobat_likes)} " \
               f"\n" \
               f"== Food Disikes ===\n" \
               f"{Catalogue.str_preferences(Catalogue.crobat_likes)} " \
               f"\n" \
               f"Timestamp: {self._timestamp}\n"


class Sirfetchd(Pokemon):
    def __init__(self, name,
                 species="Sirfetchd",
                 health=StatusBar(-0.8),
                 happiness=StatusBar(-1.7),
                 hunger=StatusBar(1.1, 0),
                 food_likes=Catalogue.sirfetchd_likes,
                 food_dislikes=Catalogue.sirfetchd_dislikes,
                 moods=Catalogue.sirfetchd_moods):
        super().__init__(name, species, health, happiness, hunger)
        self._species = species
        self._health = health
        self._happiness = happiness
        self._hunger = hunger
        self._food_likes = food_likes
        self._food_dislikes = food_dislikes
        self._moods = moods

    def __str__(self):
        """
        Format string for displaying Pokemon status.
        :return: as String
        """
        feel = "Sick" if self._is_sick else "Healthy"

        return f"{super().__str__()}" \
               f"=== Food Likes ===\n" \
               f"{Catalogue.str_preferences(Catalogue.sirfetchd_likes)} " \
               f"\n" \
               f"== Food Disikes ===\n" \
               f"{Catalogue.str_preferences(Catalogue.sirfetchd_likes)} " \
               f"\n" \
               f"Timestamp: {self._timestamp}\n"


class PokemonCreator:
    pets = {1: Scorbunny,
            2: Crobat,
            3: Sirfetchd}

    """
    Create a random Pokemon.
    """

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
    # bun = Scorbunny("Bunny")
    # print(bun)

    # bat = Crobat("Batty")
    # print(bat)

    duck = Sirfetchd("Ducky")
    print(duck)


if __name__ == "__main__":
    main()
