class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __del__(self):
        print("__del__ was called")

person = Person("John", 30)
person = None
# del person