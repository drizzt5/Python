#---------------------------------------------
# CS2020
#
# This illustrates how the Product objects are
# used from the client program
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

from product import Product

# Create two products p1 and p2  
p1 = Product("12-3455", 10)
p2 = Product("12-8988", 20)

print(p1.getPrice())
print(p2)

# Create a product with invalid id
id = "33"
#id= "12-9999"

if not Product.isIDValid(id):
    print("Invalid id value")    
else:
    p3 = Product(id, 15)
    print(p3)
    
# Update data member values 
print("p1 --->")
print(p1)

print("Update p1 ----->")
p1.setName("Decafe Kona Blend")
p1.setPrice(9.99)
p1.setBalance(45)  #try -15 and see what happens
print(p1)
