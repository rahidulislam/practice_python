price = int(input('Enter the price: '))
tax = input('Enter the tax: ')

tax_amount = int(price) * int(tax) / 100
print(f"The tax amount is {tax_amount}")
print(not (price>100 and price<200))