# Employee Management using Sets

project1 = {"Rahul", "Amit", "Sneha", "Priya", "Rohan"}
project2 = {"Sneha", "Priya", "Kiran", "Neha", "Amit"}

# Employees working on both projects
both_projects = project1.intersection(project2)

# Employees working only on Project 1
only_project1 = project1.difference(project2)

# Employees working only on Project 2
only_project2 = project2.difference(project1)

# Total unique employees
all_employees = project1.union(project2)

# Display results
print("Employees in both projects:", both_projects)
print("Employees only in Project 1:", only_project1)
print("Employees only in Project 2:", only_project2)
print("Total unique employees:", all_employees)