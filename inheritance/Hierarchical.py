class Student:
    def study(self):
        print("Student is Studying")

class CollegeStudent(Student):
    def attend_class(self):
        print("Student is attending the college")


class SportsPerson(Student):
    def play(self):
        print("Student is playing sports")

s = SportsPerson()
c = CollegeStudent()

s.play()
s.study()
c.attend_class()
c.study()