def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)

print(get_full_name("Rahidul", "Islam", lambda first_name, last_name: f"{first_name} {last_name}"))

callable =[]
for i in range(5):
    callable.append(lambda a=i: a)

for f in callable:
    print(f())


def times(n:int):
    return lambda x: x*n

print(times(2)(5))

def add(a:int, b:int):
    """Add two numbers"""
    return a+b

print(add(1, 2))
help(add)
add.__doc__