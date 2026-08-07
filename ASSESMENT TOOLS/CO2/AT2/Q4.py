words = ["writes","writing","written"]

print("{:<10}{:<10}{:<12}{:<15}{:<12}".format(
    "Word","Root","Pattern","Type","Normalized"))

for word in words:

    if word == "writes":
        pattern = "+s"
        typ = "Regular"

    elif word == "writing":
        pattern = "+ing"
        typ = "Regular"

    else:
        pattern = "irregular"
        typ = "Irregular"

    print("{:<10}{:<10}{:<12}{:<15}{:<12}".format(
        word,"write",pattern,typ,"write"))