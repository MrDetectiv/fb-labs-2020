from random import randint
import os
from ChangeSymbols import ChangeSymbols
from Crypto import LettersAmount

log = "" #Строка, куда записывается все происходящее в программе и занесется в файл

def file_update(path):
    if os.path.exists(path):
        os.remove(path)

def alpa(alpha): #Создает словарь где ключ - буква алфавита, значение - порядковый номер буквы
    alp = {}
    ind = 0
    for l in alpha:
        alp[l] = ind
        ind += 1

    return alp

def keys(n, alpha): #Создает рандомный ключ заданной длины
    i = 0
    key = ""
    while i < n:
        key += alpha[randint(0,31)]
        i += 1
    return key


def viginer_encrypt(p_text, key, alpha): #Зашифровка текста шифром Виженера
    print("key:  ", key)
    alp = alpa(alpha)

    c_text = ""
    i = 0
    while i < len(p_text):
        id = (alp[p_text[i]] + alp[key[i%len(key)]]) % len(alpha)
        c_text += alpha[id]
        i += 1

    return c_text

def viginer_decrypt(c_text, key, alpha): #Расшифровка текста с шифром Вижинера
    print("key: ", key)
    alp = alpa(alpha)

    p_text = ""
    i = 0
    while i < len(c_text):
        id = (alp[c_text[i]] - alp[key[i%len(key)]]) % len(alpha)
        p_text += alpha[id]
        i += 1

    return p_text

def index(text, alpha): #Считает индекс соответствия
    id = 0

    for l in alpha:
        sum = 0
        for w in text:
            if w == l:
                sum += 1

        id = id + sum*(sum-1)

    if len(text) > 1:
        id = id/(len(text)*(len(text)-1))

    return id

def grouper(txt, n): #Разбивает текст на блоки заданной длины
    x = []
    i = 0

    while i < n:
        x.append("")
        i += 1

    for id in range(0, len(txt)):
        x[id%n] += txt[id]

    return x

# def croneker(txt, r):
#     id = 0
#     Crock = 0
#     while id < len(txt)-r:
#         if txt[id] == txt[id+r]:
#             Crock += 1
#         id += r
#
#     return Crock

def key_analysis(letter, alpha, popular): #Находит потенциальную букву ключа, путем манипуляций с самой популярной буквой алфавита и наиболее встречаемой буквой в блоке зашифрованого текста
    id = (alpha.index(letter) - alpha.index(popular)) % len(alpha)
    return alpha[id]


def viginer_analise(c_text, alpha, popular, log, begin=2, end=None):
    if end is None:
        end = len(alpha) + 1

    log = log + "Index of cipher text: " + str(index(c_text, alpha)) + "\n"

    strk1 = ""
    r = []

    for i in range(begin, end):
        ind = []
        blocks = grouper(c_text, i) #разбиваем текст на блоки
        for bl in blocks:
            ind.append(index(bl, alpha)) #индекс соответствия для блока
        r.append(sum(ind)/len(ind)) #среднее значение индекса соответствия для блоков заданной длины
        strk1 = strk1 + "index forlength blocks " + str(i) + ";" + str(sum(ind)/len(ind)) + "\n"

    log = log + strk1

    potential = {}
    for ri in r:
        if ri > 0.05:
            potential[ri] = r.index(ri) + begin #потенциальная длина ключа

    log = log + "Potential length of key\n" + str(potential) + "\n"

    period = True
    for ri in potential:
        if potential[ri] % list(potential.values())[0] != 0:
            period = False

    if period:
        period_key = list(potential.values())[0]
        print("length of key: ", period_key)
        log = log + "length of key: " + str(period_key) + "\n"
    else:
        print("Program cann't find regularity. You need analyse it by yourself")
        print(potential)
        period_key = input("Input length of key: ")
        log = log + "custom length of key: " + str(period_key) + "\n"

    blocks = grouper(c_text, period_key)
    list_keys = []
    for i in range(0,len(popular)):
        list_keys.append("")

    for bl in blocks:
        l = list(dict(LettersAmount(bl, alpha)).keys())[0]
        for i in range(0, len(list_keys)):
            list_keys[i] += key_analysis(l, alpha, popular[i]) #Список потенциальных ключей

    log = log + "List of potential keys\n" + str(list_keys) + "\n\n\nDecrypted first block\n"
    for el in list_keys:
        #print(viginer_decrypt(c_text[0:16], el, alpha))
        log = log + "key:  " + el + "\n      " + viginer_decrypt(c_text[0:period_key], el, alpha) + "\n" #Расшифровка первых n символов текста, где n - длина ключа

    path = os.getcwd()+r'\decrypt.txt' #Путь к расшифрованому тексту
    #hack_key = list_keys[0]
    hack_key = "делолисоборотней" #Ключ!!!!
    with open(path, 'w') as d:
        d.write(viginer_decrypt(c_text, hack_key, alpha)) #Расшифровка текста прямо в файл

    log = log + "\n\nWe hack Vigenere cipher\nKey: " + hack_key + "\n"
    with open(log_path, 'w') as logi:
        logi.write(log) #Запись логов в файл


if __name__ == '__main__':
    print("start proga")
    alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    popular = "оеаин"
    key_len = (2,3,4,5,randint(10,20)) #Множество состоящие из цифр, которые мы будем использовать в качестве длины ключа

    path = os.getcwd() +r'\plain.txt' #Путь к открытому тексту
    res_path = os.getcwd() + r'\result.txt' #Путь к зашифрованому тексту разными ключами
    cip_path = os.getcwd() + r'\cipher.txt' #Путь к зашифрованому тексту из варианта
    log_path = os.getcwd() + r'\log.txt' #Путь к лошам программы
    file_update(res_path) #Очистить файл для зашифрованого текста разными ключами
    file_update(log_path) #Очистить файл с логами

    print("Modifying file")
    log = log + "modifying file\n"
    mod_path = ChangeSymbols(path, False)
    with open(mod_path, 'r') as f:
        text = f.read()
        f.seek(0)
    log = log + "\n\n\nindex for plain text: " + str(index(text, alpha)) + '\n'

    print("encryption")
    log = log + "Encryption\n"
    for k in key_len:
        key = keys(k, alpha) #получаем ключ
        result = viginer_encrypt(text, key, alpha) #получаем зашифрованый текст
        log = log + "index for cipher text wih key " + key + ": " + str(index(result, alpha)) + "\n"
        with open(res_path, 'a') as res: #записываем результат в файл
            res.write("key: "+key+"\n"*2)
            res.write(result+"\n"*2)

    print("Decryption")
    log = log + "\n\n\n\nDecryption\n"
    cip_mod = ChangeSymbols(cip_path, False)
    with open(cip_mod, 'r') as f:
        cipher = f.read()
        f.seek(0)
    viginer_analise(cipher, alpha, popular, log) #Взламываем шифр

    print('the end')
