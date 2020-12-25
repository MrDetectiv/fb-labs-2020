import numpy as np

file = open("01.txt", "r", encoding="utf-8")
output = open("output.txt", 'w', encoding = "utf-8")
russian = "абвгдежзийклмнопрстуфхцчшщьыэюя"
cipher = file.read().replace('\n', '')

def bezout(a, mod):    ------ функція розширеного алгоритму евкліда
    '''ітераційний алгоритм евкліда'''
    x, xx, y, yy = 1, 0, 0, 1
    while mod:
        q = a // mod
        a, mod = mod, a % mod
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return x, y, a
def Decryption(key, numbers, bigrams): -------------функція розшифрування 
    global russian
    decryptedtext = ''
    lengthalphabet = len(russian)
    invert = bezout(key[0], lengthalphabet ** 2)[0]
    for letter in bigrams:
        digit = (invert * (numbers[letter] - key[1])) % (lengthalphabet ** 2)
        decryptedtext = decryptedtext + russian[digit // lengthalphabet] + russian[digit % lengthalphabet]
    return decryptedtext
def GCD (x,y):
    while (y):
        x, y = y, x % y
    return x
def equation(X,Y,mod):------------------ пошуку ключа А (В функції equation я використовую функцію gcd i bezout для пошуку ключа)
    gcd = GCD(X,mod)
    a = -1
    if gcd == 1 or GCD(Y,gcd)==gcd:
        inverted = bezout(X/gcd,mod/gcd)[0]
        a = (inverted*Y/gcd)%(mod/gcd)
    return a, gcd
listofbigrams = list()
bigrams = dict()
for i in range(0,len(cipher),2):
    listofbigrams.append(cipher[i:i+2])
for elem in listofbigrams:
    if elem in bigrams:
        bigrams[elem]=bigrams[elem]+1
    else:
        bigrams[elem] = 1
max = 0
maxel = 0
mostpbigrams = dict()
bigrcopy = dict(bigrams)
for i in range(10):
    for elem in bigrcopy:
        if bigrcopy[elem] > max:
            max = bigrcopy[elem]
            maxel = elem
    mostpbigrams[maxel] = max
    bigrcopy.pop(maxel)
    maxel = 0
    max = 0
for elem in bigrams:
    bigrams[elem] = russian.index(elem[0])*len(russian) + russian.index(elem[1])
bigrrus = dict()
for elem in ['ст','но','то','на','ен','ов','ни','ра','во','ко']:
    bigrrus[elem] = russian.index(elem[0]) * len(russian) + russian.index(elem[1])
for elem in mostpbigrams:
    mostpbigrams[elem]= russian.index(elem[0]) * len(russian) + russian.index(elem[1])
keys = list(list())
a = 0
b = 0
bigrrusl = list(bigrrus.keys())
mostpbigramsl = list(mostpbigrams.keys())
for i in range(10):
    for j in range(i,10):
        for k in range(10):
            a, gcd = equation((bigrrus[bigrrusl[i % 10]] - bigrrus[bigrrusl[j % 10]]),
                              (mostpbigrams[mostpbigramsl[(k) % 10]] - mostpbigrams[mostpbigramsl[(k+1) % 10]]),
                              len(russian) ** 2)
            if a != -1:
                b = (mostpbigrams[mostpbigramsl[k % 10]] - a * bigrrus[bigrrusl[i % 10]]) % ((len(russian) ** 2) / gcd)
                keys.append((int(a), int(b)))

for i in range(10):
    for j in range(i,10):
        for k in range(10):
            a,gcd = equation((bigrrus[bigrrusl[i%10]] - bigrrus[bigrrusl[j % 10]]),(mostpbigrams[mostpbigramsl[(k+1)%10]]- mostpbigrams[mostpbigramsl[k%10]]),len(russian)**2)
            if a != -1:
                b = (mostpbigrams[mostpbigramsl[(k+1) % 10]]-a*bigrrus[bigrrusl[i % 10]])%((len(russian)**2)/gcd)
                keys.append((int(a),int(b)))
for elem in keys:
    temptext = Decryption(elem, bigrams,listofbigrams)
    array = []
    length = len(temptext)
    for let in russian:
        array.append(temptext.count(let) / length)
    entropy = (-1) * np.sum(array * np.log2(array))
    redundacy = 1 - entropy/np.log2(len(russian))
    if redundacy>0.1:
        output.write(str(elem)+  "    REDUNDANCY OK" + str(redundacy))
        output.write(temptext)
        print(elem, "    REDUNDANCY OK", redundacy)
        print(temptext)
        break
    else:
        output.write(str(elem)+" REDUNDANCY NOT OK" + str(redundacy))
        print(elem, "    REDUNDANCY NOT OK", redundacy)


