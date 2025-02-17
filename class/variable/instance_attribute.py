class Car:
    def __init__(self,brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color

car1 = Car("Toyota", "Corolla", "Red")
car2 = Car("Tesla", "Model S", "Black")

print(car1.brand)
print(car1.model)
print(car1.color)

print(car2.brand)
print(car2.model)
print(car2.color)