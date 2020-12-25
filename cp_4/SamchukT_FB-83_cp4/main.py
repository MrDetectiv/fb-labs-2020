import random

def gcd(a, b): #НСД
    while a != 0:
        a, b = b % a, a
    return b

def power(x, a, n):
    bin_num = bin(a)
    bin_num = bin_num[2:]
    k = len(bin_num)
    y = 1
    for i in range(k):
        y = (y ** 2) % n
        y = (y * x ** int(bin_num[i])) % n
    # print(y)
    return y

def euclid(a, b): #роширений алгоритм евкліда
    if (b == 0):
        return a, 1, 0
    d, x, y = euclid(b, a % b)
    return d, y, x - (a // b) * y

def ober(b, n):
    g, x, y = euclid(b, n)
    if g == 1:
        return x % n

def MilleraRabina(n, k):
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
        x = pow(a, m, n)
        if x == 1 or x == n - 1:
            continue
        j = 1
        while x != -1 and j < t:
            x = pow(x, 2, n)
            if x == n - 1:
                break
            j = j + 1
        else:
            return False
    return True

def GenerateKeyPair(n):
    while True:
        pair1 = []
        i = 0
        f = open('log.txt', 'w')
        while i != 2:
            c = random.getrandbits(n-1) + (1 << n-1)
            if not MilleraRabina(c, 10):
                back = False
                while back is False:
                    c = random.getrandbits(n-1) + (1 << n-1)
                    if MilleraRabina(c, 10):
                        pair1.append(c)
                        i += 1
                        back = True
                    else:
                        f.write(str(hex(c)) + " isn't prime \n")
        return pair1

def Encrypt(text, epsi, n):
    if text > n - 1:
        print('Long message')
        return 0
    c_text = power(text, epsi, n)
    return c_text

def Decrypt(c_text, d, n):
    d_text = power(c_text, d, n)
    return d_text

def Verify(sign_text, n, epsi, message):
    m = Encrypt(sign_text, epsi, n)
    if m == message:
        print("Verified")
        return True
    else:
        print("not verified")
        return False

def Sign(text, d, n):
    sign_text = power(text, d, n)
    return sign_text

def SendKey(m, n1, epsi1):
    cyfr_m = Encrypt(m, epsi1, n1)
    p_q_alis = GenerateKeyPair(265)
    n = p_q_alis[0] * p_q_alis[1]
    while n > n1:
        p_q_alis = GenerateKeyPair(256)
        n = p_q_alis[0] * p_q_alis[1]
    znach = (p_q_alis[0] - 1) * (p_q_alis[1] - 1)  # olier
    d = ober(epsi, znach)
    sign_text = Sign(m, d, n)
    sign_text = Encrypt(sign_text, epsi1, n1)
    return cyfr_m, sign_text, n

def ReceiveKey(cyfr_m, signature, epsi, n):
    M = Decrypt(cyfr_m, d1, n1)
    S = Decrypt(signature, d1, n1)
    M1 = Verify(S, n, epsi, M)
    return M, M1

if __name__ == "__main__":
    text = 5678
    p_q_bob = GenerateKeyPair(265)
    n1 = p_q_bob[0] * p_q_bob[1]
    epsi = 2 ** 16 + 1
    znach = (p_q_bob[0] - 1) * (p_q_bob[1] - 1) #olier
    d1 = ober(epsi, znach)

    cyfr_text, signature, n = SendKey(text, n1, epsi)
    print(ReceiveKey(cyfr_text, signature, epsi, n))
#########################
    epsi = 2 ** 16 + 3
    epsi1 = 2 ** 16 + 1
    n1 = (int('8E17C12D8D13DA9FF45A488EA41D0F764604C5729F0F9DA991295D8BFE135C70F33D6439725F1BC4249D8D2D6A2B7776D16B67F4458A6D2442367F90F5776FB7', 16))
    cyfr_text, signature, n = SendKey(text, n1, epsi1)
    print(hex(cyfr_text))
    print(hex(signature))
    print(hex(n))