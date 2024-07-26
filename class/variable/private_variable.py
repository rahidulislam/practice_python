class Student:
    def __init__(self,name,id):
        self.name=name
        self.__id=id

    def show_detail(self):
        print("Name:",self.name, "ID:",self.__id)

# ======================================================
s1=Student("Bob",33)
s1.show_detail()
print(s1.__dict__)