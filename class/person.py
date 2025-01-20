class Person:
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter +=1

    def greet(self):
        return f'Hi My name is {self.name} and I am {self.age} years old'

    # class Method
    @classmethod
    def create_anonymous(cls):
        return Person('Anonymous', 20)

person = Person("John", 30)
print(person.name)
print(person.age)
print(person.greet())

person2 = Person("Jane", 25)
print(person2.name)
print(person2.age)
print(person2.greet())

print(Person.counter)
anonymous = Person.create_anonymous()
print(anonymous.name)