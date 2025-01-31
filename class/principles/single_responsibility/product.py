class Product:
    def __init__(self,name:str,price:float, stock:int):
        self.name = name
        self.price = price
        self.stock = stock

    def add_stock(self, quantity:int):
        self.stock += quantity
        print(f"Added {quantity} units of {self.name}. New Stock:{self.stock}")

    def check_stock(self):
        print(f"Current Stock of {self.name}: {self.stock}")

    def print_product_info(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.stock}")

product = Product("Product 1", 100, 10)
product.print_product_info()
product.add_stock(5)
product.check_stock()

# with SRP
class Product2:
    def __init__(self,name:str,price:float, stock:int):
        self.name = name
        self.price = price
        self.stock = stock
class ProductManager:
    @staticmethod
    def add_stock(self, quantity:int):
        self.stock += quantity
        print(f"Added {quantity} units of {self.name}. New Stock:{self.stock}")

    @staticmethod
    def check_stock(self):
        print(f"Current Stock of {self.name}: {self.stock}")

class Product2Printer:
    @staticmethod
    def print_product_info(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.stock}")

product2 = Product2("Product 2", 200, 20)
Product2Printer.print_product_info(product2)
ProductManager.add_stock(product2, 5)
ProductManager.check_stock(product2)
