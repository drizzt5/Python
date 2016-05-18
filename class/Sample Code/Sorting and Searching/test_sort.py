#---------------------------------------------
# CS2020
#
# A sample program to test five sorting
# routines.
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

from sort import *
from random import *

'''
Check if the passed list L is sorted in ascending order
'''
def check(L):
    for i in range(0, len(L)-1):
        if L[i] > L[i+1]:
            #print(i, ":", L[i], ">", L[i+1])
            return False
        
    return True

##------------------------------------------------------------##
def selection(N):
    #numbers = [34, 2, 34, 55, 67, 28, 12, 8, 10, 77]  

    numbers = [ ]
    for i in range(0, N):
        numbers.append(randint(0, 20000))
        
    selectionSort(numbers)
    print("Selection Sort Succeeded:", check(numbers))
  
##------------------------------------------------------------##  
def bubble(N):

    numbers = [ ]
    for i in range(0, N):
        numbers.append(randint(0, 20000))

    bubbleSort(numbers)

    print("Bubble Sort Succeeded:", check(numbers))
 
##------------------------------------------------------------##   
def merge(N):

    numbers = [ ]
    for i in range(0, N):
        numbers.append(randint(0, 20000))
        
    mergeSort(numbers)
    print("Merge Sort Succeeded:", check(numbers))    
    
##------------------------------------------------------------##   
def quick(N):
   # numbers = [34, 2, 34, 55, 67, 28, 12, 8, 10, 77] 
    numbers = [ ]
    for i in range(0, N):
        numbers.append(randint(0, 20000))
        
    quickSort(numbers)
    print("Quick Sort Succeeded:", check(numbers)) 
    
##------------------------------------------------------------##   
def heap(N):
#    numbers = [34, 2, 34, 55, 67, 28, 12, 8, 10, 77] 
    numbers = [ ]
    for i in range(0, N):
        numbers.append(randint(0, 20000))
        
    heapSort(numbers)

    print("Heap Sort Succeeded:", check(numbers)) 
    
    
#################  M A I N ########################
function = [selection, bubble, merge, quick, heap]

while True:
    
    size = eval(input("Size of List to sort (None to stop): "))
    if size == None: break
    
    choice = eval(input(" 1. Selection\n 2. Bubble\n 3. Merge\n 4. Quick\n 5. Heap\n"))

    function[choice-1](size)
    print()
    
print("Good Bye")




