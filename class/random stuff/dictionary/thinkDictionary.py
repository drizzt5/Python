inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for akey in inventory.keys():     # the order in which we get the keys is not defined
   print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())
print(ks)


inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for k in inventory:
   print("Got key", k)



inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.values()))
print(list(inventory.items()))

for (k,v) in inventory.items():
    print("Got", k, "that maps to", v)

for k in inventory:
    print("Got", k, "that maps to", inventory[k])


inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")

if 'papaya' in inventory:
    print(inventory['papaya'])
else:
    print("We have no papaya")


inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}


print(inventory.get("apples"))
print(inventory.get("cherries"))
print(inventory.get("cherries", 0))


mydict = {"cat":12, "dog":6, "zebra":1, "bear":20}
keylist = list(mydict.keys())
keylist.sort()
print(keylist[3])


mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
answer = mydict["cat"] // mydict["dog"]
print(answer)

mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
answer = mydict.get("cat") // mydict.get("dog")
print(answer)

total = 0
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
for akey in mydict:
   if len(akey) > 3:
      total = total + mydict[akey]
print(total)
