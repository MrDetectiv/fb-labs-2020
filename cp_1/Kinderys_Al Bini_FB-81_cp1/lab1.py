import numpy as np
import math
import codecs
import sys
import re
file = open("text.txt", "r", encoding='utf-8')
text = file.read()
print(len(text))
punctuations = [".", ",", "!", "?", ";", ":", "-", "1", "2", "3", "4","5", "6", "7","8","9", "0","—","»","«",]
for k in range(len(punctuations)):
    text = text.replace(punctuations[k], "")# get rid of punctuations
text = text.lower()

print(len(text))
alphabet = np.array(['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я',' '])
rarity = np.zeros(len(alphabet)) # creating array of rarity for monogram
rarity2 = np.zeros(len(alphabet) ** 2) #creating array of rarity for begram
rarity2_step2 = np.zeros(len(alphabet) ** 2)
temporary = np.zeros(len(text))# array for recoded text
Hzero = np.log2(len(alphabet))
print(Hzero)

for i in range(len(alphabet)):# iterating per alphabet
    for j in range(len(text)): # iteration trought the whole text
        if text[j] == alphabet[i]:# checking for matching
            rarity[i] = rarity[i]+1 # if so plus to rarity
            temporary[j] = i # saving letter code
for k in range(len(temporary)-1): # loop for counting begram rarity
    temp1 = int(temporary[k]) # getting code of first letter

    temp2 = int(temporary[k+1]) # getting code of next letter

    rarity2[temp1*len(alphabet)+temp2] += 1 # increasing rarity of begram with (temp1, temp2)
for k1 in range(int((len(temporary) + 1) / 2) - 1):
    temp12 = int(temporary[2 * k1]) # getting code of first letter

    temp22 = int(temporary[2 * k1 + 1]) # getting code of next letter

    rarity2_step2[temp12*len(alphabet)+temp22] +=1
#print(rarity)
#print(rarity2

rarity2 = rarity2/(sum(rarity)-1)
rarity = rarity/sum(rarity)
rarity2ed = rarity2[np.nonzero(rarity2)] # get rid of all zero values
rarity1 = rarity[np.nonzero(rarity)] # get rid of all zero values
rarity2_step2 = rarity2_step2/sum(rarity2_step2)
rarity2_step2ed = rarity2_step2[np.nonzero(rarity2_step2)]
H1 = -np.dot(rarity1, np.log2(rarity1)) # measuring H1
H2 = -np.dot(rarity2ed, np.log2(rarity2ed))/2 # measuring H2
H2step2 = -np.dot(rarity2ed, np.log2(rarity2ed))/2
orig_stdout = sys.stdout
f = open('out4.txt', 'w+', encoding='utf-8')
sys.stdout = f
for i in range(len(alphabet)):
    print (alphabet [i]," = ", "%.7f" % rarity1[i],end='\t')
print ("\n\n\n\n bigrams with step2 raritys \n")
for i in range(len(alphabet)):
    for j in range (len(alphabet)):
        print ( alphabet [i],alphabet [j], " = ", "%.7f" % rarity2_step2[i*len(alphabet)+j], end='\t')
    print()
sys.stdout = orig_stdout
f.close()
"""for i in range(len(alphabet)):
    print (alphabet [i]," | ","%.7f" % rarity1[i],'\t')

print ("\n\n\n\n bigrams raritys \n")
for i in range(len(alphabet)):
    for j in range (len(alphabet)):
        print (alphabet [i],alphabet [j], " | ", "%.7f" % rarity2[i*len(alphabet)+j], " | ", "\t")
sys.stdout = orig_stdout
f.close()"""
print(H1)
print(H2)
print(H2step2)

