from math import log2

#відкриваю два файли, обива на читання
f = open('ftext(utf8).txt','r',encoding='utf8')
fws = open('fwstext(utf8).txt','r',encoding='utf8')
results = open('results.txt','a',encoding='utf8')
ftext = f.read()
fwstext = fws.read()


qa_bigr = {}
qa_bigr_ws = {}
step = 2 # 1 для перетинаючих біграм, 2 - для не перетинаючих
count = 0
count_ws = 0
fr_bigr = {}
fr_bigr_ws = {} 
entr = 0
entr_ws = 0

def redundancy():
	return 1 - (entr/log2(32))
def redundancy_ws():
	return 1 - (entr_ws/log2(31)) 

def count_each_bigr():
	for i in range(0, len(ftext)- 2, step):
		global count
		if ftext[i:i+2] not in qa_bigr:
			qa_bigr[ftext[i:i+2]] = 1
			count += 1
		else:
			qa_bigr[ftext[i:i+2]] += 1
			count += 1
def count_each_bigr_ws():
	for i in range(0, len(fwstext)- 2, step):
		global count_ws
		if fwstext[i:i+2] not in qa_bigr_ws:
			qa_bigr_ws[fwstext[i:i+2]] = 1
			count_ws += 1
		else:
			qa_bigr_ws[fwstext[i:i+2]] += 1
			count_ws += 1

def fr_bigr_():
	for item, value in qa_bigr.items():
		fr_bigr[item] = value/count

def fr_bigr_ws_():
	for item, value in qa_bigr_ws.items():
		fr_bigr_ws[item] = value/count_ws

def entr_():
	for value_inner in fr_bigr.values():
		global entr
		entr += value_inner * log2(1 / value_inner)
def entr_ws_():
	for value_inner in fr_bigr_ws.values():
		global entr_ws
		entr_ws += value_inner * log2(1 / value_inner)


count_each_bigr()
count_each_bigr_ws()
fr_bigr_()
fr_bigr_ws_()
entr_()
entr_ws_()
entr = entr/2
entr_ws = entr_ws/2

results.write('\n\n\nBIGRAMS(STEP - ' + str(step) + '), their frequencies, entropy, redundancy for text with space:\n')
results.write('Table of frequencies:\n')
temp = list(qa_bigr.keys())
temp.sort()
for key in temp:
    results.write("{:^4}{:^.5f}\n".format(key, fr_bigr[key]))
red = redundancy()
results.write('\nEntropy:  '+ str(entr) + '\n')
results.write('Redundancy:  '+ str(red) + '\n')

results.write('\n\n\nBIGRAMS(STEP - ' + str(step) + '), their frequencies, entropy, redundancy for text withOUT space:\n')
results.write('Table of frequencies:\n')
temp_ws = list(qa_bigr_ws.keys())
temp_ws.sort()
for key in temp_ws:
    results.write("{:^4}{:^.5f}\n".format(key, fr_bigr_ws[key]))
red_ws = redundancy_ws()
results.write('\nEntropy:  '+ str(entr_ws) + '\n')
results.write('Redundancy:  '+ str(red_ws) + '\n')


# закриваю всі файли
f.close()
fws.close()
results.close()
