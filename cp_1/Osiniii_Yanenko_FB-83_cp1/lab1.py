#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter, attrgetter

from math import log

f = open("C:\\Users\\Макс\\text.txt",  encoding="utf8")
data = f.read()
text=""
text1=""
dictionary1="абвгдежзийклмнопрстуфхцчшщыьюя"
for y in data:
    y = y.lower()
    for x in dictionary1:
        if y=="ё" or y=="э":
            y="e"

        if y=="ъ":
            y="ь" 

        if y==x:
            text1+=y
        else:
            continue

dictionary="абвгдежзийклмнопрстуфхцчшщыьюя "
for y in data:
    y = y.lower()
    for x in dictionary:
        if y=="ё" or y=="э":
            y="e"

        if y=="ъ":
            y="ь" 

        if y==x:
            text+=y
        else:
            continue
def mono_freq(t):
    letter = dict()
    for i in t:
        if i == u'\n':
            continue
        if i in letter:
            letter[i] = float(round(letter.get(i) + 1.0/len(t), 7))
        else:
            letter[i] = float(round(1.0/len(t), 7))
    return letter


def cross_bigrams(t):
    bigram = dict()
    for i in range(len(t)):
        if t[i:i+2] in bigram:
            bigram[t[i:i+2]] = float(bigram.get(t[i:i+2]) +1.0/len(t))
        else:
            bigram[t[i:i+2]] = float(1.0/len(t))
    return bigram

def noncross_bigrams(t):
    ncbigrm = dict()
    for i in range(0,len(t),2):
        if t[i] == u' ' and t[i+1] == u' ':
            continue
        if t[i:i+2] in ncbigrm:
            ncbigrm[t[i:i+2]] = float(round(ncbigrm.get(t[i:i+2]) + 1.0/len(t)*2, 7))
        else:
            ncbigrm[t[i:i+2]] = float(round(1.0/(len(t)*2), 7))
    return ncbigrm

def count_entropy(mydict):
    e = 0.0
    p = 0.0

    for i in mydict:
        p = float(mydict[i])
        e += p * log(p,2)
    return float(round(e*-1, 7))

def count_entropy_b(mydict):
    e = 0.0
    p = 0.0
    for i in mydict:
        p = float(mydict[i])
        e += p * log(p,2)/log(4,2)
    return float(round(e*-1, 7))

def count_entropy_b2(mydict):
    e = 0.0
    p = 0.0
    for i in mydict:
        p = float(mydict[i])
        e += p * log(p,2)/log(4,2)
    return float(round(e*-1, 7))

letter = mono_freq(text)#space
letter1 = mono_freq(text1)#nospace
bigram = cross_bigrams(text)#peretyn_space
bigram1 = cross_bigrams(text1)#peretyn_nonspace
bezpbigram = noncross_bigrams(text)
bezpbigram1 = noncross_bigrams(text1)

print ("==============================MONOGRAMS WITH SPACE=================================")
for key, value in sorted(letter.items(), key= itemgetter(1), reverse=True):
        print ("\"%s\": %s" % (key, value),end="\t")

print ("\n ")    
print ("=======================MONOGRAMS WITHOUT SPACE=====================================")
for key, value in sorted(letter1.items(), key= itemgetter(1), reverse=True):
    print ("\"%s\": %s" % (key, value),end="\t")

print ("\n ")
print ("========================CROSSING BIGRAMS WITH SPACE================================")
for key, value in sorted(bigram.items(), key= itemgetter(1), reverse=True):
    print ("%s: %s" % (key, value),end="\t")

print (" ")    
print ("=======================CROSSING BIGRAMS WITHOUT SPACE==============================")
for key, value in sorted(bigram1.items(), key= itemgetter(1), reverse=True):
    print ("%s: %s" % (key, value),end="\t")

print (" ")    
print ("=========================NON-CROSSING BIGRAMS WITH SPACE===========================")
for key, value in sorted(bezpbigram.items(), key= itemgetter(1), reverse=True):
    print ("%s: %s" % (key, value),end="\t")

print (" ")    
print ("=========================NON-CROSSING BIGRAMS WITHOUT SPACE========================")
for key, value in sorted(bezpbigram1.items(), key= itemgetter(1), reverse=True):
    print ("%s: %s" % (key, value),end="\t")

print (" ")
print ("================ with space ========================")
print ("h1",count_entropy(letter))
print ("H2 non-overlapping",count_entropy_b2(bezpbigram))
print ("H2 overlapping",count_entropy_b(bigram))

print ("================ no space ===========================")
print ("h1",count_entropy(letter1))
print ("H2 non-overlapping",count_entropy_b2(bezpbigram1)) 
print ("H2 overlapping",count_entropy_b(bigram1))
