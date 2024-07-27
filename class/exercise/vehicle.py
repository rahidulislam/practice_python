class Vehicle:
    """
    Exercise 2: Inheritance and Polymorphism

    Task: Create a base class Vehicle with the following:

        Attributes:
            make (string)
            model (string)
            year (integer)

        Methods:
            __init__(self, make, model, year): Initializes the attributes.
            info(self): Returns a string describing the vehicle.

    Then, create a subclass Car that inherits from Vehicle and adds:

        Attributes:
            number_of_doors (integer)

        Methods:
            __init__(self, make, model, year, number_of_doors): Initializes the attributes including those from the parent class.
            Override the info(self) method to include the number of doors in the description.

    Challenge: Create an instance of the Car class and print its information using the info method.ummary_
    """

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        print(self.make, self.model, self.year)


class Car(Vehicle):
    def __init__(self, make, model, year, number_of_door):
        super().__init__(make, model, year)
        self.number_of_door = number_of_door

    def info(self):
        print(self.make, self.model, self.year, self.number_of_door)


# =====================================================================

car = Car("honda", "civic", 2019, 4)
car.info()
