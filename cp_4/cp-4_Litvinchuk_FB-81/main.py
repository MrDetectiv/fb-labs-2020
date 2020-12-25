import random

def gen_random(a,b):
    return random.randint(a,b)

def euclid_NSD(a,b):
    if a == 0:
        x, y = (0, 1)
        return b, x, y
    d, x1, y1 = euclid_NSD(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y

def NSD(a,b):
    r = euclid_NSD(a,b)
    return r[0]

def mod_pow(x, a, m):
    bin_nums = [int(n) for n in bin(a)[2:] ]
    r = 1
    for n in bin_nums:
        r = r ** 2 % m
        r = r * (x ** n) % m 
    return r 

def obernenyu(x,m):
    r = euclid_NSD(x,m)
    if r[0]==1:
      if x<=m: return r[1]
      if x>m: return r[2]
    else: return None

def miller_rabin_iter(t, x):
    if NSD(t, x) != 1:
        return False
    d = t - 1
    while d % 2 == 0:
        d //= 2
    if (m := mod_pow(x, d, t)) == 1 or m == t - 1:
        return True
    while d < t - 1:
        iter_result = mod_pow(x, d, t)
        if iter_result == t - 1:
            return True
        if iter_result == 1:
            return False
        d *= 2
    return False


def Miller_Rabin_test(p):
    k=40
    for i in range(0, k):
        x = gen_random(2, p - 1)
        if not miller_rabin_iter(p, x):
            return False 
    else:
        return True

def gen_prime(l):
    min = 2**(l-1)+1
    max = 2**l-1
    while True:
       x = gen_random(min,max)
       for i in range(0,(max-x+(1-x%2))//2):
           if x % 2 == 0:
              x+=1
           if small_div_test(x):
              if Miller_Rabin_test(x):
                 return x
           x+=2

def small_div_test(n):
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,
                    53,59,61,67,71,73,79,83,89,97,101,103, 107, 
                    109, 113, 127, 131, 137, 139, 149, 151, 157,
                    163, 167, 173, 179, 181, 191, 193, 197, 199, 
                    211, 223, 227, 229, 233, 239, 241, 251, 257,
                    263, 269, 271, 277, 281, 283, 293, 307, 311, 
                    313, 317, 331, 337, 347, 349, 353, 359, 367, 
                    373, 379, 383, 389, 397, 401, 409, 419, 421,
                    431, 433, 439, 443, 449, 457, 461, 463, 467, 
                    479, 487, 491, 499, 503]
    for i in primes:
        if n%i==0 and n//i!=1: return False
    return True

def Gen_Pair_of_Keys(l):
    p = gen_prime(l)
    print(f"P = {p}")
    q = gen_prime(l)
    while p == q:
        q = gen_prime(l)
    print(f"Q = {q}")
    n = p*q
    phi_n = (p-1)*(q-1)
    e = gen_random(2,phi_n-1)
    while NSD(e,phi_n)!=1:
        e = gen_random(2,phi_n-1)
    d = obernenyu(e,phi_n)
    if d < 0:
        d = d + phi_n
    open_key = [e,n]
    private_key = [d,n]

    return [open_key,private_key]


def Encrypt(M,open_key):
    return pow(M,open_key[0],open_key[1])

def Decrypt(M,private_key):
    return pow(M,private_key[0],private_key[1])

def Sign(M,private_key):
    s = Encrypt(M,private_key)
    s_m = [M,s]
    return s_m

def Verify(s_m,open_key):
    if s_m[0] == pow(s_m[1],open_key[0],open_key[1]):
        return True
    else: return False


def SendKey(M,private_key_A,open_key_B):
    e_m = Encrypt(M,open_key_B)
    s   = Sign(M,private_key_A)
    e_s = Encrypt(s[1],open_key_B)
    return [e_m, e_s]

def ReceiveKey(M,private_key_B,open_key_A):
    e_m = M[0]
    e_s = M[1]
    m = Decrypt(e_m,private_key_B)
    s = Decrypt(e_s,private_key_B)
    if Verify([m,s],open_key_A):
        return m
    else:
        return None



print('ABONENT A:')
A = Gen_Pair_of_Keys(256)
print(f"E = {A[0][0]}")
print(f"D = {A[1][0]}")
print(f"N = {A[0][1]}\n")

print('ABONENT B:')
B = Gen_Pair_of_Keys(256)
print(f"E = {B[0][0]}")
print(f"D = {B[1][0]}")
print(f"N = {B[0][1]}\n")

mess = gen_prime(255)
print(f"MESSAGE = {mess}")
d_mess=Encrypt(mess,A[0])
print(f"ENCRYPTED MESSAGE WITH A PUB KEY = {d_mess}")
print(f"DECRYPTED MESSAGE WITH A PRIV KEY = {Decrypt(d_mess,A[1])}")
d_mess=Encrypt(mess,B[0])
print(f"ENCRYPTED MESSAGE WITH B PUB KEY = {d_mess}")
print(f"DECRYPTED MESSAGE WITH B PRIV KEY = {Decrypt(d_mess,B[1])}\n")


print('SIGN WITH A PRIVATE KEY:')
s=Sign(mess,A[1])
print(f"MESSAGE = {s[0]}")
print(f"SIGNATURE = {s[1]}")
print(f"VERIFIED: {Verify(s,A[0])}\n")


print('SENDKEY, RECEIVEKEY PROTOCOL (A TO B):')
k = gen_prime(255)
print(f"SHARED KEY = {k}")
m=SendKey(k,A[1],B[0])
print(f"ENCRYPTED MESSAGE = {m[0]}")
print(f"SIGNATURE = {m[1]}")
print(f"KEY = {ReceiveKey(m,B[1],A[0])}\n\n")


print('SENDKEY, RECEIVEKEY PROTOCOL (A TO SERVER):')
n=int("0xD75B159AD05869959926A0BE751038E07C93B6FB11AF6BE21C1F24D7EE120B7D",16)
e = int("0x10001",16)
print(f"SERVER E = {e}")
print(f"SERVER N = {n}")
k = gen_prime(255)
print(f"SHARED KEY = {k}")
m = SendKey(k, A[1], [e,n])
print(f"ENCRYPTED MESSAGE = {m[0]}")
print(f"SIGNATURE = {m[1]}\n")

URL = 'http://asymcryptwebservice.appspot.com/rsa/receiveKey?key={}&signature={}&modulus={}&publicExponent={}'.format(hex(m[0])[2:], hex(m[1])[2:], hex(A[0][1])[2:], hex(A[0][0])[2:])
print(URL) 

