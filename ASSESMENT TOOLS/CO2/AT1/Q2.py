words = ["unhappy", "happiness", "happily"]

print("{:<12}{:<10}{:<10}{:<10}{:<15}".format(
    "Word","Prefix","Root","Suffix","Type"))

for word in words:

    if word.startswith("un"):
        prefix = "un"
        root = "happy"
        suffix = "-"
    elif word.endswith("ness"):
        prefix = "-"
        root = "happy"
        suffix = "ness"
    else:
        prefix = "-"
        root = "happy"
        suffix = "ly"

    print("{:<12}{:<10}{:<10}{:<10}{:<15}".format(
        word,prefix,root,suffix,"Derivational"))