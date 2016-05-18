#---------------------------------------------
# CS2020
#
# Bare-bone exception handling
# If any statement in the try block throws an exception
# the except block is executed
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

sum = 0

while sum < 100:   
    
     try:
          num = int(input("Enter integer: "))  #this could throw an exception
          
     except:  #if exception is thrown, execute this block
              #we say this block catches the thrown exception
          
          print("Error: Non integer value is entered")
          num = 0
     
     sum += num
    
print(sum)

