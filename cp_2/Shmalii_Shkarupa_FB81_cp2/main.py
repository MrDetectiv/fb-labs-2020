# -*- coding: utf-8 -*-

import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
root = tk.Tk()
root.title("Vigener calculator")
root.geometry("900x800+325+0")
entertext = tk.Text(root)
entertext.place(width=420, height= 600,x=20, y= 10)
resulttext = tk.Text(root)
resulttext.place(width=420, height= 600,x=460, y= 10)


class Alphabet:
    chars = "[]|/\"()`':;.,?!@%&*\\«»-–…~\n1234567890abcdefghijklmnopqrstuvwxyz"
    alphabet_open_text = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    alphabet_close_text = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    filename = 'decrypt.txt'
    file = ''
    text = ''

    def ReadText(self):
        self.file = open(self.filename, 'r', encoding='utf-8')
        self.text = self.file.read().lower()
        for ch in self.chars:
            self.text = self.text.replace(ch, '')
        self.text = self.text.replace(" ", '')

    def ChoseFile(self):
        self.filename = tk.filedialog.askopenfilename(title = "Select file")
        if self.filename != '':
            self.ReadText()
        entertext.delete('1.0', tk.END)
        entertext.insert(1.0,self.text)
        print(self.text)


class Vigener(Alphabet):  # class for encrypt and decrypt text with known keys
    encrypttext = ''
    decrypttext = ''
    key = ''
    amount = dict()
    prob = dict()
    index = 0

    def __init__(self):
        super().__init__()

    def EnterKey(self):
        self.key = keytext.get("1.0","end").replace(chr(10), "")
        for ch in self.chars:
            self.key = self.key.replace(ch, '')
        self.key = self.key.replace(" ", '')

    def Encrypt(self):
        self.encrypttext = ''
        for i in range(len(self.text)):
                keysymb = self.alphabet_open_text.index(self.key[i % len(self.key)])
                temp = (self.alphabet_open_text.index(self.text[i])+keysymb) % len(self.alphabet_open_text)
                self.encrypttext = self.encrypttext+self.alphabet_open_text[temp]

    def Decrypt(self):
        self.decrypttext = ''
        for i in range(len(self.text)):
            keysymb = self.alphabet_open_text.index(self.key[i % len(self.key)])
            opensymbol = self.alphabet_open_text.index(self.text[i])+len(self.alphabet_open_text)
            temp = (opensymbol - keysymb) % len(self.alphabet_open_text)
            self.decrypttext = self.decrypttext + self.alphabet_open_text[temp]

    def probability(self, text1):
        for elem in self.alphabet_open_text:
            self.amount[elem] = text1.count(elem)
            self.prob[elem] = self.amount[elem] / len(text1)

    def Index(self, text1):
        self.probability(text1)
        array = []
        for elem in self.amount:
            array.insert(len(array), self.amount[elem])
        array = np.array(array)
        self.index = (1 / (len(text1)*(len(text1)-1))) * np.sum(array * (array-1))


class DecrVigener(Alphabet):
    r = 0
    Dr = dict()
    key = ''
    amount = dict()

    def __init__(self):
        super().__init__()
        self.decrypttext = ''

    def FindBlock(self):
        dr = dict()
        for i in range(2,31):
            amount = 0
            for a in range(len(self.text)-i):
                if self.text[a] == self.text[a+i]:
                    amount += 1
            dr[i] = amount
        self.Dr = sorted(dr.items(), key=lambda x: x[1], reverse=True)
        r = self.Dr[0][0]
        for elem in self.Dr:
            if r%elem[0] == 0:
                r = elem[0]
            elif elem[0]%r == 0:
                r = r
            else: break
        print(self.Dr)
        self.r = r

    def FindKey(self):
        for i in range(self.r):
            mostcomon = ''
            amountlet = 0
            temptext = self.text[i::self.r]
            for elem in self.alphabet_close_text:
                 if amountlet < temptext.count(elem):
                    amountlet = temptext.count(elem)
                    mostcomon = elem
            ind_mcommon = self.alphabet_close_text.index(mostcomon)
            length = len(self.alphabet_close_text)
            self.key += self.alphabet_close_text[(ind_mcommon-self.alphabet_close_text.index('о')) % length]

    def Decrypt(self):
        self.decrypttext = ''
        for i in range(len(self.text)):
            keysymb = self.alphabet_close_text.index(self.key[i % len(self.key)])
            opensymbol = self.alphabet_close_text.index(self.text[i]) + len(self.alphabet_close_text)
            temp = (opensymbol - keysymb) % len(self.alphabet_close_text)
            self.decrypttext = self.decrypttext + self.alphabet_close_text[temp]
        # for a in range(0,len(self.decrypttext),self.r):
        #     print(self.text[a:a+self.r],"----", self.key, "----",self.decrypttext[a:a+self.r])


def keyCorrection(obj):
    entropy = Entropy(obj.decrypttext, obj.alphabet_close_text )
    tempkey = obj.key
    for a in range(len(obj.key)):
        for i in range(len(obj.alphabet_close_text)):
            obj.key = obj.key[:a] + obj.alphabet_close_text[i] + obj.key[a+1:]
            obj.Decrypt()
            tempentr = Entropy(obj.decrypttext, obj.alphabet_close_text)
            if tempentr > 4.71:
                obj.key = tempkey
                break
            elif tempentr < entropy:
                entropy = tempentr
                tempkey = obj.key
            else:
                obj.key = tempkey
    print(obj.key)


