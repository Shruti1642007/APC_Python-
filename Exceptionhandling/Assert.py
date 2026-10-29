try:
    marks = int(input("enter your marks:"))
    assert marks >= 0 and marks <= 100,"marks must be between 0 and 100."
    print("your marks are:",marks)

except AssertionError as e:
    print(e)