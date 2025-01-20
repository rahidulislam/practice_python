class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Hi My name is {self.name} and I am {self.age} years old'
    
    def create_anonymous(cls):
        return cls("Anonymous", 30)
    
anonymous = Person.create_anonymous()
print(anonymous.name)