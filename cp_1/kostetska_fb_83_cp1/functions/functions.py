import math
from collections import Counter


def count_unigrams(text1):
    frequencies1 = {i: text1.count(i) / len(text1) for i in sorted(set(text1))}
    return frequencies1


def count_bigrams(text2, intersection):
    bigrams_number = len(text2) - 1 if intersection else len(text2) // 2
    bigrams = [(i + j) for (i, j) in zip(text2[0::1 if intersection else 2], text2[1::1 if intersection else 2])]
    coun = Counter(bigrams)
    frequencies2 = {i: coun[i] / bigrams_number for i in coun}
    # frequencies2 = {i: bigrams.count(i) / bigrams_number for i in sorted(set(bigrams))} # very slow
    return frequencies2


def entropy(frequencies):
    h = 0
    for i in frequencies:
        h -= frequencies[i] * math.log2(frequencies[i])
    h = h / len(list(frequencies.keys())[0])
    return h


def redundancy(h, letters_number):
    return 1 - (h / math.log2(letters_number))


def print_bigrams_table(fr, file):
    letters = sorted(set(''.join(fr.keys())))
    table = [[0.0 for i in range(len(letters))] for i in range(len(letters))]
    for i in fr:
        table[letters.index(i[0])][letters.index(i[1])] = fr[i]
    file.write('   ')
    for i in letters:
        file.write('   ' + i + '   ')
    file.write('\n')
    for i in table:
        file.write(letters[table.index(i)] + '  ')
        for j in i:
            file.write("{:.4f}".format(j * 100) + ' ')
        file.write('\n')
