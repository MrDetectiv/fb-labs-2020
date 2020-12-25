import random
from math import gcd, log2


def euclid(a, b):
    if not b:
        return (1, 0, a)
    y, x, g = euclid(b, a % b)
    return (x, y - (a // b) * x, g)

def inversmod(e, n):
    if gcd(e, n) != 1:
        return 0
    d = euclid(e, n)[0]
    if d < 0:
        d = n - d
    return d


def gorn(x, a, m = None):
    a = str(bin(a))[2:]
    res = 1
    for i in a:
        i = int(i)
        if (m == None):
            b = x ** i
            res = (res**2) * (b)
            i += 1
        else:
            b = x ** i % m
            res = (res ** 2) * (b) % m
    return res


def test(value):
    for n in [2, 3, 5, 7, 11]:
        if gcd(value, n) != 1 or pow(n, value-1, value) != 1:
            return False
    d = value - 1
    while d % 2 == 0:
        d = d // 2
    s = int(log2((value - 1) // d))
    #print(s)
    for t in range(4):
        x = random.randint(2, value-2)
        d = int(d)
        if (gcd(x, value) > 1):
            return False
        b = pow(x, d, value)
        if (b == 1 or b == value - 1):
           continue
        else:
            i = 1
            pseudo = False
            while i < s:
                buf = pow(x, d * pow(2, i), value)
                if (buf == value - 1):
                    pseudo = True
                elif buf == 1:
                    return False
                else:
                    continue
                i += 1
            if not pseudo:
                return False
    return True

def Random_prime(f, k, begin=None, end=None, length=None):
    if(begin == None and end == None and length == None):
        print("Write some params")
        return 0
    elif (begin == None and end == None and length != None):
        min = int('1'+'0'*(length-1), 2)
        max = int('1' * length, 2)
        val = random.randint(min, max)
        if (val % 2 == 0):
            x = val + 1
        else:
            x = val
        for i in range(1, (max - x) // 2):
            #print(val)
            val = x + 2 * i
            if (test(val)):
                return val
            response = "Для ключа " + k + " не прошел тест на простоту: " + str(val) + '\n'
            f.write(response)
        print("New step")
        Random_prime(length=length)
    elif (begin == None and end != None):
        val = random.randint(0, end)
        while True:
            if(test(val) == True):
                return val
            val += 1
    elif (begin != None and end != None):
        if begin > end:
            print("begin > end, it was switched")
            val = random.randint(begin, end)
        else:
            val = random.randint(begin, end)
        while True:
            if (test(val) == True):
                return val
            val += 1
    else:
        print("Error: wrong params")
        return 0;

if __name__ == "__main__":
    # num = Random_prime(length=256)
    # print("finish: ", num)
    # num = Random_prime(length=256)
    # print("finish: ", num)
    # num = Random_prime(length=256)
    # print("finish: ", num)
    # num = Random_prime(length=256)
    # print("finish: ", num)
    print(test(95499716561418340612002475814977484904588471241006525073490307194191922406607))