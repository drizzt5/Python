#---------------------------------------------
# CS2020
#
# Defining a Cat prototype using a constructor with paramaters
# and default values. When the corresponding parameter is
# ot passed, the specified default value is assigned.
#    
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

#------- This defines a Cat prototype with a constructor ---------#
class Cat:
    
    def __init__(self, aName = "unknown", aWgt = 0.0, anAge = 0):
        self.name   = aName
        self.weight = aWgt
        self.age    = anAge
        
    def __str__(self):
        return "Name: " + self.name + " Weight: " + str(self.weight) + " Age: " + str(self.age)
        
#----------------------------------------------#

kiki = Cat("Ms. Kiki", 12.5, 17)
stray = Cat()
bonbon = Cat("Bon-Bon", 10.7)

print(kiki)  # This calls __str__ method
print(stray)
print(bonbon)

