#---------------------------------------------
# CS2020
#
# A sample program to test linear and binary search
# routines.
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

from search import *
from random import *

# numbers = [34, 2, 34, 55, 67, 28, 12, 8, 10, 77]  

numbers = [ ]

for i in range(0, 10000):
    numbers.append(randint(0, 20000))

while True:
    val = eval(input("Enter positive integer (None to stop): "))
    
    if val == None: break
    
    print("Search Result: ", linearSearch(numbers, val))
    

# sort the list before binary search
numbers.sort()
    
while True:
    val = eval(input("Enter positive integer (None to stop): "))
    
    if val == None: break
    
    print("Search Result: ", binarySearch(numbers, val))