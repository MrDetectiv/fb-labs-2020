import codecs as cs
import math
from itertools import cycle
import operator

filename = input('File: ')
if len(filename) < 1: filename = 'vigenere.txt'

# =======================================

alphabet = "а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я".split()
freq = {
    'о' : 0.114725160004508,
    'е' : 0.0871670156415899,
    'а' : 0.07966000154221213,
    'н' : 0.06508609695769,
    'и' : 0.06484764723677108,
    'т' : 0.06475155555819181,
    'с' : 0.05293109277592251,
    'в' : 0.0462616184923097,
    'л' : 0.04596148028637693,
    'р' : 0.04183191074150745,
    'к' : 0.03302706582279983,
    'д' : 0.032017510039207775,
    'м' : 0.03143977365071268,
    'у' : 0.02965199390233052,
    'п' : 0.027441885295007386,
    'ь' : 0.022984892252756704,
    'я' : 0.02136438320412364,
    'ч' : 0.018103197717526054,
    'б' : 0.017389034871788788,
    'г' : 0.016890781723599996,
    'ы' : 0.016513532911399915,
    'з' : 0.015397208596053123,
    'ж' : 0.011408810776503806,
    'й' : 0.010013701961575193,
    'х' : 0.008508265663833347,
    'ш' : 0.00823066748127102,
    'ю' : 0.005617211087318864,
    'э' : 0.0035269204989649386,
    'щ' : 0.00299070520615224,
    'ц' : 0.00277242287456477,
    'ф' : 0.0012444465534524791,
    'ъ' : 0.00024200867197741253
}


def split_text(text):
    result = list()
    index_list = list()

    for i in range(1, len(text)):
        index = [*range(0, len(text), i)]
        index_list.append(index)
        
    for i in range(len(index_list)):
        res = ''
        for j in index_list[i]:
            res = res + text[j]
        result.append(res)

    return result

def filter(textLine):
    textLine = textLine.replace('ё', 'е')
    for letter in textLine:
        if letter not in alphabet:
            textLine = textLine.replace(letter, '')
    return textLine

def letter_counter(text, isFreq, isDict, isLarge):
    letters = dict()
    length = 0

    if isLarge == 1:
        for line in text:
            line = filter(line.lower())
            for sym in line:
                letters[sym] = letters.get(sym, 0) + 1
            length = length + len(line)
    else:
        text = filter(text.lower())
        for sym in text:
            letters[sym] = letters.get(sym, 0) + 1
        length = len(text)

    if isFreq == 1:
        for letter in letters:
            letters[letter] = letters[letter] / length
    if isDict == 0:
        result = list()
        for letter in letters:
            result.append(letters[letter])
        return result

    return letters

def count_index(n, arr):
    N = 1 / (n * (n - 1))
    summ = 0
    for i in range(len(arr)):
        summ += arr[i] * (arr[i] - 1)
    return N * summ

def get_indices(text):
    divided = split_text(text)
    dividedFreq = list()
    for line in divided:
        dividedFreq.append(letter_counter(line, 0, 0, 0))

    indices = list()
    for i in range(len(dividedFreq)):
        indices.append(round(count_index(len(divided[i]), dividedFreq[i]), 3))
    return indices

def encode_vigenere(text, key):
    f = lambda arg: alphabet[(alphabet.index(arg[0]) + alphabet.index(arg[1]) % 32) % 32]
    return ''.join(map(f, zip(text, cycle(key)))) 

def decode_vigenere(enc_text, key):
    f = lambda arg: alphabet[alphabet.index(arg[0]) - alphabet.index(arg[1]) % 32]
    return ''.join(map(f, zip(enc_text, cycle(key))))

def printSorted(lDict):
    tupleList = lDict.items()
    
    tupleList = sorted(tupleList, key=lambda i: i[1], reverse=True)

    for item in tupleList:
        print('\'' + item[0] + '\'' + ' : ' + str(item[1]) + ',')

    print('\n')

def split_with_key(text, key_len):
    result = list()

    for i in range(key_len):
        line = ''
        for j in range(0, len(text), key_len):
            if (i + j) < len(text):
                line = line + text[i + j]
        result.append(line)
    return result

def find_key(spl_text, arr):
    key = ''

    for i in range(len(spl_text)):
        lineFreq = letter_counter(spl_text[i], 1, 1, 0)
        
        tupleFreq = lineFreq.items()
        tupleFreq = sorted(tupleFreq, key=lambda i: i[1], reverse=True)
        key = key + get_letter(alphabet.index(arr[i]), alphabet.index(tupleFreq[0][0]))
    return key

def get_letter(p, s):
    k = s - p
    if k < 0:
        k = k + 32
    return alphabet[k]

# =======================================

hfile = cs.open(filename, "r", encoding='utf-8')
text = filter(hfile.read().lower())

spl_text = split_with_key(text, 14)
key = find_key(spl_text, ['е', 'о', 'о', 'е', 'о', 'е', 'е', 'о', 'е', 'о', 'о', 'о', 'о', 'о'])
print('Key:', key)
print('Plaintext:\n' + decode_vigenere(text, key))

# print('\n' + 'Plaintext:\n' + decode_vigenere(text, 'последнийдозор'))

# =======================================

hfile.close()
input()