class Fraction:

    def __init__(self, num, denom = 1):
        self._num = num
        self._denom = denom
        if denom == 0: raise ZeroDivisionError
        self._simplify()

    def __str__(self):
        return "%d/%d" % (self.num, self.denom)

    def _simplify(self):
        def gcd(a,b):
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


    def __add__(self, other):
        a = self._num   #self.num
        b = self._denom
        c = other._num  #other.num
        d = other._denom

        return Fraction(a*d + b*c, b*d)

    def __truediv__(self, other):
        a = self._num
        b = self._denom
        c = other._num
        d = other._denom

        return Fraction(a*d, b*c)

    def __sub__(self, other):
        a = self._num
        b = self._denom
        c = other._num
        d = other._denom

        return Fraction(a * d - b * c, b * d)

    def __mul__(self, other):
        a = self._num
        b = self._denom
        c = other._num
        d = other._denom

        return Fraction(a * c, b * d)

    def __eq__(self, other):
        a = self._num
        b = self._denom
        c = other._num
        d = other._denom

        return Fraction(a == d, b == c)