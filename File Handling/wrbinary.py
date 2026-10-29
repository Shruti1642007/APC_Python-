# Write binary data
data = b"Hello Python"

with open("example.bin", "wb") as file:
    file.write(data)

# Read binary data
with open("example.bin", "rb") as file:
    data = file.read()

print("Binary data:")
print(data)