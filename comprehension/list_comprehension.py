numbers =[]
for i in range(10):
    numbers.append(i**2)
print(numbers)

# using list comprehension
numbers  = [i**2 for i in range(10)]
print(numbers)

numbers = [i**2 for i in range(10) if i%2==0]
print(numbers)

matrix =[[i*j for j in range(1,6)]for i in range(1,4)]
print(matrix)