from pprint import pprint
class HtmlDocument:
    # class variable
    extension = 'html'
    version = '5'

    def __init__(self,name,contents):
        self.name =name
        self.contents = contents
    # callable class attribute
    def render():
        print('Rendering html document')

    def greet(self):
        print(f'Hello {self.extension}')

print(HtmlDocument.__name__)
print(type(HtmlDocument))

# check instance
print(isinstance(HtmlDocument,type))

# print class variable
print(HtmlDocument.extension)   
print(HtmlDocument.version)
media_tpye = getattr(HtmlDocument,'media_type','text/html')
print(media_tpye)

# set values of class variable
HtmlDocument.version=10
print(HtmlDocument.version)
setattr(HtmlDocument,'version',20)
print(HtmlDocument.version)

# delete class variable
# del HtmlDocument.version
# delattr(HtmlDocument,'version')
# print(HtmlDocument.version)

# class variable storage
pprint(HtmlDocument.__dict__)
HtmlDocument.render()
print(HtmlDocument.render)
print(type(HtmlDocument.render))
print(type(HtmlDocument.greet))

http_render = HtmlDocument('Render','')
print(http_render.render)
print(type(http_render.render) is type(HtmlDocument.render))
print(type(http_render.render))
print(type(HtmlDocument.render))
# http_render.render()
HtmlDocument.render()
pprint(HtmlDocument.__dict__)
print(http_render.__dict__)
print(type(HtmlDocument.__dict__))
print(type(http_render.__dict__))
print(http_render.extension)
http_render.version =9
print(http_render.__dict__)

HtmlDocument.media_type = 'text/html'
print(HtmlDocument.__dict__)
print(http_render.media_type)

home = HtmlDocument('blank','')
print(home.__dict__)
print(http_render.__dict__)

class Circle:
    pi = 3.14
    circle_list =[]

    def __init__(self,radius):
        self.radius = radius
        self.circle_list.append(self)

    def area(self):
        return self.pi * self.radius **2
    
    def circumference(self):
        return 2*self.pi*self.radius
    
c = Circle(10)
print(c.pi)
print(Circle.pi)

c2 = Circle(20)
print(c2.pi)
print(len(Circle.circle_list))
class Test:
    x=10

    def __init__(self):
        self.x=20

test = Test()
print(test.x)
print(Test.x)


class Product:
    default_discount = 0

    def __init__(self,price):
        self.price = price
        self.discount = Product.default_discount

    def set_discount(self,discount):
        self.discount = discount

    def net_price(self):
        return self.price *(1-self.discount)
    
p1 = Product(100)
print(p1.net_price())

p2 = Product(200)
p2.set_discount(0.05)
print(p2.net_price())

class Car:
    wheels =4

    def __init__(self,brand,model):
        self.brand = brand
        self.model =model

car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model S")

print(car1.wheels)
print(car2.wheels)

print(car1.brand)
print(car2.brand)

