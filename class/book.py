class Book:
    """
    get and set method for class
    """
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.price = 0

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def details(self):
        print("Book Name: ", self.name, "\nBook Author: ", self.author, "\nBook Price: ", self.price, "Taka")


# ------------------------------------
# object creation
b1 = Book("Opekkha", "Humayun Ahmed")
b1.details()
b1.set_price(255)
print(b1.get_price())
b1.details()
