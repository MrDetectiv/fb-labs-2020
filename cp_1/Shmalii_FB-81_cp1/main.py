# -*- coding: utf-8 -*-
import numpy as np
from tkinter import *

root = Tk()
root.title("Визначення ентропій та надлишковостей")
root.geometry("600x500+500+250")
lbl = Label(root, text="Ентропія: ", font=30)
lbl.place(x=80, y=50)
lbl1 = Label(root, text="Надлишковість: ", font=30)
lbl1.place(x=80, y=100)
label2 = Label(text=" ", font=30)
label2.place(x=200, y=10)
label3 = Label(text=" ", font=30)
label3.place(x= 180,y=50 )
label4 = Label(text=" ", font=30)
label4.place(x= 225,y=100 )


class Alphabet:
    chars = "[]|/\"()`':;.,?!@%&*\\«»-–…~\n1234567890abcdefghijklmnopqrstuvwxyz"
    alphabet = "абвгдежзийклмнопрстуфхцчшщыьэюя "
    amount = dict()
    prob = dict()
    entropy = 0
    length = 0
    ngram = 1
    redundancy = 0
    label_text=""

    def __init__(self):
        self.file = open("Text.txt", 'r', encoding='utf-8')
        self.text = self.file.read().lower()
        for ch in self.chars:
            self.text = self.text.replace(ch, '')
        self.text = self.text.replace('ё', 'е').replace('ъ', 'ь')

    def Entropy (self):
        array = []
        for elem in self.prob:
            if self.prob[elem] != 0:
                array.insert(len(array), self.prob[elem])
        array = np.array(array)
        self.entropy = (-1/self.ngram) * np.sum(array*np.log2(array))
        self.redundancy = 1 - self.entropy/np.log2(32)

    def Probaility(self, length):
        for elem in self.amount:
            self.prob[elem] = self.amount[elem]/length

    def probability(self):
        pass

    def Start(self):
        self.amount.clear()
        self.prob.clear()
        self.probability()
        self.Probaility(self.length)
        self.Entropy()
        labeltext= "H"+str(self.ngram)+" - "+self.label_text
        label2.config(text=labeltext)
        label3.config(text= self.entropy)
        label4.config(text=self.redundancy)
        prob1 = sorted(self.prob.items(), key=lambda x: x[1], reverse=True)
        for elem in prob1:
            print(elem[0], "\t", elem[1])


class Mono(Alphabet):
    def __init__(self):
        super().__init__()
        self.text = self.text.replace(" ", "")
        self.length = len(self.text)
        self.label_text= "monograms without spaces"

    def probability(self):
        for elem in Alphabet.alphabet.replace(" ", ""):
            self.amount[elem] = self.text.count(elem)


class MonoSpace(Alphabet):
    def __init__(self):
        super().__init__()
        self.length = len(self.text)
        self.label_text = "monograms with spaces"

    def probability(self):
        for elem in Alphabet.alphabet:
            self.amount[elem] = self.text.count(elem)


class Bigram(Alphabet):
    def __init__(self):
        super().__init__()
        self.ngram=2
        self.text = self.text.replace(" ", "")
        self.bigrams = list()
        self.label_text = "bigrams without spaces"
        for i in range(0, len(self.text), 2):
            self.bigrams.append(self.text[i:i+2])
        self.length = len(self.bigrams)

    def probability(self):
        for elem in self.bigrams:
            if elem in self.amount:
                self.amount[elem] = self.amount[elem]+1
            else:
                self.amount[elem] = 1


class BigramSpace(Alphabet):
    def __init__(self):
        super().__init__()
        self.ngram = 2
        self.bigrams = list()
        self.label_text = "bigrams with spaces"
        for i in range(0, len(self.text), 2):
            self.bigrams.append(self.text[i:i+2])
        self.length = len(self.bigrams)

    def probability(self):
        for elem in self.bigrams:
            if elem in self.amount:
                self.amount[elem] = self.amount[elem]+1
            else:
                self.amount[elem] = 1


class BigramCross(Alphabet):
    def __init__(self):
        super().__init__()
        self.ngram = 2
        self.text = self.text.replace(" ", "")
        self.bigrams = list()
        self.label_text = "crossed bigrams without spaces"
        for i in range(0, len(self.text), 1):
            self.bigrams.append(self.text[i:i + 2])
        self.length = len(self.bigrams)

    def probability(self):
        for elem in self.bigrams:
            if elem in self.amount:
                self.amount[elem] = self.amount[elem]+1
            else:
                self.amount[elem] = 1


class BigramCrossSpace(Alphabet):
    def __init__(self):
        super().__init__()
        self.ngram = 2
        self.bigrams = list()
        self.label_text = "crossed bigrams with spaces"
        for i in range(0, len(self.text), 1):
            self.bigrams.append(self.text[i:i+2])
        self.length = len(self.bigrams)

    def probability(self):
        for elem in self.bigrams:
            if elem in self.amount:
                self.amount[elem] = self.amount[elem]+1
            else:
                self.amount[elem] = 1


mono = Mono()
monoSpace = MonoSpace()
bigram = Bigram()
bigramSpace = BigramSpace()
bigramCross = BigramCross()
bigramCrossSpace = BigramCrossSpace()

monob = Button(text="Моно", command=mono.Start, activebackground='#FF0000')
monob.place(x= 200, y = 200)
monoSb = Button(text="Моно з пробілом", command=monoSpace.Start, activebackground='#FF0000')
bigr = Button(text="Біграми", command=bigram.Start, activebackground='#FF0000')
bigrSp = Button(text= "Біграми з пробілом", command=bigramSpace.Start, activebackground='#FF0000')
bigrCr = Button(text="Біграми з перетином", command=bigramCross.Start, activebackground='#FF0000')
bigrCrSp = Button(text="Біграми з перетином, та пробілом", command=bigramCrossSpace.Start, activebackground='#FF0000')
bigrCr.place(width=200, x=350, y= 400)
bigrCrSp.place(width=200, x=80, y=400)
bigrSp.place(width=200, x=80, y=350)
bigr.place(width=200, x=350, y=350)
monob.place(width=200, x=80, y=300)
monoSb.place(width=200, x=350, y=300)

root.mainloop()