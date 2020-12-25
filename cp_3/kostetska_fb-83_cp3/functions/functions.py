from collections import Counter
import math

#define Russian alphabet and five most often bigrams in language
alphabet = "абвгдежзийклмнопрстуфхцчшщьыэюя"
five_most_often = ["ст", "но", "то", "на", "ен"]

# some function from lab 1:
# to count frequencies of unigrams, bigrams, entropy
def count_unigrams(text1):
    frequencies1 = {i: text1.count(i) / len(text1) for i in sorted(set(text1))}
    return frequencies1

def count_bigrams(text, intersection):
    bigrams_number = len(text2) - 1 if intersection else len(text) // 2
    bigrams = [(i + j) for (i, j) in zip(text[0::1 if intersection else 2], text[1::1 if intersection else 2])]
    coun = Counter(bigrams)
    frequencies2 = {i: coun[i] / bigrams_number for i in coun}
    return frequencies2

def entropy(frequencies):
    h = 0
    for i in frequencies:
        h -= frequencies[i] * math.log2(frequencies[i])
    h = h / len(list(frequencies.keys())[0])
    return h

# basic euclidean algorithm
def euclid(a, b):
    if b==0:
        return abs(a)
    else:
        return euclid(b, a%b)

# extended euclidean algorithm which also calculates coefficients u, v near a and b
# so that u*a+v*b=gcd
def extended_euclid(a, b):
    # set u0, u1, v0, v1
    prevu, u, prevv, v = 1, 0, 0, 1

    # start loop while b!=0
    while b:
        q = a//b
        u, prevu = prevu-q*u, u # u[i+1]=u[i-1]+q[i]*u[i]
        v, prevv = prevv-q*v, v # v[i+1]=v[i-1]+q[i]*v[i]
        a, b = b, a%b

    # return u, v, gcd
    return [prevu, prevv, a]

# get inverse element as u from extended_euclid (only if gcd==1)
def inverse_element(a, n):
    u,v,gcd=extended_euclid(a,n)
    if gcd==1:
        return u

# calculate number that corresponds to the bigram as x = a*m+b
def upper_letter(a, b):
    return alphabet.index(a)*len(alphabet)+alphabet.index(b)

# solve linear congruence
def solve_linear(a, b, m):
    #get gcd
    gcd = euclid(a, m)

    if gcd==1:
        # one solution : inverse(a)*b modm
        return [inverse_element(a, m)*b%m]
    elif gcd>1:
        if b%gcd!=0:
            # no solutions
            return []
        else:
            # several solutions if a%gcd=b%gcd=m%gcd=0 (exactly gcd solutions)
            x0=(b/gcd*inverse_element(a/gcd, m/gcd))%(m/gcd)
            return [int(x0+m/gcd*i) for i in range(gcd)]

# get bigrams from corresponding number
def letters_from_upper_letter(x):
    return alphabet[int((x-x%len(alphabet))/len(alphabet))]+alphabet[x%len(alphabet)]

# decrypt Affine bigram cipher with given a, b
# returns '' if 'a' doesn't have inverse
def decipher_afin_bigrams(a, b, text):
    out = []
    bigrams = [(i + j) for (i, j) in zip(text[0::2], text[1::2])]
    inv = inverse_element(a, pow(len(alphabet),2))
    if inv!=None:
        for i in bigrams:
            x = int(inv*(upper_letter(i[0], i[1])-b)%pow(len(alphabet),2))
            out.append(letters_from_upper_letter(x))
    else:
        print('      error: inverse element for a not found')
    return ''.join(out)

# get coefficients by solving linear congruence with two given bigrams
def get_coefs(a, b):
    coefa = solve_linear(upper_letter(a[0][0], a[0][1]) - upper_letter(a[1][0], a[1][1]), upper_letter(b[0][0], b[0][1])-upper_letter(b[1][0], b[1][1]), pow(len(alphabet), 2))
    coefb=[]
    for ael in coefa:
        coefb.append((upper_letter(b[0][0], b[0][1])-ael*upper_letter(a[0][0], a[0][1]))%pow(len(alphabet), 2))
    return [coefa, coefb]

# sorting dictionary by values()
def sort_dict(a):
    return {k: v for k, v in sorted(a.items(), key=lambda item: item[1])[::-1]}

# criteria for the plaintext:
# entropy between 4.15 and 4.55 (avg in Russian lang is 4.35)
# and first 6 of most frequent unigrams from text include 3 most frequent letters in lang (o, a, e)
def is_plaintext(text):
    frequencies = count_unigrams(text)
    entr = entropy(frequencies)
    frequencies = list(sort_dict(frequencies).keys())
    if all([i in frequencies[:6] for i in ['о', 'а', 'е']]):
        if 4.15 <= entr <= 4.55:
            return True
        else:
            print('      error: entropy is not in (4.15; 4.55): '+ str(entr))
            return False
    else:
        print('      error: '+str(frequencies[:6]) +" doesn't contain letters o a and e")
        return False
