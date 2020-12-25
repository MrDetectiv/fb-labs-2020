import unittest
from viginer_lib import exclude_letters, crypt, decrypt, crypt_file, decrypt_file, algorithm1, shift_text, build_key
import numpy as np

key = 'абвгд'


class TestMethods(unittest.TestCase):
    """ тест кодирования/декодирования текста """
    def test1(self):
        with open('text1.txt', 'r', encoding='utf-8') as f:
            text = ''.join([exclude_letters(line) for line in f])
        self.assertEqual(text, decrypt(crypt(text, key), key))

    def test2(self):
        """ тест кодирования/декодирования файлов """
        crypt_file('text1.txt', 'crypted1.txt', key)
        decrypt_file('crypted1.txt', 'decrypted1.txt', key)
        with open('text1.txt', 'r', encoding='utf-8') as f:
            text1 = ''.join([exclude_letters(line.lower()) for line in f])
        with open('decrypted1.txt', 'r', encoding='utf-8') as f:
            text2 = ''.join([exclude_letters(line) for line in f])
        self.assertEqual(text1, text2)

    def test3(self):
        """ проверка разбиения на блоки и генерации ключа """
        Y_blocks = algorithm1('crypted.txt', 5)
        len_y = min(np.array([len(Y_blocks[item]) for item in Y_blocks]))
        crypted_freq = []
        for item in Y_blocks:
            Y_blocks[item] = Y_blocks[item][0:len_y]
            crypted_freq.append(shift_text(Y_blocks[item]))
        self.assertEqual(key, build_key([2, 3, 4, 0, 1], crypted_freq))