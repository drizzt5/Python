from person import Person

member = {}
ageGroup = {}


ssn = input("Enter SSN: ")
name = input("Enter Name: ")
age = int(input("Enter Age: "))
address = input("Enter Address: ")

each_person = Person(ssn, name, age, address)


while ssn != "000":
    if age > 0 and isinstance(age, int):

        each_person.setAge(age)


        member[ssn] = [each_person]
    else:
        print("Wrong Value for Age")

    ssn = input("Enter SSN: ")
    if ssn == "000":
        break
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    address = input("Enter Address: ")

print(member)
for key in member:
    print(member[key][0])
    print(member[key][0].age)

alist = [0,10,20,30,40,50,60,70,80,90,100]



for i in alist:
    ageGroup[i] = []
    for key in member:
        if member[key][0] >= i and member[key][0] < i+10:
            print(member[key][1])
            #ageGroup[i].append(member[key][0])


# print(ageGroup)
# for key in member:
#     print(member[key][])

# for i in alist:
#     ageGroup[i] = []
#     for key in member:
#         print(member[key][0].name)


## printing names in dict
# for key in member:
#     print(member[key][0])

# for item in member.items():
#     print(item[1][0])


#trying to print object names
# print("\n")
# print("Objects:")
# for i in people:
#     print(each_person)