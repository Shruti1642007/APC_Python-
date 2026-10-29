file = open("student.txt", "r")
count = 0
for line in file:
    count = count + len(line)
file.close()

print("Total number of characters:",count)
