def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a, m):
    if gcd(a,m) != 1:
        return None
    orig_m = m
    prevu, u = 1, 0
    prevv, v = 0, 1
    while m != 0:
        q = a//m
        u, prevu = prevu - q*u, u
        v, prevv = prevv - q*v, v
        a, m = m, a % m
    return prevu % orig_m


def linear_equation(a,b,n):
    if gcd(a,n) == 1:
        return (findModInverse(a,n) * b) % n
    if gcd(a,n) > 1:
        if b % gcd(a,n) != 0: return None
        else:
            a1 = a // gcd(a,n)
            b1 = b // gcd(a,n)
            n1 = n // gcd(a,n)
            x1 = linear_equation(a1,b1,n1)
            solutions = [i for i in range(x1,n,n1)]
            return solutions