gradesheet = {"umut": [100.0,90.0,30.0],
              "dillon": [20.0, 10.0, 100.0, 70.0]}

print('umut' in gradesheet)



#gradesheet.items
high = 0
for item in gradesheet.items():
    if len(item[1]) >high:
        high = len(item[1])
        name = item[0]
print(name)


low = 0
for key in gradesheet:
    if len(gradesheet[key]) > low:
        low = len(gradesheet[key])
        name = key
print(name)


#3rd question

for item in gradesheet.items():
    item[1].remove(min(item[1]))
print(gradesheet)

gradesheet["umut"].append(65.0)
gradesheet["dillon"] = [65.0, 75.0, 85.0]
print(gradesheet)

for key in gradesheet:
    gradesheet[key].remove(min(gradesheet[key]))
print(gradesheet)


def highGrade2(gradesheet):
    L = []
    for item in gradesheet.items():
        maxi = max(item[1])
        L.append((item[0],maxi))
    return L

def highGrade(gradesheet):
    L = []
    for key in gradesheet:
        L += [(key,max(gradesheet[key]))]
    return L

def uj(gradesheet):

    L=[]

    for item in gradesheet.items():

        L.append((item[0],max(item[1])))
    return L
print(uj(gradesheet))

print(highGrade2(gradesheet))

for item in gradesheet.items():
    print(item)