# myDict = { "Car 1": "Red",
#            "Car 2": "Blue"
#         }
#
# print(myDict)
# print("Car dictionary ended \n")
#
#
# gradesheet = {'John Smith': [90.0, 70.0, 100.0],
#               'Dillon': [10.0, 20.0, 30.0, 40.0, 50.0, 60.0],
#               'Umut': [50.0, 60.0, 70.0, 80.0],
#               'Alex': [90.0, 95.0, 100.0]
#
#               }
#
# print(gradesheet)
# print("\n")
# print(gradesheet.items())
# print("\n")
# print(gradesheet.values())
# print("\n")
# print(gradesheet.keys())
# print("\n")
# print(gradesheet["Dillon"])
# print("\n")
#
#
# for key in gradesheet:
#     for x in range(len(gradesheet[key])):
#         gradesheet[key][x]+=1
#
#
# # for item in gradesheet.items():
# #     item[1].remove(min(item[1]))
# # print(gradesheet.items())
#
# print(gradesheet.items())

newdic = {"DOG": "Dog", "CAT": "Cat", "SNAKE": "Snake", "RABBIT": "Rabbit"}

newdic["ZEBRA"] = ["Zebra"]
newdic["ZEBRA"] = newdic["ZEBRA"] + ["Jake"]
print(newdic)
