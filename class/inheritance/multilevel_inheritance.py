class Student:
    """Parent/Super/Base Class"""

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def details(self):
        print("Name:", self.name, "ID:", self.id)


# ==============================================

class CSEStudent(Student):
    """Child/Sub/Derived Class"""

    def __init__(self, name, id, labs):
        super().__init__(name, id)
        self.no_of_labs = labs

    def cry(self):
        print("CSE Student is crying because of", self.no_of_labs, "labs")


# =======================================================================
class CSEStudentFresher(CSEStudent):
    """Child/Sub/Derived Class"""

    def enroll_cse110(self):
        print(self.name,"enrolled in CSE110")


# =======================================================================
# Object Creation
s1 = CSEStudent("Bob", 11, 3)
s2 = CSEStudentFresher("Carol", 36,1)
s1.details()
s1.cry()
s2.details()
s2.cry()
s2.enroll_cse110()
# print(s1.__dict__)
# print(s2.__dict__)
# print(help(s1))