class MyNum:
    """
    নিচের উদাহরণে, MyNum ক্লাস এর ইন্সট্যান্স হিসেবে আমরা দুটো অবজেক্ট তৈরি করলাম এবং এদের প্রত্যেকের value সেট করলাম 2 এবং 3. 
    এরপর এই দুটি অবজেক্টকে সাধারণ যোগ চিহ্ন দিয়ে যোগ করলাম। আমরা চাচ্ছি এই স্পেশাল নাম্বার দুটো একটু আলাদা ভাবে আমাদের নিজেদের 
    মত করে যোগ হয়ে ফিরে আসুক। এক্ষেত্রে, c = a + b লাইনে বস্তুত c = a.__add__(b) স্টেটমেন্টটি এক্সিকিউট হবে। 
    অর্থাৎ a অবজেক্টের __add__ মেথড কল হবে এবং এর মধ্যে প্রথমে 2 এর ভ্যালু দিগুণ হবে, 
    অতঃপর b অবজেক্ট তথা other প্যারামিটার এর value 3 ও দিগুণ হবে। পরিশেষে এদের যোগ ফল রিটার্ন হবে। অর্থাৎ আউটপুট,
    """

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return (self.value * 2) + (other.value * 3)


# ==============================================
a = MyNum(2)
b = MyNum(3)
c = a + b
print(c)

# ==============================================
class Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"
    
    def __add__(self,point):
        if not isinstance(point,Point2D):
            raise ValueError('The other must be an instance of the Point2D class')
        return Point2D(self.x+point.x, self.y+point.y)


a = Point2D(12,23)
b = Point2D(14,25)
c = a+b
print(c)

# ==============================================
class Item:
    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price
    @property
    def amount(self):
        return self.qty * self.price
    
    def __str__(self):
        return f"{self.name} {self.qty} ${self.price} ${self.amount}"
class Cart:
    def __init__(self):
        self.items =[]
    
    def __iadd__(self,item):
        if not isinstance(item,Item):
            raise ValueError("The item must be an instance of the Item class")
        self.items.append(item)
        return self
    @property
    def total(self):
        return sum([item.amount for item in self.items])
    
    def __str__(self):
        if not self.items:
            return "Cart is empty"
        return "\n".join([str(item) for item in self.items])
    

if __name__ == "__main__":
    cart = Cart()
    cart += Item("Apple", 2, 10)
    cart += Item("Banana", 3, 15)
    print(cart)
    print('-'*30)
    print('Total: $', cart.total)