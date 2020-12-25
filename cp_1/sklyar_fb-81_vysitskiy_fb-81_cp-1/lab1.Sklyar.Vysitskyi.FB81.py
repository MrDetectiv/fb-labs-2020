import numpy as np
import math
import codecs
import collections

file = open("text.txt", "r", encoding='utf-8')
text = file.read()
text = text.lower()
punctuations = [".", ",", "!", "?", ";", ":", "-", "1", "2", "3", "4","5", "6", "7","8","9", "0","—","»","«",   "’","/n"]
for k in range(len(punctuations)):
    text = text.replace(punctuations[k], "")# get rid of punctuations

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


alphabet = np.array(['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я', ' '])
frequency = np.zeros(len(alphabet)) # creating array of rarity for monogram
temporary = np.zeros(len(text))# array for recoded text


for i in range(len(alphabet)):# iterating per alphabet
    for j in range(len(text)): # iteration trought the whole text
        if text[j] == alphabet[i]:# checking for matching
            frequency[i] += 1 # if so plus to rarity
            temporary[j] = i # saving letter code

frequency = frequency/(len(text))
print(sum(frequency))




f = open("results_with_spaces.txt", "w")

def to_str(var):
    return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]

for i in range (len(alphabet)):
    f.write (alphabet [i])
    f.write(" : ")
    frequency[i] = toFixed(frequency[i], 4)
    f.write( to_str( frequency[i] ) ) 
    f.write(" \t ")
    f.write(" \n ")




bigrams_f = np.zeros([34,34])

for k in range (0, len(text) - 1, 1):
        t1 = int(temporary[k])
        t2 = int(temporary[k+1])
        bigrams_f[t1,t2] +=1
       
#for i in range(len(alphabet)):
    #for j in range(len(alphabet)):
       # f.write(alphabet[i])
       # f.write(alphabet[j])
        #f.write(':')
        #bigrams_f[i][j] = toFixed(bigrams_f[i][j]/(len(text)-1),5)
        #f.write(to_str(bigrams_f[i, j]))
        #f.write("\t")
        #f.write(" \n ")

  
frequency = frequency[np.nonzero(frequency)]
H1 = -np.dot(frequency, np.log2(frequency)) 

bigrams_f = bigrams_f/(len(text)-1) # why not to do this?
bigrams_f = bigrams_f[np.nonzero(bigrams_f)]
H2 = -np.dot(bigrams_f, np.log2(bigrams_f))/2 


bigrams_f1 = np.zeros([34,34])
for n in range (0, int((len(text) +1)/2 -1), 2):
        t12 = int(temporary[n])
        t21 = int(temporary[n+1])
        bigrams_f1[t12, t21] +=1


for i in range(len(alphabet)):
    for j in range(len(alphabet)):
        f.write(alphabet[i])
        f.write(alphabet[j])
        f.write(':')
        bigrams_f1[i][j] = toFixed(bigrams_f1[i][j]/(len(text)-1),5)
        f.write(to_str(bigrams_f1[i, j]))
        f.write("\t")
        f.write(" \n ")



bigrams_f1 = bigrams_f1[np.nonzero(bigrams_f1)]
bigrams_f1=bigrams_f1/sum(bigrams_f1) #read about function SUM()
H21 = -np.dot(bigrams_f1, np.log2(bigrams_f1))/2
f.write("H1 = ")
f.write(to_str(H1))
f.write("\n")
f.write("H2 = ")
f.write(to_str(H2))
f.write("\n")
f.write("H21 = ")
f.write(to_str(H21))
f.write("\n")
f.close()
print (H1)
print (H2)
print (H21)