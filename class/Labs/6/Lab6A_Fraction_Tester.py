import unittest
from exp_fraction import Fraction

class MyTestCase(unittest.TestCase):

    def test_creation(self):
        f1 = Fraction(2,9)
        f2 = Fraction(8,18)
        f3 = Fraction(3)

        self.assertEqual(f1.num, 2)
        self.assertEqual(f1.denom, 9)

        self.assertEqual(f3.num, 3)
        self.assertEqual(f3.denom, 1)

        self.assertEqual(f2.num, 4)
        self.assertEqual(f2.denom, 9)

    def test_wrong_creation(self):
        self.assertRaises(ZeroDivisionError, Fraction, 3, 0)
        with self.assertRaises(ZeroDivisionError):
            f = Fraction(3,0)

    def test_set_methods(self):
        #I don't understand how to test these
        pass

    def test_get_methods(self):
        # I don't understand how to test these
        pass


    def test_addition(self):
        f1 = Fraction(2, 9)
        f2 = Fraction(8, 18)
        f3 = f1.__add__(f2)
        self.assertEqual(f3.num, 2)
        self.assertEqual(f3.denom, 3)

        f3 = Fraction(3)
        self.assertEqual(f3.num, 3)
        self.assertEqual(f3.denom, 1)

        f4 = f1 + f2
        self.assertEqual(f4.num, 2)
        self.assertEqual(f4.denom, 3)

        f6 = (f1 + f2 - f2) / f1
        self.assertEqual(f6.num, 1)
        self.assertEqual(f6.denom, 1)



    def test_subtraction(self):
        f1 = Fraction(2, 9)
        f2 = Fraction(8, 18)
        f3 = f1-f2
        f4 = f1.__sub__(f2)
        self.assertEqual(f3.num, -2)
        self.assertEqual(f3.denom, 9)
        self.assertEqual(f4.num, -2)
        self.assertEqual(f4.denom, 9)

    def test_division(self):
        f1 = Fraction(2, 9)
        f2 = Fraction(8, 18)
        f6 = (f1 + f2 - f2) / f1 #this is probably bad because I use other methods that could be broken
        self.assertEqual(f6.num, 1)
        self.assertEqual(f6.denom, 1)
        f5 = f1 / f2
        self.assertEqual(f5.num, 1)
        self.assertEqual(f5.denom, 2)


    def test_multiplication(self):
        f1 = Fraction(2, 9)
        f2 = Fraction(8, 18)
        f3 = (f1 * f2)
        self.assertEqual(f3.num, 8)
        self.assertEqual(f3.denom, 81)

    def test_equality(self):
        f1 = Fraction(13, 15)
        f2 = Fraction(13, 15)
        f3 = Fraction(17, 18)
        self.assertEqual(f1.num, f2.num)
        self.assertEqual(f1.denom, f2.denom)
        self.assertNotEqual(f1.num, f3.num)
        self.assertNotEqual(f1.denom, f3.denom)


    def test_str(self):
        f1 = Fraction(3)
        f2 = Fraction(8, 10)
        f3 = Fraction(2, 5)

        self.assertEqual(str(f1), "3/1")
        self.assertEqual(str(f2), "4/5")
        self.assertEqual(str(f3), "2/5")



if __name__ == '__main__':
    unittest.main()
