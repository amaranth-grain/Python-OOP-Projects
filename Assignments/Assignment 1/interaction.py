class Catalogue:
    food_items = {1: "Bloody Mary",
                  2: "Buttered Leeks",
                  3: "Carrot cake",
                  4: "Duck a l\'Orange",
                  5: "Garlic Chicken",
                  6: "Leek and Potato Cake",
                  7: "Pig Blood Curd",
                  8: "Rabbit Cacciatore",
                  9: "Red Velvet Cake",
                  10: "Spaghetti Bolognese",
                  11: "Spicy Szechuan Carrots",
                  12: "Spring Onion Oil Noodles"}

    @classmethod
    def get_food_items(cls):
        string = ""
        for k, v in cls.food_items.items():
            string += f"{k}. {v}\n"
        return string
