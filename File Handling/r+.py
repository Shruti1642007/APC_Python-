# r+ : Read and write

file = open("example.txt", "r+")
print(file.read())
file.write("\nThis is new data.")
file.close()
print("Read and write operation completed.")