#---------------------------------------------
# CS2020
#
# Word Concordance
#
# 1. Input a text document from a user-designated file.
# 2. Compute the word concordance
# 3. Save the result to a user-designated file
# 4. Repeat Steps 1 to 3 until the user enters None
#
# Python 3.0
#
# Author: Thomas Otani
#
#-------------------------------------------

def getDocument( ):

    filename = input("Name of document file (None to Stop): ")

    if filename == "None": return None

    file = open(filename, "r")

    doc = file.read() #read the whole content at once

    file.close()

    return doc

def saveDocument(dict, dict2, dict3):

    filename = input("Name of result file: ")

    file = open(filename, "w")

    for item in dict.items():
        file.write("%-15s%3d\n" % (item[0], item[1]))

    for item in dict2.items():
        file.write("%-15s%3d\n" % (item[0], item[1]))

    for item in dict3.items():
        file.write("%-15s%3s\n" % (item[0], item[1]))
    ### I think I need to fix this so it will display correctly.

    file.close()


while True:

    doc = getDocument()

    if doc == None: break

    concordance = {} #dictionary of word:cnt pairs

    wordLength = {} #dictionary of word lengths

    sameLength = {} #dictionary of len:words with those lengths

    doclist = doc.split()


    for word in doclist:

        if word in concordance:

            concordance[word] = concordance[word] + 1
                                  #word alread in dict, incr cnt by 1
        else:

            concordance[word] = 1 #found for the first time

        if len(word) in wordLength:
            wordLength[len(word)] = wordLength[len(word)] + 1

        else:
            wordLength[len(word)] = 1


        x = len(word)
        if len(word) in sameLength:
            sameLength[x].append(word)
        else:
            sameLength[x] = [word]
           # sameLength.setdefault(str(x),[]).append(word)
        ### I think this works, but I need to display it correctly.

    saveDocument(concordance, wordLength, sameLength)

