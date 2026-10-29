class Student:
    def study(self):
        print("Student is studying")

class SportsPerson:
    def play(self):
        print("Student is Playing sports")

class CollegeStudent(Student, SportsPerson):
    def attend_class(self):
        print("Student is attending college")

s = CollegeStudent()

s.attend_class()