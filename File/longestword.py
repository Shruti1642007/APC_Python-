file = open("student.txt", "r")
longest =""

for line in file:
    words = line.split()
    for word in words:
        if len(word) > len(longest):
            longest = word

file.close()
print("Longest word:", longest)
            