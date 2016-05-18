from cs3023_quiz3_q1_pet import Pet

class Kennel:


    def __init__(self):
        # self._Pet = {} # dictionary of pets
        # self._PetGroup = PetGroup
        self._PetGroup["tall"]
        self._PetGroup["grande"]
        self._PetGroup["venti"]


    def add(self, Pet):
        if Pet.age <= 5:
            self._PetGroup["tall"] = self._PetGroup["tall"] + [Pet]
        elif Pet.age <=10:
            self._PetGroup["grande"] = self._PetGroup["grande"] + [Pet]
        else:
            self._PetGroup["venti"] = self._PetGroup["venti"] + [Pet]



    def getGroup(self, groupNo):
        if groupNo == 1:
            return self._PetGroup["tall"]
        elif groupNo == 2:
            return self._PetGroup["grande"]
        elif groupNo == 3:
            return self._PetGroup["venti"]
        else:
            print("Wrong size, I mean group number.")



##main?

ken = Kennel()
ken.add(Pet("Jim", 2, 3.0, Pet.DOG))

babies = ken.getGroup(1)

print(babies)