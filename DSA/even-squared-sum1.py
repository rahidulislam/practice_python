def even_squared_sum(input_list):
    # find out even numbers
    # square them
    # sum them
    even_numbers = filter(lambda x: x%2 == 0, input_list)
    even_squared_numbers = map(lambda x: x**2, even_numbers)
    total = 0

    for num in even_squared_numbers:
        total += num
    return total

print(even_squared_sum([1,2,3,4,5,6]))