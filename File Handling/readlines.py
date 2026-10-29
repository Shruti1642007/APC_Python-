# readlines
file = open("example.txt", "r")
lines = file.readlines()
print("All lines:")

for line in lines:
    print(line, end="")

file.close()