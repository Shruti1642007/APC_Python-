class AgeError(Exception):
    pass

try:
    age = int(input("enter your age:"))

    if age < 18:
        raise AgeError("Age must be 18 or above.")

    print("You are eligible.")

except AgeError as e :
    print(e)   