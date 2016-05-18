class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return "Name: " + self._name + " Age: " + str(self._age)

    def __eq__(self, other):
        # a = self._name
        # b = self._age
        # c = other._name
        # d = other._name
        #
        # if a == c and b == d:
        #     return True
        return self._name == other._name and self._age == other._age



Joe = Person("Joe", 20)
Bob = Person("Bob", 30)

p1 = Person("John", 20)
p2 = Person("John", 20)

assert p1 != p2
