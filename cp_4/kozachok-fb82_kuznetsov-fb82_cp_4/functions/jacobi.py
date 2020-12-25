from . import gcd

class NotOddException(Exception):
    def __init__(self, x):
        print(str(x) + " is not odd")


class NotPositiveException(Exception):
    def __init__(self, x):
        print(str(x) + " is not > 0")


class JacobiSymbol:
    """Calculates the JacobiSymbol (a|b)

    Keyword arguments:
    a -- integer
    b -- positive odd integer
    """

    def __init__(self, a, b):
        if b < 0:
            raise NotPositiveException(b)
        if b % 2 == 0:
            raise NotOddException(b)
        self.a = a
        self.b = b
        if gcd(self.a, self.b) != 1:
            self.notCoPrime = True
        else:
            self.notCoPrime = False

    @staticmethod
    def __supplementary2__(x):
        if x % 8 == 1 or x % 8 == 7:
            return 1
        else:
            return -1

    @staticmethod
    def __supplementary1__(x, y):
        if x % 4 == 1 or y % 4 == 1:
            return 1
        else:
            return -1

    def calculate(self):
        if self.notCoPrime:
            return 0
        elif self.a == 1:
            return 1
        elif self.a == 2:
            return self.__supplementary2__(self.b)
        elif self.a % 2 == 0:
            return JacobiSymbol(self.a // 2, self.b).calculate() * JacobiSymbol(2, self.b).calculate()
        else:
            return JacobiSymbol(self.b % self.a, self.a).calculate() * self.__supplementary1__(self.a, self.b)
