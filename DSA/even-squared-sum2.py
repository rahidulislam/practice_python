def even_squared_sum(input_list):
    # find out even numbers
    # square them
    # sum them
    total = sum(num**2 for num in input_list if num % 2 == 0)
    return total

print(even_squared_sum([1,2,3,4,5,6]))
print(sum([1,2,3,4,5,6]))
input_list = [1,2,3,4,5,6]
generate =(num**2 for num in input_list if num % 2 == 0)
for i in generate:
    print(i)