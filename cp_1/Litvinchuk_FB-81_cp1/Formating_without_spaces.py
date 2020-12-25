#відкриваю два файли, перший на читання, другий на запис
ftext = open('ftext(utf8).txt','r',encoding='utf8')
fwstext = open('fwstext(utf8).txt','w',encoding='utf8')

#створюю проміжний рядок
temp = ''

# в кожному рядку замініюю пробіли на ''
for line in ftext:
	newline = line.replace(' ','')
	temp += newline

fwstext.write(temp)

#закриваю файли
ftext.close()
fwstext.close()