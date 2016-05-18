'''
CS3023 Spring 2016

Quiz 1

Sample Solution

'''


### Question 1 ###

'''
L is an ordered list. Create a new list by adding X to L
in the correct position so the new list is ordered.
'''
def insert(L, X):

    result = [ ]
    i = 0

    while i < len(L) and L[i] <= X:
        result.append(L[i])
        i += 1

    result.append(X)

    return result + L[i:]


'''
Recursive version of insert
'''
def rec_insert(L, X):

    if L == []:
        return [X]

    elif X < L[0]:
        return [X] + L  ## Topic: Recursion stops as we found the place for X

    else:
        return [L[0]] + rec_insert(L[1:], X)
                        ## L[0] goes before X; recurse and put X at the
                        ## postion amoung the remainder L[1:]


'''
Recursive version 2 of insert
This is a direct recursive translation of non-recursive insert.
We use a nested recursive function to keep adding elements
smaller than X into result until the correct position to insert X
'''
def rec_insert2(L, X):

    result = [ ]

    def rec_in(pos):
        if pos == len(L) or L[pos] > X:
            return pos
        else:
            result.append(L[pos])
            return rec_in(pos+1)

    xloc = rec_in(0)

    result.append(X)
    return result + L[xloc:]


##### Question 2 ######
def in_sort(L):

    if L == []:
        return []

    else: ## recurse and sort the remainder L[1:],
          ## then insert X into the returned sorted list
        return insert(in_sort(L[1:]), L[0])


##### Question 3 ######
def getAllPossibleTeams(nameList):

    if nameList == [ ]:
        return [[ ]]  ## We are returning a list of teams, with each
                      ## team as a list of names, so this is what we return at the end
    else:
        result = getAllPossibleTeams(nameList[1:])   ## list of teams for f(n-1)

        for i in range(len(result)):                 ## create list of teams for f(n)
            result.append([nameList[0]] + result[i]) ## by adding this name to all teams in f(n-1)

        return result

'''
Second version that uses the nested recursive function
'''
def getAllPossibleTeams_2(nameList):

    result = [ ]

    def rec_helper(team, names): ## team is current composed list
                                 ## names is available names to add
        if names == []:
            result.append(team)  ## when there are no names left, we're done

        else:                                        ## at each recursive level, either
            rec_helper(team, names[1:])              ## we don't include this name or
            rec_helper(team + [names[0]], names[1:]) ## we include it to the team


    rec_helper([], nameList)

    return result


### Question 4 ####
class Pet:
    def __init__(self, name = "No Name", age = 0):
        self._name = name
        self._age = age

    def __str__(self):
        return "Name: " + self._name + " Age: " + str(self._age)

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def setName(self, name):
        self._name = name

    def incAge(self):
        self._age += 1




if __name__ == '__main__':

    print(insert([10, 20, 30], 15))
    print(insert([], 15))
    print(insert([10, 20, 30], 35))

    print(rec_insert([10, 20, 30], 15))
    print(rec_insert([], 15))
    print(rec_insert([10, 20, 30], 35))

    print(rec_insert2([10, 20, 30], 15))
    print(rec_insert2([], 15))
    print(rec_insert2([10, 20, 30], 35))

    print(in_sort([5, 15, 12, 9, 7, 8]))
    print(in_sort([12]))
    print(in_sort([]))
    print(in_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

    print(getAllPossibleTeams(["A", "B", "C"]))
    print(getAllPossibleTeams_2(["A", "B", "C"]))


    p1 = Pet()
    p2 = Pet("Minnie", 10)
    print(p1)
    p1.setName("Mickey")
    print(p1)
    print(p2.getName(), p2.getAge())
    p2.incAge()
    print(p2.getName(), p2.getAge())