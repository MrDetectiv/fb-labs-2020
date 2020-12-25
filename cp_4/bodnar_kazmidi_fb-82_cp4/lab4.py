import urllib.parse
import requests
import json
import random
import numpy
import math

#=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>

def gcd(x, y):
    if (x % y) == 0:
        return y
    else:
        return gcd(y, x % y)

def euclid_ex(a,b):
    if a == 0:
        return b, 0, 1
    gcd, x, y = euclid_ex(b % a, a)
 
    x1 = y - math.floor(b / a) * x
    y1 = x
    return gcd, x1, y1

def ob(a,b):
    gcd, x, y = euclid_ex(a,b)
    if gcd != 1:
        return 0
    return x

def quick_pow(a, b, m):
    y = 1
    bin_list = "{0:b}".format(b)
    k = len(bin_list)
    for i in range(0, k):
        y = (y**2) % m
        y = (y * a**int(bin_list[i])) % m
    return y

def line_to_int(line):
    return '0d' + '0d'.join(list(map(str, (list(map(ord, [i for i in line]))))))

def int_to_line(int_list):
    return ''.join(list(map(chr, list(map(int, int_list.split('0d')[1:])))))


def EncDecRSA(M, e, n):
    M = list(map(int, M.split('0d')[1:]))
    C = list()
    for m in M:
        c = quick_pow(m, e, n)
        C.append(c)
    return '0d' + '0d'.join(list(map(str, C)))

def rozklad(p):
    d = 0
    s=p-1
    while s % 2 == 0:
        d += 1
        s //= 2
    return d,s

def rabin(prime):
    prime
    if prime % 2 == 0:
        return False
    
    k = 50
    d, s = rozklad(prime)
    for _ in range(k):
        
        x = random.randrange(2, prime - 1)
        xr = quick_pow(x, s, prime)
        if xr == 1 or xr == prime - 1:
            continue
        
        for i in range(d - 1):
            xr=pow(x, d * 2**i, prime)
            if xr == prime - 1:
                break
        else:
            return False
        
    return True                 
    
def random_easy(bits):
    while True:
        prime = random.getrandbits(bits - 2)
        binary = "{0:b}".format(prime)
        if len(binary) != (bits - 2):
            binary = (''.join(list(map(str, [(i - i) for i in range(0, (bits - 2 - len(binary)))])))) + binary
        prime = int(('1' + binary + '1'), 2)
        if rabin(prime):
            print(prime)
            return prime

def GenerateKeyPair(key_len):
    q = random_easy(key_len)
    p = random_easy(key_len)
    n = p * q
    oiler = (q - 1) * (p - 1)
    e = random.randint(2, oiler - 1)
    d = ob(e, oiler)
    while math.gcd(e, oiler) != 1:
        e = random.randint(2, oiler - 1)
        d = ob(e, oiler)

    if d < 0:
        d = d + oiler
    open_key = (e, n)
    sec_key = d
    return (open_key, sec_key)

def Sign(M, d, n):
    return EncDecRSA(M, d, n)

def Verify(M, e, n, S):
    Sm = EncDecRSA(S, e, n)
    if Sm == M:
        return True
    else:
        return False

def SendKey(M, d, e1, n, n1):
    Signature = Sign(M, d, n)
    S1 = EncDecRSA(Signature, e1, n1)
    Ms = EncDecRSA(M, e1, n1)
    return (Ms, S1)

def ReceiveKey(MS, e, d1, n, n1):
    Signature = EncDecRSA(MS[1], d1, n1)
    M = EncDecRSA(MS[0], d1, n1)
    verify = Verify(M, e, n, Signature)
    return (M, verify)



#=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>

e, d = GenerateKeyPair(256)

# text = input("text: ")
# C = EncDecRSA(line_to_int(text), e[0], e[1])
# print("ciphertext:", C)
# print("plaintext:", EncDecRSA(C, d, e[1]))
# print("certificate:", Sign(line_to_int(text), d, e[1]))

s = requests.Session()
serviceurl = 'http://asymcryptwebservice.appspot.com/rsa/'

url = serviceurl + 'serverKey?' + urllib.parse.urlencode({'keySize' : 512})
r = s.get(url)
data = r.json()
n1 = int(data["modulus"], 16)
e1 = int(data["publicExponent"], 16)

k = '0d123456'
MS = SendKey(k, d, e1, e[1], n1)

url = serviceurl + 'receiveKey?' + urllib.parse.urlencode({'key' : str(hex(int(MS[0][2:])))[2:], 'signature' : str(hex(int(MS[1][2:])))[2:], 'modulus' : str(hex(e[1]))[2:], 'publicExponent' : str(hex(e[0]))[2:]})
r = s.get(url)
data = r.json()
print(data)
print("key:", str(hex(int(k[2:])))[2:])