def Entropy(text, alphabet):
    array  = []
    probability = dict()
    length = len(text)
    for a in alphabet:
        probability[a] = text.count(a)/length
    for elem in probability:
        if probability[elem] != 0:
            array.append(probability[elem])
    entropy =(-1) * np.sum(array*np.log2(array))
    return entropy


def PrintplotDr(Dr):
    x = list()
    y = list()
    for elem in Dr:
        x.append(elem[0])
        y.append(elem[1])
    fig, ax = plt.subplots()
    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(14)
    fig.set_figheight(6)
    ax.set_xlabel("key length")
    ax.set_ylabel("repetitions")
    ax.set_title("coincidence")
    ax.xaxis.set_ticks(np.arange(2,31 , 1))
    ax.bar(x,y)


def PlotOpentext(alphabet, obj):
    keys = ["ты","сон","хлеб","козак","солнце", "система", "криптоанализатор"]
    file = open("encrypt.txt", "r", encoding="utf-8")
    text = file.read().replace(chr(10), "")
    x = list()
    y = list()
    encrtext = ''
    obj.Index(text)
    x.append("ВТ")
    y.append(obj.index)
    for key in keys:
        array = []
        for i in range(len(text)):
            keysymb = alphabet.index(key[i % len(key)])
            temp = (alphabet.index(text[i])+keysymb) % len(alphabet)
            encrtext = encrtext+alphabet[temp]
        for elem in alphabet:
            array.insert(len(array), encrtext.count(elem))
        array = np.array(array)
        index = (1 / (len(encrtext) * (len(encrtext) - 1))) * np.sum(array * (array - 1))
        x.append("R={0}".format(len(key)))
        y.append(index)
        encrtext = ''
    for i in range(len(x)):
        print(x[i], "---", y[i])
    fig, ax = plt.subplots()
    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(14)
    fig.set_figheight(6)
    ax.set_title("Indexes opentext")
    ax.set_xlabel("key length")
    ax.set_ylabel("Index")
    ax.bar(x, y)


def PrintPlotInd(text, alphabet):
    indexes = list(list())
    index = 0
    x=list()
    y = list()
    for i in range(2,31):
        for a in range(i):
            array = []
            temptext = text[a::i]
            for elem in alphabet:
                array.insert(len(array), temptext.count(elem))
            array = np.array(array)
            index += (1 / (len(temptext) * (len(temptext) - 1))) * np.sum(array * (array - 1))
        indexes.append((i, index/i))
        x.append(i)
        y.append(index/i)
        index = 0
    print(indexes)
    fig, ax = plt.subplots()
    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(14)
    fig.set_figheight(6)
    ax.set_xlabel("key length")
    ax.set_ylabel("Index")
    ax.set_title("Indexes closetext")
    ax.xaxis.set_ticks(np.arange(2, 31, 1))
    ax.bar(x, y)


openVigener = Vigener()
cipherVigener = DecrVigener()
cipherVigener.ReadText()
cipherVigener.FindBlock()
cipherVigener.FindKey()
cipherVigener.Decrypt()
print(Entropy(cipherVigener.decrypttext, cipherVigener.alphabet_close_text))
keyCorrection(cipherVigener)


def Encrypt():
    openVigener.EnterKey()
    openVigener.text = entertext.get(1.0,"end").replace(chr(10), "").lower()
    if openVigener.text != '':
        openVigener.Encrypt()
        resulttext.delete('1.0', tk.END)
        resulttext.insert(1.0, openVigener.encrypttext)
        openVigener.Index(openVigener.encrypttext)
        print("key:", openVigener.key, "--key length:", len(openVigener.key), "--Index:", openVigener.index)


def Decrypt():
    openVigener.EnterKey()
    openVigener.text = entertext.get(1.0,"end").replace(chr(10), "").lower()
    openVigener.Decrypt()
    resulttext.delete('1.0', tk.END)
    resulttext.insert(1.0, openVigener.decrypttext)
    file = open("resulttext.txt", 'w', encoding='utf-8')
    file.write(openVigener.decrypttext)

def Graphs():
    PrintplotDr(cipherVigener.Dr)
    PrintPlotInd(cipherVigener.text, cipherVigener.alphabet_close_text)
    PlotOpentext(openVigener.alphabet_open_text, openVigener)
    plt.show()


keytext = tk.Text(root)
keytext.place(width=200, height= 30,x=100, y= 650)
chosefile = tk.Button(text="Chose file", command=openVigener.ChoseFile, activebackground='#FF0000')
chosefile.place(width=100, height= 30,x=350, y= 700)
encrypt = tk.Button(text="Encrypt", command=Encrypt, activebackground='#FF0000')
encrypt.place(width=100, height= 30, x=350, y= 750)
decrypt = tk.Button(text="Decrypt", command=Decrypt, activebackground='#FF0000')
decrypt.place(width=100, height= 30, x=350, y= 650)
printgraphs = tk.Button(text="Graphs",command = Graphs, activebackground='#FF0000')
printgraphs.place(width=100, height= 30, x=480, y= 650)
root.mainloop()

