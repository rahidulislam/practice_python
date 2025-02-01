class Student:
    def __init__(self, name:str, grade:float):
        self.name = name
        self.grade = grade

    def calculate_grade_status(self):
        if self.grade >= 60:
            return "Passed"
        return "Failed"
    
    def print_student_info(self):
        print(f"Student: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"Status: {self.calculate_grade_status()}")

# instance of Student
student = Student("John", 70)
student.print_student_info()

# with SRP
class Student:
    def __init__(self, name:str, grade:float):
        self.name = name
        self.grade = grade

class GradeCalculator:
    @staticmethod
    def calculate_grade_status(student:Student):
        if student.grade >= 60:
            return "Passed"
        return "Failed"
    
class StudentInfoPrinter:
    @staticmethod
    def print_student_info(student:Student):
        print(f"Student: {student.name}")
        print(f"Grade: {student.grade}")
        print(f"Status: {GradeCalculator.calculate_grade_status(student)}")

# instance of Student
student = Student("John", 55)
StudentInfoPrinter.print_student_info(student)
