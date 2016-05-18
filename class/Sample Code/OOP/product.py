#---------------------------------------------
# CS2020
#
# This illustrates the class definition
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

'''
Product object encapsulates four pieces of information:

id of the form dd-dddd where d in [0..9] (string)
name (string) maximum of length 20 chars
unit price (float)  must be >= 0.0
stock balance (int) must be > 0
'''

class Product:
    
    ''' Prototype Level Data Members and Methods '''
    
    ID_SIZE = 7
    HYPHEN = "-"
    
    columnHeader = "%-15s%-27s%-15s%-7s" %  ("ID", "Name", "Unit Price", "Balance")  
        
    def isIDValid(idStr):
        if len(idStr) != Product.ID_SIZE:
            return False
        
        elif idStr[2] != Product.HYPHEN:
            return False
        
        else:
            nums = idStr[0:2] + idStr[3:7]
            if nums.isdigit():
                return True
            else:
                return False
            
    ##-------- Instance level data members and methods ----------------##
    
    '''
    No default values for id and balance. Non-default parameters come
    before those with default values specified
    All values must be valid
    '''
    def __init__(self, id, balance, name = "no name product", price = 0.0):
        self.id = id
        self.name = name
        self.price = price
        self.balance = balance
        
    def __str__(self):
        return "ID: "    + self.id + \
               " Name: "  + self.name + \
               " Price: " + str(self.price) + \
               " Bal: "   + str(self.balance)
        
        
    def display(self):
        print("%-15s%-22s%15.2f%12d" % (self.id, self.name, self.price, self.balance))
    

    
    ### ------------ Accessors ----------------- ###       

    def getId(self):
        return self.id


    def getName(self):
        return self.name


    def getPrice(self):
        return self.price


    def getBalance(self):
        return self.balance


    ### ------------ Mutators ----------------- ### 
    
    # No setID is defined because once it a Product is defined,
    # we should never change its id value
    # NOTE: Python won't prohibit someone from writing p.id = "123" 8-(

    def setName(self, value):
        self.name = value

    def setPrice(self, value):
        if value >= 0.0:
            self.price = value

    def setBalance(self, value):
        if value >= 0:
            self.balance = value
        
    def updateBalance(self, diff):   # negative diff for deduction
        self.setBalance(self.balance() + diff)

    

    
    
    
    
    

        