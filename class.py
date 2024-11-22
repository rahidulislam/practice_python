class Anyone:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def display(self):
        print(f" Hello {self.firstname}, {self.lastname}")

class Player(Anyone):
    pass

p1 = Player("Rahidul", "Islam")
p1.display()