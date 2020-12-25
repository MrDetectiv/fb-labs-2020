from RSA.rsa import *
from RSA.crypto_math import *

if __name__ == '__main__':
    p, q, p1, q1 = generate_key_pairs(256)

    rsa = RSA(p, q)
    rsa1 = RSA(p1, q1)

    print(rsa)
    print(rsa1)

    x = random.randint(0, rsa.n - 1)

    k1, s1 = rsa.send_key(x, rsa1)
    print(rsa1.receive_key(k1, s1, rsa))

