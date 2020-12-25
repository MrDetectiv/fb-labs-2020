from funcs import *


def generate_key_pair(key_length):
    # print("Key length is " + str(key_length))
    p = random_prime(key_length)
    print(f"We found a prime number p = {p}")
    q = random_prime(key_length)
    print(f"We found a prime number q = {q}")
    while p == q:
        q = random_prime(key_length)
    # print("\nowr p = " + str(p) + "\nand q = " + str(q))
    n = q * p
    # fi(prime) = (prime - 1)
    fi_n = (q - 1) * (p - 1)
    e = random_number(2, (fi_n - 1))

    while has_common_divider(e, fi_n):
        e += 1
        if (e + 1) == fi_n:
            e = random_number(2, (fi_n - 1))

    d = find_opposite(e, fi_n)
    public_key = [e, n]
    private_key = [d, n]  # [d, p, q]
    return [public_key, private_key]


def encrypt(message, public_key):
    return left_to_right_power(message, public_key[0], public_key[1])


def decrypt(enc_message, private_key):
    return left_to_right_power(enc_message, private_key[0], private_key[1])


def sign(original_message, private_key):
    signature = encrypt(original_message, private_key)
    return signature


def verify(message, signature, public_key):
    success = (message == decrypt(signature, public_key))
    return success


def send_key(k, a_private, b_public):
    k1 = encrypt(k, b_public)  # B private (d) B private(public) (n)
    s = sign(k, a_private)  # A private (d) A private(public) (n)
    s1 = encrypt(s, b_public)   # B public (e) B public (n)
    print(f"User A puts \n\tk: {k}\n\ts: {s}\n")
    print(f"User A puts \n\tk1: {k1}\n\ts1: {s1}\n")
    return k1, s1


def receive_key(po, public_key_a, private_key_b):
    k1, s1 = po
    k = decrypt(k1, private_key_b)  # B private (d) B public (n)
    s = decrypt(s1, private_key_b)  # B private (d) B public (n)
    print(f"User B finds \n\tk: {k}\n\ts: {s}\n")
    return verify(k, s, public_key_a)  # A public
