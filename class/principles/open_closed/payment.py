from abc import ABC, abstractmethod
class PaymentProcessor:
    def __init__(self, amount:float):
        self.amount = amount
        
    def pay_credit_card(self):
        print(f"Paid ${self.amount} using credit card")
    
    def pay_paypal(self):
        print(f"Paid ${self.amount} using PayPal")

    def pay_bkash(self):
        print(f"Paid ${self.amount} using bKash")

# Instantiate the class
payment = PaymentProcessor(100)
payment.pay_credit_card()
payment.pay_paypal()
payment.pay_bkash()

# with OCP
class PaymentProcessor(ABC):
    def __init__(self, amount:float):
        self.amount = amount
        
    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment(PaymentProcessor):
    def pay(self):
        print(f"Paid ${self.amount} using credit card")

class PayPalPayment(PaymentProcessor):
    def pay(self):
        print(f"Paid ${self.amount} using PayPal")

class BKashPayment(PaymentProcessor):
    def pay(self):
        print(f"Paid ${self.amount} using bKash")
# Instantiate the class
payment = CreditCardPayment(100)
payment.pay()

payment = PayPalPayment(100)
payment.pay()

payment = BKashPayment(100)
payment.pay()
