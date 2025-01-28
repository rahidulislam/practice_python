from abc import ABC,abstractmethod
class Employee(ABC):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @abstractmethod
    def get_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self,first_name,last_name,salary):
        super().__init__(first_name,last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary
    
class HourlyEmployee(Employee):
    def __init__(self,first_name,last_name,worked_hours,rate):
        super().__init__(first_name,last_name)
        self.worked_hours = worked_hours
        self.rate = rate
    def get_salary(self):
        return self.worked_hours * self.rate
    
class Payroll:
    def __init__(self):
        self.employee_list = []

    def add(self,employee):
        self.employee_list.append(employee)

    def print(self):
        for e in self.employee_list:
            print(f"{e.full_name} \t ${e.get_salary()}")

payroll = Payroll()
payroll.add(FullTimeEmployee("John","Doe",50000))
payroll.add(FullTimeEmployee("Jane","Doe",60000))
payroll.add(HourlyEmployee("Janifer","Smith",40,15))
payroll.add(HourlyEmployee("David","Wilson",30,20))
payroll.print()
