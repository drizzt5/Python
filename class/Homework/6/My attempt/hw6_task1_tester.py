import unittest
from math import *


## This is the permutate function from Lab 2B ##
def permutate(word):

    if word == "":
        return [""]

    else:
        result = []
        letter = word[0]

        for w in permutate(word[1:]): #for every word in the result from f(n-1)
            for i in range(len(w)+1):    # insert letter at all positions of the word
                result.append(w[0:i] + letter + w[i:])

        return result


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.word = ["Holy", "Hello", "Fancy", "Mother", "Father", "Psy"]



    def test_length_array(self):
        for i in range(len(self.word)):
            self.assertEqual(len(permutate(self.word[i])), factorial(len(self.word[i])))

    ##As word gets bigger, this slows down dramatically....
    def test_length_elements(self):
        for i in range(0, len(self.word)):
            permNum=len(permutate(self.word[i])) # Length of permutations for word[i]
            for j in range(0, permNum):
                tempWords = permutate(self.word[i])
                self.assertEqual(len(tempWords[j]), len(self.word[i]))

    def test_char_elements(self):
        for i in range(len(self.word)):
            permNum = len(permutate(self.word[i]))
            for j in range(0, permNum):
                for ch in self.word[i]:
                    self.assertTrue(ch in permutate(self.word[i])[j])

    def test_no_duplicates(self):
        word = "help"
        result = permutate(word)
        for i in range(len(result)):
            for j in range(i+1, len(result)):
                self.assertNotEqual(result[i], result[j])


if __name__ == '__main__':
    unittest.main()

