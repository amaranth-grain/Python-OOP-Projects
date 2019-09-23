from abc import ABC


class Consumable(ABC):
    def __init__(self, name, value):
        self._name = name
        self._value = value


class Food(Consumable):
    def __init__(self, name, value=-30, like_multiplier=1.1):
        super().__init__(name, value)
        self._like_multiplier = like_multiplier

    def get_name(self):
        return self._name


class Medicine(Consumable):
    def __init__(self, name="Cold Medicine", value="100"):
        super().__init__(name, value)


class Catalogue:

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

    @classmethod
    def get_food_items(cls):
        string = ""
        count = 1
        for k, v in cls.food_items.items():
            string += f"{k}. {v._name}\t\t"
            if count % 6 == 0:
                string +="\n"
            count += 1
        return string


def main():
    food = Food("Bloody Mary Drink")
    print(food._name)
    print(food._value)


if __name__ == "__main__":
    main()