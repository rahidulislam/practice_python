class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def introduce(self):
        print(f"Hello, my name is {self.get_full_name()} and I am {self.age} years old.")

    @classmethod
    def create_anonymous(cls):
        return Person('John','Doe', 20)
    
anonymous = Person.create_anonymous()
print(anonymous.introduce())
    
