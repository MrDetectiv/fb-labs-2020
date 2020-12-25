#форматування тексту
import re
text = open('text.txt','r',encoding='utf8')
ftext = open('ftext.txt','w',encoding='utf8')

temp = ''
for line in text:
	line = re.sub(r"[^а-яА-Я]+","",line)
	temp+=line

temp = temp.lower()
#temp - відредагований ВТ
ftext.write(temp)
text.close()
ftext.close()


#cтворюю словник для всіх символів
d = {0:'а', 1:'б', 2:'в', 3:'г', 4:'д', 5:'е', 6:'ж', 7:'з',
     8:'и', 9:'й', 10:'к', 11:'л', 12:'м', 13:'н', 14:'о', 15:'п',
     16:'р',17:'с', 18:'т', 19:'у', 20:'ф', 21:'х', 22:'ц', 23:'ч', 
     24:'ш', 25:'щ', 26:'ъ', 27:'ы', 28:'ь', 29:'э', 30:'ю', 31:'я'}

key = 'абвгдежзиклмопрстучн'  #визначаю ключ, яким буде відбуватись шифрування

#форматування тексту, де кожній літері співставляється деяке число
def encode_val(t):
	res=[]
	lent=len(t)
	for w in range(lent):
		for value in d:
			if t[w]==d[value]:
				res.append(value)
	return res

#з'єдную ВТ і ключ в одному словнику
def comparator(value,key):
	lk=len(key)
	dic={}
	iter=0
	f=0
	for i in value:
		dic[f]=[i,key[iter]]
		f+=1
		iter+=1
		if(iter>=lk):
			iter=0
	return dic

#перетворює ВТ у ШТ але у числовому форматі
def full_encode(value,key):
	dic=comparator(value,key)
	lis=[]
	for v in dic:
		go=((dic[v][0]+dic[v][1]) % len(d))
		lis.append(go)
	return lis

#числа переходять у символи
def decode_val(t):
	res=[]
	lent=len(t)
	for w in range(lent):
		for value in d:
			if t[w]==value:
				res.append(d[value])
	return res

ST = ''.join(decode_val(full_encode(encode_val(temp),encode_val(key)))) #ШТ

count=0
def count_each_letter(t):
	qa_letters = {'а':0, 'б':0, 'в':0, 'г':0, 'д':0, 'е':0, 'ж':0, 'з':0,
                  'и':0, 'й':0, 'к':0, 'л':0, 'м':0, 'н':0, 'о':0, 'п':0,
                  'р':0, 'с':0, 'т':0, 'у':0, 'ф':0, 'х':0, 'ц':0, 'ч':0, 
                  'ш':0, 'щ':0, 'ы':0, 'ь':0, 'э':0, 'ю':0, 'я':0, 'ъ':0}  
	for symbol in t:
		global count
		count += 1
		qa_letters[symbol] += 1
	return qa_letters

def index_v(text):
	qa=count_each_letter(text)
	index = 0
	for item, value in qa.items():
		value = int(value)
		index+= value*(value-1)
	index = index*(1/(count*(count-1)))
	return index

ID = index_v(ST)


r = open('results.txt','a',encoding='utf8')
r.write("KEY LENGTH: "+str(len(key))+'\n')
r.write("CHIPHER TEXT INDEX: "+str(ID)+'\n')
r.write('CHIPHER TEXT: '+ST+'\n\n\n')
