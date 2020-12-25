import binascii
import requests
import hashlib
import random
import sympy
import json


# logfile = open('rsa_log.txt', 'w')


# ******* gcd inverse part *******
def mod_gcd(a, b):
    if b == 0:
        return a
    return mod_gcd(b, a % b)


def euclid_gcd(a, b):
    if a == 0:
        x, y = (0, 1)
        return b, x, y
    d, x1, y1 = euclid_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y


def inverse(a, n):
    if a < 0:
        a += n
    d, x, y = euclid_gcd(a, n)
    if d == 1:
        return x
# ********************************


# ******* prime test part ********
def miller_rabin_iter(p, x):
    if mod_gcd(p, x) != 1:
        return False

    d = p - 1
    while d % 2 == 0:
        d //= 2

    if pow(x, d, p) == 1:
        return True

    while d < p - 1:
        iter_res = pow(x, d, p)

        if iter_res == p - 1:
            return True
        if iter_res == 1:
            return False

        d *= 2
    return False


def miller_rabin(p, k=40):
    for i in range(0, k):
        x = random.randrange(2, p - 1)
        if not miller_rabin_iter(p, x):
            return False
    return True


def test_by_div(p):
    for i in list(sympy.primerange(0, 100)):
        if p % i == 0:
            return False
    return True


def gen_prime(char, size):
    while True:
        _prime = random.randrange(pow(2, size - 2), pow(2, size - 1))
        if test_by_div(_prime):
            if miller_rabin(_prime):
                prime = 2 * _prime + 1
                if test_by_div(prime):
                    if miller_rabin(prime):
                        return prime
                    else:
                        print(f'[-] {char} failed Miller Rabin test: {hex(_prime)}')
                else:
                    print(f'[-] {char} divides by simple primes: {hex(_prime)}')
            else:
                print(f'[-] {char}\' failed Miller Rabin test: {hex(_prime)}')
        else:
            print(f'[-] {char}\' divides by simple primes: {hex(_prime)}')


# ********************************


# ****** rsa primitive part ******
def gen_key_pair(size):
    print('[*] Generating p:')
    p = gen_prime('p', size)
    print('[*] Generating q:')
    q = gen_prime('q', size)
    # p = 0xd26c61265c2b2271b6cc1883de8593314943082cb11697b02e2be94921c4c1e7
    # q = 0xe2d12f9f6fae59c5176b47280cc7f9a9a92e39d907be73852d61c4911632b96b

    e = 0x10001

    f = (p - 1) * (q - 1)
    n = p * q

    d = inverse(e, f)
    d %= f

    print(f'[+] p={hex(p)}\n[+] q={hex(q)}\n[+] f={hex(f)}\n[+] n={hex(n)}\n[+] e={hex(e)}\n[+] d={hex(d)}')

    return d, e, n


def encrypt(m, e, n):
    return pow(m, e, n)


def decrypt(c, d, n):
    return pow(c, d, n)


def sign(m, d, n):
    return pow(m, d, n)


def verify(m, s, e, n):
    return m == pow(s, e, n)


def send_key(k, d, n, e1, n1):
    s = sign(k, d, n)

    k1 = encrypt(k, e1, n1)
    s1 = encrypt(s, e1, n1)
    return k1, s1


def recv_key(k1, s1, d1, n1, e, n):
    k = decrypt(k1, d1, n1)
    s = decrypt(s1, d1, n1)

    if verify(k, s, e, n):
        return k
    else:
        return 0


# def encrypt_text(message, e, n):
#     block_len = n.bit_length() // 8
#     # last block padding
#     if len(message) % block_len != 0:
#         padding_len = block_len - (len(message) % block_len)
#         message += b'\0' * padding_len
#
#     block_count = len(message) // block_len
#
#     ciphertext = b''
#
#     for i in range(block_count):
#         block = message[block_len * i: block_len * (i + 1)]
#
#         m = int.from_bytes(block, 'big')
#         c = encrypt(m, e, n)
#         ciphertext += c.to_bytes(block_len, 'big')
#
#     return ciphertext
#
#
# def decrypt_text(ciphertext, d, n):
#     block_len = n.bit_length() // 8
#     block_count = len(ciphertext) // block_len
#
#     message = b''
#
#     for i in range(block_count):
#         block = ciphertext[block_len * i: block_len * (i + 1)]
#
#         c = int.from_bytes(block, 'big')
#         m = decrypt(c, d, n)
#
#         message += m.to_bytes(block_len, 'big')
#
#     return message
#
#
# def sign_hash(message, d, n):
#     hash = hashlib.sha256(message).digest()
#
#     m = int.from_bytes(hash, 'big')
#     s = pow(m, d, n)
#
#     signature = s.to_bytes(64, 'big')
#     signature = binascii.hexlify(signature)
#     return signature
#
#
# def verify_hash(message, signature, e, n):
#     hash = hashlib.sha256(message).digest()
#     signature = binascii.unhexlify(signature)
#
#     m = int.from_bytes(hash, 'big')
#     s = int.from_bytes(signature, 'big')
#
#     if m == pow(s, e, n):
#         return True
#     return False
#
#
# def sign_text(message, d, n):
#     m = int.from_bytes(message, 'big')
#     s = sign(m, d, n)
#
#     signature = s.to_bytes(64, 'big')
#     signature = hex(signature)[2:]
#     return signature
#
#
# def verify_text(message, signature, e, n):
#     m = int.from_bytes(message, 'big')
#     s = int(signature, 16)
#
#     if verify(m, s, e, n):
#         return True
#     return False
# ********************************


