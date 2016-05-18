class Student:

    def __init__(self, name = "No Name", age = 0, grade = "X"):
        self.NAME = name
        self.AGE = age
        self.GRADE = grade

    def __str__(self):
        return "Name: " + self.NAME + " Age: " + str(self.AGE) + " Grade: " + self.GRADE

    def getNAME(self):
        return self.NAME

    def getAGE(self):
        return self.AGE

    def getGRADE(self):
        return self.GRADE

    def setAGE(self, age):
        self.AGE = age

    def setGRADE(self, grade):
        self.GRADE = grade

s = Student(name = "Samuel Adams", age = 43, grade = "B")


print(s)