class Student:
    def study(self):
        print("Student is studying")

class CollegeStudent(Student):
    def attend_class(self):
        print("Stuent is attending college")

class EngineeringStudent(CollegeStudent):
    def display(self):
        print("Student is doing a project")

s = EngineeringStudent()

s.study()
s.attend_class()
s.display()