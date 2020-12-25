#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# башняяростичерныемаки

from operator import itemgetter


raw = []

possible_keys = ['','','','','']

class Result_Data:
    result_strings = []


f = open("./16.txt",  encoding="utf8")
data = f.read()[0:]
text1 = ""
dictionary1 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
common = "оаеин"
for y in data:
    y = y.lower()
    for x in dictionary1:
        if y=="ё":
            y="e"
        if y==x:
            text1+=y
        else:
            continue

thislist=list()
for i in range (0, len(dictionary1)):
    thislist.append(dictionary1[i])


def findcharnumb(ch):
    for i in range(0, len(thislist)):
        if ch==thislist[i]:
            return i

def findchar(nm):
    for i in range(0, len(thislist)):
        if nm==i:
            return thislist[i]


def mono_quantity(t):
    letter = dict()
    for i in t:
        if i == u'\n':
            continue
        if i in letter:
            letter[i] = letter.get(i) + 1
        else:
            letter[i] = 1
    return letter


def mono_freq(t):
    letter = dict()
    for i in t:
        if i == u'\n':
            continue
        if i in letter:
            letter[i] = float(round(letter.get(i) + 1.0/len(t), 7))
        else:
            letter[i] = float(round(1.0/len(t), 7))
    return letter


def index(t):
    sum_ = 0
    for i in t.values():
        sum_ += i * (i - 1)
    return sum_/(len(text1)*(len(text1)-1))


def small_index(t, t_):
    sum_ = 0
    for i in t.values():
        sum_ += i * (i - 1)
    return sum_/(len(t_)*(len(t_)-1))


def check(encrypted_text, key_length):
    return_text = ''
    rt = ''
    rl = []
    for i in range(0, key_length):
        for j in range(i, len(encrypted_text), key_length):
            return_text += encrypted_text[j]
            rt += return_text
        rl.append(return_text)
        return_text = ''
    print("\n", key_length, small_index(mono_quantity(encrypted_text), encrypted_text), "\n for each:")
    for i in range(0, len(rl)):
        print("\t", small_index(mono_quantity(rl[i]), rl[i]))
    print("Show freq? (да or skip)")
    if input() == "да":
        for i in range(0, len(rl)):
            j = 0
            print(f"\n element: {i}")
            for key, value in sorted(mono_freq(rl[i]).items(), key=itemgetter(1), reverse=True):
                if j == 0:
                    raw.append(key)
                if j % 8 == 0:
                    print("\"%s\": %s" % (key, round(value, 7)), end="\n")
                else:
                    print("\"%s\": %s" % (key, round(value, 7)), end="\t")
                j += 1
        print("")
    return encrypted_text[0:64]


# s3-буква, темп-закодована
def decode_one_letter(s3, temp3_):
    temp2 = findchar((findcharnumb(temp3_) - findcharnumb(s3) % 32))  # len 32
    if temp2 == None:
        temp__ = findcharnumb(temp3_)
        temp1__ = findcharnumb(s3)
        temp2 = findchar((32 + temp__ - temp1__) % 32)  # len 32
    return temp2


def decode_many_letters(temp_, s2, i):
    temp2 = findchar((findcharnumb(temp_[i]) - findcharnumb(s2[i % len(s2)])) % 32)  # len 32
    if temp2 is None:
        temp__ = findcharnumb(temp_[i])
        temp1__ = findcharnumb(s2[i % len(s2)])
        temp2 += findchar((32 + temp__ - temp1__) % 32)  # len 32
    return temp2


def decode(temp_, possible_keys):
    while True:
        raw_str = ''
        for i in raw:
            raw_str += i
        print(f"raw:\n\t0: {raw_str}")
        for i in range(0, 5):
            for ii in raw_str:
                possible_keys[i] += decode_one_letter(common[i], ii)
        for mi in range(0,len(possible_keys)):
            print(f"\t{mi}\t\"{common[mi]}\"", possible_keys[mi])
            possible_keys[mi] = ""
        print("letters? (0 for break)")
        s2 = input()
        if s2 == "0":
            break
        temp2_ = ""
        for i in range(0, len(temp_)):
            temp2_ += decode_many_letters(temp_, s2, i)
        print(temp2_)


var1 = ''
var2 = ''
while True:
    print("проверим длинну:", end='\t')
    c = int(input())
    print(possible_keys)
    print(c, "continue? (да, пропустить или конец)")
    x = input()
    if x == "да":
        raw = []
        var1 = c
        var2 = check(text1, c)
        print(f"key length: {var1}\n::decoding::\n")
        decode(var2, possible_keys)
        continue
    elif x == "конец":
        break



