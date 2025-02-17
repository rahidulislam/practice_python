from enum import Enum, auto

class Color(Enum):
    RED = 1
    CRIMSON = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)

class Status(Enum):
    PENDING = 1
    APPROVED =2
    REJECTED = 3

print(Status.APPROVED == Status.PENDING)
print(Status.APPROVED == Status.APPROVED)
print(Status.APPROVED is Status.APPROVED)

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3

for day in Day:
    print(day)

class Animal(Enum):
    DOG = auto()
    CAT = auto()
    LION = auto()

print(Animal.DOG.value)
print(Animal.CAT.value)
print(Animal.LION.value)