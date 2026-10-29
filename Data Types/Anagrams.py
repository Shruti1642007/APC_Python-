# Anagram Checker

def normalize(text):
    result = ""

    for ch in text.lower():
        if ch.isalnum():
            result += ch

    return result


# Input two strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Normalize strings
str1 = normalize(str1)
str2 = normalize(str2)

# Compare character frequencies
if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")