try:
    num = int(input("Enter a number:"))
    result = 10 / num

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("please enter a valid number.")

else:
    print("Result =", result)
            
