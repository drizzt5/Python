words = ["one", "hi", "wine", "two", "vodka", "brandy", "wren"]

wordD = {}


for w in words:
    wordD[w] =(len(w))


print(wordD)

def groupWords(D):
    result = []
    # #maxL = 0
    # for key in D:
    #     if D[key] > maxL
    #         result.append(key)


    #return [key for key,value in D.items()]

    return result


print(groupWords(wordD))

name = []
while len(name) != len(words):
    low = 0
    for item in wordD.items():
        print(item)
        if item[1]>low and item[0]!=name:
            low = item[1]
            name.append(item[0])

print(name)
