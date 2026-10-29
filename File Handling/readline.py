# readline() example

file = open("example.txt", "r")
line1 = file.readline()
line2 = file.readline()

print("First line:", line1)
print("Second line:", line2)
file.close()