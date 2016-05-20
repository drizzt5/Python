from PA3_helper import Helper



def split_on_separators(original, separators):
    ''' Return a list of non-empty, non-blank strings from the original string
    determined by splitting the string on any of the separators.
    separators is a string of single-character separators.'''

    # TO DO: Complete this function's body to meet its specification.
    result = []
    word = ""
    for ch in original:
        if ch in separators:

            result.append(word)
            word = ""

        else:
            word += ch
    result.append(word)
    return result

def type_token_ratio(text):
    ''' Return the type token ratio (TTR) for this text.
    TTR is the number of different words divided by the total number of words.
    text is a non-empty list of strings each ending in \n.
    At least one line in text contains a word. '''

    # TO DO: Replace this function's body to meet its specification.

    helper = Helper()
    sents = [] #sentences
    for x in text:
        sents+=x.split()

    splitWords = []
    for i in sents:
        splitWords.append(helper.clean_up(i))

    checker = []
    for word in splitWords:
        if word not in checker:
            checker.append(word)
    return len(checker) / len(splitWords)


def hapax_legomana_ratio(text):
    ''' Return the hapax_legomana ratio for this text.
    This ratio is the number of words that occur exactly once divided
    by the total number of words.
    text is a list of strings each ending in \n.
    At least one line in text contains a word.'''

    # TO DO: Replace this function's body to meet its specification.
    helper = Helper()
    sents = []  # sentences
    for x in text:
        sents += x.split()

    splitWords = []
    for i in sents:
        splitWords.append(helper.clean_up(i))

    checker = []
    for word in splitWords:
        if word not in checker:
            checker.append(word)

        elif word in checker:
            checker.remove(word)

    return len(checker) / len(splitWords)


def average_word_length(text):
    ''' Return the average length of all words in text. Do not
    include surrounding punctuation in words.
    text is a non-empty list of strings each ending in \n.
    At least one line in text contains a word.'''

    # TO DO: Replace this function's body to meet its specification.

    helper = Helper()
    sents = []  # sentences
    for x in text:
        sents += x.split()

    splitWords = []
    for i in sents:
        splitWords.append(helper.clean_up(i))

    length = 0
    for word in splitWords:
        length = length + len(word)

    result = length / len(splitWords)

    return result


def average_sentence_length(text):

    helper = Helper()

    newStr = ' '.join(text)
    sents = split_on_separators(newStr, "!?.")


    word_list = []
    count = 0
    for line in sents:
        if line != '\n':
            count+=1
        line=line.replace("\n", " ")
        for word in line.split(" "):
            cleanWord = helper.clean_up(word)
            if cleanWord != "":
                word_list.append(cleanWord)

    return len(word_list)/count


def average_sentence_complexity(text):
    '''Return the average number of phrases per sentence.
    Terminating punctuation defined as !?.
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file.
    Phrases are substrings of a sentences separated by
    one or more of the following delimiters ,;: '''

    # TO DO: Replace this function's body to meet its specification.

    newStr = ' '.join(text)
    sents = split_on_separators(newStr, "!?.")

    dm = [",",":",";"]
    senCount = 0
    phraseCount = 0

    for line in sents:
        if line != '\n':
            senCount += 1
        for word in line.split(" "):
            for char in word:
                if char in dm:
                    phraseCount+=1

    return (phraseCount + senCount)/senCount

text = ["The time has come, the Walrus said\n",
                "To talk of many things: of shoes - and ships - and sealing wax,\n",
                "Of cabbages; and kings.\n"
                "And why the sea is boiling hot;\n"
                "and whether pigs have wings.\n"]


# print(hapax_legomana_ratio(text))
# print(type_token_ratio(text))
#print(average_word_length(text))
print(average_sentence_complexity(text))