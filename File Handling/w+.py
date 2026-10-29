# w+ : Write and read

file = open("example.txt", "w+")
file.write("Hello Python")
file.seek(0)
print(file.read())
file.close()