class Engine:
    def __init__(self,horsepower):
        self.horsepower = horsepower

    def start(self):
        return"Engine started"

class Car:
    def __init__(self,model,horsepower):
        self.model = model
        self.engine = Engine(horsepower)

    def start_car(self):
        return f"{self.model} is starting: {self.engine.start()}"
car1=Car("Toyota",150)
print(car1.start_car())