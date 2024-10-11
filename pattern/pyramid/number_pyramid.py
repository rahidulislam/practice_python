def print_number_pyramid(rows):
    for i in range(1, rows+1):
        # print space
        for j in range(rows-1):
            print(" ", end=" ")
        
        # print numbers
        for k in range(2*i-1):
            print(k+1, end=" ")
        # move to next line after each row
        print()


num_rows = 5

print_number_pyramid(num_rows)