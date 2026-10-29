import re

password = input("Enter your password: ")

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&*!])[A-Za-z0-9@#$%^&*!]+$"

if re.match(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")