import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')

text = "python is a popular language and it is easy to learn."

words = word_tokenize(text)
stop_words = set(stopwords.words('english'))

filtered_words = []

for word in words:
    if word.lower() not in stop_words:
        filtered_words.append(word)

print("Original Text:")
print(text)

print("\nAfter Stop Word Removal:")
print(filtered_words)