def count_down(start:int):
    print(start)
    next = start-1
    if next>0:
        count_down(next)

count_down(3)

def sum(n:int):
    total = 0
    for i in range(n+1):
        total += i
    return total

print(sum(5))

def sum_rec(n:int):
    if n>0:
        return n+sum_rec(n-1)
    else:
        return 0

print(sum_rec(50))