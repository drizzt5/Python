def add(a, b):
    return a + b

'''
L is an ordered list. Create a new list by adding X to L
in the correct position so the new list is ordered.
'''
def insert(L, X):

    result = [ ]
    i = 0

    while i < len(L) and L[i] <= X:
        result.append(L[i])
        i += 1

    result.append(X)

    return result + L[i:]


def measure(w, L):

    result = [ ]

    def rec_measure(pair, w, L):

        if w == 0:

            if pair not in result: result.append(pair)

        elif L != []:
            left = pair[0]
            right = pair[1]
            rec_measure((left + [L[0]], right), w + L[0], L[1:])
            rec_measure((left, right), w, L[1:])
            rec_measure((left, right + [L[0]]), w - L[0], L[1:])


    rec_measure(([w], [ ]) , w, L)

    return result


def possible_changes(amount, coins):

    result = [ ]

    def rec_helper(amt, denom, cs):
        if amt == 0:
            result.append(denom)

        elif amt > 0 and len(cs) > 0:
            rec_helper(amt - cs[0], denom + [cs[0]], cs)
            rec_helper(amt, denom, cs[1:])

    rec_helper(amount, [], coins)

    return result


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