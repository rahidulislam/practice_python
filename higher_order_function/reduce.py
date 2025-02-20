from functools import reduce
import math
scroes = [78,55,99,36]
# total = 0
# for score in scroes:
#     total += score
# print(total)
# def sum(a,b):
#     print(f"a={a},b={b}, {a}+{b}={a+b}")
#     return a+b
# result = reduce(sum,scroes)
# print(result)

total = reduce(lambda a,b: a+b,scroes)
print(total)

# multiply all numbers in a list
nums = [1,2,3,4,5]
product = reduce(lambda a,b:a*b,nums)
print(product)

# find max number in a list
nums = [10,30,56,48,79]
max_num = reduce(lambda a,b: a if a>b else b,nums)
print(max_num)

# count occurrences of each element in a list
items = ['apple','banana','cherry','apple','banana','apple']
occurrences = reduce(lambda count,item : count.update({item:count.get(item,0)+1}) or count,items,{})
print(occurrences)

# gcd 

nums =[24,35,48]
gcd = reduce(math.gcd, nums)
print(gcd)

# flatten a list of lists
lists = [[1,2,3],[4,5,6],[7,8,9]]
flattened = reduce(lambda a,b: a+b,lists)
print(flattened)

