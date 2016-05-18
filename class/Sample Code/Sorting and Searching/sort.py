#---------------------------------------------
# CS2020
#
# The file contains five sorting algorithms: 
#    selection
#    bubble
#    merge
#    quicksort
#    heapsort
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

'''
Selection Sort
'''
def selectionSort(L):
    size = len(L)
    
    for startIdx in range(0, size-1):  # number of passes 
        
        minIdx = startIdx
        
        for i in range(startIdx+1, size): # find min in one pass
            if L[i] < L[minIdx]:
                minIdx = i
                
        L[startIdx], L[minIdx] = L[minIdx], L[startIdx] #swap the two
        
'''
Bubble Sort
'''
def bubbleSort(L):
    bottom = len(L) - 1
    
    while True:
        
        isSwapped = False
        
        for i in range(0, bottom):           
            if L[i] > L[i+1]: #out of order so swap
                L[i], L[i+1] = L[i+1], L[i]
                isSwapped = True
                
        if not isSwapped: # no swap is made so the list is sorted
            return
        
        #largest value is at the bottom, reduce the bottom by one
        #for the next iteration
        bottom -= 1      

'''
Merge sort
Recursive sorting routine
We will use a nested function definition for the recursion part
''' 
def mergeSort(L):  
    
    #parameter L is visible to nested functions
    
    def merge(low, mid, high):
        
        loc = low
        i = j = 0
        left = L[low:mid+1]         #divide into left (lower) and
        right = L[mid+1:high+1]     #right (upper) halves

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                L[loc] = left[i]
                i += 1
            else:
                L[loc] = right[j]
                j += 1
                            
            loc += 1
                
        #move any remaining elements from either the left
        #or the right half; only one of the two while is iterated       
        while i < len(left):
            L[loc] = left[i]
            loc += 1
            i += 1
            
        while j < len(right):
            L[loc] = right[j]
            loc += 1
            j += 1
  
            
    def sort(low, high): 
             
        if low < high: # more items in the list to sort
            
            mid = (low + high) // 2
            sort(low, mid)         # sort the lower half
            sort(mid+1, high)      # sort the upper half
            
            merge(low, mid, high)  # merge the two sorted lists
    
    sort(0, len(L)-1)
         
'''
Quicksort
Another recursive sorting routine
'''
def quickSort(L):
    
    def partition(low, high):
        i = low
        j = high
        pivot = L[low]
        
        while i < j:
            while i < j and pivot <= L[j]: 
                j -= 1       
            L[i] = L[j]
            
            while i < j and pivot >= L[i]: 
                i += 1       
            L[j] = L[i]
        
        L[i] = pivot
        
        return i      
              
    def sort(low, high):
        
        if low < high:
            mid = partition(low, high) #pivot is in position L[mid]
            sort(low, mid-1)
            sort(mid+1, high)
    
    sort(0, len(L)-1)
          
       
'''
Heap Sort
'''
def heapSort(L):
    
    # loc - index of the node; size - # of nodes in heap
    def hasChild(loc, size):
        return 2*loc+1 <= size-1
    
    # loc - index of the node; size - # of nodes in heap
    def maxChildIdx(loc, size):
        leftChildIdx = 2*loc + 1
        rightChildIdx = 2*loc + 2
        
        if rightChildIdx < size and L[leftChildIdx] < L[rightChildIdx]: 
            return rightChildIdx
        else:
            return leftChildIdx
        
    
    def construct():
        
        for i in range(len(L)-2//2, -1, -1):
            
            current = i
            done = False
            
            while not done:              
                if not hasChild(current, len(L)): #current has no child
                    done = True
                else: 
                    maxIdx = maxChildIdx(current, len(L))
                    if L[current] < L[maxIdx]:
                        L[current], L[maxIdx] =  L[maxIdx], L[current]
                        current = maxIdx #go down the heap
                    else:
                        done = True
    
    def extract():
        
        for last in range(len(L)-1, -1, -1):
            
            L[0], L[last] = L[last], L[0]
            
            current = 0
            done = False
            
            while not done:
                if not hasChild(current, last):
                    done = True
                else:
                    maxIdx = maxChildIdx(current, last)
                    if L[current] < L[maxIdx]:
                        L[current], L[maxIdx] =  L[maxIdx], L[current]
                        current = maxIdx 
                    else:
                        done = True
                        
    construct()
    extract()                   
                
                
        
        
        
                  
                