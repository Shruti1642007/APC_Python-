file = open("student.txt", "r")
count = 0

for line in file:
    count = count + 1

print("Total number of lines :", count)
file.close()
