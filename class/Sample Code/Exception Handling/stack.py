#---------------------------------------------
# CS2020
#
# Stack Implementation Using the Python List
# This version raises IndexException when invalid
# access is made
#
# Python 3.0
#
# Author: Thomas Otani
#
#-------------------------------------------

class Stack:
    
    def __init__(self):
        self.data = [ ]
                
    # PUSH:   Add the designated element to the top of the stack    
    def push(self, item):
        self.data.append(item)
        
    # POP:    Remove the topmost element from the stack
    def pop(self):
        if len(self.data) == 0 : raise IndexError
        
        topItem = self.data[len(self.data)-1]
        del self.data[len(self.data)-1]
        return topItem
    
    # PEEK:   Access the topmost element without removing it
    def peek(self):       
        if len(self.data) == 0 : raise IndexError
        
        topItem = self.data[len(self.data)-1]
        return topItem
    
    # CLEAR:  Removes all elements from the stack
    def clear(self):
        self.data = [ ] #approach 1
        
    # SIZE:   Returns the number of items in the stack
    def size(self):
        return len(self.data)
    
    # ISEMPTY:  Returns True if the stack is empty, otherwise returns False
    def isEmpty(self):
        return len(self.data) == 0
    
    