import re

pattern = re.compile(r"\d+")

text  = "Hello Python 20 "

result = pattern.search(text)

if result:
    print("Match found:", result.group())

else:
    print("No match Found")    