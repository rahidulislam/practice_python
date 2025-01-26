from pprint import pprint
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        
        if value.strip() == "":
            raise ValueError("Invalid name")
        self._name = value
        
    @name.deleter
    def name(self):
        del self._name

person = Person("John")
print(person.name)
person.name = "Smith"
print(person.name)
pprint(person.__dict__)
pprint(Person.__dict__)
del person.name
pprint(person.__dict__)
pprint(Person.__dict__)
# print(person.name)
