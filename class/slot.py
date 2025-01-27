from pprint import pprint
class Point2D:
    __slots__ = ("x","y")
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D(x={self.x}, y={self.y})"
    
# point = Point2D(10,20)
# print(point.__slots__)
# point.z = 30
# Point2D.color="black"
# pprint(Point2D.__dict__)

class Point3D(Point2D):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z

if __name__ == "__main__":
    point = Point3D(10,20,30)
    print(point.__dict__)