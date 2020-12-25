import itertools
import string
from math import log2
import collections

commonRussian = ('о', 'е', 'и', 'а', 'н', 'т')
russianBigrams = ('ст', 'но', 'ен', 'то', 'на')
alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
alphabet_length = len(alphabet)

letter_to_number = {k: v for v, k in enumerate(alphabet[:])}
number_to_letter = {v: k for v, k in enumerate(alphabet[:])}


def gcdex(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdex(b, a % b)
        return d, y, x - y * (a // b)


def countFun(a, b, n):
    result = []
    gcdOfAB = gcdex(a, n)[0]
    if gcdOfAB == 1:
        result.append((gcdex(a, n)[1] * b) % n)
        return result
    elif gcdOfAB > 1:
        if b % gcdOfAB == 0:
            x0 = countFun(a / gcdOfAB, b / gcdOfAB, n / gcdOfAB)[0]
            result.append(int(x0))
            for i in range(0, gcdOfAB - 1):
                x0 = x0 + n / gcdOfAB
                result.append(int(x0))
            return result
        else:
            result.append(0)
            return result


def bigram(ready_for_use_text):
    bigram_freq = {}
    length = len(ready_for_use_text[:])
    for i in range(0, length, 2):
        bigram = ready_for_use_text[i:i + 2]
        if bigram not in bigram_freq:
            bigram_freq[bigram] = 1 / length
            continue
        bigram_freq[bigram] += 1 / length
    return bigram_freq


def monogram(ready_for_use_text):
    sym_freq = {}
    length = len(ready_for_use_text[:])
    for i in ready_for_use_text:
        if i not in sym_freq:
            sym_freq[i] = 1 / length
            continue
        sym_freq[i] += 1 / length
    return sym_freq


def takeFive(text):
    result = []
    bigrams = sorted(bigram(text).items(), key=lambda x: x[1])
    for i in range(0, 5):
        result.append(bigrams.pop())
    for i in range(0, len(result)):
        result[i] = result[i][0]
    return result


def countBigramScore(bigrams):
    result = []
    for bigram in bigrams:
        result.append(letter_to_number[bigram[0]] * alphabet_length + letter_to_number[bigram[1]])
    return result


def countSingleBigramScore(bigram):
    result = letter_to_number[bigram[0]] * alphabet_length + letter_to_number[bigram[1]]
    return result


def findKeys(ab1, cd1, ab2, cd2):
    a = countFun(ab1 - cd1, ab2 - cd2, alphabet_length * alphabet_length)
    result = []
    if len(a) == 1:
        b = (ab1 - ab2 * a[0]) % (alphabet_length * alphabet_length)
        result.append((a[0], b))
        return result
    else:
        for value in a:
            b = (ab1 - ab2 * value) % (alphabet_length * alphabet_length)
            result.append((value, b))
        return result


def clear_text(text):
    punct = string.punctuation + '–' + '0' + '1' + '2' + '3' + '4' + '5' + '6' + '7' + '8' + '9' + '«' + '»' + '…' + '‘' + '№'
    punct = punct + string.ascii_lowercase
    for sym in punct[:]:
        text = text.replace(sym, '')
    text = text.replace('\n', '')
    text = text.replace('  ', ' ')
    return text.lower()


def compare(popular, decrypted):
    popularNumber = countBigramScore(popular)
    decryptedNumber = countBigramScore(decrypted)
    popComb = combinations(popularNumber)
    decComb = combinations(decryptedNumber)
    result = []
    for i in range(0, len(decComb)):
        for y in range(0, len(popComb)):
            keyValues = findKeys(decComb[i][0], decComb[i][1], popComb[y][0], popComb[y][1])
            if len(keyValues) == 1:
                result.append(keyValues[0])
            else:
                for value in keyValues:
                    result.append(value)
    result = list(dict.fromkeys(result))
    print(result)
    return result


def textDecryption(text, keys):
    bigrams = countBigramScore(bigram(text))
    finalKey = 0
    finalIndex = 0
    for key in keys:
        if key[0] == 0:
            continue
        decrypted = decrypt(bigrams, key)
        freq = countFrequency(decrypted)
        index = count_index(decrypted)
        if listInList(freq, commonRussian) >= 5:
            print("Trying key :", key)
            print("With index = ", index)
            if (index >= finalIndex)&(index< 0.9):
                finalIndex = index
                finalKey = key

        else:
            continue
    decrypted = decrypt(bigrams, finalKey)
    freq = countFrequency(decrypted)
    print("\nText decrypted with key : ", finalKey)
    print("The most common letters : ", freq)
    print(decrypted)
    print("index = ", finalIndex)
    print("\n---------------------------------")


def count_frequency(text):
    frequency = {}
    text = text.replace(' ', '').upper()
    counts = collections.Counter(text)
    for i in counts:
        frequency[i] = counts[i]
    return frequency


def count_index(text):
    text = text.replace(' ', '')
    length = len(text)
    if length == 1:
        result = 1 / ((length) * length)
    else:
        result = 1 / ((length - 1) * length)

    freq = count_frequency(text)
    sum = 0
    for letter in freq:
        sum += freq[letter] * (freq[letter] - 1)
    return result * sum


def listInList(list1, list2):
    result = 0
    for elem in list1:
        if elem in list2:
            result += 1
    return result


def countFrequency(text):
    result = []
    monograms = sorted(monogram(text).items(), key=lambda x: x[1])
    for i in range(0, 6):
        result.append(monograms.pop())
    for i in range(0, len(result)):
        result[i] = result[i][0]
    return result


def decountScore(bigram):
    a = bigram[0] % alphabet_length
    b = (bigram[0] - a) / alphabet_length
    ab = number_to_letter[b] + number_to_letter[a]
    return ab


def decrypt(bigrams, key):
    result = ""
    for bigram in bigrams:
        ab = decountScore(countFun(key[0], bigram - key[1], alphabet_length * alphabet_length))
        result = result + ab
    return result


def combinations(list):
    result = []
    copylist = list
    for item in list:
        for item2 in copylist:
            result.append((item2,item))
    return result


f = open("var17_.txt", encoding="utf8")
text = f.read()
text = clear_text(text)
fiveBigrams = takeFive(text)
keys = compare(russianBigrams, fiveBigrams)
textDecryption(text, keys)
print("finish")
