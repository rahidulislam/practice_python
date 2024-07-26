from multipledispatch import dispatch


class MyCalculator:
    @dispatch(int, int)
    def product(self, a, b):
        print(a * b)

    @dispatch(int, int, int)
    def product(self, a, b, c):
        print(a * b * c)


# ------------------------------------
# object create
c1 = MyCalculator()
c1.product(4, 5)
c1.product(4, 5, 6)
