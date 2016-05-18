from math import *

print(factorial(6))

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

print(permutate("holy")[0])