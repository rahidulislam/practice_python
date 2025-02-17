class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Hi My name is {self.name} and I am {self.age} years old'
    @classmethod
    def create_anonymous(cls):
        return cls("Anonymous", 30)
    
anonymous = Person.create_anonymous()
print(anonymous.name)

class Employee:
    company ="Google"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company

    def is_working_day(day):
        return day.lower() not in ["saturday", "sunday"]
    

emp1 = Employee("John", 10000)
emp2 = Employee("Jane", 20000)

print(emp1.company)
print(emp1.show_details())
print(emp2.company)
Employee.change_company("Amazon")

print(Employee.company)
print(emp1.company)
print(emp2.company)

print(Employee.is_working_day("Monday"))
print(Employee.is_working_day("Sunday"))