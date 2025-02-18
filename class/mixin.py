class Flyable:
    def fly(self):
        return "Flying"
    
class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

class Airplane(Vehicle,Flyable):
    def __init__(self,make,model,wingspan):
        super().__init__(make,model)
        self.wingspan = wingspan

airplane = Airplane("Boeing","747",100)
print(airplane.fly())
print(airplane.make)
print(airplane.model)


class LoggingMixin:
    def log(self, msg):
        print(f"Logging message: {msg}")

class User(LoggingMixin):
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def update_email(self, new_email):
        self.log(f"Updating email from {self.email} to {new_email}")
        self.email = new_email
    
user = User("John","1Hd8t@example.com")
user.update_email("mWlYQ@example.com")