import unittest


def factorial(N):
    if N == 0 or N ==1: return 1
    ans = 2
    for i in range(N, 2, -1):
        ans *= i
    return ans


def permutate(word):
    if word == "":
        return [""]

    else:
        result = []
        letter = word[0]

        for w in permutate(word[1:]):  # for every word in the result from f(n-1)
            for i in range(len(w) + 1):  # insert letter at all positions of the word
                result.append(w[0:i] + letter + w[i:])

        return result


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.data = [ "A", "JOY", "VOICE", "IMPORTED"]

    def test_result_length(self):
        for word in self.data:
            result = permutate(word)
            self.assertEqual(len(result), factorial(len(word)))

    def test_word_length(self):
        for word in self.data:
            wlen = len(word)

            for per in permutate(word):
                self.assertTrue(len(per), wlen)

                for ch in per:
                    self.assertTrue(ch in word)

    ## Letters must be unique for this test to pass
    def test_no_duplicates(self):
        for word in self.data:
            dict = {}

            for per in permutate(word):
                self.assertTrue( per not in dict)
                dict[per] = 1


if __name__ == '__main__':
    unittest.main()
