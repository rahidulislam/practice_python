class Car:
    def __init__(self, name, model):
        self.name = name
        self.model_of_year = model
        self.wheel = 4

    def view(self):
        print("The model is", self.model_of_year)
        print("It is a ", self.wheel, "car")


# -----------------------------------------------
# object create
c1 = Car("BMW", 2016)
c2 = Car("Audi", 2018)
c1.view()
c2.view()
