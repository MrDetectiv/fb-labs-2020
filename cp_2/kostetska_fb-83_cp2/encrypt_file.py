from functions.functions import *

#ask for filename
print('Print name of the file from directory text/ (d for default): ', end='')
file_to_open=input()
if file_to_open=='d':
    file_to_open='cleared_text_for_encryption.txt'

#open file and read text
with open('text/'+file_to_open, 'r', encoding='utf-8') as file:
    text = ''.join(file.readlines())

#ask for encrytion key
print('enter key for encryption: ', end='')
key=input()

#write to file encrypted text
with open('text/encrypted_vigenere_'+key+'.txt', 'w', encoding='utf-8') as file:
    file.write(encrypt_vigenere(text, key))

print('encrypted text was written to text/encrypted_vigenere_'+key+'.txt')
