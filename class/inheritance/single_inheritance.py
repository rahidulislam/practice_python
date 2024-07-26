class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):
    def bark(self):
        print(self.name, "is barking")


# ==========================================
a1 = Animal("jack")
d1 = Dog("Rover")
d1.bark()
d1.eat()
a1.eat()
# check isinstance
print(isinstance(d1,Animal))
print((isinstance(d1,Dog)))
print(isinstance(a1,Animal))
print(isinstance(a1,Dog))
# check subclass
print(issubclass(Dog,Animal))
print(issubclass(Animal,Dog))
