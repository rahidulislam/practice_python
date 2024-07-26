class MyCalculator:
    def product(self, num1, num2=None, num3=None):
        if num1 is not None and num2 is not None and num3 is not None:
            print(num1 * num2 * num3)
        elif num1 is not None and num2 is not None:
            print(num1 * num2)
        else:
            print(num1)


# ----------------------------------------------------------------------
# object create
p1 = MyCalculator()
p1.product(4, 5)
p1.product(4, 5, 6)
p1.product(6)
