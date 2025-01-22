class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old"
    
    def __repr__(self):
        return f"Person({self.first_name}, {self.last_name}, {self.age})"
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age
        return False

person = Person("John", "Doe", 30)
person2 = Person("Jane", "Doe", 30)
print(person)
print(repr(person))
print(person is person2)
print(person==person2)