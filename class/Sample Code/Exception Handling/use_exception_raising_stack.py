#---------------------------------------------
# CS2020
#
# Uses the stack that raises exception when trying
# to peek or pop an empty stack
#
# Python 3.0
#
# Author: Thomas Otani
#
#-------------------------------------------

from stack import Stack

s = Stack()

try:
#    s.push("One")
    s.pop()
    
except IndexError:
    print("Oops. Couldn't pop an empty stack")
    
finally:
    print("Finally clause is executed no matter what")
    
print("Good Bye")
