'''

    CS 3023 SPRING 2016

    QUIZ  2


'''


## ==============================================================================
##
##                QUESTION  1
##
##  Approach 1: With Dictionary (recommended approach)
##              For each word you encounter, add this word to the dictionary
##              entry table[len(word)]
##              To create the final result, you need to access the keys in the
##              word length order. There is a OrderedDict in the collections library
##              that maintains the order of the keys.
##                      from collections import OrderedDict
##
##  Approach 2: Without Dictionary
##              Reuse the idea of inserting a value into an ordered list.
##              Here the order is maintained by the length of a word.
## ==============================================================================


## Use a dictionary
def reorderWords(words):

    result = [ ]
    table = { }

    for word in words:
        w_len = len(word)

        if w_len in table:
            table[w_len].append(word)  ## Append word to the existing entry
        else:
            table[w_len] = [word]      ## new length found; create a new entry with this word

    for length in sorted(table.keys()): ## Dictionary entries are unordered
        result += table[length]         ## so we need to sort the keys

    return result


## Without using a dictionary
def reorderWords_2(words):

    result = []

    for word in words:

        ## find the index location to insert this word to maintain
        ## the list in word length order
        loc = 0
        while loc < len(result) and len(word) >= len(result[loc]):
            loc += 1

        result.insert(loc, word)

    return result

## ==============================================================================
##
##                QUESTION  2
##
## Normally we would include class definitions at the top of the source file, but
## here, we will list the definition in the middle to maintain the order of
## questions.
## ==============================================================================

class Student:

    def __init__(self, name = "No Name", age = 0, grade = "X"):
        self._name = name
        self._age = age
        self._grade = grade

    def __str__(self):
        return "Name: " + self._name + " Age: " + str(self._age) + " Grade: " + self._grade

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getGrade(self):
        return self._grade

    def setAge(self, age):
        self._age = age

    def setGrade(self, grade):
        self._grade = grade


## ==============================================================================
##
##                QUESTION  3
##
## ==============================================================================

def distribute(students):

    result =  { key : [ ] for key in "ABCDF"}

    # the above is a dictionary comprehension which is equivalent to
    # result = {}
    # result["A"] = []
    # result["B"] = []
    # result["C"] = []
    # result["D"] = []
    # result["F"] = []

    for student in students:
        result[student.getGrade()].append(student)

    return result


## ==============================================================================
##
##                QUESTION  4
##
## Create a set of student names. If the length of this set is less than the
## length of the Student list, then duplicate names exist.
##
## ==============================================================================

def has_duplicates(students):

    return len(set([s.getName() for s in students])) < len(students)


def has_duplicates_2(students):

    nameset= set([])

    for student in students:

        if student.getName() in nameset:
            return True

        nameset.add(student.getName())

    return False


## ==============================================================================
##
##                TEST MAIN
##
## ==============================================================================

if __name__ == '__main__':

    print("Question 1 Test")
    L = ["one", "five", "a", "I", "too", "to", "seven", "madam", "jack", "two"]
    print(reorderWords(L))
    print(reorderWords_2(L))
    print()

    print("Question 2 Test")
    s1 = Student()
    s2 = Student("Jack Daniel", 40, "A")
    print(s1)
    print(s2)
    print()

    print("Question 3 Test")
    names = "One Two Three Four Five Six Seven Eight Nine Ten".split()
    ages = [30, 30, 43, 20, 45, 18, 19, 10, 44, 20]
    grades = "A A B C A B C D F B".split()

    S = [Student(names[i], ages[i], grades[i]) for i in range(len(names))]

    ### FYI, you can create the S list like this too using the zip function ###
    # S = [Student(n, a, g) for n, a, g in list(zip(names, ages, grades))]

    # grade_dist = distribute(S)

    # for key in sorted(grade_dist.keys()):
    #     print(key)
    #     for student in grade_dist[key]:
    #         print("\t", student.getName(), student.getGrade())
    #     print()

    print("Question 4 Test")
    names = "One Two Three Two Ten".split()
    ages = [30, 30, 40, 44, 20]
    grades = "A A B C A".split()

    S2 = [Student(names[i], ages[i], grades[i]) for i in range(len(names))]

    print(has_duplicates(S))
    print(has_duplicates(S2))
    print()
    print(has_duplicates_2(S))
    print(has_duplicates_2(S2))


