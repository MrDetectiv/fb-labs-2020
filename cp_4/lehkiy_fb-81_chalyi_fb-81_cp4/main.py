from big_num import *

def GenerateKeyPair(len_in_bits):
    p = generate_prime(len_in_bits)
    print(f"First prime number p = {p}")
    q = generate_prime(len_in_bits)
    while p == q:
        q = generate_prime(len_in_bits)
    print(f"Second prime number q = {q}")
    n = p*q
    phi_n = (p-1)*(q-1)
    e = rand_num(2,phi_n-1)
    while gcd(e,phi_n)!=1:
        e = rand_num(2,phi_n-1)
    d = converse_a(e,phi_n)
    if d < 0:
        d = d + phi_n
    public_key = [e,n]
    private_key = [d,n]

    return [public_key,private_key]

def Encrypt(message,public_key):
    return pow(message,public_key[0],public_key[1])

def Decrypt(message,private_key):
    return pow(message,private_key[0],private_key[1])

def Sign(message,private_key):
    signature = Encrypt(message,private_key)
    signed_message = [message,signature]
    return signed_message

def Verify(signed_message,public_key):
    if signed_message[0] == pow(signed_message[1],public_key[0],public_key[1]):
        return True
    else: return False

def SendKey(k,private_key_A,public_key_B):
    k1 = Encrypt(k,public_key_B)
    S = Sign(k,private_key_A)
    S1=Encrypt(S[1],public_key_B)
    return [k1,S1]

def ReceiveKey(A_mess,private_key_B,public_key_A):
    k1 = A_mess[0]
    S1 = A_mess[1]
    k = Decrypt(k1,private_key_B)
    S = Decrypt(S1,private_key_B)
    if Verify([k,S],public_key_A):
        return k
    else:
        return None



print('Abonent A:')
A = GenerateKeyPair(256)
print(f"Public key(exponent) = {A[0][0]}")
print(f"Private key = {A[1][0]}")
print(f"modulus = {A[0][1]}")
print('Abonent B:')
B = GenerateKeyPair(256)
print(f"Public key(exponent) = {B[0][0]}")
print(f"Private key = {B[1][0]}")
print(f"modulus = {B[0][1]}")

print('message encryption and decryption with A public key:')
mess = generate_prime(255)
print(f"message = {mess}")
d_mess=Encrypt(mess,A[0])
print(f"encrypted message = {d_mess}")
print(f"decrypted message = {Decrypt(d_mess,A[1])}")

print('digital signature with A private key:')
signature=Sign(mess,A[1])
print(f"message = {signature[0]}")
print(f"signature = {signature[1]}")
print(f"From A?: {Verify(signature,A[0])}")

print('SendKey, ReceiveKey protocol:')
k = generate_prime(255)
print(f"shared key = {k}")
mess_A=SendKey(k,A[1],B[0])
print(f"encrypted message = {mess_A[0]}")
print(f"signature = {mess_A[1]}")
print(f"key = {ReceiveKey(mess_A,B[1],A[0])}")

print('We send key, server receive:')
modulus=int("0x92A1802438F8FC148DCC86E5F7E705E5EA34F627DD550AB084A23D651EDDD708FA18C236DB06565455AA86FB704279543DDADFA56341AC337D98241A4A708CDF3B",16)
exp = int("0x10001",16)
print(f"Server public key(exponent) = {exp}")
print(f"Server modulus = {modulus}")


A_mess = generate_prime(255)
server_pub = [exp,modulus]
for_server = SendKey(A_mess, A[1], server_pub)

k1, s1 = for_server
print(f"encrypted message = {k1}")
print(f"signature = {s1}")

URL = 'http://asymcryptwebservice.appspot.com/rsa/receiveKey?key={}&signature={}&modulus={}&publicExponent={}'.format(hex(k1)[2:], hex(s1)[2:], hex(A[0][1])[2:], hex(A[0][0])[2:])
print(URL)