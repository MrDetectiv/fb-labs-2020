import math
import random


def inverse_a_mod_n(a, n):
    if a == 0:
        return 0
    if n == 0:
        return a, 1, 0
    d, x, y = inverse_a_mod_n(n, a % n)
    return d, y, x - (a // n) * y


def x2d_mod_p(x, d, p):
    bin_d = bin(d)[2:]
    result = 1
    for i in range(len(bin_d)):
        if bin_d[i] == '1':
            result = (result * x) % p
        if i == len(bin_d) - 1:
            break
        result = (result ** 2) % p
    return result


def miller_rabin(p):
    k = 100
    s = 0
    d = p - 1
    while d % 2 == 0:
        s += 1
        d = d // 2
    for i in range(k):
        x = random.randint(2, p - 1)
        if math.gcd(x, p) > 1:
            return False
        else:
            x_r = x2d_mod_p(x, d, p)
            if x_r == 1 or x_r == p - 1:
                continue
            for r in range(1, s):
                x_r = (x_r ** 2) % p
                if x_r == p - 1:
                    break
                elif x_r == 1:
                    return False
            return False
    return True



def prime(length):
    n0 = 2 ** length
    n1 = 2 ** (length + 1) - 1
    # print("prime from ", n0, " to ", n1)
    p = random.randint(n0, n1)
    if p % 2 == 0:
        p += 1
    while not miller_rabin(p):
        p += 2
    return p


def generate_key_pair(key_len):
    mIn = 2 ** key_len
    mAx = 2 ** (key_len + 1) - 1
    p = prime(key_len // 2)
    q = prime(key_len // 2)
    while mIn <= p * q <= mAx:
        q = prime(key_len // 2)
    n = p * q
    fi_n = (p - 1) * (q - 1)
    e = 2 ** 16 + 1
    d = inverse_a_mod_n(e, fi_n)[1] % fi_n
    open_key = [n, e]
    secret_key = [d, p, q]
    return [open_key, secret_key]


def encrypt(msg, e, n):
    cipher_msg = x2d_mod_p(msg, e, n)
    return cipher_msg


def decrypt(C, d, n):
    M = x2d_mod_p(C, d, n)
    return M


def sign(msg, d, n):
    S = encrypt(msg, d, n)
    return S


def verify(M, S, e, n):
    if M == decrypt(S, e, n):
        return True
    else:
        return False


def send(k, n1, e1, d, n):
    k1 = encrypt(k, e1, n1)
    S = sign(k, d, n)
    S1 = encrypt(S, e1, n1)
    return [hex(k1)[2:], hex(S1)[2:]]


def receive(k1, S1, n1, d1, e, n):
    k1 = int(k1, 16)
    S1 = int(S1, 16)
    k = decrypt(k1, d1, n1)
    S = decrypt(S1, d1, n1)
    check = verify(k, S, e, n)
    if check:
        return [True, k]
    else:
        return [False, k]
