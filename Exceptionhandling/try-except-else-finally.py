try:
    num = int(input("Enter a number:"))
    result = 10 / num

except ZeroDivisionError:
    print("cannot divide by zero.")

except ValueError:
    print("please enter a valid number.")

else:
    print("Result =", result)

finally:
    print("program completed.")
    
                