#--------------------------------
#
# CS 3023 Prog 2 tank.py
# Author: Dillon Glasser
#
# This is an object-oriented version of CS 2020 Prog 2
# with modifications. The program is composed of three
# major pieces: TankManager, Tank, and the main program.
# All interactions with the users are handled by the main
# program. A Tank instance represents a single tank. A TankManager
# manages a collection of Tank instances. The tank manager handles
# all operations on the tank collection, such as, adding, deleting,
# updating, and searching.
#--------------------------------

from datetime import *

class Tank:
    '''
    Return the column header, used when displaying tank information
    You call this method using the class name as Tank.getHeader()
    '''

    @staticmethod
    def getHeader():
        return " Id\t\t\t\tSerial#\t\t\tAmt Left\t\t\tCapacity\t\tNext Maintenance"

    '''
    Return True if the given parameter is a valid ID format of dd-dddd
    You call this method using the class name as Tank.isIDValid("abcd")
    '''

    def isIDValid(x):
        idP = "0123456789"
        y = [0, 1, 3, 4, 5, 6]
        if len(x) == 7 and x[2] == '-':
            for i in y:
                #print(x[i])
                if x[i] in idP:
                    return True
        else:
            return False


    '''
    Initializer
    Parameter:
                line -- a single line of text that includes tank data such as
                        13-2222,ABC-9999-1234,34,50,2016-10-23
    '''

    def __init__(self,line):
        new_tank = line.split(",")
        self._id = new_tank[0]
        self._pNumber = new_tank[1]
        self._amtLeft = int(new_tank[2])
        self._capacity = int(new_tank[3])
        dateString = new_tank[4].split("-")
        self._date = date(int(dateString[0]), int(dateString[1]), int(dateString[2]))



    '''
    String conversion
    '''

    def __str__(self):
        return "%s,%s,%s,%s,%s\n" % (self._id, self._pNumber, str(self._amtLeft), str(self._capacity), str(self._date))

    '''
    Formatted string like
            15-9999        SAB-0000-9877           221          1300                2018-4-17
    '''
    def formatted_str(self):
        return "%s%20s%10d%20s%20s" % (self._id, self._pNumber, self._amtLeft, str(self._capacity), str(self._date))

     ### Add more methods ###

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
        self._tanks = {}  # dictionary for managing tanks


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

    '''
    Search by Amount

    Search the tank list for tanks with amount left less than, equal to, or greater than N
    where N is a threshold entered by the user.

    Parameter - amount (int)      the amount to compare
                search_type (int) negative, zero, or positive
                                  neg  means 'less than amount'
                                  zero means 'equal to amount'
                                  pos  means 'greater than amount'

    Return    - a list of tanks that match the search criteria
    '''
    def search_by_amount(self, amount, search_type):

        result = []

        for key in self._tanks:
            if search_type == -1:
                if self._tanks[key]._amtLeft < amount:
                    result.append(self._tanks[key])
            if search_type == 0:
                if self._tanks[key]._amtLeft == amount:
                    result.append(self._tanks[key])
            if search_type == 1:
                if self._tanks[key]._amtLeft > amount:
                    result.append(self._tanks[key])



        return result

    '''
    Search by Year

    Search the tank list for tanks with the year of the maintenance date equal to YYYY (e.g., 2015)
    YYYY is entered by the user

    Parameter - year (int)       the year to compare
                serch_type (int) negative, zero, or positive
                                 neg  means 'before year'
                                 zero means 'equal to year'
                                 pos  means 'after year'

    Return    - a list of tanks that match the search criteria
    '''

    def search_by_year(self, year, search_type):

        result = [ ]

        for key in self._tanks:
            if search_type == -1:
                if self._tanks[key]._date.year < year:
                    print(self._tanks[key]._date.year)
                    result.append(self._tanks[key])
            if search_type == 0:
                if self._tanks[key]._date.year == year:
                    print(self._tanks[key]._date.year)
                    result.append(self._tanks[key])
            if search_type == 1:
                if self._tanks[key]._date.year > year:
                    print(self._tanks[key]._date.year)
                    result.append(self._tanks[key])

        return result   ### MOIDFY THIS  ###

    '''
    Function Add

    Add the given tank to the collection. If the tank id already
    exists the collection, do nothing

    Parameter - tank (Tank)
                add this tank to the collection

    Return    - True if the tank is added; False otherwise
    '''
    def add(self, tank):
            if tank.getID() not in self._tanks:
                self._tanks[tank.getID()] = tank
                return True
            else:
                return False

    '''
    Delete

    Delete a tank with the given id from the collection if it exists. Otherwise,
    do nothing.

    Paramter - id (string)
               the id of a tank to be deleted if it exists in the collection

    Return   - True if the tank is deleted; False otherwise
    '''
    def delete(self, id):
            if id in self._tanks:
                del self._tanks[id]
                return True
            else:
                return False

    '''
    Transfer

    Transfer the specified amount from the source to destination tank. The operation
    fails if the specifed tanks don't exist or the specified amount cannot be
    transferred, such as the source tank does not have the specified amount or the
    capacity of the destination tank is not large enough to accept the full amount.

    Parameter - source_id (string)      -- id of tank to transfer amount from
                destination_id (string) -- id of tank to transfer amount to
                amount (int)            -- amount to transfer

    Return    - True if the full specified amount is transferred; False otherwise
    '''
    def transfer(self, source_id, destination_id, amount):
        if source_id not in self._tanks: #Does source tank exist ?
            print("Source tank does not exist.")
            return False
        if destination_id not in self._tanks: #Does destination tank exist?
            print("Destination tank does not exist.")
            return False
        if self._tanks[source_id].getAMTLEFT() < amount: #Does the source_id have enough?
            print("Source tank doesn't have enough for that.")
            return False
        if self._tanks[destination_id]._capacity-self._tanks[destination_id]._amtLeft < amount: #is remaining capacity adequate?
            print("Not enough capacity for that.")
            return False
        self._tanks[source_id]._amtLeft -= amount
        self._tanks[destination_id]._amtLeft += amount
        return True




