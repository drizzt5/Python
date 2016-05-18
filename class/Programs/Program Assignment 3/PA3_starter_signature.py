
from math    import *
from time import *
import re
from PA3_helper import

class Signature:

    ### Methods you need to implement. Read the comments very carefully ###

    def split_on_separators(self, original, separators):
        ''' Return a list of non-empty, non-blank strings from the original string
        determined by splitting the string on any of the separators.
        separators is a string of single-character separators.'''

        # TO DO: Complete this function's body to meet its specification.
        result = ""
        for ch in original:
            if ch in separators:
                result = result + '*&('
            else:
                result = result + ch
        result = result.split("*&(")
        return result


    def average_word_length(self, text):
        ''' Return the average length of all words in text. Do not
        include surrounding punctuation in words.
        text is a non-empty list of strings each ending in \n.
        At least one line in text contains a word.'''

        # TO DO: Replace this function's body to meet its specification.

        ## Changes to string form
        # newStr = ""
        # for i in text:
        #     newStr = newStr + i + " "
        newStr = ' '.join(text)


        ## takes all words and puts into a list
        splitWords = re.findall(r"[\w']+", newStr)

        length = 0
        for word in splitWords:
            length = length + len(word)

        result = length / len(splitWords)

        return result

    def type_token_ratio(self, text):
        ''' Return the type token ratio (TTR) for this text.
        TTR is the number of different words divided by the total number of words.
        text is a non-empty list of strings each ending in \n.
        At least one line in text contains a word. '''

        # TO DO: Replace this function's body to meet its specification.
        ## Changes to string form
        newStr = ""
        for i in text:
            newStr = newStr + i + " "

        ## takes all words and puts into a list
        splitWords = re.findall(r"[\w']+", newStr)

        checker = []
        for word in splitWords:
            if word not in checker:
                checker.append(word)

        return len(checker) / len(splitWords)


    def hapax_legomana_ratio(self, text):
        ''' Return the hapax_legomana ratio for this text.
        This ratio is the number of words that occur exactly once divided
        by the total number of words.
        text is a list of strings each ending in \n.
        At least one line in text contains a word.'''

        # TO DO: Replace this function's body to meet its specification.
        newStr = ""
        for i in text:
            newStr = newStr + i + " "

        ## takes all words and puts into a list
        splitWords = re.findall(r"[\w']+", newStr)

        checker = []
        for word in splitWords:
            if word not in checker:
                checker.append(word)

            elif word in checker:
                checker.remove(word)

        return len(checker) / len(splitWords)


    def average_sentence_length(self, text):
        ''' Return the average number of words per sentence in text.
        text is guaranteed to have at least one sentence.
        Terminating punctuation defined as !?.
        A sentence is defined as a non-empty string of non-terminating
        punctuation surrounded by terminating punctuation
        or beginning or end of file. '''

        # TO DO: Replace this function's body to meet its specification.

        newStr = ' '.join(text)

        result = self.split_on_separators(newStr, "!?.")
        print(result)

        return 1.0


    def average_sentence_complexity(self, text):
        '''Return the average number of phrases per sentence.
        Terminating punctuation defined as !?.
        A sentence is defined as a non-empty string of non-terminating
        punctuation surrounded by terminating punctuation
        or beginning or end of file.
        Phrases are substrings of a sentences separated by
        one or more of the following delimiters ,;: '''

        # TO DO: Replace this function's body to meet its specification.
        return 1.0


    def compare_signatures(self, sig1, sig2, weight):
        '''Return a non-negative real number indicating the similarity of two
        linguistic signatures. The smaller the number the more similar the
        signatures. Zero indicates identical signatures.
        sig1 and sig2 are 6 element lists with the following elements
        0  : author name (a string)
        1  : average word length (float)
        2  : TTR (float)
        3  : Hapax Legomana Ratio (float)
        4  : average sentence length (float)
        5  : average sentence complexity (float)
        weight is a list of multiplicative weights to apply to each
        linguistic feature. weight[0] is ignored.
        '''

        # TO DO: Replace this function's body to meet its specification.
        return  0.0