class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):
    def bark(self):
        print(self.name, "is barking")


# ==========================================
a1 = Animal("jack")
d1 = Dog("Rover")
d1.bark()
d1.eat()
a1.eat()
# check isinstance
print(isinstance(d1,Animal))
print((isinstance(d1,Dog)))
print(isinstance(a1,Animal))
print(isinstance(a1,Dog))
# check subclass
print(issubclass(Dog,Animal))
print(issubclass(Animal,Dog))

# =========================================
# single inheritence
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Hi My name is {self.name} and I am {self.age} years old'
    
class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def greet(self):
        return super().greet() + f" I am a {self.job_title}"

# =========================================
p1 = Person("John", 30)
print(p1.greet())
e1 = Employee("Jane", 25, "Manager")
print(e1.greet())
print(hex(id(p1)))
print(isinstance(p1,Person))
print(Person.__name__)
print(type(Person))
