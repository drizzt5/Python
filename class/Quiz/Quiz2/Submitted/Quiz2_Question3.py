class Person:

    def __init__(self, SSN = "000-00-0000", NAME = "No Name", AGE = 0, ADDRESS = "1"):
        self.ssn = SSN
        self.name = NAME
        self.age = AGE
        self.address = ADDRESS

    def __str__(self):
        return "SSN: " + self.ssn + " Name: " + self.name + " Age: " + str(self.age)

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
        self.age = age

    def setAddress(self, address):
        self.address = address

    def multiplyTwo(self):
        self.age = self.age * 2


myDict = {}

ssn = input("Enter SSN: ")
name = input("Enter Name: ")
age = int(input("Enter Age: "))
address = input("Enter Address: ")

each_person = Person(ssn, name, age, address)

PL = []
PL.append(each_person)
print(PL)