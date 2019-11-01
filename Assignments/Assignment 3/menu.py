class Menu:
    start_menu = {
        1: "Build your own pizza",
        2: "Quit"
    }

    cheese_menu = {
        1: "Parmigiano Reggiano",
        2: "Fresh Mozzarella",
        3: "Daiya Cheese",
        4: "Check out",
        5: "Quit"
    }

    toppings_menu = {
        1: "Peppers",
        2: "Pineapple",
        3: "Mushrooms",
        4: "Fresh Basil",
        5: "Spinach",
        6: "Pepperoni",
        7: "Beyond Meat",
        8: "Add more cheese",
        9: "Check out",
        10: "Quit"

    }

    @staticmethod
    def print_menu(menu):
        output = ""
        for num, item in menu.items():
            output += f"{num}. {item}\n"
        print(output)