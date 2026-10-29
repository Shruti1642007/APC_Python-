import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "Hello,How are you doing today? I hope you are having a great day!"

Words = word_tokenize(text)

print("Word Tokenization")
print(Words)
