#---------------------------------------------
# CS2020
#
# The file contains two search algorithms: linear
# and binary. The binary search works only on the
# sorted list.
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

NOT_FOUND = -1

'''
Linear Search
'''
def linearSearch(L, searchValue):
    loc = 0
    size = len(L)
    
    while loc < size:
        if L[loc] == searchValue:
            return loc
        
        loc += 1
        
    return NOT_FOUND

'''
Binary Search
The list L must be sorted in ascending order
'''
def binarySearch(L, searchValue):
    low = 0
    high = len(L) - 1
    
    while low <= high: # more elements to search
        
        mid = (low + high) // 2
        
        if L[mid] == searchValue:
            return mid
        
        elif L[mid] < searchValue: # search the upper half
            low = mid + 1
            
        else: # L[mid] > searchValue  # search the lower half
            high = mid - 1
            
    return NOT_FOUND

