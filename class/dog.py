class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def update_color(self, color):
        self.color = color

    def poke(self):
        print(self.color, self.name, "is smiling")


# ----------------------------------------------------
# object creation
d1 = Dog("Rover", "Brown")
d2 = Dog("Tomy", "White")
d1.poke()
d1.update_color("Black")
d1.poke()
print(d1.__dict__)  # represent as a dictionary of an object
# shows all built-in attributes and methods which will be available for this object including object's own attribute
# and methods
print(dir(d1))
