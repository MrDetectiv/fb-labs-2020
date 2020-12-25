import re
from itertools import product
import numpy as np

alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя'

d1 = {alphabet[i]: i for i in range(0, len(alphabet))}
d2 = {i: alphabet[i] for i in range(0, len(alphabet))}


def exclude_letters(text):
    """ исключение из текста символов не из алфавита """
    return ''.join([letter for letter in text if letter in alphabet])


def encrypt(text, a, b):
    text = text.lower()
    text = re.sub('ё', 'е', text)
    text = exclude_letters(text)
    m = np.power(len(alphabet), 2)
    bi_lst = [text[i:i + 2] for i in range(0, len(text), 2)]
    bi_n_lst = np.array([define_N(item) for item in bi_lst], dtype='int32')
    return ''.join([bigrams_dict[item] for item in (a * bi_n_lst + b) % m])


def define_N(bigram):
    try:
        return alphabet.index(bigram[0]) * len(alphabet) + alphabet.index(bigram[1])
    except:
        print('Error on ', bigram)


def make_bigrams_dict():
    return {define_N(item): ''.join(item) for item in product(alphabet, repeat=2)}


bigrams_dict = make_bigrams_dict()
