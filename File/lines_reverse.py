file = open("student.txt","r")

lines = file.readlines()
file.close()

print("lines in reverse order:")
for line in reversed(lines):
    print(line, end="")
    