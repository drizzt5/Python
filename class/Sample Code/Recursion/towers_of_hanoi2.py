#---------------------------------------------
# CS2020
#
# Towers of Hanoi
#
# This version indents the output lines to clearly
# the levels of nesting
#
# Python 3.0
#
# Author: Thomas Otani
#
#-------------------------------------------
def moveOne(fro, to, indent) :
    print(("%" + str(2*indent) + "d ---> %d") % (fro, to))


def towersOfHanoi(N, fro, to, spare, indent) :

    if N == 1:
        moveOne(fro, to, indent)
    else:
        towersOfHanoi(N-1, fro, spare, to, indent+1)
        moveOne(fro, to, indent+1)
        towersOfHanoi(N-1, spare, to, fro, indent+1)
	
	
	
##------------------- main ---------------------------##
towersOfHanoi(2, 1, 3, 2, 0)
print()
towersOfHanoi(3, 1, 3, 2, 0)
print()
towersOfHanoi(4, 1, 3, 2, 0)