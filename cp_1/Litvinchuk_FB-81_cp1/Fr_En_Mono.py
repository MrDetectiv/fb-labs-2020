from math import log2

#відкриваю два файли, обива на читання
ftext = open('ftext(utf8).txt','r',encoding='utf8')
fwstext = open('fwstext(utf8).txt','r',encoding='utf8')
results = open('results.txt','a',encoding='utf8')

qa_letters = {'а':0, 'б':0, 'в':0, 'г':0, 'д':0, 'е':0, 'ж':0, 'з':0,
              'и':0, 'й':0, 'к':0, 'л':0, 'м':0, 'н':0, 'о':0, 'п':0,
              'р':0, 'с':0, 'т':0, 'у':0, 'ф':0, 'х':0, 'ц':0, 'ч':0, 
              'ш':0, 'щ':0, 'ы':0, 'ь':0, 'э':0, 'ю':0, 'я':0, ' ':0} 
qa_letters_ws = {'а':0, 'б':0, 'в':0, 'г':0, 'д':0, 'е':0, 'ж':0, 'з':0,
                 'и':0, 'й':0, 'к':0, 'л':0, 'м':0, 'н':0, 'о':0, 'п':0,
                 'р':0, 'с':0, 'т':0, 'у':0, 'ф':0, 'х':0, 'ц':0, 'ч':0, 
                 'ш':0, 'щ':0, 'ы':0, 'ь':0, 'э':0, 'ю':0, 'я':0} 

count = 0
count_ws = 0
entr = 0
entr_ws = 0
fr_letters = {} # з пробілами
fr_letters_ws = {} # без пробілів

# надлишковість з пробілами
def redundancy():
	return 1 - (entr/log2(32))
# надлишковість без пробілів
def redundancy_ws():
	return 1 - (entr_ws/log2(31))

# скільки разів кожна літера зустрічається в тексті(з ппробілами)
def count_each_letter():
	for line in ftext:
		for symbol in line:
			global count
			count += 1
			qa_letters[symbol] += 1
# скільки разів кожна літера зустрічається в тексті(без пробілів)
def count_each_letter_ws():
	for line in fwstext:
		for symbol in line:
			global count_ws
			count_ws += 1
			qa_letters_ws[symbol] += 1

# частота літер з пробілами
def fr_letters_():
    for item, value in qa_letters.items():
        fr_letters[item] = value/count
# частота літер без пробілів
def fr_letters_ws_():
    for item, value in qa_letters_ws.items():
        fr_letters_ws[item] = value/count_ws

# обчислення ентропії для тексту з пробілами
def entr_():
    for value_inner in fr_letters.values():
        global entr
        entr = entr + value_inner * log2(1 / value_inner)
# обчислення ентропії для тексту без пробілів
def entr_ws_():
    for value_inner in fr_letters_ws.values():
        global entr_ws
        entr_ws = entr_ws + value_inner * log2(1 / value_inner)


# в наступних рядках почергово викликаю функції та записую резуьтат до 'results.txt'
count_each_letter()
count_each_letter_ws()
fr_letters_()
fr_letters_ws_()
entr_()
entr_ws_()

results.write('\n\n\nMONOGRAMS, their frequencies, entropy, redundancy for text with space:\n')
results.write('Table of frequencies:\n')
temp = list(qa_letters.keys())
temp.sort()
for key in temp:
    results.write("{:^4}{:^.5f}\n".format(key, fr_letters[key]))
red = redundancy()
results.write('\nEntropy:  '+ str(entr) + '\n')
results.write('Redundancy:  '+ str(red) + '\n')

results.write('\n\n\nMONOGRAMS, their frequencies, entropy, redundancy for text withOUT space:\n')
results.write('Table of frequencies:\n')
temp_ws = list(qa_letters_ws.keys())
temp_ws.sort()
for key in temp_ws:
    results.write("{:^4}{:^.5f}\n".format(key, fr_letters_ws[key]))
red_ws = redundancy_ws()
results.write('\nEntropy:  '+ str(entr_ws) + '\n')
results.write('Redundancy:  '+ str(red_ws) + '\n')

# закриваю всі файли
ftext.close()
fwstext.close()
results.close()
