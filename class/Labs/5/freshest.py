# gradesheet = {"umut": [100.0, 90.0, 30.0],
#               "dillon": [20.0, 10.0, 100.0, 70.0]}
#
#
# for key in gradesheet:
#     if gradesheet[key] == max(gradesheet.values()):
#         print(key,gradesheet[key])

dicTest = {"a": [4,1,8],
            "b": [7,5,2],
            "c": [100,25,5]
           }

words = ["one", "hi", "wine", "two", "vodka", "brandy", "wren"]

def insert(L, X):

    result = [ ]
    i = 0

    while i < len(L) and L[i] <= X:
        result.append(L[i])
        i += 1

    result.append(X)

    return result + L[i:]

def in_sort(L):

    if L == []:
        return []

    else: ## recurse and sort the remainder L[1:],
          ## then insert X into the returned sorted list
        return insert(in_sort(L[1:]), L[0])



for key in dicTest:
    dicTest[key] = in_sort(dicTest[key])

#for i in range(0, len(words)-1):

print(in_sort(words))


print(dicTest)

#
# for key in dicTest:
#     print(dicTest[key])


print([dicTest.items()])