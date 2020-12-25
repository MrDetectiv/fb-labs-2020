import re
import math

def gcd(a, b): #НСД
    while a != 0:
        a, b = b % a, a
    return b

def euclid(a, b): #роширений алгоритм евкліда
    if (b == 0):
        return a, 1, 0
    d, x, y = euclid(b, a % b)
    return d, y, x - (a // b) * y

def ober(b, n):
    g, x, y = euclid(b, n)
    if g == 1:
        return x % n

def lin_riv(a,b,m): #ax = b mod m
                    # a = x* - x**
                    # b = y* - y**
    if gcd(a, m) == 1:
        return (ober(a,m) * b) % m
    if gcd(a, m) > 1 and b%gcd(a, m) == 0:
        a, b, n = a // gcd(a, m), b // gcd(a, m), m // gcd(a, m)
        x = lin_riv(a,b,n)

        res = []
        for i in range(x,m,n):
            res.append(i)
        return res

alphabet1 = 'абвгдежзийклмнопрстуфхцчшщьыэюя'

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

def fixed_num(n, prec=0):
    return f"{n:.{prec}f}"

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
    return frequency

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

def last5(dict):
    list_d = list(dict.items())
    list_d.sort(key=lambda i: i[1], reverse=True)
    list_d = list_d[0:5]
    return list_d

def create_dict():
    d = dict()
    for i in alphabet1:
        for j in alphabet1:
            a = i + j
            val = (alphabet1.index(i) * len(alphabet1)) + alphabet1.index(j)
            d.update({a: val})
    return d

def find_a_b(list1, list2):
    diction = create_dict()
    len_alphabet = len(alphabet1)

    list_res = []
    for i in range(5):
        for j in range(5):
            x = diction[list1[i]] - diction[list1[j]]
            for k in range(5):
                y = diction[list2[i]] - diction[list2[k]]
                print(x, y)
                res_a = lin_riv(x, y, len_alphabet**2)
                if res_a == None:
                    print('для пари:', list2[i], list2[k], 'з шифрованого тексту і для пари ', list1[i],  list1[j], 'з реального тексту')
                    print("Коренів немає")
                    pass
                else:
                    print('для пари:', list2[i], list2[k], 'з шифрованого тексту і для пари ', list1[i],  list1[j], 'з реального тексту')
                    print('a = ', res_a)
                    if type(res_a) != int:
                        break
                    else:
                        res_b = (diction[list2[i]] - res_a * diction[list1[i]]) % len_alphabet ** 2
                        print('b = ', res_b)
                    a = []
                    a.append(res_a)
                    a.append(res_b)
                    list_res.append(a)
    return list_res

def check_text(text):
    norm_frec = ['о', 'а', 'е', 'и', 'н']
    res = 0
    dc = text
    while len(dc) > 1:
        big = dc[:2]
        dc = dc[1:]
        if big == 'аь':
            res += 1
    count1 = {}
    per = []
    for i in alphabet1:
        count1.update({i: 0})

    for i in text:
        count1[i] += 1
    list = last5(count1)
    real = []
    for i in range(len(list)):
        a = list[i][0]
        real.append(a)
    # print(real)
    for i in real:
        par = 0
        for j in norm_frec:
            if i == j:
                par += 1
        if par != 1:
            res += 1

    if res < 3:
        a = open('res.txt', 'w')
        a.write(text)
        a.close()
        print(text)
        return text

def decrypt(text, a_b):
    for i in range(len(a_b)):
        t = text
        decrypt_text = ''
        a = a_b[i][0]
        b = a_b[i][1]
        print(a, b)
        while len(t) > 1:
            # t = text
            big = t[:2]
            t = t[2:]
            y = dict[big]
            obern = ober(a, 961)
            if obern == None:
                print("cant create obernene")
                break
            else:
                x = (obern * (y - b)) % 961
                # print(x)
                for key in dict.keys():
                    if dict[key] == x:
                        decrypt_text += key
        check_text(decrypt_text)
if __name__ == '__main__':
    # a = bigram(alphabet1, clear_text1('var.txt'), per=2) #біграма без пробілів, біграми не перетинаються
    # print(last5(a))
    # перші 5 найчастіші біграми шифрованого тексту
    #('ве', '0.02720'),
    # ('да', '0.01620'),
    # ('эб', '0.01244'),
    # ('ге', '0.01157'),
    # ('ме', '0.01157'),
    # print(create_dict())
                                            #(ст, но, то, на, ен) найчастіші біграми в реальній мові
    list1 = ['то', 'ст', 'но',  'на', 'ен'] #відкритий текст     X*
    list2 = ['ве', 'да', 'эб', 'ге', 'ме']  #шифр текст          Y* ою чм

    a_b = find_a_b(list1, list2)
    dict = create_dict()
    print(a_b)
    decrypt(clear_text1('var.txt'), a_b)