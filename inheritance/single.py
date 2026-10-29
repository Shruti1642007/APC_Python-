# single inheritance

class Student:
    def study(self):
        print("Student is studying")

class CollegeStudent(Student):
    def display(self):
        print("Student is attending college")  

s = CollegeStudent()

s.study()
s.display()