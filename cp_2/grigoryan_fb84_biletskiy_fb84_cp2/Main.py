import re
import math
import collections
from itertools import cycle
dict = {}
alphabet = (
    'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
    'ч',
    'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я')
#sumletters = 0

letter_ord = 0
def sumabukv(text):
    sumletters = 0
    for i in text:
        for j in i:
            if j in alphabet:
                sumletters += 1
    return sumletters

message = open("filteredtext.txt", 'r', encoding="utf-8")
letters = re.findall(r'(?=([а-я," "]{1}))', message.read())  # ділим посимвольно ВТ.

# key = ("да", "нет", "липа", "зачем", "необразованый")
def encryption(key,text):
    #key = ("григорянанаперездачу")
    encr_mess = ""
    key *= sumabukv(text) // len(key)  # розтягуєм ключ на всю довжину Відкритого тексту
    for i, j in zip(text, key):
        # print(ord(i), "+", ord(j), "=", ord(i) + ord(j), "==", ((ord(i) + ord(j)) % 32 + 1072))  # по пріколу для перевірки.
        letter_ord = ord(i) + ord(j)
        encr_mess += chr(letter_ord % 32 + 1072)  # зашифрований текст
    print(encr_mess)
def decryption(key, text):
    a = lambda arg: alphabet[alphabet.index(arg[0]) - alphabet.index(arg[1]) % 32]
    return ''.join(map(a, zip(text, cycle(key))))

from collections import Counter

def index_vidpovidnosti(text,sum):
    sum=sumabukv(text)
    index = 0
    for t in Counter(text):  # для відкритого тексту замінити encr_mess на letters.
        N = text.count(t)  # кількість появи букви t у шифротексті.........для відкритого тексту замінити encr_mess на letters.
        index += N * (N - 1)  # чисельник
    index = index / (sum * (sum - 1))  # Індекс Відповідності тексту

    print('Індекс відповідності тексту: ', index)
    return index

a = 0
message1 = open("text.txt", 'r', encoding="utf-8")
letters1 = re.findall(r'(?=([а-я," "]{1}))', message1.read())

for i in letters1:
    a += 1
    if a % 30 == 0:
        print()
    else:
        print(i, " ", end="")

def blocks(text, num_block):
    newarr = []
    i = 0
    j = 0
    suma = 0
    while i < num_block:
        newarr.append("")
        i += 1
    for l in range(0, len(text)):
        newarr[l%num_block] += text[l]
    while j < num_block:
        indexforblocks = index_vidpovidnosti(newarr[j], newarr[j])
        j += 1

        # indexforblocks+=indexforblocks/num_block
        suma += indexforblocks / num_block
    print("Середнє: ", suma)
    return newarr

def monogram_of_blocks(arr,n):
    for k in alphabet:
        dict[k] = arr[n].count(str(k))/sumabukv(arr[n])
    alphlist = sorted(dict.items(), reverse=True, key=lambda x: x[1])
    print("Буква часто встречающая в блоке: "+ str(alphlist[0]))


print()
index2=blocks(letters1,7) #Блоки

for i in range(7):
    print("BLOCK #" + str(i+1))
    monogram_of_blocks(index2,i) #Монограмы для блока

def analysis(letter, alphabet, popular):
    a = (alphabet.index(letter) - alphabet.index(popular)) % len(alphabet)
    return alphabet[a]

for l in "оеа": #предологаемые ввиды ключа
    print("\n")
    for i in "фьяруйтцотьхью":
        print(analysis(i,alphabet,l), end='')

print("\n")
print(decryption("последнийдозор", letters1)) #расшифровка по ключу
