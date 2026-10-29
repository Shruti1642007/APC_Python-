class Student:
    def study(self):                 
        print("Student is studying")

    def _study_protected(self):      
        print("Student is studying (protected)")


class CollegeStudent(Student):
    def attend_class(self):                
        print("Student is attending college")

    def _college_protected(self):    
        print("College student is attending class (protected)")

    def __private_college(self):    
        print("Private method of CollegeStudent")


class EngineeringStudent(CollegeStudent):
    def display(self):               
        print("Student is doing a project")

    def show_details(self):
        
        self.study()

       
        self._study_protected()
        self._college_protected()

        

s = EngineeringStudent()

s.study()                 
s._study_protected()      
s.attend_class()          
s._college_protected()    
s.display()              

