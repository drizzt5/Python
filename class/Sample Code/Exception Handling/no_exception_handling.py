#---------------------------------------------
# CS2900
#
# Sample code with no exception handling. See what
# happens when an invalid input is entered, an input
# that cannot be converted to an int
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

sum = 0

while sum < 100:

    try:

        num = int(input("Enter integer: "))  #this statement could throw
        sum += num

    except:
        raise TypeError('You need to be smart')
                                #an exception

    
print(sum)