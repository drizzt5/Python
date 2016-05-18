class Fraction:

    def __init__(self, num = 0, denom = 1):
        '''
        negative fraction is represented as -num/denom

        :param num: numerator of the fraction
        :param denom: denominator of the fraction
        '''
        if denom == 0: raise ZeroDivisionError

        if num == 0:
            self._num = 0
            self._denom = 1
            return

        ### Check sign ###
        self._num   = -abs(num) if num * denom < 0 else abs(num)
        self._denom = abs(denom)

        ## above two are equivalent to below ##
        # if num * denom < 0:
        #     self._num = -1 * abs(num)
        #     self._denom = abs(denom)
        # else:
        #     self._num =  abs(num)
        #     self._denom = abs(denom)

        ### Below is another way to set the sign correctly
        # if denom < 0:
        #     self._num = -num
        #     self._denom = -denom
        # else:
        #     self._num =  num
        #     self._denom = denom

        self._simplify()

    def __str__(self):
        return "%d/%d" % (self._num, self._denom)

    def _simplify(self):
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        d = gcd(self._num, self._denom)
        self._num   //= d
        self._denom //= d

    @property
    def num(self):
        return self._num

    @property
    def denom(self):
        return self._denom

    @num.setter
    def num(self, value):
        self._num = value

    @denom.setter
    def denom(self, value):
        if value == 0: raise ZeroDivisionError
        self._denom = value

#### Conversion ######
    def __float__(self):
        return self._num / self._denom


#### Arithmetic operations ######
    def __add__(self, other):
        a, b = self._num, self._denom
        c, d = other._num, other._denom

        return Fraction(a*d + b*c, b*d)

    def __sub__(self, other):
        a, b = self._num, self._denom
        c, d = other._num, other._denom

        return Fraction(a * d - b * c, b * d)

    def __truediv__(self, other):
        a, b = self._num, self._denom
        c, d = other._num, other._denom

        return Fraction(a * d, b * c)

    def __mul__(self, other):
        a, b = self._num, self._denom
        c, d = other._num, other._denom

        return Fraction(a * c, b * d)

#### Unary operators #####
    def __neg__(self):
        return Fraction(-self._num, self._denom)

    def __pos__(self):
        return Fraction(self._num, self._denom)

#### Comparison operators #######
    def __eq__(self, other):
        a, b = self._num, self._denom
        c, d = other._num, other._denom

        return a == c and b == d

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return float(self) < float(other)

    def __ge__(self, other):
        return not self < other

    def __gt__(self, other):
        return float(self) > float(other)

    def __le__(self, other):
        return not self > other


if __name__ == '__main__':

    f1 = Fraction(2, 9)
    f2 = Fraction(8, 18)  ## internally it is represented as 4/9
    f3 = Fraction(3)  ## this is 3/1
    f4 = f1 + f2
    f5 = f1 / f2
    f6 = (f1 + f2 - f2) / f1
    f7 = f1 * f3

    print(f1)
    print(f2)  ## displays 4/9
    print(f3)
    print(f4)  ## displays 2/3
    print(f5)
    print(f6)
    print(f7)

    print(f7.num, f7.denom)

    print(f1 == f2)  ## prints out False
    print(f1 == Fraction(2,9))