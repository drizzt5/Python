#---------------------------------------------
# CS2020
#
# Towers of Hanoi
#
# Python 3.0
#
# Author: Thomas Otani
#
#-------------------------------------------

def moveOne(fro, to) :
    print(str(fro) + " ---> " + str(to))


def towersOfHanoi(N, fro, to, spare) :

    if N == 1:
        moveOne(fro, to)
    else:
        towersOfHanoi(N-1, fro, spare, to)
        moveOne(fro, to)
        towersOfHanoi(N-1, spare, to, fro)
	
	
##------------------- main ---------------------------##
towersOfHanoi(2, 1, 3, 2)
print()
towersOfHanoi(3, 1, 3, 2)
print()
towersOfHanoi(4, 1, 3, 2)