from abc import ABC, abstractmethod
class Worker:
    def work(self):
        pass
    def eat(self):
        pass

class Human(Worker):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")

class Robot(Worker):
    def work(self):
        print("Robot is working")

    def eat(self):
        raise NotImplementedError("Robot can't eat")
    
# h1 = Human()
# h1.work()
# h1.eat()

# r1 = Robot()
# r1.work()
# r1.eat()

# with OCP

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")

class Robot(Workable):
    def work(self):
        print("Robot is working")

    
h1 = Human()
h1.work()
h1.eat()

r1 = Robot()
r1.work()
