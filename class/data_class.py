from dataclasses import dataclass, field
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
    
    # def __str__(self):
    #     return f"Person(name='{self.name}', age={self.age}) is created"
    
p1 = Person("John", 30)
print(p1)

@dataclass
class Person2:
    name:str
    age:int=18
    city:str = field(default="New York")
    hobbies:list = field(default_factory=list)


    def __post_init__(self):
        if self.age < 18:
            raise ValueError("Age must be at least 18")
    
p2 = Person2("Alice", 25)
p2.hobbies.append("Reading")
print(p2)
p2.age = 35
print(p2)

@dataclass(frozen=True)
class Person2:
    name:str
    age:int=18
    city:str = field(default="New York")

    def __post_init__(self):
        if self.age < 18:
            raise ValueError("Age must be at least 18")
    
p3 = Person2("Alice", 25)
print(p3)
# p3.age = 35
# print(p3)