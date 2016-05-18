#Question 1

gradesheet = {'John Smith': [90.0, 70.0, 100.0],
              'Dillon': [10.0, 20.0, 30.0, 40.0, 50.0, 60.0],
              'Umut': [50.0, 60.0, 70.0, 85.0],
              'Alex': [90.0, 95.0, 100.0]

              }
print("Dictionary we are working with:")
#print(gradesheet)
print(gradesheet.items())
print(gradesheet.values())
print(gradesheet.keys())
print("\n")

# Add a value to Umut's grades
gradesheet['Umut'].append(100.0)
# Print the last value of the list
print(gradesheet['Umut'][-1])



#a. Write an expression to check if student "John Smith" is in the gradesheet dictionary.
print("Is John Smith in gradesheet?")
if "John Smith" in gradesheet:
    print("Yes\n")


#b.
# display the student with the most test scores
print("Who has the most test scores?")
most = 0
for item in gradesheet.items():
    if len(item[1])>most:
        most = len(item[1])
        name = item[0]
print(name + "\n")


#b2.
# My own challenge. Display the student with the least test scores.
print("Who has the least test scores?")
least = most
for key, value in gradesheet.items():
    if len(value) < least:
        least = len(value)
        name = key
print(name + "\n")


#C.
# write a code fragment to remove the lowest test score from all students
print("remove lowest test score")
for item in gradesheet.items():
    item[1].remove(min(item[1]))
print(gradesheet.items())

# Professor recommends key and values
print("Remove highest test score")
for value in gradesheet.items():
    value[1].remove(max(value[1]))
print(gradesheet.items())
print("\n")


def uj(gradesheet):

    L=[]

    for item in gradesheet.items():

        L.append((item[0],max(item[1])))
    return L
print(uj(gradesheet))

#regular way
print("Two different ways of displaying the top test score with name for each student:")
def highPairs(gradesheet):
    result=[]
    for key,value in gradesheet.items():
        result.append((key, max(value)))
    return result
print(highPairs(gradesheet))

#listcomp way

def highPairs2(gradesheet):
    return [(key,max(value)) for key, value in gradesheet.items()]

print(highPairs2(gradesheet))








