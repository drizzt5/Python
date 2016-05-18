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

def saveDocument(dict):
    
    filename = input("Name of result file: ")
    
    file = open(filename, "w")
    
    for item in dict.items():
        
        file.write("%-15s%3d\n" % (item[0], item[1]))
        
    file.close()
        

while True:
    
    doc = getDocument()
    
    if doc == None: break
    
    concordance = {} #dictionary of word:cnt pairs
    
    doclist = doc.split()
    
    for word in doclist:
        
        if word in concordance:
            
            concordance[word] = concordance[word] + 1
                                  #word alread in dict, incr cnt by 1
        else:
            
            concordance[word] = 1 #found for the first time
            
    saveDocument(concordance)