import random
from math import gcd
from reverse import Reverse
from req import ServerSide

def miller_rabin(p):
    if p == 2:
        return True
    elif p == 3:
        return True
    elif p % 2 == 0:
        return False
    else:
        s = 0
        d = p - 1
        while d % 2 == 0:
            d = d // 2
            s += 1

        for i in range(5):
            randprime = random.randrange(2, p - 1)
            x = pow(randprime, d, p)
            j = 0
            if x == 1:
                continue
            elif x == p - 1:
                continue
            while j < s - 1:
                x = pow(x, 2, p)
                if x == p - 1:
                    break
                j += 1
            else:
                return False
        return True

def primegenerator(size):
    a = open(r'C:\Users\funro\Desktop\univer\kripta\cryptolabs\fb-labs-2020\cp_4\miller_rabin.log','w+')
    while True:
        number=pow(2,size-1)
        for i in range(1,size-1,1):
            b = random.randint(0,1)
            number += (pow(2,i)*b)
        number += 1
        if miller_rabin(number):
            return number
        else:
            a.write(f'\n{number} not OK - this number failed Miller-Rabin test.')
            continue

def generatekeypairs(keysize):
    a_keys,b_keys = [],[]
    a_keys.append(primegenerator(keysize))
    a_keys.append(primegenerator(keysize))
    while True:
        b1,b2 = primegenerator(keysize),primegenerator(keysize)
        if b1 * b2 >= a_keys[0] * a_keys[1]:
            b_keys.append(b1)
            b_keys.append(b2)
            break
    return a_keys,b_keys

def findkeysets(p,q):
    n = p*q
    phi_n = (p-1)*(q-1)
    while True:
        e = random.randint(2,phi_n-1)
        if gcd(e,phi_n) == 1:
            break
    #n,e = findopenkeys(p,q,n,phi_n)
    d = Reverse().reverse(e,phi_n) 
    public_n_e = [n,e]
    private_d_p_q = [d,p,q]
    return public_n_e,private_d_p_q

def encrypt(M,e,n):
    return pow(M,e,n)

def decrypt(encrypted_message,d,n):
    return pow(encrypted_message,d,n)

def sign(decrypted_message,d,n):
    return pow(decrypted_message,d,n)

def verify(decrypted_message,signature,e,n):
    return pow(signature,e,n) == decrypted_message

def send_key(public_n_e,public_n1_e1,private_d_p_q,opentext):
    encrypted_message = encrypt(opentext,public_n1_e1[1],public_n1_e1[0])
    signature = sign(opentext,private_d_p_q[0],public_n_e[0])
    encrypted_signature = encrypt(signature,public_n1_e1[1],public_n1_e1[0])
    return encrypted_message,encrypted_signature

def recieve_key(encrypted_message,signature,public_n_e,public_n1_e1,private_d1_p1_q1):
    verified = {}
    decrypted_message = decrypt(encrypted_message,private_d1_p1_q1[0],public_n1_e1[0])
    decrypted_signature = decrypt(signature,private_d1_p1_q1[0],public_n1_e1[0])
    if verify(decrypted_message,decrypted_signature,public_n_e[1],public_n_e[0]):
        verified[decrypted_signature] = decrypted_message
    return verified

def main():
    keys = generatekeypairs(256)
    p,q = keys[0][0],keys[0][1]
    public_n_e,private_d_p_q = findkeysets(p,q)
    p1,q1 = keys[1][0],keys[1][1]
    public_n1_e1,private_d1_p1_q1 = findkeysets(p1,q1)
    random_opentext = random.randint(0,public_n_e[0])
    #print(f'Open text: {hex(random_opentext)};')
    ciphertext,signature = send_key(public_n_e,public_n1_e1,private_d_p_q,random_opentext)
    #print(f'Ciphertext: {hex(ciphertext)};')
    verified = recieve_key(ciphertext,signature,public_n_e,public_n1_e1,private_d1_p1_q1)
    for key,value in verified.items():
        print(f'Verified signature: {str(hex(key))[2:]}\nDecrypted text: {str(hex(value))[2:]}')
    print(f'Modulus: {str(hex(public_n_e[0]))[2:]}\nPublic Exponent: {str(hex(public_n_e[1]))[2:]}')
    # print(f'Modulus B: {str(hex(public_n1_e1[0]))[2:]}\nPublic Exponent B: {str(hex(public_n1_e1[1]))[2:]}')
    # print(f'p: {str(hex(p))[2:]}\nq: {str(hex(q))[2:]}\np1: {str(hex(p1))[2:]}\nq1: {str(hex(q1))[2:]}')
    # print(f'Private Key: {str(hex(private_d_p_q[0]))[2:]}\nPrivate Key B: {str(hex(private_d1_p1_q1[0]))[2:]}')
    # print(f'Ciphertext: {ciphertext}')


def checkdecrypt(server):
    p = primegenerator(256)
    q = primegenerator(256)
    public_n_e = findkeysets(p,q)[0]
    public_n1_e1 = server.generatekeys(512)
    open_text = random.randint(0,public_n_e[0])
    print(open_text)
    cipher_text = encrypt(open_text,public_n1_e1[1],public_n1_e1[0])
    print(server.decrypt(cipher_text))

def checkencrypt(server):
    p = primegenerator(256)
    q = primegenerator(256)
    public_n_e,private_d_p_q = findkeysets(p,q)
    server.generatekeys(512)
    open_text = random.randint(0,public_n_e[0])
    ciphertext = server.encrypt(open_text,public_n_e[1],public_n_e[0])
    print(open_text)
    print(decrypt(ciphertext,private_d_p_q[0],public_n_e[0]))

# server = ServerSide()
# checkencrypt(server)
# checkdecrypt(server)
main()