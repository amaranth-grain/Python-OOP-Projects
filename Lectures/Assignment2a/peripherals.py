from abc import ABC


class Consumable(ABC):
    def __init__(self, name, value):
        self._name = name
        self._value = value


class Food(Consumable):
    def __init__(self, name, value=-40, like_multiplier=1.1):
        super().__init__(name, value)
        self._like_multiplier = like_multiplier

    def get_name(self):
        return self._name


class Medicine(Consumable):
    def __init__(self, name="Cold Medicine", value="100"):
        super().__init__(name, value)


class StatusBar():
    """
    Represent a Pokemon status with ongoing changing values.
    """
    def __init__(self, rate=-1.0, curr=100, max=100,
                 multiplier=1.0):
        self.rate = rate
        self.curr = int(curr)
        self.max = max
        self.multiplier = multiplier

class Catalogue:
    """
    Store catalogue of information used in Tamagotchi simulation.
    """

    start_menu = {1: "Hatch your Pokemon",
                  2: "Quit game"}

    pet_menu = {1: "Check the status of your Pokemon",
                2: "Give your Pokemon an item",
                3: "Play a game with your Pokemon",
                4: "Quit game"}

    minigame_menu = {1: "Guess that Pokemon!",
                     2: "Water, Fire, Grass",
                     3: "Whack-a-Drilbur"}

    items_menu = {1: "Food",
                  2: "Medicine",
                  3: "Back"}

    food_items = {1: Food("Bloody Mary Drink"),
                  2: Food("Buttered Leeks"),
                  3: Food("Carrot Cake Slice"),
                  4: Food("Duck a l\'Orange"),
                  5: Food("Garlic Chicken"),
                  6: Food("Leek and Potato Cake"),
                  7: Food("Pig Blood Curd"),
                  8: Food("Rabbit Cacciatore"),
                  9: Food("Red Velvet Cake"),
                  10: Food("Spaghetti Bolognese"),
                  11: Food("Szechuan Carrots"),
                  12: Food("Spring Onion Oil Noodles")}

    """
    Information on Scorbunny
    """
    scorbunny_likes = ('Spicy Szechuan Carrots', 'Carrot Cake Slice',
                       'Spaghetti Bolognese', 'Red Velvet Cake')

    scorbunny_dislikes = (
        'Bloody Mary Drink', 'Pig Blood Curd', 'Rabbit Cacciatore')

    scorbunny_moods = {"sick": "sick\n／(˃ᆺ˂)＼",
                       "happy": "happy\n／(^ᆺ^)＼ ~♡",
                       "frustrated": "frustrated\n／(≧ x ≦)＼",
                       "neutral": "neutral\n／(･ᆺ･)＼",
                       "angry": "angry\n／(＞×＜#)＼"}
    """
    Information on Crobat
    """
    crobat_likes = ('Bloody Mary Drink', 'Pig Blood Curd',
                    'Rabbit Cacciatore')

    crobat_dislikes = ('Carrot Cake Slice', 'Leek and Potato Cake',
                       'Buttered Leeks', 'Garlic Chicken')

    crobat_moods = {"sick": "sick\n/|\(＋_＋)/|\\",
                    "happy": "happy\n/|\(≧◡≦)/|\\ ~♡",
                    "frustrated": "frustrated\n/|\( ;,;)/|\\",
                    "neutral": "neutral\n/|\(￣～￣)/|\\",
                    "angry": "angry\n/|\(╬◣﹏◢)/|\\"}

    """
    Information on Sirfetchd
    """
    sirfetchd_likes = ('Leek and Potato Cake', 'Buttered Leeks',
                       'Spring Onion Oil Noodles')

    sirfetchd_dislikes = ('Pig Blood Curd', 'Rabbit Cacciatore',
                          'Garlic Chicken', 'Duck a l\'Orange')

    sirfetchd_moods = {"sick": "sick\n⋛⋋( ‘Θ’)⋌⋚",
                       "happy": "happy\n♡~ ♩є(･Θ･｡)э",
                       "frustrated": "frustrated\n(⊙ө⊙)",
                       "neutral": "neutral\n( ˘⊖˘)",
                       "angry": "angry\n(｀Θ´)"}

    @classmethod
    def str_preferences(cls, menu):
        output = ""
        for item in menu:
            output += f"* {item} \n"
        return output

    @classmethod
    def print_menu(cls, menu):
        output = ""
        for k, v in menu.items():
            output += f"{k}. {v}\n"
        print(output)

    @classmethod
    def print_food(cls):
        output = ""
        count = 1
        for k, v in cls.food_items.items():
            output += f"{k}. {v.get_name()}\t\t"
            if count % 6 == 0:
                output += "\n"
            count += 1
        print(f"{output}\n")