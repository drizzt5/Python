#---------------------------------------------
# CS2020
#
# We can add multiple catch blocks to handle
# each type of exceptions differently
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

while True:
    try:
        filename = input("Filename: ")
        
        file = open(filename, "r")
        
        line = file.readline()
        
        num = int(line.strip())
        
        print(num)
        
       # file.close()
        
        break
    
    except IOError:
        print("File I/O Error")
        print("Try again")
        
    except ValueError:
        print("File content cannot be converted to an integer")
        print("Try again")
        
    finally:
        file.close()
        
        
        
        