class Vehicle:

    def __init__(self, VIN = "AAA123", owner = "FFFF, LLLL"):


        if isinstance(VIN, int):
            raise TypeError("You must pass a string.")
        elif len(VIN) != 6:
            raise ValueError("You need 6 characters. eg. AAA123")

        abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums = "1234567890"
        for i in range(0,2):
            if VIN[i] not in abc:
                raise ValueError("The first 3 characters in VIN must be letters!")
            if VIN[i+3] not in nums:
                raise ValueError("The last 3 characters in VIN must be numbers!")


        self._VIN = VIN

        if "," not in owner:
            raise ValueError
        else:
            self._owner = owner



car = Vehicle("AAA132", "John, Doe")

print(car)

garage = []

cnt = 0
while cnt < 10:
    garage.append(car)
    cnt +=1

print(garage)