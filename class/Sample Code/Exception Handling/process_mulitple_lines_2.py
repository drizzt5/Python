def getFile(filename, mode):
    
    try:    
        file = open(filename, mode)                  
        return file
    
    except IOError:
        return None

   
    
def computeSum(file):
    sum = 0
    cnt = 0
        
    for line in file:
        try:
            sum += int(line) 
            cnt += 1
        except: 
            pass
        
    if cnt > 0:
        return sum
    else:
        return None
    


### -------- MAIN -------------###
filename = input("Filename: ")
inputFile = getFile(filename, "r")

if inputFile == None:
    print("Can't open file")
else:
    total = computeSum(inputFile) 
    print(total)
    inputFile.close()
    
