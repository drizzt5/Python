#---------------------------------------------
# CS2020
#
# This program illustrates how a list of 
# Product objects is created 
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

from product import Product

productList = []

while True:
    
    #no input checking; we assume the user enters all values correctly
    
    id = input("ID (None to stop): ")
    
    if eval(id) == None: break
    
    name    = input("Name: ")
    price   = eval(input("Unit Price (float): "))
    balance = eval(input("Stock Balance (int): "))
    
    #create a new Product instance and add it to the list
    #No check on duplicate ID is done; we assume the input id is unique
    p = Product(id, balance, name, price)
    
    productList.append(p)
    
    #or eliminate the temp variable p altogether by
    #productList.append(Product(id, balance, name, price))
    
    
print()
print(Product.columnHeader)
for item in productList:
    item.display()
