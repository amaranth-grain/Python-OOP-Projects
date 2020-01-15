"""
Quick 2-hour fun project to see which meme reigns supreme, tournament style.
"""

from random import uniform
from random import randint
from random import choice
from time import sleep


class Meme:
    """
    Represent an internet Meme that will duke it out with fellow memes in a
    tournament.
    """

    names = ["Very Doge", "Woman Yelling at Cat", "Distracted Boyfriend",
             "Surprised Pikachu", "Left Exit 12 Off Ramp", "Taps Forehead",
             "Big Brain", "One Does Not Simply", "You Get a Car", "Why You No"]

    def __init__(self, name="Janet"):
        """
        Represent a Meme that engages in battle
        :param health: float
        :param strength: int
        :param name: str
        """
        self._max_health = randint(20, 30)
        self._health = self._max_health
        self._meme_power = randint(1, 15)
        self._name = name
        self._dodge_chance = uniform(0, 1)
        self._critical_chance = uniform(0, 1)

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def is_alive(self):
        return self._health > 0

    def reset(self):
        """
        Reset Meme's health to maximum health after a tournament battle ends.
        :return: None
        """
        self._health = self._max_health

    def attack(self):
        """
        Represent Meme's attack.  Damage dealt is
        dependent on critical chance.
        :return: Damage dealt (int)
        """
        if uniform(0, 1) < self._critical_chance:
            damage = self._meme_power * 2
            print("-" * 60)
            print("Critical hit!")
            print(f"{self._name} deals {damage} damage!")
            return damage
        else:
            damage = self._meme_power
            print("-" * 60)
            print(f"{self._name} deals {damage} damage!")
            return damage

    def take_damage(self, damage):
        """
        Represent Meme receiving an attack.  Damage
        dealt is dependent on dodge chance.
        :param damage: int
        :return: bool
        """
        if uniform(0, 1) >= self._dodge_chance:
            if self._health <= damage:
                self._health = 0
            else:
                self._health -= damage

            print(f"{self._name} takes a hit! {self._name} has "
                  f"{self._health} remaining.")
            return True
        else:
            print(f"{self._name} dodges the hit!")
            return False

    @classmethod
    def generate_rand_character(cls):
        """
        Generate random tournament Meme participant.
        :return: Meme
        """
        name = choice(Meme.names)
        Meme.names.remove(name)
        return Meme(name)

    def __str__(self):
        """
        String representation of meme.
        :return:
        """
        dodge = "{0:.2f}".format(self._dodge_chance * 100)
        crit = "{0:.2f}".format(self._critical_chance * 100)
        return f"Name: {self._name}\n" \
               f"Health: {self._health}/{self._max_health}\n" \
               f"Strength: {self._meme_power}\n" \
               f"Dodge %: {dodge}%\n" \
               f"Crit %: {crit}%\n"


class BattleSimulator:
    """
    Simulate a battle between two Memes... to the death!
    """
    def __init__(self, character1, character2):
        """
        Initialise BattleSimulator with two Memes
        :param character1: Meme
        :param character2: Meme
        """
        self._character1 = character1
        self._character2 = character2

    def simulate(self):
        """
        While both characters are still alive, attack, dodge, and deal
        crits until death.
        :return: Winning character (Meme)
        """
        while self._character1.is_alive and self._character2.is_alive:
            if randint(0, 1):
                damage = self._character1.attack()
                self._character2.take_damage(damage)
            else:
                damage = self._character2.attack()
                self._character1.take_damage(damage)

            sleep(0.5)

        return self._character1 if self._character1.is_alive else \
            self._character2


class Driver:
    """
    Drive the program by setting up participants and BattleSimulators.
    """

    def __init__(self):
        """
        Initialise Driver with an empty list of participants.
        """
        self._participants = []

    def generate_participants(self):
        """
        Generate the eight participants in the tournament.
        :return: None
        """
        for n in range(8):
            self._participants.append(Meme.generate_rand_character())

    def select_participant(self):
        """
        Select the participant for the current battle.
        :return: Meme
        """
        character = choice(self._participants)
        self._participants.remove(character)
        return character

    def start(self):
        """
        Start the simulated tournament.
        :return: None
        """
        self.generate_participants()
        winner = None

        for i in range(7):
            c1 = self.select_participant()
            c2 = self.select_participant()
            sim = BattleSimulator(c1, c2)
            winner = sim.simulate()
            winner.reset()
            self._participants.append(winner)

        print("=" * 60)
        print(f"The winner of this tournament is {winner.name}!")
        print("-" * 60)
        print(winner)


def main():
    driver = Driver()
    driver.start()


if __name__ == "__main__":
    main()
