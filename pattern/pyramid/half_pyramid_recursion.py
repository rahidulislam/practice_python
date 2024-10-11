def half_pyramid_recursion(n):
    if n >0:
        half_pyramid_recursion(n-1)
        print("*" * n)
rows = int(input("Enter the number of rows: "))
half_pyramid_recursion(rows)