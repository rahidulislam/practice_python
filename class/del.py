class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"{self.name} {self.age} destroyed")

person = Person("John", 30)
# person = None
del person