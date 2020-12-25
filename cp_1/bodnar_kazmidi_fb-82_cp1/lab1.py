import codecs as cs
import math

filename = input('File: ')
if len(filename) < 1: filename = 'text.txt'
spaces = int(input('Spaces? (0, 1): '))
doubleStep = int(input('Bigram step? (1, 2): ')) - 1

# =======================================

def entropy(dataDict):
    entr = 0
    for k in dataDict:
        entr = entr + dataDict[k] * math.log2(dataDict[k])
    return entr * (-1)

def printSorted(lDict):
    tupleList = lDict.items()
    
    tupleList = sorted(tupleList, key=lambda i: i[1], reverse=True)

    for item in tupleList:
        value = str(round(item[1] * 100, 3)).replace('.', ',')
        print(item[0].replace(' ', '_') + ' ' + '\t' + ' ' + value)

    print('\n')

def filter(textLine):
    alphabet = "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я".split()
    alphabet.append(' ')

    for letter in textLine:
        if letter not in alphabet:
            textLine = textLine.replace(letter, ' ')
    return textLine

# =======================================

text = cs.open(filename, encoding='utf-8')
letters = dict()
bigrams = dict()
letterCounter = 0
bigramCounter = 0
prevChar = 0
isDouble = 1

for line in text:
    line = filter(line.lower())
    line = line.strip()
    line = ' '.join(line.split())

    if spaces == 0:
        line = line.replace(' ', '')

    for sym in line:
        letters[sym] = letters.get(sym, 0) + 1
        
        if doubleStep: isDouble = letterCounter % 2 == 1

        if letterCounter != 0 and isDouble:
            bigram = prevChar + sym
            bigrams[bigram] = bigrams.get(bigram, 0) + 1
            prevChar = sym
            bigramCounter = bigramCounter + 1
        elif not isDouble or not doubleStep:
            prevChar = sym

        letterCounter = letterCounter + 1


# =======================================

for k in letters:
    letters[k] = letters[k] / letterCounter
for k in bigrams:
    bigrams[k] = bigrams[k] / bigramCounter

print('Letters:')
printSorted(letters)
print('Bigrams:')
printSorted(bigrams)

H1L = round(entropy(letters), 6)
H2B = round(entropy(bigrams) / 2, 6)

print('Entropy:')
print('H1L:', H1L)
print('H2B:', H2B)

# =======================================

input()