from datetime import *



# x = date.today()
# y = date(2009, 5, 14)
#
#
# print(x)
# print(y)
# print(x-y)


#print(isIDValid("12-2000"))



class Tank:


    @staticmethod
    def getHeader():
        return "Header"   ### MOIDFY THIS  ###

    def isIDValid(x):
        idP = "0123456789"
        y = [0, 1, 3, 4, 5, 6]
        if len(x) == 7 and x[2] == '-':
            for i in y:
                print(x[i])
                if x[i] not in idP:
                    return False
        else:
            return False
        return True

    def __init__(self, id = '00-0000', pNumber = 'aaa-0000-0000', amtLeft = 0, capacity = 0, date = date(2000, 1, 1)):
        self._id = id
        self._pNumber = pNumber
        self._amtLeft = amtLeft
        self._capacity = capacity
        self._date = date


    def __str__(self):
        return "\t" + self._id + "\t\t" + self._pNumber + "\t\t" + str(self._amtLeft) \
    + "\t\t" + str(self._capacity) + "\t\t" + str(self._date)


    def getID(self):
        return self._id

    def getPNUMBER(self):
        return self._pNumber

    def getAMTLEFT(self):
        return self._amtLeft

    def getCAPACITY(self):
        return self._capacity

    def getDATE(self):
        return self._date

    def setPNUMBER(self, pNumber):
        self._pNumber = pNumber

    def setAMTLEFT(self, amtLeft):
        self._amtleft = amtLeft

    def setCAPACITY(self, capacity):
        self._capacity = capacity

    def setDATE(self, date):
        self._date = date


class TankManager:

    def __init__(self):
        self._tanks = { }  # dictionary for managing tanks
        self._tanks[self._id] = [self._pNumber, self._amtLeft, self._date]

    def loadData(self, filename, erase):
        if erase: self._tanks.clear()

        datafile = open(filename, "r")

        ## in the overwrite mode, erase == False,
        ## the data for the tank with duplicate id will
        ## be overwritten.
        for line in datafile:
            tank = Tank(line)

            self._tanks[tank.getID()] = tank

        datafile.close()


    def saveData(self, filename):

        datafile = open(filename, "w")

        for tank in self._tanks.values():
            datafile.write(str(tank))

        datafile.close()


tank1 = Tank('12-1234', 'abc-1234-1234', amtLeft=10, capacity= 30, date = (2001, 2, 5))

print(tank1)

mydict = {'george':16,'amber':19}
print(list(mydict.keys())[list(mydict.values()).index(16)])

search_age = 16
for name, age in mydict.items():
    if age == search_age:
        print(name)