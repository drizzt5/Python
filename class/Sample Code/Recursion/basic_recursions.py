#---------------------------------------------
# CS2020
#
# Basic functions implemented using recursion
#
# Python 3.0
#
# Author: Thomas Otani
#
#-------------------------------------------

#Compute Factorial of N >= 0
#
def factorial(N) :
    
    if N == 0:
        return 1
    else:
        return N * factorial(N-1)
    

#Compute 1 + 2 + ... + N, N >=1, recursively
def recSum(N) :
    
    if N == 1:
        return 1
    else:
        return N + recSum(N-1)
    
#Compute Nth Fibonacci number
#F(0) = 1, F(1) = 1, F(N) = F(N-1) + F(N-2), N >= 2
def fibonacci(N) :
    if N == 0 or N == 1:
        return 1
    else:
        return factorial(N-1) + factorial(N-2)
    
    
##------------------- main -------------------------##
print(factorial(5))
print(recSum(5))
print(fibonacci(5))