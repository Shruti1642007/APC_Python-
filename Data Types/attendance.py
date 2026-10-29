# Attendance Management System

attendance = {
    "Monday": {"Amit", "Sneha", "Rahul", "Priya"},
    "Tuesday": {"Amit", "Sneha", "Rahul"},
    "Wednesday": {"Amit", "Sneha", "Priya"},
    "Thursday": {"Amit", "Sneha", "Rahul", "Priya"},
    "Friday": {"Amit", "Sneha", "Priya"}
}

# Find students who attended all classes
all_days = set.intersection(*attendance.values())

# Find all unique students
all_students = set.union(*attendance.values())

# Find students who attended only one class
only_one_class = set()

for student in all_students:
    count = 0
    
    for students in attendance.values():
        if student in students:
            count += 1
    
    if count == 1:
        only_one_class.add(student)

# Display results
print("Students who attended all classes:", all_days)
print("Students who attended only one class:", only_one_class)
print("Total unique students:", len(all_students))