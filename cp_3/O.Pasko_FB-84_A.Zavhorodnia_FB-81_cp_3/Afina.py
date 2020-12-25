import os
from math import gcd
from collections import OrderedDict
from ChangeSymbols import ChangeSymbols


alphabet = "абвгдежзийклмнопрстуфхцчшщьыэюя"
m = len(alphabet)


def phi(n):
    res = n
    if n % 2 == 0:
        while n % 2 == 0:
            n = n // 2
        res = res // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n = n // i
            res = res // i
            res = res * (i - 1)
        i = i + 2
    if n > 1:
        res = res // n
        res = res * (n - 1)
    return res

def modul(a, b, mod):
    if gcd(a, mod) == 1:
        x = (b * a ** (phi(mod) - 1)) % mod
    elif b % gcd(a, mod) != 0:
        x = 0
    else:
        d = gcd(a, mod)
        x = modul(int(a/d), int(b/d), int(mod/d))
    return x

def key_answ(x, y):
    X = alphabet.index(x[0]) * m + alphabet.index(x[1])
    Y = alphabet.index(y[0]) * m + alphabet.index(y[1])
    print("X, Y ", X, Y)
    a = modul(X, Y, m**2)
    b = (Y - X*m)%m**2
    return (a, b)

def key_gen(x1, x2, y1, y2):
    X1 = alphabet.index(x1[0]) * m + alphabet.index(x1[1])
    X2 = alphabet.index(x2[0]) * m + alphabet.index(x2[1])
    Y1 = alphabet.index(y1[0]) * m + alphabet.index(y1[1])
    Y2 = alphabet.index(y2[0]) * m + alphabet.index(y2[1])
    a = modul(X1-X2, Y1-Y2, m**2)
    b = (Y1 - a*X1)%m**2
    return (a, b)

def Mono(text):
    LA = {}
    for let in alphabet:
        LA[let] = 0

    for let in text:
        LA[let] = LA[let] + 1

    LF = {}
    for let in alphabet:
        LF[let] = round(LA[let] / len(text), 5)

    return LF

def Bigrams(text):
    BA = {}
    for let in alphabet:
        for bi in alphabet:
            key = let + bi
            BA[key] = 0

    i = 0
    while i < len(text) - 1:
        key = text[i] + text[i + 1]
        BA[key] = BA[key] + 1
        i = i + 2

    BF = {}
    for key in BA.keys():
        BF[key] = round((BA[key]) / ((len(text) / 2)), 5)

    return OrderedDict(sorted(BF.items(), key=lambda x: x[1], reverse=True))

def encrypt(text, key):
    if len(text) % 2 == 1:
        text += "о"
    c_text = ""
    i = 0
    while i < len(text):
        X = alphabet.index(text[i]) * m + alphabet.index(text[i+1])
        Y = (key[0]*X+key[1]) % (m**2)
        y1 = Y//m
        y2 = Y%m
        c_text = c_text + alphabet[y1] + alphabet[y2]
        i += 2

    return c_text

def decrypt(text, key):
    o_text = ""
    i = 0
    while i < len(text):
        Y = alphabet.index(text[i]) * m + alphabet.index(text[i + 1])
        #print(Y)
        X = modul(key[0], Y-key[1], m**2)
        #print(X)
        x1 = X//m
        x2 = X%m
        #print("x1, x2: ", x1, "  ", x2)
        o_text = o_text + alphabet[x1] + alphabet[x2]
        i += 2

    return o_text

def Stress_Test(text):
    Res = True

    popular_letters = ["о", "е", "а", "и", "т"]
    i = 0
    for l in OrderedDict(sorted(Mono(text).items(), key=lambda x: x[1], reverse=True)):
        if i < 2:
            if l not in popular_letters:
                Res = False
        else:
            break
        i += 1
    if Res != False:
        #print("work with unpopular")
        unpopular_letters = ["ф", "э", "щ", "ц", "ш"]
        i = 0
        for l in OrderedDict(sorted(Mono(text).items(), key=lambda x: x[1])):
            if i < 2:
                if l not in unpopular_letters:
                    Res = False
            else:
                break
            i += 1
        if Res != False:
            popular_bi = ["ст", "но", "ен", "то", "на", "ов", "ни", "ра", "во", "ко"]
            i = 0
            print("work with bigrams in open text")
            for l in Bigrams(text):
                if i < 4:
                    if l[0]+l[1] not in popular_bi:
                        Res = False
                else:
                    break
                i += 1
            if Res != False:
                return True
            else:
                return False
        else:
            return False
    else:
        return False




def Analise(text):
    popular_bi = ["ст", "но", "ен", "то", "на", "ов", "ни", "ра", "во", "ко"]
    #popular_bi = ["ст", "но", "ен", "то"]

    bi = []
    i = 0
    for el in Bigrams(text):
        if i < 5:
            bi.append(el[0]+el[1])
            i += 1
        else:
            break

    print(bi)
    keys = []
    for bigr in popular_bi:
        for b in popular_bi:
            for bigc in bi:
                for bc in bi:
                    if bigr != b and bigc != bc:
                        keys.append(key_gen(bigr, b, bigc, bc))

    for key in keys:
        if key[0] == 0:
            keys.remove(key)

    print(len(keys))

    result = ""
    i = 0
    for key in keys:
        open = decrypt(text, key)
        Correct = Stress_Test(open)
        print(i)
        i += 1
        if Correct == True:
            print(key)
            result = open
            break
            #result = result + open + "\n\n\n"
        else:
            result = ""
            #result += ""

    # key = key_gen("ьб", "ьш", "ае", "фм")
    # print("key: ", key)
    # result = decrypt(text, key)
    return result




if __name__ == "__main__":
    path = os.getcwd()+r'\cipher.txt'
    path = ChangeSymbols(path, space=False)
    res = os.getcwd()+r'\result.txt'

    with open(path, 'r') as f:
        text = f.read()
        f.seek(0)

    #text = "Huisosiguboitryasi"

    result = Analise(text)

    with open(res, 'w') as r:
        r.write(result)
