import math
#symbol enthropy  without space
f = open('text.txt','r',encoding = 'utf-8')
mytext = f.read().replace('-','').replace('?','').replace('"','').replace(' ', '').replace('\n', '').lower().replace('!','').replace('(','').replace(')','').replace('.','').replace(',','').replace(':','').replace(';','')
f.close()
lenght = len(mytext)
frequency_dictionary = { }   #dictionary of symbols(=keys) and their counts
for symbol in mytext:
    count = frequency_dictionary.get(symbol,0)
    frequency_dictionary[symbol] = count + 1
    
frequency_symbols = frequency_dictionary.keys() #symbols(=keys), набор ключей словаря
enthropy = 0

output1=open("results.txt", "a")

for symbols in frequency_symbols:
    print (symbols, frequency_dictionary[symbols]/lenght)
    enthropy -= (frequency_dictionary[symbols]/lenght)*math.log(frequency_dictionary[symbols]/lenght,2)
output1.write('monogram enthropy without spaces ')
output1.write(str(enthropy))
output1.write('\n---------------------------------------------\n')
output1.close()


#symbol enthropy  with space
f2 = open('text.txt','r',encoding = 'utf-8')
mytext2 = f2.read().replace('-','').replace('?','').replace('"','').replace('\n', '').lower().replace('!','').replace('(','').replace(')','').replace('.','').replace(',','').replace(':','').replace(';','')
f2.close()
lenght2 = len(mytext2)

frequency_dictionary2 = { }
for symbol in mytext2:
    count2 = frequency_dictionary2.get(symbol,0)
    frequency_dictionary2[symbol] = count2 + 1

output2=open("results.txt", "a")
       
frequency_symbols2 = frequency_dictionary2.keys()
enthropy2 = 0
for symbols in frequency_symbols2:
    print (symbols, frequency_dictionary2[symbols]/lenght2)
    enthropy2 -= (frequency_dictionary2[symbols]/lenght2)*math.log(frequency_dictionary2[symbols]/lenght2,2)
output2.write('monogram enthropy with spaces ')
output2.write(str(enthropy2))
output2.write('\n---------------------------------------------\n')
output2.close()
