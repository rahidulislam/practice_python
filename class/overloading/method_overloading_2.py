class MyCalculator:
    def product(self, *nums):
        result = 1
        for x in nums:
            result = result * x
        print(result)


# ------------------------------------
# object create
p1 = MyCalculator()
p1.product(4, 5)
p1.product(4, 5, 6)
