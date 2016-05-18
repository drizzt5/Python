while True:
    try:
        filename = input("Filename: ")
        
        file = open(filename, "r")
        
        sum = 0
        
        for line in file:
            try:
                sum += int(line) 
            except: 
                break
            
        print(sum)
        
        file.close()
    
    except IOError:
        print("File I/O Error")
        print("Try again")
