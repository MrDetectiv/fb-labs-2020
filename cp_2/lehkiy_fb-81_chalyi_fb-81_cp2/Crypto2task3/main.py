def clear_text(text):
    text1 = text.replace('\n','')
    return text1

def find_key_lenght(text):
    counter_same={}
    for key_size in range(6,32):
       counter_same[key_size]=0
       for j in range(0,key_size-1):
         block=text[j::key_size]
         for i in range(0, len(block)-1):
           if block[i] == block[i+1]: counter_same[key_size]+=1
    print('Dr:')
    print(counter_same)

def encode_caesar_symbol(sym,key,alphabet):
    enc = alphabet[(alphabet.find(sym) + alphabet.find(key)) % 32]
    return enc

def encode_Visener(text,key,alphabet):
    i=0
    encr_text = ''
    for letter in text:
        encr_text=encr_text+encode_caesar_symbol(text[i],key[i%len(key)],alphabet)
        i=i+1
    return encr_text

def decode_caesar_symbol(sym,key,alphabet):
    dec = alphabet[(alphabet.find(sym) - alphabet.find(key)) % 32]
    return dec

def decode_Visener(text,key,alphabet):
    i=0
    decr_text = ''
    for letter in text:
        decr_text=decr_text+decode_caesar_symbol(letter,key[i%len(key)],alphabet)
        i=i+1
    return decr_text

def restoring_key(text,key_size,alphabet):
     frequence = {}
     key1 = ''
     key2 = ''
     key3 = ''
     for i in range(0,key_size):
        block = text[i::key_size]
        max = 0
        maxletter=''
        for letter in alphabet:
            frequence[letter] = block.count(letter)
            if block.count(letter) > max:
                max = block.count(letter)
                maxletter = letter
        key1=key1+decode_caesar_symbol(maxletter,'о',alphabet)
        key2 = key2 + decode_caesar_symbol(maxletter, 'е',alphabet)
        key3 = key3 + decode_caesar_symbol(maxletter, 'и',alphabet)

     print(key1)
     print(key2)
     print(key3)

f = open('text.txt','r')
f1 = f.read()
f1 = clear_text(f1)
f.close()
alphabet_Zm = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
find_key_lenght(f1)
key_lenght=input('Введите длину ключа:')
restoring_key(f1,int(key_lenght),alphabet_Zm)
key = input('Введите ключ:')
f3=decode_Visener(f1,key,alphabet_Zm)
print(f3)
fdecr = open('decrypted.txt','w')
fdecr.write(f3)
fdecr.close()
input('Press any key to continue...')


