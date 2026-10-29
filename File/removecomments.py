file = open("program.py", "r")
new_file = open("without_comments.py", "w")

for line in file:
    if not line.strip().startswith("#"):
        new_file.write(line)

file.close()
new_file.close()

print("Comments removed successfully.")
