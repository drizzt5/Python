import unittest
from cs3023_lab6a_fraction import Fraction

class MyTestCase(unittest.TestCase):

    def test_creation(self):
        f1 = Fraction(2,9)
        f2 = Fraction(8,18)
        f3 = Fraction(3)

        self.assertEqual(f1.getNum(), 2)
        self.assertEqual(f1.getDenom(), 9)

        self.assertEqual(f3.getNum(), 3)
        self.assertEqual(f3.getDenom(), 1)

        # self.assertEqual(f2.getNum(), 4)
        # self.assertEqual(f2.getDenom(), 9)

    def test_wrong_creation(self):
        self.assertRaises(ZeroDivisionError, Fraction, 3, 0)
        with self.assertRaises(ZeroDivisionError):
            f = Fraction(3,0)

    def test_set_methods(self):
        pass

    def test_get_methods(self):
        pass

    def test_addition(self):
        f1 = Fraction(2, 9)
        f2 = Fraction(8, 18)


    def test_subraction(self):
        pass

    def test_division(self):
        pass

