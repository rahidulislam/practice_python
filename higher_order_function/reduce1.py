from functools import reduce
numbers = [1,2,3,4,5]
total = reduce(lambda a,b:a+b,numbers,0)
print(total)
result = reduce(lambda a,b:a*b,numbers)
print(result)