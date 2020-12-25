import re
import math
import math
import collections
from itertools import cycle

def clear_text1(file): # без пробіла
    with open(file, 'rb') as file:
        binary = file.read()
    text = binary.decode('utf-8')
    text = text.replace('ъ', 'ь')
    text = text.replace('ё', 'е')
    text = re.sub(r'[^а-яА-Я]', '', text)
    text = text.lower()
    a = open('clear_text1.txt', 'w')
    a.write(text)
    a.close()
    return text


def clear_text2(file): #з пробілом
    with open(file, 'rb') as file:
        binary = file.read()
    text = binary.decode('utf-8')
    text = text.replace('ъ', 'ь')
    text = text.replace('ё', 'е')
    text = re.sub(r'[^ а-яА-Я]', '', text)
    text = text.lower()
    while text.find('  ') != -1:
        text = text.replace('  ', ' ')

    a = open('clear_text2.txt', 'w')
    a.write(text)
    a.close()
    return text

alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя'
# alphabet2 = ' абвгдежзийклмнопрстуфхцчшщыьэюя'

def create_dict():
    d = {}
    num = 0
    for i in alphabet:
        d.update({i: num})
        num += 1
    return d

def key_gen(text, key):
    n = len(text) // len(key)
    k = len(text) % len(key)
    new_key = key * n + key[:k]
    return new_key

def to_ascii(text):
    list_code = []
    d = create_dict()
    for i in text:
        for value in d:
            if i == value:
                list_code.append(d[value])
    return list_code


def to_text(asci):
    list_code = []
    d = create_dict()
    for i in asci:
        for value in d:
            if i == d[value]:
                list_code.append(value)
    return list_code

def encrupt(text, key):
    text = to_ascii(text)
    key = to_ascii(key)
    res = []
    for t, k in zip(text, key):
        let = (t + k) % 32
        res.append(let)
    return res

def decrypt(key, text):
    res = []
    text = to_ascii(text)
    key = to_ascii(key)
    for t, k in zip(text, key):
        let = (t - k + 32) % 32
        res.append(let)

    return to_text(res)

def by_value(item):
    return item[1]

def index_vidpov(text):
    count = dict()
    ind = []
    kilk = len(text)
    for i in alphabet:
        count.update({i: 0})

    for i in text:
        count[i] += 1

    for i in count:
        a = (count[i] * (count[i] - 1)) / (kilk * (kilk - 1))
        ind.append(a)

    index = sum(ind)
    return index

def last5(dict):
    list_d = list(dict.items())
    list_d.sort(key=lambda i: i[1], reverse=True)
    list_d = list_d[0:5]
    return list_d

def frec(text):
    count = dict()
    ind = []
    kilk = len(text)
    for i in alphabet:
        count.update({i: 0})

    for i in text:
        count[i] += 1
    for i in count:
        a = count[i]/len(text)
    res = last5(count)
    return res



def cesar(text):
    for i in text:
        num = to_ascii(i)
        num = num + 1

def decrypt1(text, key):
    c = 0
    res = ''
    for i in text:
        a = chr((ord(i) - ord(key[c%15])) % 32 + 1072)
        res += a
        c += 1

    return res

def max_dict(dict):
    return max(dict.keys(), key=(lambda k: dict[k]))

def find_key(list):
    n = 0
    al = 'оеаик'
    for i in al:
        c = 0
        keys = []
        for i in maxi:
            list = text[c::15]
            c += 1
            key = chr((ord(i) - ord(al[n])) % 32 + 1072)
            keys.append(key)
        print(al[n], ' : ', keys)
        n += 1



if __name__ == '__main__':
    text = list(clear_text2('text.txt'))
    key = list('терморегуляционныйло')
    new_key = key_gen(text, key)
    cript = encrupt(text, new_key)
    cript = to_text(cript)
    crip = ''
    for i in cript:
        crip += i
    print(crip)
    t = decrypt(new_key, cript)
    res = ''
    for i in t:
        res += i
    # print(res)
    print('Індекс відповідності для тексту шифрованого ключем: ', key, ' = ', index_vidpov(cript))


    text = clear_text1('var.txt')
    index = index_vidpov(text)
    print('Індекс відповідності зашифрованого тексту: ', index)
    for i in range(2, 32):
        zriz = text[::i]
        # print(zriz)
        ind = index_vidpov(zriz)
        print('Індекс відповідності для ', i, ' : ', '\t', ind, '\t')

    list = []
    for i in range(15):
        a = text[i::15]
        list.append(a)
    # print(list) #текст розбитий на блоки
    maxi = []
    for i in list:
        count = dict()
        ind = []
        kilk = len(i)
        for j in alphabet:
            count.update({j: 0})

        for k in i:
            count[k] += 1
        # print(count)
        maxim = str(max_dict(count))
        maxi.append(maxim)
    print('Максимуми ', maxi) #максимуми з кожного блоку

    find_key(list)
    key = 'человеквфутляре'
    decr = decrypt1(text, key)
    a = open('decrypt_var.txt', 'w')
    a.write(decr)
    a.close()








