import random
import math
import requests
import json


def NSD(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        nsd, x, y = NSD(b % a, a)
        return (nsd, y - (b // a) * x, x)


def obratnoe(b, n):
    nsd, x, y = NSD(b, n)
    if nsd == 1:
        return x % n


def primenumber_check(n, k):  # Міллер-Рабін
    t = 0
    m = n - 1
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    while m % 2 == 0:
        m = m // 2
        t += 1
    for i in range(k):
        a = random.randrange(2, n - 1)
        u = pow(a, m, n)
        if u == 1:
            continue
        if u == n - 1:
            continue
        j = 1
        while u != -1 and j < t:
            u = pow(u, 2, n)
            if u == n - 1:
                break
            j = j + 1
        else:
            return False
    return True

def GeneratePrime(n):
    n = n-1
    num=2**n
    i = 1
    while i != n:
        rand = random.randint(0,1)
        num += (2**i)*rand
        i = i + 1
    num += 1
    return num

def GenerateKeyPair(n):
    while True:
        pair = []
        i = 0
        f = open('log.txt', 'w')
        while i != 2:
            c = GeneratePrime(n)
            if not primenumber_check(c, 10):
                back = False
                while back is False:
                    c = GeneratePrime(n)
                    if primenumber_check(c, 10):
                        pair.append(c)
                        i += 1
                        back = True
                    else:
                        f.write(str(hex(c)) + " isn't prime \n")
        return pair



def FindOpenKey(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    while True:
        e = random.randint(2, phi - 1)
        if math.gcd(e, phi) == 1:
            d = obratnoe(e, phi)
            print("n " + str(hex(n)))
            print("e " + str(hex(e)))
            print("d " + str(hex(d)))
            return n, e, d


def Encrypt(K, e, n):
    return pow(K, e, n)


def Decrypt(K, d, n):
    return pow(K, d, n)


def Sign(K, d, n):
    return pow(K, d, n)


def Verify(K, s, e, n):
    return pow(s, e, n) == K


def SendKey(K, n1, d1, n2, e2):
    print("------SENDED KEYS---------")
    K1 = Encrypt(K, e2, n2)
    print("K1 = {}".format(hex(K1)[2:]))
    S = Sign(K, d1, n1)
    print("S = {}".format(hex(S)[2:]))
    S1 = Encrypt(S, e2, n2)
    print("S1 = {}".format(hex(S1)[2:]))

    return K1, S1


def ReceiveKey(eK, S1, n1, e1, n2, d2):
    print("------RECIEVED KEYS---------")
    S = Decrypt(S1, d2, n2)
    K = Decrypt(eK, d2, n2)
    if Verify(K, S, e1, n1):
        print("S = {}".format(hex(S)[2:]))
        print("K = {}".format(hex(K)[2:]))
        return K, S


while True:
    a = input("1.Server / 2.Local?")
    if a in '2':
        print('\n' * 100)
        while True:
            pair1 = GenerateKeyPair(512)
            pair2 = GenerateKeyPair(512)
            p, q, p1, q1 = pair1[0], pair1[1], pair2[0], pair2[1]
            if p*q <= p1*q1:
                break
        print("p: " + str(hex(p)), "q: " + str(hex(q)), "p1: " + str(hex(p1)), "q1: " + str(hex(q1)), sep='\n')
        n1, e1, d1 = FindOpenKey(p, q)  # A
        n2, e2, d2 = FindOpenKey(p1, q1)  # B

        Message = random.randint(0, n1)
        print("K: " + str(hex(Message)[2:]))
        print(d2)
        EncryptedMessage, EncryptedSignature = SendKey(Message, n1, d1, n2, e2)
        ReceiveKey(EncryptedMessage, EncryptedSignature, n1, e1, n2, d2)
        print("\n" * 3)

    if a in '1':
        print('\n' * 100)
        print('\n' * 100)
        pair1= GenerateKeyPair(256)
        pair2 = GenerateKeyPair(256)
        p, q = pair1[0], pair1[1]
        p1,q1 = pair2[0],pair2[1]
        n1, e1, d1 = FindOpenKey(p, q)  # A
        a = requests.get('http://asymcryptwebservice.appspot.com/rsa/serverKey?keySize=512')
        cookie = a.cookies
        cookie_name = cookie.keys()[0]
        cookie_value = cookie.values()[0]
        a = json.loads(a.text)
        e2 = int(a['publicExponent'], 16)
        n2 = int(a['modulus'], 16)
        print("e2: " + str(hex(e2)))
        print("n2: " + str(hex(n2)))
        while n2 < n1:
            print('\n'*100)
            pair1 = GenerateKeyPair(256)
            p, q = pair1[0], pair1[1]
            n1, e1, d1 = FindOpenKey(p, q)  # A
        Message = random.randint(0, n1)
        print("K: " + str(hex(Message)[2:]))
        EncryptedMessage, EncryptedSignature = SendKey(Message, n1, d1, n2, e2)
        cookie = {cookie_name: cookie_value}

        print("------RECIEVED KEYS---------")
        request = "http://asymcryptwebservice.appspot.com/rsa/receiveKey?key={k}&signature={s}&modulus={n}&publicExponent={e}".format(
            k=hex(EncryptedMessage)[2:], s=hex(EncryptedSignature)[2:], n=hex(n1)[2:], e=hex(e1)[2:])
        a = json.loads(requests.get(request, cookies=cookie).text)

        if a['key'][0] == '0':
            print("K: " + a['key'][1:])
        else:
            print("K: " + a['key'])
        print("Verified: " + str(a['verified']))
        print("\n" * 3)
