# def foods(fruit):
#     for food in fruit:
#         print(food)

# fruits = ["apple", "banana", "cherry"]
# foods(fruits)

# def fruits(fruit1,fruit2, fruit3):
#     print("The first fruit is "+ fruit1)
#     print("The second fruit is "+ fruit2)
#     print("The third fruit is "+ fruit3)

# fruits(fruit1="apple", fruit2="banana", fruit3="cherry")

# def new_fruits(*fruits):
#     print(fruits)

# new_fruits("apple", "banana", "cherry")
# def new_recursion(n):
#     if n>0:
#         result = n + new_recursion(n-1)
#         print(result)
#     else:
#         result = 0
#     return result
# print(new_recursion(5))

# a = lambda x: x+20
# print(a(10))

# store_lamda = lambda x,y: x*y
# print(store_lamda(10,20))

# store_lamda2 = lambda *args: sum(args)
# print(store_lamda2(1,2,3,4,5,6,7,8,9,10))

# store_lamda3 = lambda **kwargs: sum(kwargs.values())
# print(store_lamda3(a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8,i=9,j=10))

# store_lamda4 = lambda *args, **kwargs: sum(args) + sum(kwargs.values())
# print(store_lamda4(1,2,3,4,5,6,7,8,9,10,a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8,i=9,j=10))

# store_lamda5 = lambda x,y,z: x+y+z
# print(store_lamda5(1,2,3))

def new_multiplied(k):
    return lambda x: x*k
new_double = new_multiplied(2)
new_triple = new_multiplied(3)

# print(new_multiplied(4))
print(new_double(10))
print(new_triple(10))

def add(a, b):
    return a+5, b+5
result = add(3, 2)
print(result)