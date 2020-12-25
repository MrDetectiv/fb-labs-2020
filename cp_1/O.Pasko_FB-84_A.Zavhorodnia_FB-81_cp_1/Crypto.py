import sys
import os
import math
from collections import OrderedDict
from ChangeSymbols import ChangeSymbols
from decimal import Decimal

result_path = os.getcwd() + r'\result.txt'

def LettersAmount(text, alphabet):
    LA = {}
    for let in alphabet:
        LA[let] = 0

    for let in text:
        LA[let] = LA[let] + 1

    #print(LA)

    LF = {}
    for let in alphabet:
        LF[let] = round(LA[let]/len(text), 5)

    return OrderedDict(sorted(LF.items(), key = lambda x: x[1], reverse=True))

def BigramsAmount(text, alphabet, cross = True):
    BA = {}
    for let in alphabet:
        for bi in alphabet:
            key = let + bi
            BA[key] = 0

    if(cross):
        i = 0
        while i < len(text)-1:
            key = text[i] + text[i+1]
            BA[key] = BA[key] + 1
            i = i + 1

        BF = {}
        for key in BA.keys():
            BF[key] = round(Decimal(BA[key]) / Decimal((len(text) - 1)), 5)

    else:
        if len(text)%2 == 1:
            text += "о"
        i = 0
        while i < len(text) - 1:
            key = text[i] + text[i+1]
            BA[key] = BA[key] + 1
            i = i + 2

        BF = {}
        for key in BA.keys():
            BF[key] = round(Decimal(BA[key]) / Decimal((len(text)/2)), 5)


    return BF
    #return OrderedDict(sorted(BF.items(), key=lambda x: x[1], reverse=True))

def Entropy(Dict, n):
    Entr = 0
    for key in Dict.keys():
        if Dict[key] != 0:
            Entr = Entr + (float(Dict[key]) * math.log2(1/Dict[key])/n)

    return Entr

def BuildTable(Data, alphabet):
    Table = {}
    Table[0] = list(" " + alphabet)
    for i in range(1, len(alphabet)+1):
        Table[i] = list(alphabet[i - 1])

    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            Table[i + 1] = Table[i + 1] + [(Data[alphabet[i] + alphabet[j]])]
    for i in range(0, len(alphabet)+1):
        Temp = ""
        for j in range(len(Table[i])):
            Temp += str(Table[i][j]) + (5 - len(str(Table[i][j]))) * " "
        Table[i] = Temp[0:len(Temp)]

    Temp = ""

    for i in range(len(Table)):
        Temp += str(Table[i]) + "\n"
    Table = Temp
    with open(result_path, 'a') as res:
        res.write(Table)

def redudancy(entropy, alphabet):
    return 1 - (entropy/math.log2(len(alphabet)))

def main_func(path, alphabet):
    n_p = os.getcwd() + r'\modify.txt'
    with open(n_p) as f:
        text = f.read()
        f.seek(0)

    Sorted_LF = LettersAmount(text, alphabet)
    MonoEntr = Entropy(Sorted_LF, 1)
    with open(result_path, 'a') as res:
        for i in Sorted_LF:
            Sorted_LF[i] = '{:f}'.format(Sorted_LF[i])
            res.write(str(i)+':'+str(Sorted_LF[i])+'\n')

    with open(result_path, 'a') as res:
        res.write('H letter: ' + str(MonoEntr) + '\n')
        res.write('R letter: ' + str(redudancy(MonoEntr, alphabet)) + '\n')

    BF_cross = BigramsAmount(text, alphabet, True)
    BiCEntr = Entropy(BF_cross, 2)
    BuildTable(BF_cross, alphabet)

    with open(result_path, 'a') as res:
        res.write('H cross bigrams: ' + str(BiCEntr) + '\n')
        res.write('R cross bigrams: ' + str(redudancy(BiCEntr, alphabet)) + '\n')

    BF = BigramsAmount(text, alphabet, False)
    BiEntr = Entropy(BF, 2)
    BuildTable(BF, alphabet)

    with open(result_path, 'a') as res:
        res.write('H non-cross bigrams: ' + str(BiEntr) + '\n')
        res.write('R non-cross bigrams: ' + str(redudancy(BiEntr, alphabet)) + '\n')



if __name__ == '__main__':
    #path = sys.argv[1]
    path = os.getcwd() + r'\crypto.txt'

    with open(result_path, 'w') as res:
        res.write('Results with spaces\n')
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
    ChangeSymbols(path, True)  # модификация текста
    main_func(path, alphabet)

    with open(result_path, 'a') as res:
        res.write('\n\n\nResults without spaces\n')
    alpha = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    ChangeSymbols(path, False)  # модификация текста
    main_func(path, alpha)
