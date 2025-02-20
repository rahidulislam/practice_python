def decorator_function(func):
    def wrapper_function():
        print("Before function call")
        func()
        print("After function call")
    return wrapper_function

def say_hello():
    print("Hello")

say_hellow = decorator_function(say_hello)
say_hellow()

@decorator_function
def say_hellow2():
    print("Hellow World")

say_hellow2()

def decorator_function2(func):
    def wrapper_function(*args, **kwargs):
        print("Function is being called with arguments")
        return func(*args, **kwargs)
    return wrapper_function

@decorator_function2
def add(a,b):
    return a+b

print(add(2,3))

def class_decorator(cls):
    class WrapperClass(cls):
        def new_method(self):
            print("This is a new method added by decorator")
    return WrapperClass

@class_decorator
class MyClass:
    def orginal_method(self):
        print("This is original method")

obj = MyClass()
obj.orginal_method()
obj.new_method()