class Order:
    def __init__(self, order_id:str, product:str,quantity:int):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity

    def validate_order(self):
        print(f"Order {self.order_id} validated")

    def confirm_order(self):
        print(f"Order {self.order_id} confirmed")

    def log_order(self):
        print(f"Logged: Order {self.order_id} for {self.product} (Quantity: {self.quantity})")

# Instantiate the class
order = Order('123456', 'Laptop', 2)
order.validate_order()
order.confirm_order()
order.log_order()

# with SRP
class Order:
    def __init__(self, order_id:str, product:str,quantity:int):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity

class OrderManager:
    @staticmethod
    def validate_order(order:Order):
        print(f"Order {order.order_id} validated")
    @staticmethod
    def confirm_order(order:Order):
        print(f"Order {order.order_id} confirmed")
class OrderLogger:
    @staticmethod
    def log_order(order:Order):
        print(f"Logged: Order {order.order_id} for {order.product} (Quantity: {order.quantity})")

# Instantiate the class
order = Order('123456', 'Laptop', 2)
OrderManager.validate_order(order)
OrderManager.confirm_order(order)
OrderLogger.log_order(order)