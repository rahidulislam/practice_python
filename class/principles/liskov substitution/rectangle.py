class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def area(self):
        return self.width * self.height
    
class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

    def set_width(self,width):
        self.width = width
        self.height = width

    def set_height(self,height):
        self.width = height
        self.height = height

def resize_rectangle(rectangle, new_width, new_height):
    rectangle.set_width(new_width)
    rectangle.set_height(new_height)
    print(f"New area: {rectangle.area()}")


rect =Rectangle(5,10)
square = Square(5)
resize_rectangle(rect,7,12)
resize_rectangle(square,7,12)
#==================================================
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def area(self):
        return self.width * self.height
    
class Square(Shape):
    def __init__(self,side):
        self.side = side

    def set_side(self,side):
        self.side = side

    def area(self):
        return self.side * self.side
    

def print_area(shape:Shape):
    print(f"Area: {shape.area()}")


rect =Rectangle(5,10)
square = Square(5)
print_area(rect)
print_area(square)

rect.set_width(7)
rect.set_height(12)
square.set_side(7)
print_area(rect)
print_area(square)