import re 
text = "My name is shruti and marks 100 out of 90"

result = re.findall(r"\d+",text)

if result:
    print("Match found:", result)
else:
    print("No match found")
        