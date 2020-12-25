from Vigenere_cipher_op import *
       
keys_arr=[]
file=codecs.open( "keys.txt", "r", "utf-8" )

key_len_range=file.readline().split('-')
min_len=int(key_len_range[0])
max_len=int(key_len_range[1])

for i in range(min_len,max_len+1):
       keys_arr.append(file.readline()[:-2])

plain_text = codecs.open( ".\\my_text\\plain_text.txt", "r", "utf-8" ).read()
output_file=codecs.open( "indexes.txt", "w", "utf-8" )

for key in keys_arr:
       index=calculate_INDEX(v_encode(plain_text,key))
       print("key={}, r={}, INDEX={}".format(key, len(key), index))
       output_file.write("{}\t{}\n".format(len(key), index))
print("no key(plaintext) INDEX={}".format(calculate_INDEX(plain_text)))

output_file.close()
file.close()
