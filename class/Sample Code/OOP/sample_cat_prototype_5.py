#---------------------------------------------
# CS2020
#
# Defining a Cat prototype with accessors and mutators.
# Accessors are also called get methods and mutators
# set methods. We can provide additional protection
# by making clients interact with objects strictly
# via the defined accessors and mutators.
#    
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

#------- This defines a Cat prototype with a constructor ---------#
class Cat:
    
    def __init__(self, aName = "unknown", aFamilyName = "NFN", aWgt = 0.0, anAge = 0):
        self.first  = aName
        self.last   = aFamilyName
        self.weight = aWgt
        self.age    = anAge

        
    def __str__(self):
        return "Name: " + self.last + "," + self.first + " Weight: " + str(self.weight) + " Age: " + str(self.age)
        # or
        #return "Name: " + self.fullname() + " Weight: " + str(self.weight) + " Age: " + str(self.age)
 
    #-------------------- Accessors ------------------------#  
    #-- Use 'get' prefix for accessors to avoid possible  --#
    #-- conflicts with some features of Python            --#
                                  
    def getAge(self):
        return self.age
    
    def getWeight(self):
        return self.weight
    
    def getHeight(self):
        return self.height
    
    def getLast(self):
        return self.last
    
    def getFirst(self):
        return self.first
    
    def getFullname(self):
        return self.last + ", " + self.first

    #------------------ Mutators -----------------------------#
    #-- Use 'set' prefix for mutators for naming convention --#
    
    def setFirst(self, value):
        self.first = value


    def setLast(self, value):
        self.last = value


    def setWeight(self, value):
        if value >= 1.0:
            self.weight = value
            
            
    def setAge(self, value):
        if value > 0:
            self.age = value
    
        
#----------------------------------------------#

kiki = Cat("Kiki", "Otani", 12.5, 17)
bonbon = Cat("Bon-Bon", "Otani", 10.7)

print(kiki.getFullname())
print(bonbon.getFullname())

bonbon.setAge(-10)
kiki.setAge(18)

print(kiki.getFirst() + " will be " + str(kiki.getAge()+10) + " in 10 years")

print(bonbon)



