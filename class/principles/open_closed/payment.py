from abc import ABC, abstractmethod
# class PaymentProcessor:
#     def __init__(self, amount:float):
#         self.amount = amount
        
#     def pay_credit_card(self):
#         print(f"Paid ${self.amount} using credit card")
    
#     def pay_paypal(self):
#         print(f"Paid ${self.amount} using PayPal")

#     def pay_bkash(self):
#         print(f"Paid ${self.amount} using bKash")

# Instantiate the class
# payment = PaymentProcessor(100)
# payment.pay_credit_card()
# payment.pay_paypal()
# payment.pay_bkash()

# with OCP
class PaymentMethod(ABC):
        
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self,amount):
        print(f"Paid ${amount} using credit card")

class PayPalPayment(PaymentMethod):
    def pay(self,amount):
        print(f"Paid ${amount} using PayPal")

class BKashPayment(PaymentMethod):
    def pay(self,amount):
        print(f"Paid ${amount} using bKash")
# Instantiate the class

class PaymentProcessor:
    def __init__(self,payment_method:PaymentMethod):
        self.payment_method = payment_method
    
    def process_payment(self,amount):
        self.payment_method.pay(amount)

processor1 =PaymentProcessor(CreditCardPayment())
processor1.process_payment(100)

processor2 =PaymentProcessor(PayPalPayment())
processor2.process_payment(200)

processor3 =PaymentProcessor(BKashPayment())
processor3.process_payment(300)
