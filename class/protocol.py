from typing import List, Protocol


class Item(Protocol):
    quantity:int
    price:float

class Product:
    def __init__(self,name:str,quantity:int, price:float):
        self.name = name
        self.quantity = quantity
        self.price = price

def calculate_total(items:List[Item])->float:
    return sum([item.quantity*item.price for item in items])

total = calculate_total([Product("Apple",10,150),Product("Banana",5,280)])

print(total)

class Stock:
    def __init__(self,product_name,quantity,price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

total = calculate_total([Stock("Apple",10,950),Stock("Banana",5,850)])
print(total)

