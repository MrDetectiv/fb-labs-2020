from collections import Counter
from itertools import product
import numpy as  np
from l_algerba import solve, bezout_recursive

alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя'


def exclude_letters(text):
    """ исключение из текста символов не из алфавита """
    return ''.join([letter for letter in text if letter in alphabet])


def find_ab(bigrams):
    """ поиск ключа по набору биграм. Возвращаются все возможные варианты ключа,
    т.к. линейное сравнение может иметь не единственное решение """
    try:
        rus_bigrams = bigrams[2:]
        bigrams = bigrams[:2]
    except:
        print(bigrams)
    X1 = define_N(rus_bigrams[0])
    X2 = define_N(rus_bigrams[1])
    Y1 = define_N(bigrams[0])
    Y2 = define_N(bigrams[1])
    m = len(alphabet)
    a = solve(np.abs(X1-X2), np.abs(Y1-Y2), np.power(m, 2))
    b = [np.mod(Y1 - a_i*X1, np.power(m, 2)) for a_i in a]
    return zip(a, b)


def decrypt(text, a, b):
    """ расшировка текста с известным ключом (a, b) """
    bi_lst = set([text[i:i + 2] for i in range(0, len(text), 2)])
    a_1 = bezout_recursive(a, np.power(len(alphabet), 2))[0]
    decrypt_dict = {item: bigrams_dict[(a_1 * (define_N(item) - b)) % np.power((len(alphabet)), 2)]
                    for item in bi_lst}
    bi_lst = [text[i:i + 2] for i in range(0, len(text), 2)]
    decrypt_list = [decrypt_dict[item] for item in bi_lst]
    return ''.join(decrypt_list)


def text_and_bigrams(file):
    """ получение текста и биграм из текстового файла файла """
    with open(file, 'r', encoding='utf-8') as f:
        text = ''.join([line for line in f])
    text = exclude_letters(text)
    return text, [text[i:i+2] for i in range(0, len(text), 2)]


def decrypt_slice(file):
    """ расшифровка текстового файла с получением среза начальных символов """
    text, bi_lst = text_and_bigrams(file)
    common_bi = product([item[0] for item in Counter(bi_lst).most_common(5)], repeat=2)
    common_rus = product(most_freq, repeat=2)
    for item in product(common_bi, common_rus):
        if (item[0][0] != item[0][1]) & (item[1][0] != item[1][1]):
            z = find_ab(list(item[0]) + list(item[1]))
            for subitem in z:
                decrypted = decrypt(text, subitem[0], subitem[1])
                most_freq_dec = [item[0] for item in Counter([decrypted[i:i+2] for i in range(0, len(decrypted), 2)]).most_common(10)]
                score = 0
                for b_gram in most_freq_dec:
                    if b_gram in most_freq:
                        score += 1
                if score > 3:
                    print(decrypted[:41], ' ', subitem[0], subitem[1])


def decrypt_file(file, a, b):
    """ дешифровка полного текстового файла с записью ре"""
    with open(file, 'r', encoding='utf-8') as f:
        text = ''.join([line for line in f])
    text = exclude_letters(text)
    res = decrypt(text, a, b)
    with open('decrypted.txt', 'w', encoding='utf-8') as f:
        for item in res:
            f.write(item)


def define_N(bigram):
    """ получение номера биграмы """
    try:
        return alphabet.index(bigram[0]) * len(alphabet) + alphabet.index(bigram[1])
    except:
        print('Error on ', bigram)


def make_bigrams_dict():
    """ формирование словаря биграм для быстрого сопоставления """
    return {define_N(item): ''.join(item) for item in product(alphabet, repeat=2)}


def def_most_freq(file):
    """ определение наиболее часто встречающихся биграм из эталонного (длинного) текста """
    text, bigrams = text_and_bigrams(file)
    return [item[0] for item in Counter(bigrams).most_common(25)]


bigrams_dict = make_bigrams_dict()
most_freq = def_most_freq('text.txt')

