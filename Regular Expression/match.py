import re

text = "Python is easy"

result = re.match(r"Python", text)

if result:
    print("Matched")
