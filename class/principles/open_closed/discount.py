from abc import ABC, abstractmethod
class DiscountCalculator:
    def apply_discount(self, discount_type:str, price:float):
        if discount_type == "percentage":
            return price * 0.2
        elif discount_type == "fixed":
            return price - 20
        elif discount_type == "seassonal":
            return price *0.1
calculator = DiscountCalculator()
print(calculator.apply_discount("percentage", 100))
print(calculator.apply_discount("fixed", 100))
print(calculator.apply_discount("seassonal", 100))

class Discount(ABC):
    @abstractmethod
    def apply_discount(self, price:float)->float:
        pass

class PercentageDiscount(Discount):
    def apply_discount(self, price:float):
        return price * 0.2

class FixedDiscount(Discount):
    def apply_discount(self, price:float):
        return price - 20

class SessonalDiscount(Discount):
    def apply_discount(self, price:float):
        return price * 0.1
    
# Instantiate the class
percentage_discount = PercentageDiscount()
fixed_discount = FixedDiscount()
sessonal_discount = SessonalDiscount()

print(percentage_discount.apply_discount(100))
print(fixed_discount.apply_discount(100))
print(sessonal_discount.apply_discount(100))