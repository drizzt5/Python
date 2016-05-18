#---------------------------------------------
# CS2020
#
# Defining a Cat prototype
#     Most basic format
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

#------- This defines a Cat prototype ---------#
class Cat:
    name = "unknown"
    weight = 0.0
#----------------------------------------------#

##=========== Main ======================##    

kiki   = Cat()
bonbon = Cat()

print(kiki)      #these will print the prototype name
print(bonbon)    #and the addresses they are stored

#Individual are not customized yet, so
#the following will print the values set for the prototype
print(kiki.name)
print(kiki.weight)

print(bonbon.name)
print(bonbon.weight)

#Customize kiki
kiki.name = "Lovely Kiki"
kiki.weight = 12.5

print(kiki.name)
print(kiki.weight)

print(bonbon.name)
print(bonbon.weight)

#Now what happens when the value of the prototype Cat
#is updated

Cat.name = "not given"
Cat.weight = 1.0

kiki.color = "black"
print(kiki.name)     #kiki has customized values so no changes
print(kiki.weight)
print(kiki.color)

print(bonbon.name)   #bonbon has no customized values, it still points to
print(bonbon.weight) #to the prototype
##print(bonbon.color) #<--- ERROR


