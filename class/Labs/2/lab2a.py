#### Question 1 ####
def gcd(a, b):

    while b != 0:
        a, b = b, a % b

    return a

def gcd_rec(a, b):

    if b == 0:
        return a
    else:
        return gcd_rec(b, a % b)


#### Question 2 #####
def fibo_bad(N):
    if N == 0 or N == 1:
        return 1
    else:
        return fibo_bad(N-1) + fibo_bad(N-2)

def fibo(N):

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



while True:
    a = int(input("a (> 0; 0 to stop): "))
    b = int(input("b (>= 0): "))

    if a == 0: break

    print(a, b, gcd(a, b))
    print(a, b, gcd_rec(a, b))


while True:

    n = int(input("N (0 to stop: "))

    if n == 0: break

    print(n, fibo_bad(n))
    print(n, fibo(n))