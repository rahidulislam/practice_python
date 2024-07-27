from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark")
    def eat(self):
        print("eat")
# =========================================

d1 = Dog()
d1.make_sound()
d1.eat()
