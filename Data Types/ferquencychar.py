# Character Frequency Counter

text = input("Enter a string: ")

choice = input("Ignore case? (yes/no): ")

# Ignore case if user chooses yes
if choice.lower() == "yes":
    text = text.lower()

# Dictionary to store character frequency
frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

# Sort by frequency in descending order
sorted_frequency = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

# Display result
print("\nCharacter Frequency:")

for ch, count in sorted_frequency:
    if ch == " ":
        print("Space :", count)
    else:
        print(ch, ":", count)