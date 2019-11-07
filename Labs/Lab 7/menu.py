class Menu:

    item_type = {
        1: "Book",
        2: "DVD",
        3: "Journal"
    }

    start_menu = {
        1: "Find book by title",
        2: "Add book to collection",
        3: "Remove book from collection",
        4: "Check out a copy",
        5: "Return your copy",
        6: "Display all available books",
        7: "Quit Menu"
    }

    @staticmethod
    def print(menu) -> None:
        """
        Helper method.
        :param menu: Menu dictionary
        :return: None
        """
        output = ""
        for k, v in menu.items():
            output += f"{k}. {v}\n"
        print(output)

    @staticmethod
    def get_user_choice(menu) -> int:
        Menu.print(menu)
        try:
            user_input = int(input("Enter menu choice: "))
            if user_input not in range(1, len(menu) + 1):
                raise ValueError("Enter valid integer.")
        except ValueError as e:
            print(f"Exception: {e}")
        else:
            return user_input