import unittest
from cs3023_quiz3_q1_pet import Pet

class PetTestCase(unittest.TestCase):

    def test_creation(self):
        p1 = Pet("Jack", 2, 3.5, Pet.DOG)
        p2 = Pet("Jill", 4, 2.3, Pet.CAT)

        self.assertTrue(p1.species != Pet.SNAKE)
        self.assertTrue(p2.species != Pet.RABBIT)

    def test_walk(self):
        p1 = Pet("Jane", 2, 3.5, Pet.RABBIT)
        p2 = Pet("John", 5, 2.0, Pet.CAT)

        p1.eat()
        self.assertEqual(p1.weight, 3.6)

        p2.exercise()
        self.assertEqual(p2.weight, 1.8)

    def test_str(self):
        p1 = Pet("Jack", 2, 3.0, Pet.DOG)
        p2 = Pet("Jill", 3, 2.5, Pet.CAT)
        p3 = Pet("Jane", 4, 3.0, Pet.SNAKE)
        p4 = Pet("John", 5, 2.5, Pet.RABBIT)

        self.assertEqual(str(p1), "Jack : 2 : 3.0 : Dog")
        self.assertEqual(str(p2), "Jill : 3 : 2.5 : Cat")
        self.assertEqual(str(p3), "Jane : 4 : 3.0 : Snake")
        self.assertEqual(str(p4), "John : 5 : 2.5 : Rabbit")


if __name__ == '__main__':
    unittest.main()
