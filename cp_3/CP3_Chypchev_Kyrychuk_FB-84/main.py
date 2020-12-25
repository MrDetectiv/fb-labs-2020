import os
from collections import Counter,OrderedDict
import itertools
from math import gcd

cyrillic = 'абвгдежзийклмнопрстуфхцчшщьыэюя'

class Text:
    def __init__(self,path):
        self.path = path

    def getcleartext(self):
        with open(self.path,'r',encoding='utf-8') as cryptofile:
            text = cryptofile.read().lower().rstrip().replace('ъ','ь').replace('ё','е').replace('\n','')
            #удаляем переносы строк
        return text

class Bigramms:
    def __init__(self,text):
        self.text = text
        self.bigramms_amount = 0
        self.bigramms_intersect_amount = 0
        self.bigramms = {}
        self.bi_no_intersect = {}


    def break_into_bigramms(self):
        n = 2
        bigramms_list = []
        for i in range(0,len(self.text),n):
            bigramms_list.append(self.text[i:i+n])
        self.bigramms_amount = len(bigramms_list)
        self.bigramms = OrderedDict(dict(Counter(bigramms_list)))

    def bigramms_no_intersect(self):
        n = 2
        bigramms_list = []
        for i in range(0,len(self.text),n):
            bigramms_list.append(self.text[i:i+n])
        self.bi_no_intersect = bigramms_list

    def frequency(self,dictionary,bigramms_amount):
        freq = {}
        for char in dictionary.items():
            freq[char[0]] = char[1]/bigramms_amount
            # print(
            #     char[0],
            #     '{:.12f}'.format(freq[char[0]])
            # )
        return freq

class Reverse:
    def ensd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            nsd, x, y = self.ensd(b % a, a)
            return (nsd, y - (b//a) * x,x)

    def reverse(self, b, n):
        self.nsd, x, y = self.ensd(b, n)
        #print(g,x,y)
        if self.nsd == 1:
            return x % n

def find_keys(lang1,lang2,bgrm1,bgrm2,alpha,m):
    x1 = cyrillic.index(lang1[0]) * m + cyrillic.index(lang1[1])
    x2 = cyrillic.index(lang2[0]) * m + cyrillic.index(lang2[1])
    #популярные биграммы в шифротексте
    y1 = cyrillic.index(bgrm1[0]) * m + cyrillic.index(bgrm1[1])
    y2 = cyrillic.index(bgrm2[0]) * m + cyrillic.index(bgrm2[1])

    rev = Reverse()
    nsd = rev.ensd((x1 - x2)%m**2, m**2)
    solution = []
    if nsd[0] == 1:
        solution = rev.reverse((x1-x2)%m**2, m**2)
    elif nsd[0] > 1:
        a = (y1 - y2) % nsd[0]
        if a != 0:
            solution = None
        elif a == 0:
            a1 = (x1 - x2) // nsd[0]
            a2 = (y1 - y2) // nsd[0]
            a3 = (m ** 2) // nsd[0]
            a_reversed = rev.reverse(a1, a3)
            res = 0
            # число, которое мы добавляем инкрементом
            incremented = a3
            while incremented <= m ** 2:
                res = (a_reversed + incremented) % (m ** 2)
                solution.append(res)
                incremented += a3

        final_pairs = []

        # когда одно решение
        if type(solution) == int:
            a = ((y1 - y2) * (solution)) % m ** 2
            b = (y1 - x1 * a) % m ** 2
            final_pairs.append((a, b))
        else:
            if solution != None:
                for sol in solution:
                    a = (a2 * (sol)) % m ** 2
                    b = (y1 - x1 * a) % m ** 2
                    final_pairs.append((a, b))

        # print(final_pairs)
        return final_pairs


def correspondance_index(text):
    result = 0
    length = len(text)
    frequency = dict(Counter(text))
    for freq in frequency.values():
        result += freq * (freq - 1)
    return result / (length * (length - 1))

    # даём на вход биграмму, получаем число


def decrypt(a_reversed, b, bigramm, m, cyrillic):
    def num_to_bgrm(x):
        x1 = x // m
        x2 = x - x1 * m
        return x1, x2

    decrypted_bigramm = ''
    y = cyrillic.index(bigramm[0]) * m + cyrillic.index(bigramm[1])
    x = (a_reversed * (y - b)) % m ** 2
    x1, x2 = num_to_bgrm(x)
    decrypted_bigramm = cyrillic[x1] + cyrillic[x2]
    return decrypted_bigramm


filename = 'lab3_var11.txt'
abs_path = os.path.dirname(__file__)
full_path = os.path.join(abs_path, filename)

ready_text = Text(full_path).getcleartext()

bigramms = Bigramms(ready_text)
bigramms.break_into_bigramms()
bigramms.bigramms_no_intersect()
frequency = bigramms.frequency(bigramms.bigramms, bigramms.bigramms_amount)
lang_popular_bigrams = ['ст', 'но', 'то', 'на', 'ен']
mod = 31
top = sorted(frequency.items(), key=lambda x: -x[1])[:5]
cipher_popular_bigrams = [i[0] for i in top]

result = []
l_double_combos = [i for i in itertools.permutations(lang_popular_bigrams, 2)]
ci_double_combos = [i for i in itertools.permutations(cipher_popular_bigrams, 2)]
for la_pair in l_double_combos:
    for ci_pair in ci_double_combos:
        key_pair = find_keys(la_pair[0], la_pair[1], ci_pair[0], ci_pair[1], cyrillic, 31)
        for pair in key_pair:
            result.append(pair)

logfile = open(
    r'C:\Users\funro\Desktop\univer\kripta\cryptolabs\fb-labs-2020\cp_3\CP3_Chypchev_Kyrychuk_FB-84\laba.log', 'w+')

rev = Reverse()
for lst in list(set(result)):
    try:
        text = ''
        for bigram in bigramms.bi_no_intersect:
            a_reversed = rev.reverse(lst[0], mod ** 2)
            text += decrypt(a_reversed, lst[1], bigram, 31, cyrillic)
        index = correspondance_index(text)
        if index > 0.055:
            logfile.write(
                f'\nRight keys found: a={lst[0]}, b={lst[1]} - correspondance index is {index}\nDecrypted text:\n{text}\n')
        else:
            logfile.write(f'\nKeys a={lst[0]}, b={lst[1]} are dropped - correspondance index is too low: {index}')
    except:
        pass