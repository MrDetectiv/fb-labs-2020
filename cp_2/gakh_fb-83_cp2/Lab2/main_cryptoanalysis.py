from Caesar_cipher_op import *
from Vigenere_cipher_op import *

cipher_text = codecs.open( ".\\var6_text\\ciphertext_var6.txt", "r", "utf-8" ).read()


lens_indexes=codecs.open( "indexes.txt", "r", "utf-8" ).read().split('\n')[:-1]

cur_INDEX=calculate_INDEX(cipher_text)
print("Calculated ciphertext INDEX = {}".format(cur_INDEX))
print(cipher_text[:60])
for r in range(2, 60): 
       divided_text=divide_text(cipher_text, r)
       key=''
       for txt in divided_text:
              num=c_deduce_key(txt)
              key+=char(num%alphabet_len)
       
       dt=v_decode(cipher_text, key)
       i=calculate_INDEX(dt)
       if i >=0.04:
              print("Suggested key length(r) = {}".format(r))
              print("Suggested key: {}".format(key))
              print(dt[:80])
              print("INDEX = {}".format(i))
              print('-------------------------------------------------')

print('\n')
key='ВОЗВРАЩЕНИЕДЖИННА'
vt=v_decode(cipher_text, key)
for char in cipher_text[:120]:
       print(char.upper(), end="")
print('')
for i in range(0,120):
       print(key[i%len(key)],end="")
print('') 
print(vt[:120])
print('')
i=14
print("Frequencies for subtext number {}:".format(i))
divided_text=divide_text(vt, 17)[i]
cur_counts=get_counts_in_text(divided_text)
cur_freq_rating = sorted(cur_counts.items(), key=lambda item: item[1])[::-1]
print(cur_freq_rating)

codecs.open( ".\\deciphered_text_var6.txt", "w", "utf-8" ).write(vt)

