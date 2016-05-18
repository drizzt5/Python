import unittest
import mycode

class MyTestCase(unittest.TestCase):

    def isOrdered(self, L):
        for i in range(len(L)-1):
            if L[i] > L[i+1]: return False
        return True


    ### setUp method is called before each test method is executed
    def setUp(self):
        self.L = [20, 30, 40, 50, 60]

    def test_length(self):
        newlist = mycode.insert(self.L, 25)
        self.assertEqual(len(self.L) + 1, len(newlist))

    def test_sorted(self):
        self.assertTrue(self.isOrdered(mycode.insert(self.L, 35)))

    def test_add_begin(self):
        newList = mycode.insert(self.L, 10)
        self.assertEqual(newList[0], 10)
        #self.test_sorted()  ## It is possible to call another test method from a test method

    def test_add_end(self):
        newList = mycode.insert(self.L, 90)
        self.assertEqual(newList[-1], 90)


if __name__ == '__main__':
    unittest.main()
