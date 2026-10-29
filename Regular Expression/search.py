import re

text ="My name is shruti"

result = re.search(r"\d+",text)

if result:
    print("Match found:", result.group())
else:
    print("No match found")    