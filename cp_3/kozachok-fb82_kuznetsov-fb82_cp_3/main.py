# -*- coding: utf-8 -*-
import codecs as cs
import math
from typing import Dict, List, Tuple

ciphertext_filename = "09.txt"
alphabet = list("абвгдежзийклмнопрстуфхцчшщьыэюя")
inacceptable_bigrams = [ "жы", "шы", "аь", "аы", "уы", "еы", "оы" ]
freq = [ 
    'то', 'ов', 'на', 'не', 'но', 'ст', 'по', 'ко', 'он', 'от', 'ен',
    'ни', 'ос', 'го', 'ал', 'ра', 'ро', 'ка', 'ет', 'ть', 'во', 'пр',
    'ер', 'ак', 'ес', 'ас', 'ло', 'ол' 
]
letter_number = {letter: i for i, letter in enumerate(alphabet)}
number_letter = {i: letter for i, letter in enumerate(alphabet)}
m = 31

def gcd(x: int, y: int) -> int:
    "Greatest Common Divisor"
    return y if (x % y) == 0 else gcd(y, x % y)

def euclid_extended(a: int, b: int) -> Tuple[int, int, int]:
    "Extended Euclidean Algorithm"
    if a == 0:
        return b, 0, 1
    gcd, x, y = euclid_extended(b % a, a)
 
    x1 = y - math.floor(b / a) * x
    y1 = x
    return gcd, x1, y1

def filter_text(text: str) -> str:
    "Filter out unnecessary characters from text"
    text = text.replace('ё', 'е')
    text = text.replace('ъ', 'ь')
    for letter in text:
        if letter not in alphabet:
            text = text.replace(letter, '')
    
    text = text.strip()
    text = ' '.join(text.split())
    text = text.replace(' ', '')

    return text

def bigram_counter(line: str):
    "Count bigrams"
    bigrams = {}
    bigram_counter = 0
    letter_counter = 0

    line = filter_text(line.lower())

    for symbol in line:
        isOdd = letter_counter % 2 == 1
        if letter_counter != 0 and isOdd:
            bigram = prev_char + symbol
            bigrams[bigram] = bigrams.get(bigram, 0) + 1
            prev_char = symbol
            bigram_counter += 1
        else:
            prev_char = symbol
        letter_counter += 1

    tupleList = sorted(bigrams.items(), key=lambda i: i[1], reverse=True)
    for bi, n in tupleList:
        print("{}\t{}".format(bi, n))
        
    # Return list of bigrams sorted by descending frequency
    return [ item[0] for item in tupleList]

def split_to_bigrams(text: str) -> List[str]:
    "Split text to bigrams and returns list of bigrams"
    text = filter_text(text.lower())
    return [ text[i] + text[i+1] for i in range(0, len(text), 2) ]


def get_reverse_number(a: int, b: int) -> int:
    "Find a^-1 for a * a^-1 = 1 mod(m)"
    gcd, x, y = euclid_extended(a,b)
    return 0 if not gcd == 1 else x


def solve_eq(a: int, b: int, n: int) -> List[int]:
    "Solve equation ax=b mod(n)"
    X = []
    d = gcd(a, n)

    if d == 1:
        X.append((get_reverse_number(a, n) * b) % n)
    else:
        if (b % d) == 0:
            res = (get_reverse_number(int(a / d) * int(b / d) , int(n / d))) % int(n / d)
            for i in range(d):
                X.append(res + i * int(n / d))
        else:
            X.append(-1)
    return X

def decode_bigramm(w: str, a: int, b: int) -> str:
    """
    :w: bigramm
    :a: number
    :b: 
    :return: encoded bigramm
    """
    i1=letter_number[w[0]]
    i2=letter_number[w[1]]
    N = i1 * m + i2
    x = (get_reverse_number(a, m**2) * (N-b)) % (m**2)
    x1 = x % m
    x2 = int((x-x1) / m)
    
    res = str(alphabet[(x2) % m]) + str(alphabet[x1])
    return res

def decode_list(text: str, a: int, b: int) -> str:
    lb = split_to_bigrams(text)
    lb_decoded=[]
    for x in range(0,len(lb)):
        t=decode_bigramm(lb[x], a, b)
        lb_decoded.append(t)
    return ''.join(lb_decoded)

def get_coprime_numbers(n: int) -> List[int]:
    "Find numbers that has no divisors to 'n' except 1"
    result = []
    for i in range(1, n):
        if gcd(n, i) == 1:
            result.append(i)
    return result

def check_wrong_bigram_in_text(text: str):
    "Check if inacceptable bigram is in text and "
    for wrong_bg in inacceptable_bigrams:
        if wrong_bg in text:
            return wrong_bg
    else:
        return 0

def find_key(X1: int, X2: int, Y1: int, Y2: int) -> List[Tuple[int, int]]:
    a_list: List[int] = solve_eq((X1 - X2), (Y1 - Y2), m**2)

    keys = []
    for a in a_list:
        if a != -1:
            k = (a, ((Y1 - a * X1) % (m ** 2)))
            keys.append(k)

    return keys

def get_letter_pairs(sorted_bigrams: List[str], i: int, j: int):
    sbg1 = sorted_bigrams[i]
    pbg1 = freq[i]
    sbg2 = sorted_bigrams[j]
    pbg2 = freq[j]

    Y1 = letter_number[sbg1[0]] * m + letter_number[sbg1[1]]
    Y2 = letter_number[sbg2[0]] * m + letter_number[sbg2[1]]
    X1 = letter_number[pbg1[0]] * m + letter_number[pbg1[1]]
    X2 = letter_number[pbg2[0]] * m + letter_number[pbg2[1]]

    return Y1, Y2, X1, X2

def apply_key():
    pass

def break_ciphertext(ciphertext: str, print_rejected: bool=True) -> None:
    "Find key for the ciphertext"
    ciphertext = filter_text(ciphertext.lower())
    coprimes = get_coprime_numbers(m ** 2)
    sorted_bigrams = bigram_counter(ciphertext)[:15]
    format_key_string = "Key: ({}, {})"
    format_wrong_text_string = "Text \"{}\" is wrong because it contains wrog bigramm: \"{}\""

    for i in range(0, len(sorted_bigrams) - 1):
        for j in range(0, len(sorted_bigrams) - 1):
            if i == j:
                continue

            Y1, Y2, X1, X2 = get_letter_pairs(sorted_bigrams, i, j)
            keys = find_key(X1, X2, Y1, Y2)
            
            if len(keys) == 0:
                continue

            for key in keys:
                if key[0] not in coprimes:
                    continue

                decoded_text = decode_list(text, key[0], key[1])
                wrong_bg = check_wrong_bigram_in_text(decoded_text)
                if wrong_bg == 0:
                    print(decoded_text)
                    print(format_key_string.format(str(key[0]), str(key[1])))
                elif print_rejected:
                    print(format_wrong_text_string.format(decoded_text[:39], wrong_bg))
                    print(format_key_string.format(str(key[0]), str(key[1])))
                        

if __name__ == '__main__':
    text = cs.open(ciphertext_filename, "r", encoding='utf-8').read()
    print_debug = input('Print rejected text? (y/n): ')
    break_ciphertext(text, True if print_debug.lower() == 'y' else False)
