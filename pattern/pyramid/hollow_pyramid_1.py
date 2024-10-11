def hollow_inverted_pyramid(n):
    for i in range(n,0,-1):
        for j in range(n-1):
            print(" ",end="")
        for k in range(i):
            if k ==0 or k==i-1 or i ==n:
                print("*",end="")
            else:
                print(" ",end="")
        print()

hollow_inverted_pyramid(5)