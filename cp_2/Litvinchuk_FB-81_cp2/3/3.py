import re
text = open('text.txt','r',encoding='utf8')
ftext = open('ftext.txt','w',encoding='utf8')

temp = ''
for line in text:
	line = re.sub(r"[^а-яА-Я]+","",line)
	temp+=line

#temp - один суцільний рядок
ftext.write(temp)
text.close()
ftext.close()

d = {0:'а', 1:'б', 2:'в', 3:'г', 4:'д', 5:'е', 6:'ж', 7:'з',
     8:'и', 9:'й', 10:'к', 11:'л', 12:'м', 13:'н', 14:'о', 15:'п',
     16:'р',17:'с', 18:'т', 19:'у', 20:'ф', 21:'х', 22:'ц', 23:'ч', 
     24:'ш', 25:'щ', 26:'ъ', 27:'ы', 28:'ь', 29:'э', 30:'ю', 31:'я'}

def encode_val(t):
	res=[]
	lent=len(t)
	for w in range(lent):
		for value in d:
			if t[w]==d[value]:
				res.append(value)
	return res


def decode_val(t):
	res=[]
	lent=len(t)
	for w in range(lent):
		for value in d:
			if t[w]==value:
				res.append(d[value])
	return res


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

def full_decode(value,key):
	dic=comparator(value,key)
	lis=[]
	for v in dic:
		go=((dic[v][0]-dic[v][1]+len(d)) % len(d))
		lis.append(go)
	return lis


def count_each_letter(t):
	qa_letters = {'а':0, 'б':0, 'в':0, 'г':0, 'д':0, 'е':0, 'ж':0, 'з':0,
                  'и':0, 'й':0, 'к':0, 'л':0, 'м':0, 'н':0, 'о':0, 'п':0,
                  'р':0, 'с':0, 'т':0, 'у':0, 'ф':0, 'х':0, 'ц':0, 'ч':0, 
                  'ш':0, 'щ':0, 'ы':0, 'ь':0, 'э':0, 'ю':0, 'я':0, 'ъ':0} 
	for symbol in t:
		qa_letters[symbol] += 1
	return qa_letters


def index_v(text):
	qa=count_each_letter(text)
	index = 0
	count = 0
	for s in text:
		count+=1 
	for item, value in qa.items():
		value = int(value)
		index+= value*(value-1)
	index = index*(1/(count*(count-1)))
	return index


def fr_letters_(text):
	qa=count_each_letter(text)
	fr_letters = {}
	count = 0
	for s in text:
		count+=1 
	for item, value in qa.items():
		fr_letters[item] = value/count
	return fr_letters



from collections import defaultdict
blocks= defaultdict(list)
indexes = defaultdict(list)
indexes_sycypn = {} 
indexes_minus = {}
index_teor = 0.05539331456786139
id_s=0
r_max=32

for r in range(2,r_max):
	for i in range(0,r):
		b=''
		for n in range(i,len(temp),r):
			b+=temp[n]
		blocks[r].append(b)
		indexes[r].append(index_v(b))
	id_s=0
	for i in range(0,r):
		id_s+= indexes[r][i]
	id_s=id_s/r
	indexes_sycypn[r]=id_s

	indexes_minus[r]=abs(index_teor-id_s)
min_r = min(indexes_minus.values())
rr=0
for r in range(2,r_max):
	if min_r==indexes_minus[r]:
		rr = r



tempkey=''
max_fr=0
max_symb=14
for i in range(0,rr):
	i_br=0;
	fr = fr_letters_(str(blocks[rr][i]))
	max_fr = max(fr.values())
	for item,value in fr.items():
		if max_fr==value:
			for it, vl in d.items():
				if vl==item:
					it=(it-max_symb+32)%32
					item = d[it]
					break
			tempkey+=item
			break


VT=''.join(decode_val(full_decode(encode_val(temp),encode_val(tempkey))))



r = open('results.txt','a',encoding='utf8')
ot = open('OT.txt','a',encoding='utf8')
r.write("INDEXES (SER): \n")
for i in range(2,r_max):
	r.write(str(i)+' - '+str(indexes_sycypn[i])+'\n')
r.write("\nKEY : "+str(tempkey)+'\n')
r.write("OPEN TEXT : \n")
r.write(VT)
r.close()


tempkey='венецианскийкупец'
VT=''.join(decode_val(full_decode(encode_val(temp),encode_val(tempkey))))
ot.write(VT)
blocks= defaultdict(list)
for i in range(0,rr):
	b=''
	for n in range(i,len(VT),rr):
		b+=VT[n]
	blocks[rr].append(b)

ot.write("\nFR of 15 block: "+ str(fr_letters_(str(blocks[17][14]))))
ot.write("\nFR of 16 block: "+ str(fr_letters_(str(blocks[17][15]))))
ot.close()