# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from functions import *

class Alphabet:
    chars = "[]|/\"()`':;.,?!@%&*\\«»-–…~\n1234567890abcdefghijklmnopqrstuvwxyz "
    alphabet = "абвгдежзийклмнопрстуфхцчшщьыэюя"
    impossiblebigram = ['аь','оь','иь','уь','оь','щй','щф','щх','щц','щч','щш','щщ', 'гщ']
    fileAlph = ''
    textAlph = ''
    amountsortedAlph = ''
    entropyAlph = 0
    bigramsAlph = list()
    amountAlph = dict()

    def __init__(self):
        self.textAlph = Readfile(self.chars, "Text.txt")
        self.bigramsAlph = makebigrams(self.textAlph)
        self.amountsortedAlph = frequency(self.bigramsAlph)
        BigramNumber(self.amountsortedAlph, self.alphabet)
        self.entropyAlph = Entropy(self.textAlph, self.alphabet)

class TestAffine(Alphabet):
    text = ''
    file = ''
    bigrams = ''
    amountsorted = ''
    amount = ''
    decryptedtext = ''
    keys = list(list())
    correctkey = (1,0)

    def __init__(self):
        super().__init__()
        self.text = Readfile(self.chars,"24.txt")
        self.bigrams = makebigrams(self.text)
        self.amountsorted = frequency(self.bigrams)
        BigramNumber(self.amountsorted, self.alphabet)
        self.amount = NonSortedBigramNumber(self.bigrams, self.alphabet)

test = TestAffine()
test.keys = FindKeys(test.amountsorted, test.amountsortedAlph, len(test.alphabet))
file = open("keys.txt", 'w')
for ak in test.keys:
    text = Decrypt(ak,test.amount, test.bigrams, test.alphabet)
    if CheckKey(ak,test.alphabet, text, test.impossiblebigram, test.entropyAlph, file):
        test.correctkey = ak
        file = open("decrypttext.txt", 'w')
        file.write(text)
        break
print(Decrypt(test.correctkey, test.amount,test.bigrams, test.alphabet))