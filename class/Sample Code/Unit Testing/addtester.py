import unittest
from mycode import add


class MyTestCase(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(1,2), 3)
        self.assertNotEqual(add(1,2), 4)

    def test_negative_add(self):
        self.assertEqual(add(-1,-1), -2)
        self.assertEqual(add(-3, 0), -3)


if __name__ == '__main__':
    unittest.main()
