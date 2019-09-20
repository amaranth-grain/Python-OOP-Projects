from item import Item

class Dvd(Item):
    
    def __init__(self, title, call_no, author, num_copies, release,
                 region)
        self._release = release
        self._region = region
        super().__init__(title, call_no, author, num_copies)