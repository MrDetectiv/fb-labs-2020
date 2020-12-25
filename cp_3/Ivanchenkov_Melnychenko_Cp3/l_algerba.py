import numpy as np
from itertools import product


def solve(a, b, n):
    """ решение линейного сравнения, функция возвращает все решения """
    d = np.gcd(a, n)
    if a // n > 0:
        a = a % n
    if d == 1:
        a_rev, y, z = bezout_recursive(a, n)
        x = [np.mod(a_rev * b, n)]
    else:
        if b % d != 0:
            x = [0]
        else:
            n1 = int(n / d)
            x0 = solve(int(a / d), int(b / d), int(n / d))
            x = [x0_0 + i * n1 for x0_0, i in product(x0, range(0, d))]
    return x


def bezout_recursive(a, n):
    """ Рекурсивная имплементация расширенного алгоритма Евклида """
    if not n:
        return 1, 0, a
    y, x, g = bezout_recursive(n, a % n)
    return x, y - (a // n) * x, g