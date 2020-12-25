import string
from math import log2
import re


def monogram(ready_for_use_text):
    sym_freq = dict()
    length = len(ready_for_use_text[:])

    for i in ready_for_use_text:
        if i not in sym_freq:
            sym_freq[i] = 1
            continue
        sym_freq[i] += 1
    print(" Frequency: ")

    sym_freq = {k: v for k, v in sorted(sym_freq.items(), key=lambda item: item[1], reverse=True)}
    print(sym_freq)
    sym_probs = {k: v/length for k, v in sym_freq.items()}
    print(sym_probs)

    entropy_sym = 0
    for i in sym_probs.values():
        entropy_sym += i * log2(i)
    entropy_sym *= -1
    print(" Entropy: ")
    print(entropy_sym, log2(length))
    redundancy = 1 - entropy_sym/log2(32)
    print("redundancy ")
    print(redundancy)


def bigram(ready_for_use_text):
    bigram_freq = {}
    length = len(ready_for_use_text[:])
    for i in range(length):
        bigram = ready_for_use_text[i:i + 2]
        if bigram not in bigram_freq:
            bigram_freq[bigram] = 1
            continue
        bigram_freq[bigram] += 1
    print(" Frequency: ")
    print(len(bigram_freq))
    bigram_freq = {k: v for k, v in sorted(bigram_freq.items(), key=lambda item: item[1], reverse=True)}
    print(bigram_freq)
    bigram_probs = {k: v/length for k, v in bigram_freq.items()}
    print(bigram_probs)

    entropy_bigram = 0
    for i in bigram_probs.values():
        entropy_bigram += i * log2(i)
    entropy_bigram *= -1
    print(" Entropy: ")
    print(entropy_bigram, log2(length))
    redundancy = 1 - entropy_bigram/log2(32**2)
    print("redundancy ")
    print(redundancy)

def bigram_2(ready_for_use_text):
    bigram_2_freq = {}
    length = len(ready_for_use_text[:])
    for i in range(0, length, 2):
        bigram2 = ready_for_use_text[i:i + 2]
        if bigram2 not in bigram_2_freq:
            bigram_2_freq[bigram2] = 1
            continue
        bigram_2_freq[bigram2] += 1
    print(" Frequency: ")
    print(len(bigram_2_freq))
    bigram_2_freq = {k: v for k, v in sorted(bigram_2_freq.items(), key=lambda item: item[1], reverse=True)}
    print(bigram_2_freq)
    bigram_2_probs = {k: v / (length//2) for k, v in bigram_2_freq.items()}
    print(bigram_2_probs)

    entropy_bigram2 = 0
    for i in bigram_2_probs.values():
        entropy_bigram2 += i * log2(i)
    entropy_bigram2 *= -1
    print(" Entropy: ")
    print(entropy_bigram2, log2(length))
    redundancy = 1 - entropy_bigram2/log2(32**2)
    print("redundancy ")
    print(redundancy)

def clear_text(text, space):
    text = ' '.join(text.split())
    out_text = ""
	
    for symbol in text:
        match = re.match('[а-я ]$', symbol.lower())
        if match:
            symbol = match.group(0)
            if symbol == 'ъ':
                symbol = 'ь'
            elif symbol == 'ё':
                symbol = 'е'

            out_text += symbol
	
    text = re.sub(' ', '' if space is False else '_', out_text)
    return ' '.join(text.split())

def main():
    f = open("1.txt", encoding="utf8")
    file_read = f.read()
    
    text = clear_text(file_read, True)
    print("\nMonograms : \n")
    monogram(text)
    print("\nBigrams : \n")
    bigram(text)
    print("\nBigrams with step 2: \n")
    bigram_2(text)
    f.close()

    text = clear_text(file_read, False)
    print("\nMonogram without spaces: \n")
    monogram(text)
    print("\nBigrams without spaces: \n")
    bigram(text)
    print("\nBigrams without spaces with step 2: \n")
    bigram_2(text)
    f.close()

if __name__ == '__main__':
    main()
