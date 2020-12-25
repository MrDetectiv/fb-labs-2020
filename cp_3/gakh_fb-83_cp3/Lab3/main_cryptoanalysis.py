from Affine_cipher import *


def deduce_key(X1_str,Y1_str,X2_str,Y2_str):
       #print("{} -> {}, {} -> {}".format(X1_str,Y1_str,X2_str,Y2_str))
       X1=encode_bigramm(X1_str)
       Y1=encode_bigramm(Y1_str)
       X2=encode_bigramm(X2_str)
       Y2=encode_bigramm(Y2_str)
       
       XY_LQ=XY_LINEAR_EQUATION(X1,Y1,X2,Y2, m)
       return XY_LQ.solve()
       
       

cipher_text = filter_raw_text(".\\06.txt").upper()
print(cipher_text[:60])
cur_counts=get_counts_of_bigramms(cipher_text)

deciphered_text=''

cur_counts = sorted(cur_counts.items(), key=lambda item: item[1])[::-1]
#print(cur_counts)
#print(freq_rating)
print('')
for i in range(0,20):
       for j in range(i+1,20):
              all_keys=deduce_key(freq_rating[i], cur_counts[i][0], freq_rating[j], cur_counts[j][0])
              if all_keys is not None:
                     #print(all_keys)
                     for key in all_keys:
                            plain_text=decipher_affine(cipher_text, key[0], key[1])
                            if plain_text is not None:
                                   index=calculate_INDEX(plain_text)
                                   if index > 0.05:
                                          print("index: {}, key: {}, text: {}".format(index, key, plain_text[:200]))
                                          print('--------------------------------------------------------------------------------\n')
                                          deciphered_text=plain_text
codecs.open( 'deciphered_text.txt', "w", "utf-8" ).write(deciphered_text)

