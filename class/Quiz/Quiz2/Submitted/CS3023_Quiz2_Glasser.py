###########################
#   CS3023 Quiz 2
#
#   Dillon Glasser
#
#   4 Questions
###########################

# Question 1

words = ["one", "hi", "wine", "two", "vodka", "brandy", "wren"]


def groupWords(WL):
    wordD2 = {}

    for w in words:
        wordD2[len(w)] = []

    for w in words:
            wordD2[len(w)].append(w)

    list = []
    for item in wordD2.items():
        for s in item[1]:
            list.append(s)
    return list

print(groupWords(words))




# Question 2

class Student:

    def __init__(self, name = "No Name", age = 0, grade = "X"):
        self.NAME = name
        self.AGE = age
        self.GRADE = grade

    def __str__(self):
        return "Name: " + self.NAME + " Age: " + str(self.AGE) + " Grade: " + self.GRADE

    def getName(self):
        return self.NAME

    def getAge(self):
        return self.AGE

    def getGrade(self):
        return self.GRADE

    def setAge(self, age):
        self.AGE = age

    def setGrade(self, grade):
        self.GRADE = grade


SL = {}


s = Student(name = "Samuel Adams", age = 43, grade = "B")
name = s.getName()
grade = s.getGrade()
SL[name] = [grade]

t = Student(name = "Jay", age = 42, grade = "A")
name = t.getName()
grade = t.getGrade()
SL[name] = [grade]

u = Student(name = "Kay", age = 43, grade = "C")
name = u.getName()
grade = u.getGrade()
SL[name] = [grade]

v = Student(name = "May", age = 43, grade = "B")
name = v.getName()
grade = v.getGrade()
SL[name] = [grade]

w = Student(name = "Way", age = 43, grade = "D")
name = w.getName()
grade = w.getGrade()
SL[name] = [grade]

x = Student(name = "Qay", age = 43, grade = "F")
name = x.getName()
grade = x.getGrade()
SL[name] = [grade]


print(s)

# Question 3

def distribute(S):
    gd = {}
    gd['A'] = []
    gd['B'] = []
    gd['C'] = []
    gd['D'] = []
    gd['F'] = []
    for item in S.items():
        if item[1] == ['A']:
            gd['A'].append(item[0])
        elif item[1] == ['B']:
            gd['B'].append(item[0])
        elif item[1] == ['C']:
            gd['C'].append(item[0])
        elif item[1] == ['D']:
            gd['D'].append(item[0])
        elif item[1] == ['F']:
            gd['F'].append(item[0])

    return gd

print(distribute(SL))



#Question 4


z = Student(name = "Qay", age = 5, grade = "A")
myList = [s.getName(),t.getName(),u.getName(),v.getName(),w.getName(),x.getName(),z.getName()]

def has_duplicates(S):
    testSet = set(S)
    if len(testSet) == len(S):
        return False
    else:
        return True

print(has_duplicates(myList))
