from item import Item

class Journal(Item):
    # def __init__(self, title, call_no, author, num_copies):
    # def __init__(self, name="Blurgo", lives=2, health=110, weapon="Club"):
    #     self._weapon = weapon
    #     super().__init__(name, lives, health)
    def __init__(self, title, call_no, author, num_copies, name,
                 issue, publisher):
        self._name = name
        self._issue = issue
        self._publisher = publisher
        super().__init__(title, call_no, author, num_copies)



