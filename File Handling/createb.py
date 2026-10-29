# Create a binary file
data = b"Hello Python"
with open("example.bin", "wb") as file:
    file.write(data)
print("Binary file created successfully.")