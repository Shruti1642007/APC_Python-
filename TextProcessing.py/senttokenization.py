import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "python is easy to learn. It is a high-level programming language.It is widely used in data science."

sentences = sent_tokenize(text)

print("Sentence Tokenization:")

for sentence in sentences:
    print(sentence)