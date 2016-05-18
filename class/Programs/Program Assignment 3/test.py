import re
import string
from PA3_helper import Helper

def type_token_ratio(text):
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

    checker =[]
    for word in splitWords:
        if word not in checker:
            checker.append(word)

    return len(checker)/len(splitWords)


def hapax_legomana_ratio(text):
    ''' Return the hapax_legomana ratio for this text.
    This ratio is the number of words that occur exactly once divided
    by the total number of words.
    text is a list of strings each ending in \n.
    At least one line in text contains a word.'''

    # TO DO: Replace this function's body to meet its specification.
    newStr = ""
    for i in text:
        newStr = newStr + i + " "
    #print(newStr)

    ## takes all words and puts into a list
    splitWords = re.findall(r"[\w']+", newStr)
    #print(splitWords)

    checker = []
    for word in splitWords:
        if word not in checker:
            checker.append(word)
        elif word in checker:
            checker.remove(word)


    return len(checker) / len(splitWords)


def average_sentence_length(text):
    ''' Return the average number of words per sentence in text.
    text is guaranteed to have at least one sentence.
    Terminating punctuation defined as !?.
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file. '''

    # TO DO: Replace this function's body to meet its specification.


    newStr = ""
    for i in text:
        newStr = newStr + i
    # m = re.search('(?<=.)\w+', newStr)
    # return m.group()


    for ch in newStr:
        if ch in


    helper = Helper()
    raw = helper.clean_up(newStr)

    return raw


    # result = ""
    # for ch in original:
    #     if ch in separators:
    #         result = result + '*&('
    #     else:
    #         result = result + ch
    # result = result.split("*&(")
    # return result



    # regex = re.compile('[%s]' % re.escape(string.punctuation))
    #
    # return regex.sub('', newStr)


text = ["The time has come, the Walrus said\n",
        "To talk of many things: of shoes - and ships - and sealing wax,\n",
        "Of cabbages; and kings.\n"
        "And why the sea is boiling hot;\n"
        "and whether pigs have wings.\n"]

print(average_sentence_length(text))


