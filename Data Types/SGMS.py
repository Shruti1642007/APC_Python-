#Student Grade Management System
students = []
grades = []
def add_student():
        Name=input("enter name of students:")
        grade=float(input("enter grade:"))
        students.append(Name)
        grades.append(grade)
        print("Student add successfully:")

def update_grades():
        Name=input("enter name to update:")
        if Name in students:
                index = students.index(Name)
                grades[index]=float(input("enter new grades:"))
                print("Grade updated successfully:")
        else:
                print("Student not found.") 

def remove_student():
        Name=input("enter student name to remove:")
        if Name in students:
                index = students.index(Name)
                students.pop(index)
                grades.pop(index)
                print("Student removed successfully.")
        else:
                print("Student not found")

def average_grades():
        if len(grades) > 0:
                avg = sum(grades) / len(grades)
                print("Average grade:",avg)
        else:
                print("No student record.")

def display_grades():
        if len(grades) > 0:
                print("Highest grade:", max(grades))
                print("Lowest grade:", min(grades))
        else:
                print("No student records.")

while True:
        print("\n Student Grade Management System")
        print("1.Add Student")
        print("2.update Student")
        print("3.remove Student")
        print("4.Calculate Average Grade")
        print("5.Display highest and lowest grade")
        print("6.Display student list")
        print("7.Exit")

        choice = int(input("Enter your choice:"))

        if choice == 1:
                add_student()
        elif choice == 2:
                update_grades()
        elif choice == 3:
                remove_student()
        elif choice == 4:
                average_grades()
        elif choice == 5:
                display_grades()
        elif choice == 6:
                print("\nStudents Records:")
                for i in range(len(students)):
                        print(students[i], "_", grades[i])
        elif choice == 7:
                print("program Ended.")
                break
        else:
                print("Invalid choice")                                              

        