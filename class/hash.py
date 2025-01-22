class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __eq__(self, value):
        return isinstance(value, Person) and self.age == value.age

    def __hash__(self):
        return hash(id(self))
    
p1 = Person("John", 30)
p2 = Person("Jane", 25)

print(hash(p1))
print(hash(p2))
print(p1.__hash__())