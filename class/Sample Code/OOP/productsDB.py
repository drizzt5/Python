#--------------------------------
#
# CS 2020 Object-Oriented Products Database
#
# This sample program illustrates an object-oriented approach
# for implementing the products database. Instead of generic
# list of lists, we will implement the products database
# as list of Product objects.

# Python 3.0
#
# Author: Thomas Otani
#
#--------------------------------

from product import Product

ID    = 0
NAME  = 1
PRICE = 2
BAL   = 3
COMMA = ","
NL    = "\n"

ADD    = 1
DELETE = 2
MODIFY = 3
SEARCH = 4
QUIT   = 0

SEARCH_BY_ID   = 1
SEARCH_BY_NAME = 2
SEARCH_BY_BAL  = 3

WILDCARD = "*"
NO_MATCH = "------------------ No  Match ----------------"


####################################################################
#   You do not have to understand the getData and saveData         #
#   functions.                                                     #
####################################################################

def getData( ):
    
    filename = input("Enter input filename: ")
    
    datafile = open(filename, "r")
    
    list = []
    
    for line in datafile:
        item = line.split(COMMA) 
        list.append(Product(item[ID], int(item[BAL]), item[NAME],float(item[PRICE]))) 
        
    datafile.close()
    
    return list



def saveData(list):
    
    filename = input("Enter output filename: ")
    
    datafile = open(filename, "w")
    
    for item in list:
        datafile.write(item.getId() + COMMA)
        datafile.write(item.getName() + COMMA)
        datafile.write(str(item.getPrice()) + COMMA)
        datafile.write(str(item.getBalance()) + NL)
                       
    datafile.close()
    

########################################################################
  
#Display all members in a give list
def displayAll(list):
    for prod in list:
        prod.display()
    
    
#Display menu choices for search
#return the selection to the caller
def displaySearchMenu( ):
    while True:
        choice = input(\
            "Search: \n" + \
            "   By ID       ---> " + str(SEARCH_BY_ID)   + "\n" + \
            "   By Name     ---> " + str(SEARCH_BY_NAME) + "\n" + \
            "   By Balance  ---> " + str(SEARCH_BY_BAL)  + "\n")
        
        choice = eval(choice)
        
        if SEARCH_BY_ID <= choice <= SEARCH_BY_BAL:
            
            return choice
        
        else:
            print("Error: Invalid selection. Try again.\n")
            
            
    
#Display menu choices and
#return the selection to the caller
def displayMenu( ):
    while True:
        choice = input("\nMenu: \n" + \
                       "   Add    ---> 1\n" + \
                       "   Delete ---> 2\n" + \
                       "   Modify ---> 3\n" + \
                       "   Search ---> 4\n" + \
                       " ----------------\n" + \
                       "   Quit   ---> 0\n")
        
        choice = eval(choice)
        
        if QUIT <= choice <= SEARCH:
            return choice
        
        else:
            print("Error: Invalid selection. Try again.\n")
   
        
            
#Input the ID, if input is not WILDCARD and invalid format
#prompt again until valid ID or WILDCARD is entered.
#
def getID( ):
    while True:
        id = input("Enter ID (dd-dddd): ")
        
        if id == WILDCARD or Product.isIDValid(id):
            return id
        
        else:
            print("Error: Invalid input. Try again.")
            
            
#Input the balance cutoff. Must be nonnegative
#Repeat until valid data is entered
def getBalance( ):
    while True:
        bal = eval(input("Enter Balance (>= 0): "))
        
        if bal >= 0: return bal
        
        else:
            print("Error: Invalid input. Try again.")

            
#Check if the parameter id is already in the list
#Return the matching member if found; otherwise, return None
#
def searchProduct(id, list):
    
    for prod in list:
        if prod.id() == id: 
            return prod
    
    return None   #no match found


            
#Search the members list by the ID
def searchByID(list):
    searchID = getID()
    
    print(Product.columnHeader)
    
    if searchID == WILDCARD: #display all members
        
        displayAll(list)
            
    else:
        for prod in list: #display one with the matching ID
            
            if searchID == prod.id():
                prod.display()
                break #or return
        
        else:
            print(NO_MATCH)
            
        ## this for loop can be written by using list comprehension
        #result = [mem for mem in list if searchID == mem.id()]
        #if len(result) > 0: display(result[0])
        #else: print(NO_MATCH)  
    
    
