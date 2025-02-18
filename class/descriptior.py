class Descriptor:
    def __get__(self, instance, owner):
        return "Hello world"

    def __set__(self, instance, value):
        print(f"Set new: {value}")

    def __delete__(self, *args, **kwds):
        print("Deleting value")

class MyClass:
    my_attr = Descriptor()

obj = MyClass()
print(obj.my_attr)
obj.my_attr = 42
print(obj.my_attr)