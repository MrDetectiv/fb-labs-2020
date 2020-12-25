import random
import math

def evclid (a, b):
    if(b == 0):
        return (1, 0, a)
    v, u, d = evclid(b, a%b)
    return (u, v - (a//b)*u, d)

def obern (a, n):
    u, v, d = evclid(a, n)
    if d != 1:
        print("No reverse")
        return 0
    else: return u

def isPrime(p):
    b = 10
    for i in [2, 3, 5, 7, 11]:
        if math.gcd(i, p) > 1:
            print('Divisible by {}'.format(i))
            return 0
    d = p - 1
    s = 0
    while d%2 == 0:
        s += 1
        d //= 2
    d = int(d)
    for i in range(5):
        x = random.randint(2, p-1)
        if math.gcd(x, p) > 1:
            print('MillerRabin test is failed')
            return 0
        else:
            if pow(x, d, p) != 1 and pow(x, d, p) != p-1:
                isprimenum = 0
                for r in range(1, s):
                    xr = pow(x, d*(2**r), p)
                    if xr == 1:
                        print('MillerRabin test is failed')
                        return 0
                    if xr == p-1:
                        isprimenum = 1
                        break
                if not isprimenum:
                    print('MillerRabin test is failed')
                    return 0
    return 1

def findPrime (amountbits):
    p, m0 = 0, 0
    used_x = []
    n0 = int(('0b1' + '0'*(amountbits - 2) + '1'), 2)
    n1 = int(('0b' + '1'*amountbits), 2)
    while (p == 0):
        x = random.randint(n0, n1)
        while x in used_x:
            x = random.randint(n0, n1)
        used_x.append(x)
        if(x%2 == 0):
            m0 = x+1
        else:
            m0 = x
        for i in range(int((n1 - m0)/2)):
            print(hex(m0 + 2*i))
            if isPrime(m0 + 2*i):
                p = m0 + 2*i
                break
    return p

def GetPQ():
    p, q = findPrime(256), findPrime(256)
    return p, q

def GenerateKeyPair(p, q):
    n = p*q
    phi = (p-1)*(q-1)
    e = random.randint(2, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d = obern(e, phi)
    return d, [n, e]

def Encrypt(M, e, n):
    if M > n - 1:
        print('Long M')
        return 0
    C = pow(M, e, n)
    return C

def Decrypt(C, d, n):
    M = pow(C, d, n)
    return M

def Sign(M, d, n):
    S = pow(M, d, n)
    return [M, S]

def Verify(M, S, e, n):
    if M == pow(S, e, n): return 1
    else: return 0

def SendKey(public1, secret1, public2, k):
    while(public2[0] < public1[0]):
        p, q = GetPQ()
        secret1, [public1[0], public1[1]] = GenerateKeyPair(p, q)
    n, e = public1[0], public1[1]
    n1, e1 = public2[0], public2[1]
    d = secret1
    k1 = Encrypt(k, e1, n1)
    S = Sign(k, d, n)[1]
    S1 = Encrypt(S, e1, n1)
    return [k1, S1]

def RecieveKey(public2, secret2, public1, message):
    k = Decrypt(message[0], secret2, public2[0])
    S = Decrypt(message[1], secret2, public2[0])
    if Verify(k, S, public1[1], public1[0]):
        print('Sign verified')
        return [k, S]
    else:
        print('Sign unverified')
        return [0, 0]

pA, qA = GetPQ()
pB, qB = GetPQ()
if pA*qA >= pB*qB:
    pA, pB = pB, pA
    qA, qB = qB, qA

print('p = ', hex(pA))
print('q = ', hex(qA))
print('p1 = ', hex(pB))
print('p2 = ', hex(qB))

secretA, publicA = GenerateKeyPair(pA, qA)
print('''Secret A: {}\nPublicA: {}, {}'''.format(hex(secretA), hex(publicA[0]), hex(publicA[1])))
secretB, publicB = GenerateKeyPair(pB, qB)
print('''SecretB: {}\nPublicB: {}, {}'''.format(hex(secretB), hex(publicB[0]), hex(publicB[1])))

M = random.randint(0, publicA[0] - 1)
print('Message M: {}'.format(hex(M)))
CA = Encrypt(M, publicA[1], publicA[0])
print('Encrypted message A: {}'.format(hex(CA)))
CB = Encrypt(M, publicB[1], publicB[0])
print('Encrypted message B: {}'.format(hex(CB)))

DA = Decrypt(CA, secretA, publicA[0])
print('Decrypted message A: {}'.format(hex(DA)))
DB = Decrypt(CB, secretB, publicB[0])
print('Decrypted message B: {}'.format(hex(DB)))

MessA = Sign(M, secretA, publicA[0])
print('''Signed message A: {}\n{}'''.format(hex(MessA[0]), hex(MessA[1])))
MessB = Sign(M, secretB, publicB[0])
print('''Signed message B: {}\n{}'''.format(hex(MessB[0]), hex(MessB[1])))

if Verify(MessA[0], MessA[1], publicA[1], publicA[0]):
    print('A verified')
if Verify(MessB[0], MessB[1], publicB[1], publicB[0]):
    print('B verified')

[n1, e1] =  [int('8E9ADF6514943513235A9446F726B61C58F62F0388234AAAF16DEB95E61539D5C302B6257E49F6332324AF25DBEDCA346121B3E4B89E88185A4449C10E70D369', 16), int('10001', 16)]
p0, q0 = GetPQ()
d, [n, e] = GenerateKeyPair(p0, q0)
print(hex(d))
print(hex(n), hex(e))
print('Key: ')
k = random.randint(1, 513)
print(hex(k))
sended = SendKey([n, e], d, [n1, e1], k)
print(hex(sended[0]), hex(sended[1]))
#recieved = RecieveKey([n1, e1], d1, [n, e], sended)
#print('Recieved:')
#print(hex(recieved[0]), hex(recieved[1]))
