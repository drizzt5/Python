class Pet:

    DOG = "Dog"
    CAT = "Cat"
    SNAKE = "Snake"
    RABBIT = "Rabbit"


    def __init__(self, name, age, weight, species):
        self._name = name
        self._age = age
        self._weight = weight
        self._species = species


    def __str__(self):
        return self._name + " : " + str(self._age) + " : " + str(self._weight) + " : " + self._species

    ############# Accessors ###################
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def weight(self):
        return self._weight

    @property
    def species(self):
        return self._species

    ############### Mutators ##################
    @name.setter
    def name(self, value):
        self._name = value

    @age.setter
    def age(self, value):
        self._age = value

    @weight.setter
    def weight(self, value):
        self._weight = value

    @species.setter
    def species(self, value):
        self._species = value

    def eat(self):
        self._weight = self._weight + .1

    def exercise(self):
        self._weight = self._weight - .2









