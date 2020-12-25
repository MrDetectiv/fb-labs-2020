#імпортую модуль для роботи з регулярними виразами
import re

#відкриваю два файли, перший на читання, другий на запис
text = open('text(utf8).txt','r',encoding='utf8')
ftext = open('ftext(utf8).txt','w',encoding='utf8')

#створюю проміжний рядок
temp = ''

for line in text:
	i=0
	# на цьому кроці я замінюю будь-які символи що НЕ є російськими буквами на пробіли
	newline = re.sub(r"[^а-яА-ЯёЁ]+"," ",line)
	newline = newline.lower()
	# виконую заміну символів ё на е, ъ на ь
	for symbol in newline:
		if symbol == "ё":
			newline = newline[:i]+'е'+newline[i+1:]
		elif symbol == "ъ":
			newline = newline[:i]+'ь'+newline[i+1:]
		i+=1
	# видаляю лишні пробіли: методом split() розділяю слова, таким чином ствоючи list
	# методом join() об'єдную всі елементи списку, розділяючи їх пробілами
	newline = ' '.join(newline.split())
	# якщо newline не пустий рядок, то додаю до temp + ' '
	# якщо newline пустий, то не роблю нічого, так як може добавитись лишній пробіл
	if len(newline)!=0:
		temp += newline + ' '
ftext.write(temp)

#закриваю файли
text.close()
ftext.close()