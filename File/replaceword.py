old_word = input("Enter the word to be replaced:")
new_word = input("Enter the new word:")

file = open("student.txt", "r")
content = file.read()

file.close()

content = content.replace(old_word, new_word)
file = open("new_student.txt", "w")

file.write(content)
file.close()

print("Word replaced successfully.")