if __name__ == '__main__':
    m = random.getrandbits(64)
    session = requests.Session()

    # ************************************************************************************************
    print('[*] Obtaining remote server public key')
    url_rsa_pub_key = 'http://asymcryptwebservice.appspot.com/rsa/serverKey?keySize=512'

    response = session.get(url_rsa_pub_key)
    response_json = json.loads(response.text)

    _n = response_json['modulus']
    _e = response_json['publicExponent']

    _n = int(_n, 16)
    _e = int(_e, 16)
    print()
    # ************************************************************************************************
    # generate key pair
    d, e, n = gen_key_pair(256)

    m_hex = hex(m)[2:]
    n_hex = hex(n)[2:]
    e_hex = hex(e)[2:]

    print()
    # ************************************************************************************************
    print('[*] Testing server encryption: decrypt remotely generated ciphertext')

    print(f'[*] Original message: "{m_hex}"')
    url_rsa_encrypt = 'http://asymcryptwebservice.appspot.com/rsa/encrypt?modulus=' + n_hex \
                      + '&publicExponent=' + e_hex + '&message=' + m_hex + '&type=BYTES'

    response = session.get(url_rsa_encrypt)
    response_json = json.loads(response.text)

    _c = int(response_json['cipherText'], 16)
    print(f'[*] Remotely generated ciphertext: {hex(_c)}')

    _m_hex = hex(decrypt(_c, d, n))[2:]

    print(f'[+] Decrypted ciphertext: "{_m_hex}"')

    if m_hex == _m_hex:
        print('[+] Content matched!')
    else:
        print('[-] Mismatch!')
    print()
    # ************************************************************************************************
    print('[*] Testing server encryption: decrypt locally generated ciphertext')
    print(f'[*] Original message: "{m_hex}"')
    c = encrypt(m, _e, _n)

    c_hex = hex(c)[2:]

    print(f'[+] Locally generated ciphertext: {c_hex}')

    url_rsa_decrypt = 'http://asymcryptwebservice.appspot.com/rsa/decrypt?cipherText=' + \
                      c_hex + '&expectedType=BYTES'

    response = session.get(url_rsa_decrypt)
    response_json = json.loads(response.text)

    _m_hex = hex(int(response_json['message'], 16))[2:]

    print(f'[+] Remotely decrypted ciphertext: "{_m_hex}"')

    if str(m_hex) == _m_hex:
        print('[+] Content matched!')
    else:
        print('[-] Mismatch!')
    print()
    # ************************************************************************************************
    print('[*] Testing server signatures: verify remotely generated signature')
    url_rsa_sign = 'http://asymcryptwebservice.appspot.com/rsa/sign?message=' + m_hex \
                   + '&type=BYTES'

    response = session.get(url_rsa_sign)
    response_json = json.loads(response.text)

    _s = int(response_json['signature'], 16)
    print(f'[+] Remotely generated signature: {hex(_s)}')
    if verify(m, _s, _e, _n):
        print('[+] Signature is ok!')
    else:
        print('[-] Signature mismatch!')
    print()
    # ************************************************************************************************
    print('[*] Testing server signatures: verify locally generated signature')

    s = sign(m, d, n)
    s_hex = hex(s)[2:]
    print(f'[+] Locally generated signature: {s_hex}')
    url_rsa_verify = 'http://asymcryptwebservice.appspot.com/rsa/verify?message=' + m_hex \
 \
                     + '&type=BYTES' + '&signature=' + s_hex + '&modulus=' + n_hex \
                     + '&publicExponent=' + e_hex

    response = session.get(url_rsa_verify)
    response_json = json.loads(response.text)

    verified = response_json['verified']
    if verified:
        print('[+] Signature is ok!')
    else:
        print('[-] Signature mismatch!')
    print()
    # ************************************************************************************************
    print('[*] Testing key exchange algorithm: obtain remote server session key')
    url_rsa_send_key = 'http://asymcryptwebservice.appspot.com/rsa/sendKey?modulus=' + n_hex \
                       + '&publicExponent=' + e_hex

    response = session.get(url_rsa_send_key)
    response_json = json.loads(response.text)

    _k = int(response_json['key'], 16)
    _s = int(response_json['signature'], 16)

    print(f'[+] Remote server encrypted session key: {hex(_k)}, signature: {hex(_s)}')

    k = recv_key(_k, _s, d, n, _e, _n)
    if k:
        print(f'[+] Signature OK! decrypted session key: {hex(k)}')
    print()
    # ************************************************************************************************
    print('[*] Testing key exchange algorithm: send remote server session key')
    #
    key = random.getrandbits(64)
    k, s = send_key(key, d, n, _e, _n)

    print(f'[+] Locally generated session key: {hex(key)}')
    print(f'[+] Encrypted session key: {hex(k)}')
    print(f'[+] Session key signature: {hex(s)}')
    print(f'[*] Sending to server.')

    url_rsa_recv_key = 'http://asymcryptwebservice.appspot.com/rsa/receiveKey?key=' + \
                       hex(k)[2:] + '&signature=' + hex(s)[2:] \
                       + '&modulus=' + n_hex + '&publicExponent=' + e_hex

    response = session.get(url_rsa_recv_key)
    response_json = json.loads(response.text)

    _k = response_json['key']
    verified = response_json['verified']

    if verified:
        print(f'[+] Signature is ok! Key: {_k}')
    print()
