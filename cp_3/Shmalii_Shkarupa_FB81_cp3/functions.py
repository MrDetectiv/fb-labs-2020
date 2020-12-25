import numpy as np
import  os
def Readfile(chars, filename):
    file = open(filename, 'r', encoding='utf-8')
    text = file.read().lower()
    for ch in chars:
        text = text.replace(ch, '')
    text = text.replace('ё', 'е').replace('ъ', 'ь')
    return text

def Entropy(text, alphabet):
    array  = []
    probability = dict()
    length = len(text)
    for a in alphabet:
        probability[a] = text.count(a)/length
    for elem in probability:
        if probability[elem] != 0:
            array.append(probability[elem])
    entropy =(-1) * np.sum(array*np.log2(array))
    return entropy


def frequency(bigramsAlph):
    amountAlph = dict()
    for elem in bigramsAlph:
        if elem in amountAlph:
            amountAlph[elem] = amountAlph[elem] + 1
        else:
            amountAlph[elem] = 1
    frequencylist = sorted(amountAlph.items(), key=lambda x: x[1], reverse=True)
    amountAlph.clear()
    for a in range(len(frequencylist)):
        amountAlph[frequencylist[a][0]] = frequencylist[a][1]
    return amountAlph


def makebigrams(textAlph):
    bigramsAlph = list()
    for i in range(0, len(textAlph), 2):
        bigramsAlph.append(textAlph[i:i + 2])

    return bigramsAlph
def gcd(a,b):
    if a == 0:
        return b
    if a > b:
        tmp = a
        a = b
        b = tmp
    return gcd(b%a, a)

def Converse(mod, number):
    if number == 0:
        return mod, 1, 0
    d, x, y = Converse(number, mod % number)
    return d, y, x - (mod // number) * y


def BigramNumber(amount, alphabet):
    length = len(alphabet)
    for elem in amount:
        number = alphabet.index(elem[0]) * length + alphabet.index(elem[1])
        amount[elem] = number


def NonSortedBigramNumber(bigrams, alphabet):
    length = len(alphabet)
    amount = dict()
    for elem in bigrams:
        number = alphabet.index(elem[0]) * length + alphabet.index(elem[1])
        amount[elem] = number
    return amount


def CheckKey(key,alphabet, decryptedkey, impossbigr, langentr, file):
    file.write(str(key) + "  -> ")
    print(key, end="  -> ")
    entropy = Entropy(decryptedkey, alphabet)
    lowentr = langentr - 0.1
    highentr = langentr + 0.1
    if lowentr <= entropy <=highentr:
        for b in impossbigr:
            if b in decryptedkey:
                print ("Error key! Decrypted text have impossible bigram")
                file.write("Error key! Decrypted text have impossible bigram\n")
                return False
        print("Correct key")
        file.write("Correct key\n")
        return True
    else:
        print("Error! Incorrect entropy!", entropy)
        file.write("Error! Incorrect entropy!\n")
        return False
    pass


def FindKeys(bigrams, bigramsAlph, leng, ):
    keyslist = list(list())
    bkeys = list(bigrams.keys())[0:20]
    bAlph = list(bigramsAlph.keys())[0:20]
    lbk = len(bkeys)
    length = leng**2
    for i in range(lbk):
        for k in range(1,lbk):
            for j in range(len(bAlph)):

                xstar = bigramsAlph[bAlph[i % lbk]]
                x2star = bigramsAlph[bAlph[k % lbk]]
                ystar = bigrams[bkeys[j % lbk]]
                y2star = bigrams[bkeys[(j+1) % lbk]]
                Gcd = gcd(abs(xstar-x2star),length)
                if Gcd == 1 or gcd(abs(ystar-y2star), Gcd)==Gcd :
                    acon = (Converse(length/Gcd, (xstar - x2star)/Gcd))
                    a = (acon[2]*(ystar-y2star)/Gcd) % (length/ Gcd)
                    b = (ystar - a * xstar) % (length/ Gcd)
                    keyslist.append((int(a), int(b)))
                    a = (acon[2] * (y2star - ystar)/Gcd) % (length/Gcd)
                    b = (y2star - acon[2] * xstar) % (leng ** 2)
                    keyslist.append((int(a), int(b)))
    #changing order of keys(optionally) it is for
    a = list()
    a = keyslist[0]
    keyslist[0]= keyslist[8]
    keyslist[8] = a
    return keyslist


def Decrypt(key, amount, bigrams, alphabet):
    text = ''
    length = len(alphabet)
    acon = (Converse(length ** 2, key[0])[2]) % (length**2)
    for elem in bigrams:
        number = (acon * (amount[elem] - key[1])) % (length ** 2)
        text = text + alphabet[number // length] + alphabet[number % length]
    return text