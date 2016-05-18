#---------------------------------------------
# CS2020
#
# Defining a Cat prototype with a constructor
#    No data members are defined at the prototype level
#    Each individual has its own copy of data members.
#    Data members are not shared anymore
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

#------- This defines a Cat prototype with a constructor ---------#
class Cat:
    
    def __init__(self):
        self.name = "unknown"
        self.weight = 0.0
        self.age = 0
        
#----------------------------------------------#

##=========== Main ======================##    

kiki   = Cat()
bonbon = Cat()

print(kiki)      #these will print the prototype name
print(bonbon)    #and the addresses they are stored

print(kiki.name)   #prints the default name of kiki

##print(bonbon.__class__.name)  #see explanation below; this statement is invalid
                                #because at this point, there no prototype-level
                                #data member called 'name'

kiki.height = 7.5   #we still can define a unique data member to a specific instance
print(kiki.height)

Cat.name = "not given"  #this dynamically defines a prototype-level data member
Cat.weight = 1.0

print(bonbon.name)
print(bonbon.__class__.name)
