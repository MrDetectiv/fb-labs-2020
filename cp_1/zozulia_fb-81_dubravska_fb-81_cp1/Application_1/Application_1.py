from collections import Counter
import re
import math

def remove_norus(fname, fresult): #Удаление всех символов кроме русского алфавита и пробелов
    alphabet = ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя ')
    fin = open(fname, encoding="utf-8")
    fout = open(fresult, "wt", encoding="utf-8")
    
    for letter in fin.read(): 
        if letter in alphabet:
            fout.write(letter)

def remove_all_norus(fname, fresult): #Удаление всех символов кроме русского алфавита
    alphabet = ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя ')
    fin = open(fname, encoding="utf-8")
    fout = open(fresult, "wt", encoding="utf-8")
    
    for letter in fin.read(): 
        if letter in alphabet:
            fout.write(letter)

def remove_double_spaces(fname): #Удаление всех повторяющихся пробелов
    for num in range(64):
        with open(fname, 'r+') as f:
            text = ''.join([line.replace("  ", " ") for line in f.readlines()])
            f.seek(0)
            f.write(text)
            f.close()

def remove_all_spaces(fname): #Удаление всех пробелов
    for num in range(64):
        with open(fname, 'r+') as f:
            text = ''.join([line.replace(" ", "") for line in f.readlines()])
            f.seek(0)
            f.write(text)
            f.close()

def replace_1(fname): #Замена ё на е
    for num in range(25):
        with open(fname, 'r+') as f:
            text = ''.join([line.replace("ё", "е") for line in f.readlines()])
            f.seek(0)
            f.write(text)
            f.close()

def replace_2(fname): #Замена ъ на ь
    for num in range(25):
        with open(fname, 'r+') as f:
            text = ''.join([line.replace("ъ", "ь") for line in f.readlines()])
            f.seek(0)
            f.write(text)
            f.close()

def lower(fname): #Замена заглавных на строчные
        with open(fname, 'r+') as f:
            text = ''.join([line.lower() for line in f.readlines()])
            f.seek(0)
            f.write(text)
            f.close()

def num_counter(fname): #Подсчет количества и частот букв
    alphabet = ('абвгдежзийклмнопрстуфхцчшщыьэюя ')
    let_count = 0
    fin = open(fname)
    for let in fin.read():
                let_count += 1 
    fin.close()
    temp_count = 0
    for c in alphabet:
        fin = open(fname)
        for let in fin.read():
            if c == let:
                temp_count += 1
        fin.close()
        print(c, temp_count*100/let_count, end='\n')
        temp_count = 0

def print_frequency (matrix, bigramm_count):
   alphabet = ('абвгдежзийклмнопрстуфхцчшщъыьэюя_')
   for i in range(len(matrix)):
       print(alphabet[i], end=' ')
       for j in range(len(matrix[i])): 
          print("{:10f}".format(round(matrix[i][j]*100/bigramm_count, 6)), end = "") 
       print()

def bigramm_counter_intersection(fname): #Подсчет количества и частот биграмм с пересечениями
    with open(fname, 'r') as file:
        text = file.read().replace('\n', '')

    map = [[0] * 33 for i in range(33)]

    bigramm_count=len(text)-1

    for letter in range(len(text)-100):
        if text[letter] != ' ' and text[letter+1] != ' ':
            map[ord(text[letter])-1072][ord(text[letter+1])-1072] += 1
        if text[letter] == ' ' and text[letter+1] != ' ':
            map[32][ord(text[letter+1])-1072] += 1
        if text[letter] != ' ' and text[letter+1] == ' ':
            map[ord(text[letter])-1072][32] += 1
    
    alphabet = ('абвгдежзийклмнопрстуфхцчшщъыьэюя_')
    for letter in alphabet:
        print('       ', letter, end=' ')
    print()
    print_frequency(map, bigramm_count)

def bigramm_counter_no_intersection(fname): #Подсчет количества и частот биграмм без пересечений
    with open(fname, 'r') as file:
        text = file.read().replace('\n', '')
    map = [[0] * 33 for i in range(33)]

    bigramm_count=round(len(text)/2)

    for letter in range(round((len(text)-100)/2)):
        if text[letter*2] != ' ' and text[letter*2+1] != ' ':
            map[ord(text[letter*2])-1072][ord(text[letter*2+1])-1072] += 1
        if text[letter*2] == ' ' and text[letter*2+1] != ' ':
            map[32][ord(text[letter*2+1])-1072] += 1
        if text[letter*2] != ' ' and text[letter*2+1] == ' ':
            map[ord(text[letter*2])-1072][32] += 1
    
    alphabet = ('абвгдежзийклмнопрстуфхцчшщъыьэюя_')
    for letter in alphabet:
        print('       ', letter, end=' ')
    print()
    print_frequency(map, bigramm_count)

def H1_counter(fname): #Подсчет H1
    alphabet = ('абвгдежзийклмнопрстуфхцчшщыьэюя ')
    let_count = 0

    fin = open(fname)
    for let in fin.read():
                let_count += 1 
    fin.close()
    
    temp_count = 0
    map = [0 for j in range(33)]
    num = 1

    H = 0


    for c in alphabet:
        fin = open(fname)
        for let in fin.read():
            if c == let:
                temp_count += 1
        if temp_count != 0:
            H -= temp_count/let_count * math.log2(temp_count/let_count)
        fin.close()
        temp_count = 0

    print(H)

def H2_counter_intersection(fname): #Подсчет H2 с пересечениями
    with open(fname, 'r') as file:
        text = file.read().replace('\n', '')
    map = [[0] * 33 for i in range(33)]

    bigramm_count=len(text)-1

    for letter in range(len(text)-2):
        if text[letter] != ' ' and text[letter+1] != ' ':
            map[ord(text[letter])-1072][ord(text[letter+1])-1072] += 1
        if text[letter] == ' ' and text[letter+1] != ' ':
            map[32][ord(text[letter+1])-1072] += 1
        if text[letter] != ' ' and text[letter+1] == ' ':
            map[ord(text[letter])-1072][32] += 1
    
    H = 0

    for i in range(len(map)):
       for j in range(len(map[i])):
               if map[i][j] != 0:
                H -= map[i][j]/bigramm_count * math.log2(map[i][j]/bigramm_count) / 2

    print(H)

def H2_counter_no_intersection(fname): #Подсчет H2 без пересечений
    with open(fname, 'r') as file:
        text = file.read().replace('\n', '')
    map = [[0] * 33 for i in range(33)]

    bigramm_count=round(len(text)/2)

    for letter in range(round((len(text)-100)/2)):
        if text[letter*2] != ' ' and text[letter*2+1] != ' ':
            map[ord(text[letter*2])-1072][ord(text[letter*2+1])-1072] += 1
        if text[letter*2] == ' ' and text[letter*2+1] != ' ':
            map[32][ord(text[letter*2+1])-1072] += 1
        if text[letter*2] != ' ' and text[letter*2+1] == ' ':
            map[ord(text[letter*2])-1072][32] += 1
    
    H = 0

    for i in range(len(map)):
       for j in range(len(map[i])):
               if map[i][j] != 0:
                H -= map[i][j]/bigramm_count * math.log2(map[i][j]/bigramm_count) / 2

    print(H)

num_counter('result_nospaces.txt')