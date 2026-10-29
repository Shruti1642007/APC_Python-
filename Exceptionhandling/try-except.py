try:
    a = int(input("enter first number:"))
    b = int(input("enter seconde number:"))
    result = a/b
    print("Result=", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
        

