from fractions import gcd

class Fraction:

    def __init__(self, num, denom = 1):
        self._num = num
        self._denom = denom
        if denom == 0: raise ZeroDivisionError
        self._simplify()

    def _simplify(self):
        def gcd(a,b):
            while b != 0:
                a, b = b, a % b
                return a

        d = gcd(self._num, self._denom)

        self._num // d
        self._denom // d




    def __str__(self):
        if self._denom == 1:
            return "%s" % str(self._num)
        else:
            return "%s/%s" % (str(self._num), str(self._denom))

    def getNum(self):
        return self._num

    def getDenom(self):
        return self._denom

    def addOP(self):
        return True

    def subOP(self):
        return True
    def divOP(self):
        return True
    def multOP(self):
        return True
    def is_eq(self):
        if self._num == self._denom:
            return True
        else:
            return False


# f1 = Fraction(2,9)
# print(f1)
# f2 = Fraction(8, 18)
# print(f2)
# f3 = Fraction(3)
# print(f3)
# f4 = Fraction(50, 1000)
# print(f4)
