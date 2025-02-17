class Person:
    def __init__(self,name):
        self._name=name

    def get_name(self):
        return self._name

    def set_name(self,name):
        if isinstance(name,str):
            self._name=name
        else:
            raise ValueError("Invalid name")
    
p =  Person("John")
print(p.get_name())
p.set_name("Smith")
print(p.get_name())

class Person2:
    def __init__(self,name):
        self._name=name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name,str):
            self._name=name
        else:
            raise ValueError("Name must be is a string")
p2 = Person2("Alice")
print(p2.name)
p2.name="Bob"
print(p2.name)
print(p2.__dict__)
print(Person2.__dict__)