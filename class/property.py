class Person:
    def __init__(self, name, age):
        self.name = name
        # self.set_age(age)
        self.age = age

    # def get_age(self):
    #     return self._age
    @property
    def age(self):
        return self._age

    # def set_age(self, age):
    #     if age<0:
    #         raise ValueError("Invalid age")
    #     self._age = age
    @age.setter
    def age(self, age):
        if age<0:
            raise ValueError("Invalid age")
        self._age = age
    # age = property(get_age, set_age)
    # age = property(age, set_age)
    # age = age.setter(set_age)
    
john = Person("John", 30)
# john.set_age(-40)
print(Person.age)
print(john.__dict__)
john.age = 40
print(john.__dict__)
print(Person.__dict__)
print(john.age)
# print(john.get_age())