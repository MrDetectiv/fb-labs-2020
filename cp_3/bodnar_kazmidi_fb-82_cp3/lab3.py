import codecs as cs
import math

#=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>

alphabet = "а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ь ы э ю я".split()
wrong_text = [ "жы", "шы", "аь", "аы", "уы", "еы", "оы" ]
freq = [ 
    'то', 'ов', 'на', 'не', 'но',
    'ст', 'по', 'ко', 'он', 'от',
    'ен', 'ни', 'ос', 'го', 'ал',
    'ра', 'ро', 'ка', 'ет', 'ть',
    'во', 'пр', 'ер', 'ак', 'ес',
    'ас', 'ло', 'ол' 
]

def filter(textLine):
    textLine = textLine.replace('ё', 'е')
    textLine = textLine.replace('ъ', 'ь')
    for letter in textLine:
        if letter not in alphabet:
            textLine = textLine.replace(letter, '')
    return textLine

def bigram_counter(line):
    bigrams = dict()
    bigramCounter = 0
    letterCounter = 0

    line = filter(line.lower())
    line = line.strip()
    line = ' '.join(line.split())
    line = line.replace(' ', '')

    for sym in line:
        isDouble = letterCounter % 2 == 1
        if letterCounter != 0 and isDouble:
            bigram = prevChar + sym
            bigrams[bigram] = bigrams.get(bigram, 0) + 1
            prevChar = sym
            bigramCounter = bigramCounter + 1
        else:
            prevChar = sym
        letterCounter = letterCounter + 1

    tupleList = bigrams.items()
    tupleList = sorted(tupleList, key=lambda i: i[1], reverse=True)

    result = list()
    for item in tupleList:
        result.append(item[0])
    return result

def split_to_bigrams(text):
    text = filter(text.lower())
    text = text.strip()
    text = ' '.join(text.split())
    text = text.replace(' ', '')
    result = list()

    for i in range(0, len(text), 2):
        result.append(text[i] + text[i+1])

    return result

def gcd(x, y):
    if (x % y) == 0:
        return y
    else:
        return gcd(y, x % y)

def euclid_ex(a,b):
    if a == 0:
        return b, 0, 1
    gcd, x, y = euclid_ex(b % a, a)
 
    x1 = y - math.floor(b / a) * x
    y1 = x
    return gcd, x1, y1

def ob(a,b):
    gcd, x, y = euclid_ex(a,b)
    if gcd != 1:
        return 0
    return x

def solve_eq(a, b, n):
    result = list()
    d = gcd(a, n)

    if d == 1:
        res = (ob(a, n)*b) % n
        result.append(res)
    else:
        if (b % d) == 0:
            res = (int(b / d) * ob(int(a / d), int(n / d))) % int(n / d)
            for i in range(d):
                result.append(res + i * int(n / d))
        else:
            result.append(-1)
    return result

def find_key(X1, X2, Y1, Y2):
    a_list = solve_eq((X1 - X2), (Y1 - Y2), 31**2)
    
    result = list()
    for a in a_list:
        if a != -1:
            k = (a, ((Y1 - a * X1) % (31**2)))
            result.append(k)
    return result

def encode_bigramm(w,a,b):
    i1=alphabet.index(w[0],0,len(alphabet))
    i2=alphabet.index(w[1],0,len(alphabet))
    N=i1*31+i2
    half_res=(a*N+b)%(31**2)
    x1=half_res%31
    x2=int((half_res-x1)/31)
    res=str(alphabet[x2])+str(alphabet[x1])
    return res

def decode_bigramm(w,a,b):
    i1=alphabet.index(w[0],0,len(alphabet))
    i2=alphabet.index(w[1],0,len(alphabet))
    N=i1*31+i2
    x=(ob(a,31**2)*(N-b))%(31**2)
    x1=x%31
    x2=int((x-x1)/31)
    
    res=str(alphabet[(x2)%31])+str(alphabet[x1])
    return res

def encode_list(listb,a,b):
    listb = split_to_bigrams(text)
    encoded_list=[]
    for x in range(0,len(listb)):
        t=encode_bigramm(listb[x],a,b)
        encoded_list.append(t)
    return ''.join(encoded_list)
def decode_list(text,a,b):
    listb = split_to_bigrams(text)
    decoded_list=[]
    for x in range(0,len(listb)):
        t=decode_bigramm(listb[x],a,b)
        decoded_list.append(t)
    return ''.join(decoded_list)

def coprime_ints(n):
    result = list()
    for i in range(1, n):
        if gcd(n, i) == 1:
            result.append(i)
    return result

def check_text(text):
    for wrong_bg in wrong_text:
        if wrong_bg in text:
            return wrong_bg
    else:
        return 0

def break_cipher(text):
    text = filter(text.lower())
    text = text.strip()
    text = ' '.join(text.split())
    text = text.replace(' ', '')
    coprime = coprime_ints(31**2)
    bc = bigram_counter(text)[:15]

    for i in range(0, len(bc)-1):
        for j in range(0, len(bc)-1):
            if i != j:
                sbigram1 = bc[i]
                pbigram1 = freq[i]
                sbigram2 = bc[j]
                pbigram2 = freq[j]

                Y1 = alphabet.index(sbigram1[0]) * 31 + alphabet.index(sbigram1[1])
                Y2 = alphabet.index(sbigram2[0]) * 31 + alphabet.index(sbigram2[1])
                X1 = alphabet.index(pbigram1[0]) * 31 + alphabet.index(pbigram1[1])
                X2 = alphabet.index(pbigram2[0]) * 31 + alphabet.index(pbigram2[1])

                keys = find_key(X1, X2, Y1, Y2)
                if len(keys) != 0:
                    for key in keys:
                        if key[0] in coprime:
                            decoded_text = decode_list(text, key[0], key[1])
                            wrong_bg = check_text(decoded_text)
                            if wrong_bg == 0:
                                print(decoded_text)
                                print('Key:', '(' + str(key[0]) + ',', str(key[1]) + ')')
                            else:
                                print('Text: ' + decoded_text[:30] + '..... ' + 'rejected, because it contains: ' + wrong_bg)
                                print('Key:', '(' + str(key[0]) + ',', str(key[1]) + ')')

#=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>

hfile = cs.open('02.txt', "r", encoding='utf-8')
text = hfile.read()
break_cipher(text)

