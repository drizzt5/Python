#--------------------------------
#
# CS 3023 Prog 2 tank.py
# Author: Dillon Glasser
#
# This is an object-oriented version of CS 2020 Prog 2
# with modifications. The program is composed of three
# major pieces: TankManager, Tank, and the main program. Tank
# and TankManager classes are defined in tank.py
#
# All interactions with the users are handled by this main
# program. Specification for each function is provided as
# the header comment. It outlines what each function is
# supposed to do.
#-------------------------------


from tank import Tank, TankManager

ADD         = 1
DELETE      = 2
TRANSFER    = 3
SEARCH_AMT  = 4
SEARCH_YEAR = 5

LOAD_DATA   = 6
SAVE_DATA   = 7

QUIT        = 0


#Display menu choices and
#return the selection to the caller
def displayMenu( ):
    while True:
        choice = input("\nMenu: \n" + \
                       "   Add         ---> 1\n" + \
                       "   Delete      ---> 2\n" + \
                       "   Transfer    ---> 3\n" + \
                       "   Search Amt  ---> 4\n" + \
                       "   Search Year ---> 5\n" + \
                       "   Load Data   ---> 6\n" + \
                       "   Save Data   ---> 7\n" + \
                       " ----------------------\n" + \
                       "   Quit        ---> 0\n")

        choice = int(choice)

        if QUIT <= choice <= SAVE_DATA:
            return choice

        else:
            print("Error: Invalid selection. Try again.\n")
'''
Add

1. Get information for a new tank from the user.
2. Create a new Tank from the given information.
3. Request TankManager to add this Tank to the collection.
4. Inform the user whether the new Tank is added to the collection or not.
'''
def add():
    id = input("Enter new Tank ID: ")
    if Tank.isIDValid(id) == False:
        print("Invalid ID entered.\n Tank Not Added.")
        return
    pNumber = input("Enter Part Number: ")
    amtLeft = input("Enter Amount Left: ")
    capacity = input("Enter Capacity: ")
    date = input("Enter the date (Y-M-D): ")
    newTank = id +"," + pNumber + "," + amtLeft + "," + capacity + "," + date
    addedTank = Tank(newTank)
    if tank_manager.add(addedTank) == True:
        print("Tank with ID: %s Added." % id)
    else:
        print("Tank Not Added.")

'''
Delete

1. Get the id of a tank to remove
2. Ask the Tank class that the id has the valid format. If invalid, print
   out error message and exit (return)
3. Add the tank manager to delete a tank with this id.
4. Inform the user whether a tank is deleted or not.
'''
def delete():
    id = input("Enter the id of the tank you want to remove: ")
    if Tank.isIDValid(id) == False:
        print("Invalid ID entered. \n Back to Menu.")
        return
    if tank_manager.delete(id) == True:
        print("Tank with ID: %s terminated." % id)
    else:
        print("Tank Not terminated.")

'''
Transfer

1. Get the id of the source and destination tanks.
2. Ask the Tank class that the ids have the valid format. If either one is invalid, print
   out error message and exit (return)
3. Get the amount to transfer. Repeat until you get a positive value for amount.
4. Ask the tank manager to transfer the amount from the source to the destination tank.
5. Inform the user whether the requested transfer is successfully completed or not.
'''
def transfer():
    sID = input("Enter source ID: ")
    if Tank.isIDValid(sID) == False:
        print("Invalid ID entered. \n Back to Menu.")
        return
    dID = input("Enter Destination ID: ")
    if Tank.isIDValid(dID) == False:
        print("Invalid ID entered. \n Back to Menu.")
        return
    transferAMT = 0
    while(transferAMT <= 0):
        transferAMT = int(input("Enter positive amount to transfer: "))

    if tank_manager.transfer(sID, dID, transferAMT) == True:
        print("Tank ID: %s transfered %d to Tank ID: %s" % (sID, transferAMT, dID))
    else:
        print("Did not transfer.")

'''
Search by Amount

1. Get the amount to search from the user.
2. Get the search type (< , == , >) from the user.
3. Request the tank manager to retrieve tanks that match the search criteria.
4. Display the result by using the display function defined here.
'''
def search_by_amount():
    amount = int(input("Enter the amount you are looking for: "))
    print("Enter [ < ] for less than the amount you entered. \n"
          "Enter [ > ] for greater than the amount you entered. \n"
          "Enter [ == ] for equal to the amount you entered.")
    symbol = input("Enter <, >, or == : ")
    if symbol == '<':
        search_type = -1
    elif symbol == '>':
        search_type = 1
    elif symbol == '==':
        search_type = 0
    else:
        print("\nInvalid symbol entered.\n Back to menu!")
        return
    tanks = tank_manager.search_by_amount(amount, search_type)
    display(tanks)


'''
Search by Year
1. Get the year to search from the user.
2. Get the search type (< , == , >) from the user.
3. Request the tank manager to retrieve tanks that match the search criteria.
4. Display the result by using the display function defined here.
'''
def search_by_year():
    year = int(input("Enter the year you are looking for: "))
    print("Enter [ < ] for less than the year you entered. \n"
          "Enter [ > ] for greater than the year you entered. \n"
          "Enter [ == ] for equal to the year you entered.")
    symbol = input("Enter <, >, or == : ")
    if symbol == '<':
        search_type = -1
    elif symbol == '>':
        search_type = 1
    elif symbol == '==':
        search_type = 0
    else:
        print("\nInvalid symbol entered.\n Back to menu!")
        return
    tanks = tank_manager.search_by_year(year, search_type)
    display(tanks)

'''
Load Data

1. Get the name of a file to load the tank data from the user
2. Get the load type (erase the current collection or add to the current collenction)
   from the user.
3. Request the tank manager to load the data from the designated file and load type
'''
def load_data():
    filename = input("Enter the filename: ")
    eraseAdd = input("Would you like to erase or add?: ")
    tank_manager.loadData(filename, overWrite(eraseAdd))

    print("\n%s Loaded!\n" % filename)

def overWrite(eraseAdd):
    if eraseAdd == "erase":
        return False
    if eraseAdd == "add":
        return True




'''
Save Data

1. Get the name of a file to save the tank data from the user
2. Request the tank manager to save the data to the designated file.
'''
def save_data():
    filename = input("Enter the filename you want to save as: ")
    tank_manager.saveData(filename)

    print("\n%s has been saved!\n" % filename)


'''
    Display

    Display the tank information in the passed tank list

    Parameter - tanks (list)      list of Tank objects

    Return    - None
    '''
def display(tanks):

    ## Implement the Tank class appropriately, so this code
    ## works as intended.

    ## DO NOT MODIFY this function ##

    print(Tank.getHeader())

    for tank in tanks:
        print(tank.formatted_str())


########################################################################

#--------------------------------------------#
#               M A I N                      #
#                                            #
#--------------------------------------------#


if __name__ == '__main__':

    tank_manager = TankManager()


    while True:
        selection = displayMenu()

        if selection == ADD:
            add()

        elif selection == DELETE:
            delete()

        elif selection == TRANSFER:
            transfer()

        elif selection == SEARCH_AMT:
            search_by_amount()

        elif selection == SEARCH_YEAR:
            search_by_year()

        elif selection == LOAD_DATA:
            load_data()

        elif selection == SAVE_DATA:
            save_data()

        else: #QUIT
            break
    #
    #
    # outputfile = input("Enter output filename: ")
    # saveData(outputfile, tanks)

    print("Program shuts down. Good-Bye.")
