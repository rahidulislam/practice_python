class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current
    
    def reset(self):
        self.__current = 0

counter = Counter()
counter.increment()
counter.increment()
counter.current = -999
counter.increment()
print(counter.value())
print(counter.__dict__)
print(counter._Counter__current)

class Car:
    def __init__(self,make,model,year):
        self.__make = make
        self.__model = model
        self.__year = year

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year
    
    def set_make(self,make):
        self.__make = make

    def set_model(self,model):
        self.__model = model

    def set_year(self,year):
        self.__year = year

car1=Car("Toyota","Corolla",2022)
print(car1.get_make())
print(car1.get_model())
print(car1.get_year())

car1.set_make("Tesla")
car1.set_model("Model S")
car1.set_year(2023)

print(car1.get_make())
print(car1.get_model())
print(car1.get_year())