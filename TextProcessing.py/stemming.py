import nltk 
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

text = "The student are Studying and Learning new things every day."

words = word_tokenize(text)

print("Original Words:")
print(words)

print("\nAfter Stemming:")

for word in words:
    print(word, "->", stemmer.stem(word))
    

