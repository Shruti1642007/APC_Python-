import re 
email = input("enter your email:")
pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$"

if re.match(pattern,email):
    print("Valid email")
else:
    print("invalid Email")    