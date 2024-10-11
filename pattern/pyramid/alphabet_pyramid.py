n = 5
alph = 65
for i in range(0,n):
    print(" "*(n-i),end=" ")
    for j in range(0,i+i):
        print(chr(alph),end=" ")
        alph = alph+1
    alph = 65
    print()