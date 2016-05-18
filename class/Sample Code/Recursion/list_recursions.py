#---------------------------------------------
# CS2020
#
# Recursive List Manipulations
#
# Python 3.0
#
# Author: Thomas Otani
#
#-------------------------------------------

#Compute sum of elements in a given list
def sum(list) :
    
    if list == [] :
        return 0
    else:
        return list[0] + sum(list[1:])
    

#Same as sum but without creating sublist
#every time recursive call is made
#We pass the second argument to specify
#the location of next element to add
def sum2(list, idx) :
    
    if idx == len(list) - 1 :
        return list[idx]
    else:
        return list[idx] + sum2(list,idx+1)
    
    
#Same as sum2 but with tail recursion improvement
#every time recursive call is made
#We pass the third argument to keep the running total
def sum3(list, idx, total) :
    
    if idx == len(list) - 1 :
        return list[idx] + total
    else:
        return sum3(list, idx+1, list[idx] + total)    
    
    
    
#Return the index of position of the first 
#match item found in a given list
#Retun None if the item is not in the list
#This is similar to the standard list 'find' method
#but this one does not treat 'not found' case as an error
def find(list, item, idx) :
    if idx == len(list) :
        return None
    elif item == list[idx]:
        return idx
    else:
        return find(list, item, idx+1)
    
    
    
#Return the number times the item is found in
#a given list. Works like the standard list 'count' method
def count(list, item, idx) :
    if idx == len(list) :
        return 0
    elif item == list[idx]:
        return 1 + count(list, item, idx+1)
    else:
        return count(list, item, idx + 1)
    
    
    
#Return the reverse of a given list
#Work the same as the standard list 'reverse' method
def reverse(list) :
    if list == [] :
        return [ ]
    else:
        return reverse(list[1:]) + [list[0]]
    
    
    
#Same as reverse, but without list concatenation
def reverse2(list):
    if list == []:
        return []
    else:
        rev = reverse2(list[1:])
        rev.append(list[0])
        return rev
    
        ##NOTE: the else part cannot be written as
        ##   return reverse2(list[1:]).append(list[0])
        ##
        ## because the append method is a void function
        
    
    
    
##------------------- main -------------------------##
numlist = [10, 20, 30, 40, 50, 60]

print(sum(numlist))
print(sum2(numlist,0))
print(sum3(numlist,0,0))

numlist = [10, 20, 10, 20, 30, 10, 20]
print(find(numlist, 30, 0))
print(count(numlist, 10, 0))

numlist = [10, 20, 30, 40, 50]
print(reverse(numlist))
print(reverse2(numlist))