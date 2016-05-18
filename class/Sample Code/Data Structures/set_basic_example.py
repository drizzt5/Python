#---------------------------------------------
# CS2020
#
# Basic Set Manipulation Example
#
# Python 3.0
#
# Author: Thomas Otani
#
#-------------------------------------------

S = set([10, 20, 30])
T = set([20, 30, 40, 50])

print("S: ", S)
print("T: ", T)
print()

S.add(60)

U = S.union(T)

I = S.intersection(T)

D1 = S.difference(T)

D2 = T.difference(S)

print("U: ", U)
print("I: ", I)
print("D1:", D1)
print("D2:", D2)
print()

for item in S:
    if item in T: T.remove(item)
    
print("S: ", S)
print("T: ", T)
