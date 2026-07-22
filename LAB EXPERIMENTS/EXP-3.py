import nltk
from nltk.stem import PorterStemmer

ps = PorterStemmer()

text = input("Enter words separated by spaces: ")

words = text.split()

print("\nMorphological Analysis")
print("----------------------")

for word in words:
    stem = ps.stem(word)
    print(f"Word : {word}")
    print(f"Stem : {stem}")
    print()