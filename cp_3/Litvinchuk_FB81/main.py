from math import gcd
import re
import heapq

list_of_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                   'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'э', 'ю', 'я']


def inverse (a, m):
    if gcd(a, m)==1:
        x = 1
        for i in range(1000):
            if (a * x) % m == 1:
                return x
            x+=1
        return 34;
    raise Error("Inverse not exists")


count_bigr=0
def count_each_bigr(text):
	qa_bigr={}
	for i in range(0, len(text)- 2, 2):
		global count_bigr
		if text[i:i+2] not in qa_bigr:
			qa_bigr[text[i:i+2]] = 1
			count_bigr += 1
		else:
			qa_bigr[text[i:i+2]] += 1
			count_bigr += 1
	return qa_bigr

def fr_bigr_func(text):
	qa_bigr = count_each_bigr(text)
	fr_bigr={}
	for item, value in qa_bigr.items():
		fr_bigr[item] = value/count_bigr
	return fr_bigr

def check_rus(text):
    alphabet = ('оеафщь')
    let_count = 0
    for let in text:
        let_count += 1

    for c in alphabet:
        t = 0
        for let in text:
            if c == let:
                t += 1
        if c == 'о' and t*100/let_count < 7:
            print('Frequency of o= '+str(t*100/let_count)+ '\n')
            return 0
        if c == 'е' and t*100/let_count < 6:
            print('Frequency of е= '+str(t*100/let_count)+ '\n')
            return 0
        if c == 'а' and t*100/let_count < 6:
            print('Frequency of а= '+str(t*100/let_count)+ '\n')
            return 0
        if c == 'ф' and t*100/let_count > 1:
            print('Frequency of ф= '+str(t*100/let_count)+ '\n')
            return 0
        if c == 'щ' and t*100/let_count > 1:
            print('Frequency of щ= '+str(t*100/let_count)+ '\n')
            return 0
    print('PROBABLY CORRECT TEXT')
    return 1

def decrypt(crypt_text, a, b):
	buff = ''
	for i in range(0, len(crypt_text)-2, 2):
		y1 = list_of_letters.index(crypt_text[i])
		y2 = list_of_letters.index(crypt_text[i+1])
		Y = y1*31+y2
		X = (inverse(a,31*31)*(Y-b)) % (31*31)
		X = list_of_letters[(X//31)]+list_of_letters[(X%31)]
		buff += X
	return buff

def solve_eq(a, b, n):
    "Solve equation ax=b mod(n)"
    X = []
    d = gcd(a, n)

    if d == 1:
        X.append((inverse(a, n) * b) % n)
    else:
        if (b % d) == 0:
            res = (inverse(int(a / d) * int(b / d) , int(n / d))) % int(n / d)
            for i in range(d):
                X.append(res + i * int(n / d))
        else:
            X.append(-1)
    return X



#ФОРМАТУВАННЯ ВХІДНОГО ТЕКСТУ----------------------------
text = open('11.txt','r',encoding='utf8')
ftext = open('ftext.txt','w',encoding='utf8') #ФАЙЛ З ФІДФОРМАТОВАНИМ ТЕКСТОМ
temp = ''

for line in text:
	i=0
	newline = re.sub(r"[^а-яА-Яё]+"," ",line)
	newline = ' '.join(newline.split())
	if len(newline)!=0:
		temp += newline.lower() + ' '
ftemp = ''
for line in temp:
	newline = line.replace(' ','')
	ftemp += newline
ftext.write(ftemp)
text.close()
ftext.close()
#-----------------------------------------------------------



f = open('ftext.txt','r',encoding='utf8')
res = open('results.txt','a',encoding='utf8')
f = f.read()

#Знаходимо частоти всіх біграм шифртексту
fr_bigr = fr_bigr_func(f)  

#Найчастіші біграми російської мови
#розташування в списку за спаданням частот
teor_most_fr_bigr = ["ст", "но", "то", "на", "ен"]

#Вибираємо 5 біграм шифр тексту з найбільшими частотами
#розташування в списку за спаданням частот
crypt_most_fr_bigr = heapq.nlargest(5, fr_bigr, key=fr_bigr.get) 

possible_keys = []
for i in range(0,4):
	for j in range(0,5):
		for n in range(0,5):
			if n==j:
				continue

			X1 = list_of_letters.index(teor_most_fr_bigr[j][0])*31+list_of_letters.index(teor_most_fr_bigr[j][1])
			X2 = list_of_letters.index(teor_most_fr_bigr[n][0])*31+list_of_letters.index(teor_most_fr_bigr[n][1])
			Y1 = list_of_letters.index(crypt_most_fr_bigr[i][0])*31+list_of_letters.index(crypt_most_fr_bigr[i][1])
			Y2 = list_of_letters.index(crypt_most_fr_bigr[i+1][0])*31+list_of_letters.index(crypt_most_fr_bigr[i+1][1])

			a_list = solve_eq((X1-X2),(Y1-Y2),31*31)
			for a in a_list:
				if a!=-1:
					k = (a, ((Y1-a*X1)%(31*31)))
					possible_keys.append(k)

for key in possible_keys:
	print(str(key)+'\n')
	decoded_text = decrypt(f,key[0],key[1])
	if check_rus(decoded_text)==1:
		print('OK, writing to results!\n')
		res.write("KEY - "+str(key)+'\n'+decoded_text+'\n')
