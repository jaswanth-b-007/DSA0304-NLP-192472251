from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["relational","relation","relate"]

print("{:<12}{:<15}".format("Word","Final Stem"))

for word in words:
    stem = ps.stem(word)
    print("{:<12}{:<15}".format(word,stem))