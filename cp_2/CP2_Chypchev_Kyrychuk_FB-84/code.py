import re
from collections import Counter
from itertools import cycle

cyrillic = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ж', 
    'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
    'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 
    'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
]

class Text:
    def __init__(self,textpath,keyspath):
        self.rusalpha = r'[^а-яА-Я|\s]+'
        self.ready_text = ''
        self.keys = []
        self.textpath = textpath
        self.keyspath = keyspath
    
    def getcleartext(self):
        textfile = open(self.textpath,'r',encoding='utf-8')
        self.ready_text = textfile.read().lower().rstrip().replace(' ', '')
        self.ready_text = re.sub(self.rusalpha,'',self.ready_text).replace('\n','')

    def getkeys(self):
        with open(self.keyspath,'r',encoding='utf-8') as keyfile:
            for key in keyfile:
                self.keys.append(key.replace('\n',''))
            

class Vigenere:
    def __init__(self,alpha):
        self.alpha = alpha

    def encrypt(self,text,key):
        re.sub('ё','е',text)
        def calculate(a,b):
            num = (self.alpha.index(a) + self.alpha.index(b)) % 32
            #print(num)
            return self.alpha[num]

        encrypted = ''
        for symb,k in zip(text,cycle(key)):
            encrypted += calculate(symb,k)
        return encrypted

    def decrypt(self,ciphertext,key):
        re.sub('ё','е',ciphertext)
        decrypted = ''
        for symb,k in zip(ciphertext,cycle(key)):
            decrypted += self.alpha[(self.alpha.index(symb) - self.alpha.index(k) + 32) % 32]
        return decrypted


#індекс відповідності
def correspondance_index(text):
    result = 0
    length = len(text)
    frequency = dict(Counter(text))
    for freq in frequency.values():
        result += freq * (freq - 1)
    return result / (length * (length - 1))  


def break_into_blocks(text,keylen):
    blocks = []
    for step in range(0,keylen):
        string = ''
        for i in range(step,len(text),keylen):
            string += text[i]
        blocks.append(string)
    return blocks

#індекс відповідності для всіх довжин ключа
def findkeylen():
    rdict = {}
    for blocklen in range(2,31):
        summa = 0
        blocks = break_into_blocks(text.ready_text,blocklen)
        for block in blocks:
            summa += correspondance_index(block)
        #print(summa/blocklen)
        rdict[blocklen] = summa/blocklen
    return rdict

def findkey(letters):
    part_of_key = ''
    for letter in letters:
        part_of_key += cyrillic[(cyrillic.index(letter[0]) - cyrillic.index('о') % 32)]
    return part_of_key

def crackthekey(ciphertext,keylen):
    most_common = []
    blocks = break_into_blocks(ciphertext,keylen)
    for block in blocks:
        common = Counter(block).most_common(1)[0]
        if common[0] not in most_common:
            most_common.append(common)
    return most_common
            

########################################
#Шифруємо наш текст
########################################
our_text = Text(r'C:\Users\funro\Desktop\univer\kripta\cryptolabs\fb-labs-2020\cp_2\CP2_Chypchev_Kyrychuk_FB-84\crypto.txt',
    r'C:\Users\funro\Desktop\univer\kripta\cryptolabs\fb-labs-2020\cp_2\CP2_Chypchev_Kyrychuk_FB-84\keys.txt')
our_text.getcleartext()
our_text.getkeys()

#шифруем всеми ключами
with open(r'C:\Users\funro\Desktop\univer\kripta\cryptolabs\fb-labs-2020\cp_2\CP2_Chypchev_Kyrychuk_FB-84\resultedtexts.txt','w+',encoding='utf-8') as writefile:
    for key in our_text.keys:
        encrypted = Vigenere(cyrillic).encrypt(our_text.ready_text,key)
        writefile.write(f'\n{key}\n')
        writefile.write(encrypted + '\n')
        writefile.write(f'Індекс відповідності: {correspondance_index(encrypted)}\n')


########################################
#Індекс відповідності для тексту по варіанту
########################################

text = Text(r'C:\Users\funro\Desktop\univer\kripta\cryptolabs\fb-labs-2020\cp_2\CP2_Chypchev_Kyrychuk_FB-84\cp_var11.txt',None)
text.getcleartext()
#найбільше значення у довжини ключа 17
keylen = findkeylen()
# вывели самые популярные буквы из каждоый части всех 17 блоков
# наш найденный ключ - венецианскийкужьц

#отримали ключ - венецианскийкужьц
common = crackthekey(text.ready_text,17)

key = 'венецианскийкупец'
#расшифровка текста готовым ключём
most_common = []
a = Vigenere(cyrillic)

blocks = break_into_blocks(a.decrypt(text.ready_text,key),17)
#найпопулярніші букви у 15 блоці
most_common_14 = Counter(blocks[14]).most_common()
#найпопулярніші букви у 16 блоці
most_common_15 = Counter(blocks[15]).most_common()#[0]