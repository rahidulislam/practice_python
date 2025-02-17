class Person:
    __slots__ = ("name","age")
    def __init__(self,name,age):
        self.name = name
        self.age = age
p = Person("John",20)
# p.city = "New York"
print(p.__slots__)