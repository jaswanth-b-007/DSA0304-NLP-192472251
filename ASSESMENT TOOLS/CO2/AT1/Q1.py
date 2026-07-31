words = ["connected", "connecting", "connection"]

rules = {
    "ed": ("connect", "Inflectional"),
    "ing": ("connect", "Inflectional"),
    "ion": ("connect", "Derivational")
}

print("{:<12}{:<12}{:<10}{:<15}{:<12}".format(
    "Word","Root","Suffix","Type","Normalized"))

for word in words:
    for suf in rules:
        if word.endswith(suf):
            root, typ = rules[suf]
            print("{:<12}{:<12}{:<10}{:<15}{:<12}".format(
                word, root, suf, typ, root))