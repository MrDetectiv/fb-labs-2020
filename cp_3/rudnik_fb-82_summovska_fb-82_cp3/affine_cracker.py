import itertools as it
import cryptomath
import affine
import lab1
import re
letters = list('абвгдежзийклмнопрстуфхцчшщьыэюя')
alph_len = len(letters)
letters_map = {letters[key] : key for key in range(alph_len)}
bigrams_map = {}
for i in letters:
    for j in letters:
        x2i_1 = letters_map[i]
        x2i = letters_map[j]
        bigrams_map[i + j] =  x2i_1*alph_len+x2i
text = open('16.txt','r').read()
text = re.sub('\n','',text)
frequent_rus_bigram = ["ст", "но", "то", "на", "ен"]
frequent_encrypted_bigram = lab1.ngram_freq(text,2,False)[:5]
frequent_encrypted_bigram_seq = list(it.permutations(frequent_encrypted_bigram, 2))
frequent_rus_bigram_seq = list(it.permutations(frequent_rus_bigram, 2))

rus_and_encrypted = []
for i in range(len(frequent_rus_bigram_seq)):
    for j in range(len(frequent_encrypted_bigram_seq)):
        if frequent_rus_bigram_seq[i][0] != frequent_rus_bigram_seq[j][0] and frequent_encrypted_bigram_seq[i][1] != frequent_encrypted_bigram_seq[j][1]:
            rus_and_encrypted.append((frequent_rus_bigram_seq[i][0], frequent_rus_bigram_seq[j][0], frequent_encrypted_bigram_seq[i][1], frequent_encrypted_bigram_seq[j][1]))


def icx(text):
    len_of_text = len(text)
    letters_map = {i:0 for i in letters}
    for letter in text:
        if letter in letters_map:
            letters_map[letter] += 1
        else:
            continue
    arr = sum([letters_map[item] * (letters_map[item] - 1) for item in letters_map])
    div = len_of_text * (len_of_text - 1)
    result = arr / div
    return result


def break_affine():
    keys = []
    for i in rus_and_encrypted:
        Y1 = bigrams_map[i[2]]
        Y2 = bigrams_map[i[3]]
        X1 = bigrams_map[i[0]]
        X2 = bigrams_map[i[1]]
        X1_X2 = X1 - X2
        Y1_Y2 = Y1 - Y2
        if X1_X2 < 0:
            X1_X2 += alph_len ** 2
        if Y1_Y2 < 0:
            Y1_Y2 += alph_len ** 2
        a_keys = cryptomath.linear_equation(X1_X2, Y1_Y2, alph_len ** 2)

        if not isinstance(a_keys, list):
            a_keys = [a_keys]
        if None not in a_keys:
            for a in a_keys:
                if cryptomath.gcd(a,alph_len ** 2) != 1:
                    continue


                b = (Y1 - a * X1) % alph_len ** 2
                if b < 0:
                    b += alph_len ** 2
                if (a,b) in keys:
                    continue



                keys.append((a,b))

    for key in keys:
        candidate = affine.cipher(text,key[0],key[1],'decrypt')
        if icx(candidate) >= 0.050:
            print(key)
            print(candidate)

break_affine()