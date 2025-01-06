def even_squared_sum(input_list):
    # find out even numbers
    # square them
    # sum them
    even_squared_numbers = []
    total = 0
    for num in input_list:
        if num%2 == 0:
            even_squared_numbers.append(num**2)
    for num in even_squared_numbers:
        total += num
    return total

print(even_squared_sum([1,2,3,4,5,6]))