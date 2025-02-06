class Bird:
    def fly(self):
        print(("Flying high in the sky"))
class Sparrow(Bird):
    def fly(self):
        print("sparrow is flying")

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostrich can't fly")
    
def make_bird_fly(bird:Bird):
    bird.fly()

sparrow = Sparrow()
ostrich = Ostrich()
make_bird_fly(sparrow)
# make_bird_fly(ostrich)

class Bird2:
    pass
class FlyingBird(Bird2):
    def fly(self):
        print("Flying high in the sky")

class NonFlyingBird(Bird2):
    pass

class Sparrow2(FlyingBird):
    def fly(self):
        print("Sparrow2 is flying")

class Ostrich2(NonFlyingBird):
    def walk(self):
        print("Ostrich is walking")
def make_bird_fly2(bird:FlyingBird):
    bird.fly()

sparrow2 = Sparrow2()
ostrich2 = Ostrich2()
make_bird_fly2(sparrow2)

