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


if __name__ == '__main__':

    ## include appropriate tests here
    print(measure(8, [2, 2, 1, 4]))
    print(measure(3, [2, 2, 1, 4]))