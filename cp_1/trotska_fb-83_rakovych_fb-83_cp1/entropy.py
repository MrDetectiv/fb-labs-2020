import string
from math import log2


def monogram(ready_for_use_text, spaces=True):
    sym_freq = dict()
    length = len(ready_for_use_text[:])

    for i in text:
        if i not in sym_freq:
            sym_freq[i] = 1
            continue
        sym_freq[i] += 1
    print(" Frequency: ")

    if spaces:
        sym_freq = {k: v for k, v in sorted(sym_freq.items(), key=lambda item: item[1], reverse=True)}
    else:
        sym_freq = {k: v for k, v in sorted(sym_freq.items(), key=lambda item: item[1], reverse=True) if not k == ' '}
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
    print(redundancy*100)


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
    print(redundancy*100)

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
    print(redundancy*100)

def clear_text(text):

    punct = string.punctuation + '–' + '0' + '1' + '2' + '3' + '4' + '5' + '6' + '7' + '8' + '9' + '«' + '»' + '…' + '‘' + '№'
    punct = punct + string.ascii_lowercase
    print(punct)
    for sym in punct[:]:
        text = text.replace(sym, '')
    text = text.replace('\n', '')
    text = text.replace('  ',' ')
    return text.lower()


f = open("text_cleared.txt", encoding="utf8")
words = f.read()
text = clear_text(words)
print("\nMonograms : \n")
monogram(text)
print("\nBigrams : \n")
bigram(text)
print("\nBigrams with step 2: \n")
bigram_2(text)

f = open('text_cleared_wout_spaces.txt', encoding='utf8')
text_copy = f.read()
text_copy = clear_text(text_copy)

print("\nMonogram without spaces: \n")
monogram(text_copy, spaces=False)
print("\nBigrams without spaces: \n")
bigram(text_copy)
print("\nBigrams without spaces with step 2: \n")
bigram_2(text_copy)


