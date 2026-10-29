# a+ : Append and read
file = open("example.txt", "a+")
file.write("\nThis data is appended.")
file.seek(0)
print(file.read())
file.close()