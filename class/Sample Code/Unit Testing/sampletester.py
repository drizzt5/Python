import unittest


class MyTestCase(unittest.TestCase):

    ## sample basic tests from python.org

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    ## Added example:
    ##      This is another way to assert the raising (throwing) of an exception
    def test_split_2(self):
        s = "hello world"
        self.assertRaises(TypeError, s.split, 2)
                    ## expected exception, funtion to call, argument(s) to pass to this function

if __name__ == '__main__':
    unittest.main()
