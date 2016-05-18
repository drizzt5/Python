'''
Comparison of finding duplicates with and without using a dictionary
'''

import time
import random
import sys

'''
Return True if xs contains duplicate values.
Implement without using a dictionary
Performance is O(N*N)
'''
def has_dup_no_dict(xs):

    for loc in range(len(xs)):
        val = xs[loc]

        for i in range(loc+1, len(xs)):
            if val == xs[i]: return True

    return False

'''
Return True if xs contains duplicate values
Implement by using a dictionary
Performance is O(N)
'''
def has_dup_with_dict(xs):

    dup = {} ## dictionary to keep track of values found in xs

    for loc in range(len(xs)):
        
        if xs[loc] in dup: return True

        dup[xs[loc]] = 1  ## Add entry for this number in dictionary
                          ## The value for the entry is not significant,
                          ## any value will do

    return False


if __name__ == '__main__':

    ## Create a large list of random numbers
    # L = random.sample(range(sys.maxsize), 10000)

    L = [num for num in range(10000)]

    print("Start Comparison Test")

    start = time.time()
    has_dup_no_dict(L)
    end = time.time()

    print("No Dictionary Performance: %7.3f" % (end - start))

    start = time.time()
    has_dup_with_dict(L)
    end = time.time()

    print("WITH Dictionary Performance: %7.3f" % (end - start))


