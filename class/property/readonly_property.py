import math
class Circle:
    def __init__(self,radius):
        self._radius = radius
        self._area = None
    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self._radius ** 2
        return self._area
    
    @radius.setter
    def radius(self,value):
        if value < 0:
            raise ValueError("Radius should be positive")
        if value != self._radius:
            print("Setting new radius")
            self._area = None
            self._radius = value
    
c = Circle(10)
print(c.area)
print(c.radius)
c.radius = 10
print(c.area)