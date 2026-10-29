#seak Function
with open("example.txt", "r") as file:
    file.seek(2)
    print(file.read())