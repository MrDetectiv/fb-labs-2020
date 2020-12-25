import random

from RSA.exceptions import number_is_not_prime


def gcd(a, b):
    if b != 0:
        return gcd(b, a % b)
    return a


def euclid(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = euclid(b, a % b)
    return d, y, x - (a // b) * y


def inverse(b, n):
    g, x, y = euclid(b, n)
    if g == 1:
        return x % n


def miller_rabin(number):
    d = number - 1
    s = 0

    x = random.randint(2, d)

    _gcd = gcd(x, number)
    if _gcd > 1:
        raise number_is_not_prime(hex(number), 'is not prime because gcd = ', _gcd)

    tmp = pow(x, d, number)

    if not (tmp == 1 or tmp == -1):
        is_pseudo_prime = False
        for r in range(1, s - 1):
            xr = pow(x, d * pow(2, r)) % number
            if xr == number - 1:  # == -1
                is_pseudo_prime = True
            if xr == 1:
                raise number_is_not_prime(hex(number), 'is not prime because is not pseudo prime')
            else:
                continue

        if not is_pseudo_prime:
            raise number_is_not_prime(hex(number), 'is not prime because is not pseudo prime')

    return True


def is_prime(number, attempts_amount=50):
    simple_divisors = [2, 3, 5, 7, 11]

    for it in simple_divisors:
        if gcd(number, it) != 1 and number != it:
            raise number_is_not_prime(hex(number), 'is not prime because can be divided by', it)

    attempts_passed = 0
    for it in range(0, attempts_amount):
        try:
            if miller_rabin(number):
                attempts_passed += 1
        except number_is_not_prime as exc:
            print(exc)
            return False

    if attempts_passed != attempts_amount:
        return False
    return True


def generate_prime_number(length):
    x = False
    key = 0
    while not x:
        try:
            key = random.randint(2 ** (length-1), 2 ** length)
            if is_prime(key):
                x = True
        except number_is_not_prime as exc:
            print(exc)

    return key


def generate_key_pairs(length):
    p, q = generate_prime_number(length), generate_prime_number(length)
    p1, q1 = generate_prime_number(length), generate_prime_number(length)

    if p * q <= p1 * q1:
        return p, q, p1, q1
    return generate_key_pairs(length)


def generate_key_pair(length):
    p, q = generate_prime_number(length), generate_prime_number(length)
    return p, q


def euler_func(p, q):
    return (p - 1) * (q - 1)


if __name__ == '__main__':
    pass
