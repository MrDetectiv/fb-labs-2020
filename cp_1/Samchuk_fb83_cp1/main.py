import re
import math

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

alphabet1 = 'абвгдежзийклмнопрстуфхцчшщыьэюя'
alphabet2 = ' абвгдежзийклмнопрстуфхцчшщыьэюя'

def sort_dict(dict):
    list_key = list(dict.items())
    list_key.sort(key=lambda i: i[1], reverse=True)
    for i in list_key:
        print(i[0], ':', '\t', round(i[1], 5))

def fixed_num(n, prec=0):
    return f"{n:.{prec}f}"

def monogam(alphabet, text):
    count = dict()

    for i in alphabet:
        count.update({i: 0})

    for i in text:
        count[i] += 1

    length = len(text)
    sum_entropy = []
    frequency = dict()
    for char, val in count.items():
        if val != 0:
            period = val / length
            entropy = -period * math.log2(period)
            sum_entropy.append(entropy)
            frequency.update({char: period})

    sum_entropy = sum(sum_entropy)

    print("Entropy:", sum_entropy)

    redundancy = 1 - sum_entropy / math.log2(len(alphabet))

    print("Rendundancy:", redundancy)

    sort_dict(frequency)

def bigram(alphabet, text, per):

    bigramm_dict = dict()

    for i in alphabet:
        for j in alphabet:
            key = i + j
            bigramm_dict.update({key: 0})

    count_big = 0

    while text:
        bigramm = text[:2]
        text = text[per:]
        if len(bigramm) < 2:
            break
        else:
            count_big += 1
            bigramm_dict[bigramm] += 1

    print(bigramm_dict)
    sum_entropy = []
    frequency = dict()

    for char, val in bigramm_dict.items():
        if val == 0:
            period = 0
        else:
            period = val / count_big
            entrophy = -period * math.log2(period) / 2
            sum_entropy.append(entrophy)

        frequency.update({char: period})

    for char, val in frequency.items():
        frequency.update({char: fixed_num(val, 5)})
    print(frequency)

    sum_entropy = float(sum(sum_entropy))
    print("Entropy: ", sum_entropy)
    redundancy = 1 - sum_entropy / math.log2(len(alphabet))
    print("Redundancy: ", redundancy)
    output(frequency, alphabet1)



def output(dict, alphabet):
    list = []
    # alphabet = ' ' + alphabet
    for i in alphabet:
        a = []
        a.append(i)
        for char, val in dict.items():
            if i == char[0]:
                a.append(val)
        list.append(a)
    alphabet = ' ' + alphabet
    for i in alphabet:
        print("%10s" % i, end="\t")
    print()
    for i in range(len(list)):
        for j in range(len(list[i])):
            print("%10s" % list[i][j], end="\t")
        print()

# =============================================
monogam(alphabet1, clear_text1('voynaa.txt')) #монограма без пробілів
# monogam(alphabet2, clear_text2('voynaa.txt')) # монограма з пробілами
# bigram(alphabet1, clear_text1('voynaa.txt'), per=1) #біграма без пробілів, біграми перетинаються
# bigram(alphabet1, clear_text1('voynaa.txt'), per=2) #біграма без пробілів, біграми не перетинаються
# bigram(alphabet2, clear_text2('voynaa.txt'), per=1) #біграма з пробілами, біграми перетинаються
# bigram(alphabet2, clear_text2('voynaa.txt'), per=2) #біграма з пробілами, біграми не перетинаються


