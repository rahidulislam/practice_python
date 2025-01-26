class Person:
    def __init__(self,name):
        self._name = name

    def greet(self):
        return f"Hello, I am {self._name}"
    
class Employee(Person):
    def __init__(self,name,title,base_pay):
        # self.name = name
        super().__init__(name)
        self.title = title
        self.base_pay = base_pay

    def greet(self):
        return f"Hello, I am {self.name} and I am a {self.title}"
    
    def get_pay(self):
        return self.base_pay

class SalesEmployee(Employee):
    def __init__(self,name,title,base_pay,sales_incentive):
        super().__init__(name,title,base_pay)
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return super().get_pay() + self.sales_incentive
    
person = Person("John")
print(person.greet())
employee = Employee("John","Software Engineer",50000)
print(employee.get_pay())


print(type(person))
print(type(employee))
print(type(Person))
print(type(Employee))

# check instance
print(isinstance(person,Person))
print(isinstance(employee,Employee))
print(isinstance(employee,Person))
print(isinstance(person,Employee))

# check subclass
print(issubclass(Employee,Person))

sales_man = SalesEmployee("Jane","Sales",10000,5000)
print(sales_man.get_pay())

if __name__ == "__main__":
    print(employee.get_pay())
    print(sales_man.get_pay())