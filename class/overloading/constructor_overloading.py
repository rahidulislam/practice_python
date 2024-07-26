class Student:
    def __init__(self, **kwargs):
        first_name = kwargs.get('first_name')
        middle_name = kwargs.get('middle_name')
        last_name = kwargs.get('last_name')

        if first_name and middle_name and last_name:
            self.full_name = first_name + " " + middle_name + " " + last_name
        elif first_name and last_name:
            self.full_name = first_name + " " + last_name
        
        else:
            self.full_name=None

    def display_full_name(self):
        if self.full_name:
            print(self.full_name)
        else:
            print("Full name is not provided")

# ----------------------------------------------------
# object creation
s1 = Student(first_name="Rahidul", last_name="Islam")
s2 = Student(first_name="John",middle_name="doe",last_name="mike")
s1.display_full_name()
s2.display_full_name()
