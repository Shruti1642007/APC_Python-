import re
text = "apple,banana;orange"
result = re.split(r"[,;]", text)
print(result)
