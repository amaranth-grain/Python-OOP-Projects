import pizza

class Menu:
    start_menu = {
        1: "Build your own pizza",
        2: "Quit"
    }

    # cheese_menu = {
    #     1: "Parmigiano Reggiano",
    #     2: "Fresh Mozzarella",
    #     3: "Daiya Cheese",
    #     4: "Add other toppings",
    #     5: "Check out",
    #     6: "Quit"
    # }

    cheese_menu = {
        1: pizza.Ingredient("Parmigiano Reggiano", 4.99),
        2: pizza.Ingredient("Fresh Mozzarella", 3.99),
        3: pizza.Ingredient("Vegan Cheese", 5.99),
        4: "Add other toppings",
        5: "Check out",
        6: "Quit"
    }

    cheese_dec = {
        1: pizza.ParmigianoPizzaDecorator,
        2: pizza.MozzarellaPizzaDecorator,
        3: pizza.VeganPizzaDecorator
    }

    toppings_menu = {
        1: pizza.Ingredient("Peppers", 1.5),
        2: pizza.Ingredient("Pineapple", 2),
        3: pizza.Ingredient("Mushrooms", 1.5),
        4: pizza.Ingredient("Fresh Basil", 2),
        5: pizza.Ingredient("Spinach", 1),
        6: pizza.Ingredient("Pepperoni", 3),
        7: pizza.Ingredient("Beyond Meat", 4),
        8: "Add more cheese",
        9: "Check out",
        10: "Quit"
    }

    toppings_dec = {
        1: pizza.PeppersPizzaDecorator,
        2: pizza.PineapplePizzaDecorator,
        3: pizza.MushroomPizzaDecorator,
        4: pizza.BasilPizzaDecorator,
        5: pizza.SpinachPizzaDecorator,
        6: pizza.PepperoniPizzaDecorator,
        7: pizza.BeyondPizzaDecorator
    }

    @staticmethod
    def print(menu):
        output = ""
        for num, item in menu.items():
            output += f"{num}. {item}\n"
        print(output)