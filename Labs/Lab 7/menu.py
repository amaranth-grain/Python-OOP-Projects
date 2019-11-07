class Menu:

    item_type = {
        1: "Book",
        2: "DVD",
        3: "Journal"
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