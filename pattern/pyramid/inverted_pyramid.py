def inverted_pyramid(n):
    for i in range(n,0,-1):
        # inner loop for leading space in each tor
        for j in range(n-i):
            print(" ",end="")
        for k in range(2*i-1):
            print("*",end="")
        print()

inverted_pyramid(5)