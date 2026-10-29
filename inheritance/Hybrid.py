class Student:
    def study(self):
        print("Student is studying")

class CollegeStudent(Student):
    def attend_class(self):
        print("Stuent is attending college")

class EngineeringStudent(Student):
    def display(self):
        print("Student is doing a project")

class SportsPerson(CollegeStudent, EngineeringStudent):
    def play(self):
        print("Student is Playing sports")

s = SportsPerson()
s.study()
s.attend_class()
s.display()
s.play()

            