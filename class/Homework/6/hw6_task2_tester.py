import unittest
from hw6_fraction_final import Fraction

class FractionTestCase(unittest.TestCase):

    def test_creation_whole(self):
        f1 = Fraction(3)
        f2 = Fraction(0)
        self.assertTrue(f1.num == 3 and f1.denom == 1)
        self.assertTrue(f2.num == 0 and f2.denom == 1)


    def test_creation_sign(self):
        f1 = Fraction(3, 5)
        f2 = Fraction(-3, 5)
        f3 = Fraction(3, -5)
        f4 = Fraction(-3, -5)
        f5 = Fraction(-0, 130)
        f6 = Fraction(0, 3)

        self.assertTrue(f1.num == 3 and f1.denom == 5)
        self.assertTrue(f2.num == -3 and f2.denom == 5)
        self.assertTrue(f3.num == -3 and f3.denom == 5)
        self.assertTrue(f4.num == 3 and f4.denom == 5)
        self.assertTrue(f5.num == 0 and f5.denom == 1)
        self.assertTrue(f6.num == 0 and f6.denom == 1)

    def test_creation_simplify(self):

        f1 = Fraction(200, 400)
        f2 = Fraction(200, 200)
        f3 = Fraction(30, -50)
        f4 = Fraction(-30, -50)

        self.assertTrue(f1.num == 1 and f1.denom == 2)
        self.assertTrue(f2.num == 1 and f2.denom == 1)
        self.assertTrue(f3.num == -3 and f3.denom == 5)
        self.assertTrue(f4.num == 3 and f4.denom == 5)



    def test_compare_equality(self):

        f1 = Fraction(200, 400)
        f2 = Fraction(200, 200)
        f3 = Fraction(30, -50)
        f4 = Fraction(-30, -50)

        self.assertTrue(f1 == Fraction(200, 400))
        self.assertTrue(f1 == f1)
        self.assertTrue(f3 == Fraction(-3, 5))
        self.assertTrue(f4 == Fraction(3, 5))

        self.assertTrue(f1 != f2)
        self.assertTrue(f2 != f1)
        self.assertTrue(f3 != Fraction(8,9))


    ### And many many many more ###


if __name__ == '__main__':
    unittest.main()
