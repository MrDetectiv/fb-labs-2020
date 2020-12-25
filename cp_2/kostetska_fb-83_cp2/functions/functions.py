import collections
import matplotlib.pyplot as plt

#russian alphabet
alphabet = [chr(i) for i in range(ord('а'),ord('я')+1)]

max_key_length= 30

def encrypt_vigenere(pt, key):
    ct=''
    n=0
    for i in range(0, len(pt)):
        #if char is in alphabet, encrypt and write to ciphertext, else - write to ciphertext
        if pt[i] in alphabet:
            # ciphertext_char = (plaintext_char + key_char) mod alphabet_length
            ct+=alphabet[(alphabet.index(pt[i])+alphabet.index(key[n%len(key)]))%len(alphabet)]
            n+=1
        else:
            ct+=pt[i]
    return ct

def decrypt_vigenere(ct, key):
    pt=''
    n=0
    for i in range(0, len(ct)):
        #if char is in alphabet, decrypt and write to plaintext, else - write to plaintext
        if ct[i] in alphabet:
            # plaintext_char = (ciphertext_char - key_char + alphabet_length) mod alphabet_length
            pt+=alphabet[(alphabet.index(ct[i])-alphabet.index(key[n%len(key)])+len(alphabet))%len(alphabet)]
            n+=1
        else:
            pt+=ct[i]
    return pt

# index = sum(Ni*(Ni-1))/n*(n-1)
def index_of_coincidence(text):
    sum =0
    for i in set(text):
        count = text.count(i)
        sum+=count*(count-1)
    return sum/(len(text)*(len(text)-1))

def all_indexes(ct):
    indexes=[]
    for i in range(1, max_key_length+1):
        #get each ith char form ciphertext
        ct_part=[ct[p] for p in range(0, len(ct), i)]

        indexes.append(index_of_coincidence(''.join(ct_part)))
    return indexes


def try_guess_length(indexes):
    #for each possible length (l) check if every lth index is bigger than previous l-1 indexes
    # eg [1 2 3 4 5 6 7 8 9 10] for l=3: check if 3 is bigger than 1 and 2, if 6 is bigger than 4 and 5, if 9 is bigger than 7 and 8
    for l in range(2, max_key_length+1):
        if all(z==True for z in [all(p<indexes[i-1] for p in indexes[i-l:i-1]) for i in [l+k*l for k in range(0, int(len(indexes)/l))]]):
            return l

def count_frequencies(part_ct):
    c = collections.Counter(part_ct)
    # frequencies as {letter : frequency}
    frequencies = {i:c[i]/len(part_ct)  for i in c}
    return frequencies

def find_most_frequent(part_ct):
    frequencies=count_frequencies(part_ct)
    for key, value in frequencies.items():
        if value==max(frequencies.values()):
            return key


def generate_key(ct, key_len, chan):
    #most frequent letters in Russian alphabet
    most_frequent=['о', 'а', 'е', 'и', 'н', 'т', 'р', 'с']

    key=''
    for i in range(key_len):
        #find most frequent letter in block
        fr=find_most_frequent([ct[k] for k in range(i, len(ct), key_len)])

        #key_char = (most_frequent_in_block - most_frequent_in_language + alphabet_length) mod alphabet_length
        key+=alphabet[(alphabet.index(fr)-alphabet.index(most_frequent[chan[i]%len(most_frequent)])+len(alphabet))%len(alphabet)]

    return key

def paint_bar(indexes):
    #set values for x, y
    x=[xel+2 for xel in range(len(indexes))]
    y=indexes

    #make a bar plot
    plt.bar(x,y,align='center')

    #set title, labels for x, y
    plt.title('indexes of coincidence bar chart')
    plt.xlabel('r')
    plt.ylabel('indexes')

    #show plot
    plt.show()
