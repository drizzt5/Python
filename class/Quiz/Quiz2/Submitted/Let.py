words = ["one", "hi", "wine", "two", "vodka", "brandy", "wren"]


def groupWords(WL):
    wordD2 = {}

    for w in words:
        wordD2[len(w)] = []

    for w in words:
            wordD2[len(w)].append(w)

    list = []
    for item in wordD2.items():
        for s in item[1]:
            list.append(s)
    return list

print(groupWords(words))