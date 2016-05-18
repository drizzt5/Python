def fibo_one(N):
    if N == 0 or N == 1:
        return 1
    else:
        return fibo_one(N-1) + fibo_one(N-2)


def fibo_two(N):

    F = [1, 1]

    def rec_fibo(N):

        if N == 0 or N == 1:
            return 1

        elif N < len(F):
            return F[N]

        else:
            fib = rec_fibo(N-1) + rec_fibo(N-2)
            F.append(fib)
            return fib

    return rec_fibo(N)


def fibo_three(N):

    if N == 0 or N == 1:
        return 1

    else:
        fib0 = fib1 = 1

        for i in range(2, N+1):
            fib0, fib1 = fib1, fib0 + fib1

        return fib1



if __name__ == '__main__':

    while True:

        N = int(input("N (0 to stop): "))

        if N == 0: break

        print(fibo_one(N))
        print(fibo_two(N))
        print(fibo_three(N))