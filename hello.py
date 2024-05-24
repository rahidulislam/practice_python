# number = int(input("Enter a number: " ))
# for i in range(1, 10):
#     result = number * i
#     print(number, "X", i, " = " , number*i)


def times(number):
    for i in range(1, 10):
        print(number, "X", i, " = ", number * i)

times(int(input("Enter a number: ")))
