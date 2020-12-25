import re, math, string, collections, pprint

print('\n       TASK 1 and 2\n')

file=open('d:/UniverziTET/Crypt/lab2/Pushkin.txt','r',encoding='utf-8').read()
file=file.lower()
rus_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

for letter in file:
        if letter not in rus_alph:
            file=file.replace(letter,'')

file=file.replace('ё','е').replace('\n','')
file = re.sub(" +", " ", file)

print('Открытый текст:\n',file,'\n')

rus_alph_crypt = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
letter_place={}
place_letter={}

#####індекси відповідності
word_count = collections.Counter(file)

# pprint.pprint(dict(word_count))

index_open_text=0

for i in word_count:
    index_open_text+=word_count[i]*(word_count[i]-1)

index_open_text=index_open_text/(len(file)*(len(file)-1))

print('\n','INDEX OPEN TEXT: ',index_open_text, '\n')

##########################
i=0
for letter in rus_alph_crypt:
    letter_place[letter]=i
    place_letter[i]=letter
    i+=1

print(letter_place['а'])

keys=["юг","май","июнь","запад","неравнодушный"]
j=0
encrypt_texts=[]
fr_ecrypt_texts=[]
encrypt_text=""
len_keys=len(keys)

for j in range(0,len_keys):
    key=keys[j]
    len_key=len(key)
    i=0
    for letter in file:
        open_letter=letter_place[letter]
        encrypt_letter_pos=(open_letter+letter_place[key[i]])%32
        encrypt_letter=place_letter[encrypt_letter_pos]
        i=(i+1)%len(key)   
        encrypt_text+=str(encrypt_letter)

    print('Зашифрованый текст з ключем ',key,', длины ', len_key,':\n',encrypt_text,'\n')
    
    amount_encrypt=len(encrypt_text)
    word_count_encrypt = collections.Counter(encrypt_text)


    index_encrypt_text=0

    for n in word_count_encrypt:
        index_encrypt_text+=word_count_encrypt[n]*(word_count_encrypt[n]-1)
    
    index_encrypt_text=index_encrypt_text/((len(encrypt_text)-1)*len(encrypt_text))

    print('\n','INDEX ENCRYPT TEXT WITH KEY',key, ' : ',index_encrypt_text, '\n')

    fr_ecrypt_texts.append(index_encrypt_text)
    encrypt_texts.append(encrypt_text)
    encrypt_text=""
    j+=1

####### TASK 3

print('\n       TASK 3\n')

word_fr = {'а': '0.08267',
 'б': '0.01787',
 'в': '0.04306',
 'г': '0.01597',
 'д': '0.03169',
 'е': '0.08788',
 'ж': '0.01063',
 'з': '0.01618',
 'и': '0.06673',
 'й': '0.01210',
 'к': '0.03309',
 'л': '0.04911',
 'м': '0.03424',
 'н': '0.06605',
 'о': '0.10897',
 'п': '0.02385',
 'р': '0.04139',
 'с': '0.05668',
 'т': '0.06016',
 'у': '0.02625',
 'ф': '0.00142',
 'х': '0.00788',
 'ц': '0.00292',
 'ч': '0.01534',
 'ш': '0.00846',
 'щ': '0.00315',
 'ъ': '0.00021',
 'ы': '0.01991',
 'ь': '0.02139',
 'э': '0.00498',
 'ю': '0.00547',
 'я': '0.02434'}

max_fr_let=0

for i in word_fr:
    if max_fr_let<float(word_fr[i]):
        max_fr_let=float(word_fr[i])
        max_let=i



max_let_place=int(letter_place[max_let])

th_index=0

for n in word_fr:
    th_index+=pow(float(word_fr[n]),2)

print('\n','THEORETICAL INDEX : ',th_index, '\n')

encrypt_file=open('d:/UniverziTET/Crypt/lab2/var15_encrypt.txt','r',encoding='utf-8').read()
encrypt_file=encrypt_file.replace('\n','')

encrypt_amount=len(encrypt_file)
encrypt_fr = collections.Counter(encrypt_file)

print(encrypt_file)

indexs_y={}
y_mass={}
for r in range(1,33,1):
    y=[]

    for j in range(0,r,1):
        
        y_letters=""
        index_y=0
        
        for i in range(j,len(encrypt_file),r):
            letter=encrypt_file[i]
            y_letters+=letter
        
        y_letters_fr=collections.Counter(y_letters)
       # print('\n',y_letters,'\n')

        for i in y_letters_fr:
            index_y+=y_letters_fr[i]*(y_letters_fr[i]-1)
            
        index_y=index_y/(len(y_letters)*(len(y_letters)-1))

        y.append(index_y)

    
    y_mass[r]=sum(y)/len(y)


print(y_mass)

closest=9999
for i in range(2,31,1):
    iq=math.fabs(th_index-y_mass[i])
    #print(th_index,'-',y_mass[i],'=',iq)
    if iq<closest:
        closest=iq
        closest_amount=y_mass[i]
        key_r=i


print('\nКлюч r=',key_r,'\nЗначение:',closest_amount,'самое близкое к теоретическому значению',th_index,'\n')

y=[]
encrypt_word_mass=[]
encrypt_word=""
for j in range(0,key_r,1):
    print('\nY',j)
    y_letters=""
    index_y=0
    
    for i in range(j,len(encrypt_file),key_r):
        letter=encrypt_file[i]
        y_letters+=letter
    
    y_letters_fr=collections.Counter(y_letters)
    #print('\n',y_letters,'\n')
    
    for i in y_letters_fr:
        fr=y_letters_fr[i]/(len(y_letters))
        fr='%.5f' % fr
        y_letters_fr[i]=fr


    max_fr=0
    max_fr_mass=[]
    for i in y_letters_fr:
        if max_fr<float(y_letters_fr[i]):
            max_fr=float(y_letters_fr[i])
            max_letter=i
    
    print('Самую большую частоту имеет буква: ',max_letter,', частота: ',max_fr,'\n')

    place=int(letter_place[max_letter])
    encrypt_key=(place-14)%32

    print('Буква ключа:',place_letter[encrypt_key])
    encrypt_word_mass.append(place_letter[encrypt_key])
    encrypt_word+=place_letter[encrypt_key]
    encrypt_key=(place)%32
    print('Возможная буква для замены:',place_letter[encrypt_key])

print('\nKEY: ', encrypt_word)

i=0
decr_file=""
for letter in encrypt_file:
    decr_letter_place=(int(letter_place[letter])-int(letter_place[encrypt_word_mass[i]]))%32
    decr_letter=place_letter[decr_letter_place]
    decr_file+=decr_letter
    i=(i+1)%key_r

print('\nDecrypt file:\n',decr_file)
print()