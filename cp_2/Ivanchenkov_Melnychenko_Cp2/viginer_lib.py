import re
from collections import Counter, OrderedDict
import numpy as np
import matplotlib.ticker as ticker

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

d1 = {alphabet[i]: i for i in range(0, len(alphabet))}
d2 = {i: alphabet[i] for i in range(0, len(alphabet))}


def exclude_letters(text):
    """ исключение из текста символов не из алфавита """
    return ''.join([letter for letter in text.lower() if letter in alphabet])


def crypt(text, key):
    """ шифрование текста """
    text = text.lower()
    text = re.sub('ё', 'е', text)
    text = exclude_letters(text)
    res = ''
    counter = 0
    for letter in text:
        add = key[counter]
        new_symbol = d1[letter] + d1[add] if d1[letter] + d1[add] < len(alphabet) else d1[letter] + d1[add] - len(alphabet)
        res += d2[new_symbol]
        counter = 0 if (counter >= len(key)-1) else counter+1
    return ''.join(res)


def decrypt(text, key):
    """ дешифрование текста """
    res = ''
    counter = 0
    text = exclude_letters(text)
    for letter in text:
        add = key[counter]
        new_symbol = d1[letter] - d1[add] if (d1[letter] - d1[add]) >= 0 else d1[letter] - d1[add] + len(alphabet)
        try:
            res += d2[new_symbol]
        except:
            print(new_symbol-1)
        counter = 0 if (counter >= len(key)-1) else counter+1
    return ''.join(res)


def crypt_file(file, fileout, key):
    """ шифрование текстового файла """
    with open(file, 'r', encoding='utf-8') as f:
        res = [crypt(line, key) for line in f]
    with open(fileout, 'w', encoding='utf-8') as f:
        for item in res:
            f.write(item + '\n')


def decrypt_file(file, decryptedfile, key):
    """ расшифровка текстового файла """
    with open(file, 'r', encoding='utf-8') as f:
        res = decrypt(''.join([line for line in f]), key)
    with open(decryptedfile, 'w', encoding='utf-8') as f:
        for item in res:
            f.write(item)


def conformity_index(text):
    """ расчет индекса соответствия с использованием NumPy """
    c_dict = Counter(text)
    n = len(text)
    freq = np.array([c_dict[key] for key in c_dict.keys()])
    np_ones = np.ones(len(freq))
    f_sum = freq * (freq-np_ones)
    f_sum = sum(f_sum)
    return 1/(n*(n-1)) * f_sum


def conformity_index_file(file):
    """ расчет индекса соответствия по тексту из файла
        используется для получение индекса соответствия нешифрованного длинного текста """
    with open(file, 'r', encoding='utf-8') as f:
        return conformity_index(''.join(exclude_letters(line) for line in f))


def algorithm1(file, guess_r):
    """ выделение блоков и шифртекста согласно алгоритму 1 """
    with open(file, 'r', encoding='utf-8') as f:
        text = ''.join([exclude_letters(line) for line in f])
    Y_blocks = {i: [] for i in range(0, guess_r)}
    counter = 0
    for letter in text:
        Y_blocks[counter].append(letter)
        counter = 0 if counter+1 == guess_r else counter + 1
    for item in Y_blocks:
        Y_blocks[item] = ''.join(Y_blocks[item])
    return Y_blocks


def shift_text(cryptedtext):
    """ частоты символов шифрованного текста """
    res = ''.join(exclude_letters(cryptedtext))
    raw_freq = Counter(res)
    denom = len(res)
    freq2 = {item: raw_freq[item]/denom for item in raw_freq}
    freq2_ordered = OrderedDict(sorted(freq2.items(), key=lambda x: x[1], reverse=True))
    return freq2_ordered


def shift_file(text_file):
    """ частоты символов шифрованного файла """
    with open(text_file, 'r', encoding='utf-8') as f:
        res = ''.join(exclude_letters(line) for line in f)
        raw_freq = Counter(res)
        denom = len(res)
        freq1 = {item: raw_freq[item]/denom for item in raw_freq}

    freq1_ordered = OrderedDict(sorted(freq1.items(), key=lambda x: x[1], reverse=True))
    return freq1_ordered


def build_key(combo, crypted_freq):
    """ построение ключа из частотных словарей по порядковым номерам """
    inv_key = ''
    counter = 0
    for item in crypted_freq:
        inv_key += list(item.keys())[combo[counter]]
        counter += 1
    key = ''
    for letter in inv_key:
        shift = alphabet.index(letter) - alphabet.index('о')
        if shift < 0:
            shift += len(alphabet)
        key += alphabet[shift]
    return key
