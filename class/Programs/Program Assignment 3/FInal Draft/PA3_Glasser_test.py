"""
Author: Dillon Glasser
Class: CS3023 Intermediate Programming
Assignment: Program Assignment 3
Date: 5/18/2016

"""


import unittest
from PA3_Glasser_signature import Signature


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.sig = Signature()

    # test average_word_length
    def test_average_word_length(self):

        text = [
            "James Fennimore Cooper\n",
            "Peter, Paul, and Mary\n",
        ]

        self.assertAlmostEqual(self.sig.average_word_length(text), 5.14285714286, 4)

    # test type_token_ratio and hapax_legomana_ratio
    def test_type_and_hapax(self):

        text = [
            "James Fennimore Cooper\n",
            "Peter, Paul, and Mary\n",
            "James Gosling\n"
        ]

        self.assertAlmostEqual(self.sig.type_token_ratio(text), 0.88888, 4)

        self.assertAlmostEqual(self.sig.hapax_legomana_ratio(text), 0.777777777778, 4)

    # test split_on_separators
    def test_split_on_separators(self):

        hooray = "Hooray! Finally, we're done."
        thesplit = ['Hooray', ' Finally', " we're done."]


        self.assertEqual(self.sig.split_on_separators(hooray, "!,"), thesplit)


    # test average_sentence_length and average_sentence_complexity
    def test_average_sentence(self):

        text = ["The time has come, the Walrus said\n",
                "To talk of many things: of shoes - and ships - and sealing wax,\n",
                "Of cabbages; and kings.\n"
                "And why the sea is boiling hot;\n"
                "and whether pigs have wings.\n"]

        self.assertAlmostEqual(self.sig.average_sentence_length(text), 17.5, 4)

        self.assertAlmostEqual(self.sig.average_sentence_complexity(text), 3.5, 4)


    # test compare_signatures
    def test_compare_signatures(self):

        sig1 = ["a_string", 4.4, 0.1, 0.05, 10.0, 2.0]
        sig2 = ["a_string2", 4.3, 0.1, 0.04, 16.0, 4.0]
        weight = [0, 11, 33, 50, 0.4, 4]

        self.assertAlmostEqual(self.sig.compare_signatures(sig1, sig2, weight), 12, 4)


if __name__ == '__main__':
    unittest.main()
