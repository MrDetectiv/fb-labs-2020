import logging
from random import randint, randrange
from typing import Tuple


def modular_power(x: int, a: int, m: int) -> int:
    """ 
    (x^a)mod(m)
    """
    bin_nums = [ int(num) for num in bin(a)[2:] ]
    res = 1
    for num in bin_nums:
        res = res ** 2 % m
        res = res * (x ** num) % m 

    return res 

def gcd(a: int, b: int):
    if(b == 0): 
        return a 
    else: 
        return gcd(b, a % b)

def euclid_algorithm_gcd(a: int, b: int) -> Tuple[int, int, int]:
    if a == 0:
        x, y = (0, 1)
        return b, x, y
    d, x1, y1 = euclid_algorithm_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y


def inverse(n: int, mod: int):
    n = modular_power(n, 1, mod)
    d, x, y = euclid_algorithm_gcd(n, mod)
    if d == 1:
        return x


def miller_rabin_iteration(p: int, x: int) -> bool:
    if gcd(p, x) != 1:
        return False

    d = p - 1
    while d % 2 == 0:
        d //= 2


    if (m := modular_power(x, d, p)) == 1 or m == p - 1:
        return True

    while d < p - 1:
        iter_res = modular_power(x, d, p)

        if iter_res == p - 1:
            return True
        if iter_res == 1:
            return False

        d *= 2

    return False


def miller_rabin_test(p: int, k: int=40) -> bool:
    for i in range(0, k):
        x = randrange(2, p - 1)
        if not miller_rabin_iteration(p, x):
            return False 
    else:
        return True

def gen_prime_number(bits: int) -> int:
    bits_str = '1'

    for i in range(bits - 1):
        bits_str += str(randint(0, 1))

    logging.debug(f"{len(bits_str)=}\n{bits_str=}")

    n = int(bits_str, 2)

    if n % 2 == 0:
        n += 1

    for num in range(n, n*2 - 1, 2):
        if miller_rabin_test(num):
            prime = num
            logging.info("[*] Prime number {}".format(hex(prime)))
            break
        else:
            logging.debug('[*] Number {} is not prime'.format(hex(num)))

    return num

def gen_key_pair(bits_length: int) -> Tuple[int, int, int]:
    ":return: exponent, private key, public key"
    logging.info("[*] Generating prime number 'p' ...")
    p = gen_prime_number(bits_length)
    logging.info("[!] Generated prime 'p'")

    logging.info("[*] Generating prime number 'q' ...")
    q = gen_prime_number(bits_length)
    logging.info("[!] Generated prime 'q'")

    e = 0x10001

    f = (p - 1) * (q - 1)
    n = p * q

    d = inverse(e, f)
    d %= f

    logging.info(
        '[+] p={}\n[+] q={}\n[+] f={}\n[+] n={}\n[+] e={}\n[+] d={}' \
        .format(hex(p), hex(q), hex(f), hex(n), hex(e), hex(d))
        )

    return e, d, n


def encrypt(m: int, e: int, n: int) -> int:
    'Encrypt with public key'
    return modular_power(m, e, n)


def decrypt(c: int, d: int, n: int) -> int:
    'Decrypt with private key'
    return modular_power(c, d, n)


def sign(m: int, d: int, n: int) -> int:
    'Encrypt with priate key'
    return modular_power(m, d, n)


def verify(m: int, s: int, e: int, n: int) -> bool:
    'Decrypt with public key'
    return m == modular_power(s, e, n)

def send_key(k: int, d: int, n: int, e1: int, n1: int) -> Tuple[int, int]:
    ":return: k1 - message, S1 - encrypted message for verification"
    S = modular_power(k, d, n)

    k1 = modular_power(k, e1, n1)
    S1 = modular_power(S, e1, n1)

    return k1, S1

def receive_key(k1: int, S1, d1: int, n1: int, e: int, n: int) -> int:
    k = modular_power(k1, d1, n1)
    S = modular_power(S1, d1, n1)

    if verify(k, S, e, n):
        return k
    return 0

