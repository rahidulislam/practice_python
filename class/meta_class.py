class MyMeta(type):
    def __new__(cls, name,bases,dict):
        print(f"Creating class: {name}")
        return super().__new__(cls,name,bases,dict)
class MyClass(metaclass=MyMeta):
    x=10
class MyClass2:
    x=30
print(MyClass.x)
print(type(MyClass))
print(MyClass2.x)
print(type(MyClass2))

class AutoAddAttributes(type):
    def __new__(cls,name,bases,dict):
        dict['auto_var'] = 100
        return super().__new__(cls,name,bases,dict)
    
class MyClass3(metaclass=AutoAddAttributes):
    x=10

print(MyClass3.x)
print(MyClass3.auto_var)

class SingletonMeta(type):
    _isinstance ={}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._isinstance:
            cls._isinstance[cls] = super().__call__(*args, **kwargs)
            return cls._isinstance[cls]
        return cls._isinstance[cls]
class SingletonClass(metaclass=SingletonMeta):
    pass

obj1 = SingletonClass()
obj2 = SingletonClass()
print(obj1 is obj2)

class MyMeta2(type):
    def __new__(cls, name,bases,dict):
        print(f"Creating class: {name}")
        dict['class_created'] = True
        return super().__new__(cls,name,bases,dict)
    
class MyClass4(metaclass=MyMeta2):
    pass

print(MyClass4.class_created)
print(MyClass4.__dict__)          