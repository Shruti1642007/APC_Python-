# Append Binary (ab)

data = b"Hello Python\n"

with open("example.bin", "ab") as file:
    file.write(data)

print("Binary data appended successfully.")