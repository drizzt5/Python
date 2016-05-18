#---------------------------------------------
# CS2020
#
# Defining a Cat prototype with a constructor and __str()__ method
# The constructor requires parameters
#    
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

#------- This defines a Cat prototype with a constructor ---------#
class Cat:
    
    def __init__(self, aName, aWgt, anAge):
        self.name = aName
        self.weight = aWgt
        self.age = anAge
        
    def __str__(self):
        return "Name: " + self.name + " Weight: " + str(self.weight) + " Age: " + str(self.age)

#----------------------------------------------#

kiki = Cat("Ms. Kiki", 12.5, 17)

print(kiki)  # This calls __str__ method

print(kiki.name)
print(kiki.weight)
print(kiki.age)

print("%s is %2d years old and weighs %4.2f lbs" % (kiki.name, kiki.age, kiki.weight))
