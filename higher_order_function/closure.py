def outer(x):
    def inner(y):
        return x + y
    return inner

closure_function  = outer(15)
print(closure_function(10))

def counter(start=0):
    count=start
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
my_counter = counter(5)
print(my_counter())
print(my_counter())
print(my_counter())