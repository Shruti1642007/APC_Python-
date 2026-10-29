# Vocabulary Analysis of Two Books

book1 = input("Enter text of Book 1: ")
book2 = input("Enter text of Book 2: ")

# Convert text into sets of unique words
words1 = set(book1.lower().split())
words2 = set(book2.lower().split())

# Common words
common_words = words1.intersection(words2)

# Words unique to Book 1
unique_book1 = words1.difference(words2)

# Words unique to Book 2
unique_book2 = words2.difference(words1)

# All unique words
all_words = words1.union(words2)

# Display results
print("\nUnique words in Book 1:", words1)
print("Unique words in Book 2:", words2)

print("\nCommon words:", common_words)

print("Words unique to Book 1:", unique_book1)
print("Words unique to Book 2:", unique_book2)

print("\nTotal unique words across both books:", len(all_words))