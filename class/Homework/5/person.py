class Person:

    def __init__(self, SSN = "000-00-0000", NAME = "No Name", AGE = 0, ADDRESS = "1"):
        self.ssn = SSN
        self.name = NAME
        try:
            self.age = int(AGE)
        except:
            self.age = 0
            print("Error: Invalid input for Age. Default used instead.")
        self.address = ADDRESS

    def __str__(self):
        return "SSN: " + self.ssn + "\t|\tName: " + self.name + "\t|\tAge: " + str(self.age)

    def getSsn(self):
        return self.ssn

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getAddress(self):
        return self.address

    def setSsn(self, ssn):
        self.ssn = ssn

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        try:
            self.age = int(age)
        except:
            print("Error: You must enter an Integer. No changes made.")

    def setAddress(self, address):
        self.address = address

    def multiplyTwo(self):
        self.age = self.age * 2