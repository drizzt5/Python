##### Question 1 ######

def measure(w, L):

    answer = [ ]

    def rec_measure(result, w, L):

        if w == 0:
            if result not in answer: # this will eliminate duplicates
                answer.append(result) # when there multiple weights with the same value

        elif L != []:
            left = result[0]
            right = result[1]

            rec_measure((left, right + [L[0]]), w - L[0], L[1:])
            rec_measure((left + [L[0]], right), w + L[0], L[1:])
            rec_measure(result, w, L[1:])

        ## Notice that we have no explicit case for L == [] because
        ## when L is empty,  there are no more weights to consider
        ## so se stop the recursion by doing nothing. Partially
        ## build result (which is a local variable) will be ignored,
        ## i.e., it won't get added to answer

    rec_measure(([w], []), w, L) # We start the recursion by putting
                                 # w into left and nothing into right

    return answer

##### Question 2 ######
## This is the permutate function from Lab 1B ##
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

def test_permutate(word):

    def factorial(N):
        ans = 2
        for i in range(N, 2, -1):
            ans *= i
        return ans


    ## For this test, we are testing with no duplicates in the string
    ## we pass to permutate

    result = permutate(word)

    # Check 1: len(result) == len(word)!
    if len(result) != factorial(len(word)): return False

    # Check 2: all elements in result have len(word)
    wordlength = len(word)
    for element in result:
        if len(element) != wordlength: return False

    # Check 3: all elements in result have exactly one character from word
    #          this check assumes characters in word are unique.
    #          what happens if we remove this assumption?
    #  Note: Checks 2 and 3 can be done together in a single loop.
    #        We do them separately here for easy reading.
    for element in result:
        for ch in word:
            if ch not in word: return False

    # Check 4: No duplicates in result
    #          Note: we'll see a more efficient way of finding
    #                duplicates later in the course
    for i in range(len(result)):
        for j in range(i+1, len(result)):
            if result[i] == result[j]: return False

    ## Passed all checks ##
    return True



### Test Main for Q1 and Q2 ###

print(measure(8, [2, 2, 1, 4]))
print(measure(3, [2, 2, 1, 4]))
print(measure(18, [2, 2, 1, 4]))
print(measure(2, [3, 4]))

print(len(permutate("word")))
print(permutate("hello"))
print(test_permutate("ABCD"))
print(test_permutate("JOYDEAN"))