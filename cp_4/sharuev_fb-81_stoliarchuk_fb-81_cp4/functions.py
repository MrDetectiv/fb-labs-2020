from random import randint
from math import log


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def known_primes(length):
    list_of_known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,	47,	53]
    p_min = pow(2, length)
    p_max = pow(2, length + 1) - 1
    while 1:
        p = randint(p_min, p_max)
        for i in list_of_known_primes:
            if p % i == 0:
                break
            if i == 53 and p % i != 0:
                return p


def miller_rabin(p):
    k = int(log(p, 2))
    d = p - 1
    s = 0

    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        x = randint(1, p - 1)
        if gcd(x, p) > 1:
            return False
        if pow(x, d, p) == 1 or pow(x, d, p) == (p - 1):
            continue
        else:
            is_strong_pseudo_prime = False
            for r in range(1, s):
                xr = pow(x, d * pow(2, r), p)
                if xr == p - 1:
                    is_strong_pseudo_prime = True
                elif xr == 1:
                    return False
            if not is_strong_pseudo_prime:
                return False
    return True


def prime_number(length):
    print()
    while True:
        p = known_primes(length)

        if miller_rabin(p):
            print("Prime number: " + str(hex(p)))
            break
        else:
            print("Not prime number: " + str(hex(p)))
            continue
    return p


def generate_key_pair(length):
    p = prime_number(length)
    q = prime_number(length)

    while p == q:
        q = prime_number(length)

    n = p * q
    euler = (q - 1) * (p - 1)

    e = randint(2, (euler - 1))

    while gcd(e, euler) != 1:
        e = randint(2, (euler - 1))

    d = pow(e, -1, euler)

    open_key = [e, n]
    secret_key = [d, n]

    print("p = {}".format(hex(p)))
    print("q = {}".format(hex(q)))
    print("n = {}".format(hex(n)))
    print("e = {}".format(hex(e)))
    print("d = {}".format(hex(d)))

    return [open_key, secret_key]


def encrypt(message, open_key):
    encrypted_message = pow(message, open_key[0], open_key[1])
    return encrypted_message


def decrypt(encrypted_message, secret_key):
    decrypted_message = pow(encrypted_message, secret_key[0], secret_key[1])
    return decrypted_message


def sign(message, secret_key):
    signature = encrypt(message, secret_key)
    return signature


def verify(message, signature, open_key):
    if message == decrypt(signature, open_key):
        return True
    else:
        return False


def send_key(message, sender_secret_key, recipient_open_key):
    encrypted_message = encrypt(message, recipient_open_key)
    signature = sign(message, sender_secret_key)
    encrypted_signature = encrypt(signature, recipient_open_key)
    return encrypted_message, encrypted_signature


def receive_key(encrypted_message_and_signature, sender_open_key, recipient_secret_key):
    encrypted_message, encrypted_signature = encrypted_message_and_signature
    message = decrypt(encrypted_message, recipient_secret_key)
    signature = decrypt(encrypted_signature, recipient_secret_key)
    verification = verify(message, signature, sender_open_key)
    return message, verification
