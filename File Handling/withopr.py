# With function

# Write operation
with open("example.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("Welcome to File Handling\n")

# Read operation
with open("example.txt", "r") as file:
    print("File Content:")
    print(file.read())

# Append operation
with open("example.txt", "a") as file:
    file.write("This is appended data.\n")

# Read updated content
with open("example.txt", "r") as file:
    print("Updated File Content:")
    print(file.read())