import re
from collections import Counter
import math
from itertools import cycle
import string

file = open("C:/Users/user/Desktop/texti.txt", "r", encoding='utf-8')
text1 = file.read()
text1 = text1.lower()
text1 = text1.replace('ё','е')
text1 = re.sub('[^а-я]', '', text1)
open("ready", 'w').write(text1)
text = open('ready', 'r').read()
alphabet='абвгдежзийклмнопрстуфхцчшщъыьэюя'
i_alphabet=dict((alphabet[i], i) for i in range(len(alphabet)))


def encode_f(text, key):
    func = lambda arg: alphabet[(alphabet.index(arg[0])+alphabet.index(arg[1])) %32]
    return ''.join(map(func, zip(text, cycle(key))))


encode_f(text, 'не') #2
encode_f(text, 'вот') #3
encode_f(text, 'поле') #4
encode_f(text, 'князь') #5
encode_f(text, 'деконтаминация') #14

open('text_2.txt', 'w').write(encode_f(text, 'не'))
open('text_3.txt', 'w').write(encode_f(text, 'вот'))
open('text_4.txt', 'w').write(encode_f(text, 'поле'))
open('text_5.txt', 'w').write(encode_f(text, 'князь'))
open('text_14.txt', 'w').write(encode_f(text, 'деконтаминация'))




    

texto = open("ready", "r").read()

def accordance_index(some_dict, number):
    result_index=0
    for i in some_dict:
        result_index+=some_dict[i]*(some_dict[i]-1)
    result_index=result_index/(len(number)*(len(number)-1))
    return result_index

accordance_index(Counter(text), texto)
print('theoretical value:', accordance_index(Counter(text), texto))

def text_read(name):
    t = open(name, 'r').read()
    return t
print('ключ "не":',accordance_index(Counter(text_read('text_2.txt')), texto))
print('ключ "вот":',accordance_index(Counter(text_read('text_3.txt')), texto))
print('ключ "поле":',accordance_index(Counter(text_read('text_4.txt')), texto))
print('ключ "внязь":',accordance_index(Counter(text_read('text_5.txt')), texto))
print('ключ "деконтаминация":',accordance_index(Counter(text_read('text_14.txt')), texto))



word_f = dict([('о', 0.114725160004508),
 ('е', 0.0871670156415899),
 ('а', 0.07966000154221213),
 ('н', 0.06508609695769),
 ('и', 0.06484764723677108),
 ('т', 0.06475155555819181),
 ('с', 0.05293109277592251),
 ('в', 0.0462616184923097),
 ('л', 0.04596148028637693),
 ('р', 0.04183191074150745),
 ('к', 0.03302706582279983),
 ('д', 0.032017510039207775),
 ('м', 0.03143977365071268),
 ('у', 0.02965199390233052),
 ('п', 0.027441885295007386),
 ('ь', 0.023226900924734117),
 ('я', 0.02136438320412364),
 ('ч', 0.018103197717526054),
 ('б', 0.017389034871788788),
 ('г', 0.016890781723599996),
 ('ы', 0.016513532911399915),
 ('з', 0.015397208596053123),
 ('ж', 0.011408810776503806),
 ('й', 0.010013701961575193),
 ('х', 0.008508265663833347),
 ('ш', 0.00823066748127102),
 ('ю', 0.005617211087318864),
 ('э', 0.0035269204989649386),
 ('щ', 0.00299070520615224),
 ('ц', 0.00277242287456477),
 ('ф', 0.0012444465534524791)])




encrypt_text=open("C:/Users/user/Desktop/bbc.txt",'r',encoding='utf-8').read()
encrypt_text=encrypt_text.replace('\n','')

real_index=0

for i in word_f:
    real_index+=pow(float(word_f[i]),2)

def f(step, some_encrypt_file):
    list_accord_indexes=[]                         

    for j in range(0,step): 
        temp_string=""                             
        
        for i in range(j,len(some_encrypt_file),step):
            temp_string+=some_encrypt_file[i]
        
        temp_string_freq=Counter(temp_string)      
        list_accord_indexes.append(accordance_index(temp_string_freq, temp_string)) 
    return sum(list_accord_indexes)/len(list_accord_indexes)
        
        
d1=dict((f(r,encrypt_text), r) for r in range(1,33))
       
res = dict((v,k) for k,v in d1.items())


dict_diff = {}
for i in range(2,31):
    dict_diff[i]=abs(real_index - res[i])

closest_val= min(dict_diff, key=dict_diff.get)

print('Ключ r =', closest_val)

len_our_block = closest_val


i_alp = dict((v,k) for k,v in i_alphabet.items()) 


def f1(number_block,encrypt_text,r):
    temp_list=[]
    for i in range(number_block,len(encrypt_text),r):
        temp_list.append(encrypt_text[i])
            
    amount_lett_every_block = Counter(temp_list) 
    print(amount_lett_every_block)
    symbol_max=max(amount_lett_every_block, key=amount_lett_every_block.get)  
    
   
    y = i_alphabet[symbol_max]
    kk = (y - 14)%32
  
    key.append(i_alp[kk])
    return print('блокY=',number_block,': наибольшая частота у буквы: ',symbol_max,' => Буква ключа:', i_alp[kk],'\n')
   
    
    
        
    
key=[]
for k in range(0,len_our_block):
    f1(k,encrypt_text,len_our_block)
    



key_of_text=''.join([str(elem) for elem in key])    
print('KEY: ', key_of_text)

def decode_func(text, keytext):
    func = lambda arg: alphabet[(alphabet.index(arg[0])-alphabet.index(arg[1])) %32]
    return ''.join(map(func, zip(text, cycle(keytext))))

decode_func(encrypt_text,key_of_text )
print(decode_func(encrypt_text,"экомаятникфуко"))