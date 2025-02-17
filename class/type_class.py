MyClass = type('MyClass', (), {'x':10})
obj = MyClass()
print(obj.x)
print(type(MyClass))
print(isinstance(obj,MyClass))
print(isinstance(obj,type))

class Base:
    y=20

ChildClass = type('ChildClass',(Base,),{'x':10})
obj2 = ChildClass()
print(obj2.x)
print(obj2.y)

def hello(self):
    return f"Hello from {self.name}"

Person = type('Person',(),{'name':'John','greet':hello})
obj3 = Person()
print(obj3.greet())