#Search the products list by the last name
def searchByName(list):
    
    searchName = input("Enter Product Name to Search: ")
     
    print(Product.columnHeader)
    
    if searchName == WILDCARD:
        
        displayAll(list)
        
    else:
        result = [ ]
    
        for prod in list:
            if searchName == prod.name():
                result.append(prod)
            
        # Equivalently in list comprehension
        #  
        # result = 
        #    [member for member in list if inputName == member.name()]
          
        if result == []:
        
            print(NO_MATCH)
        
        else:
        
            displayAll(result)
            print("")
    
    
    
#Search the products list by the balance
def searchByBalance(list):
    
    cutoff = getBalance( )
    
    print(Product.columnHeader)
    
    result = [ ]
    
    for prod in list:
        if prod.balance <= cutoff:
            result.append(prod)
        
    # Equivalently in list comprehension
    #  
    # result = 
    #    [prod for prod in list if prod.balance() <= cutoff]
      
    if result == []:
    
        print(NO_MATCH)
    
    else:
    
        displayAll(result)
        print("")
    
    
#Search for the designated product in the given list            
def search(list):
    
    choice = displaySearchMenu()
    
    if choice == SEARCH_BY_ID:
        searchByID(list)
        
    elif choice == SEARCH_BY_NAME: 
        searchByName(list)
        
    else:
        searchByBalance(list)

        
        
        
#Input four pieces of information for a new product
# 
def getProductInfo( ):
    
    while True:
        id = getID()
        
        if id == WILDCARD:
            print("Error: " + WILDCARD + " not a valid id for product")
            
        elif searchProduct(id, list) != None: 
            print("Error: Duplicate ID.")
            
        else:
            break
    
    name  = input("Enter Product Name:  ")
    
    if len(name) > 20: 
        print("Name too long. Truncated to 20 chars")
        name = name[:20]    
    
    while True:
        unitPrice = input("Enter unit price (>=0.0): ")
        if unitPrice >= 0.0: break
        print("Error. Invalid input. Try again")
        
    while True:
        balance = input("Enter stock balance (>0): ")
        if balance > 0 : break
        print("Error. Invalid input. Try again")
        
    ##return [id, name, unitPrice, balance]
    return Product(id, name, unitPrice, balance)


#Add a new member to a list
#
def add(list):
    newProduct = getProductInfo() 
                  #dup is handled inside getProductInfo
                  #only valid product info return

    list.append(newProduct)
    print("New product is added to the list")
    newProduct.display()

    
    
#Delete the designated product from the given list
def delete(list):
        
    delID = getID()
    
    product = searchProduct(delID, list)
    
    if product == None:
        
        print("Error: Member not found")
    
    else:  
        list.remove(product)
        print("The following member is removed:")
        product.display()

    
    
#Change the point values of the given member
#
def changeBalance(product):
    
    product.display()
    
    while True:
        amt = input("Enter balance change (neg for deduction) " + \
                    "and (pos for addition): ")
        
        newBal = product.balance() + amt;
        
        if newBal >= 0 :
            product.setBalance(newBal)
            return
        
        else:
            print("Error. Pt balance can't go negative. Try again.")
            


#Modify the point balance of the designated member in
#the given list
#
def modify(list):
    
    modID = getID()
    
    product = searchProduct(modID, list)
    
    if product == None:
        
        print("Error. Not Found.")
        
    else:
        
        changeBalance(product)
        
        print("Updated Member:")
        product.display()
    
    
    
#--------------------------------------------#
#               M A I N                      #
#                                            #
#--------------------------------------------#
products = getData()

while True:
    selection = displayMenu()

    if selection == SEARCH:
        search(products)
    
    elif selection == ADD:
        add(products)
        
    elif selection == DELETE:
        delete(products)
        
    elif selection == MODIFY:
        modify(products)
        
    else: #QUIT
        break


saveData(products)

print("Program shuts down. Good-Bye.")






    
    