def half_pyramid(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()


half_pyramid(5)