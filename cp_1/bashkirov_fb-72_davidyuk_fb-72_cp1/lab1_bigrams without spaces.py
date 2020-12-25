import re
import math
frequency = {}
f = open('text.txt', 'r',encoding = 'utf-8')
mytext = f.read().replace('?','').replace(' ','').replace('"','').replace('\n', '').lower().replace('!','').replace('(','').replace(')','').replace('.','').replace(',','').replace(':','').replace(';','')
f.close()
match_pattern = re.findall('\w\w', mytext)
 
for bigram in match_pattern:
    count = frequency.get(bigram,0)
    frequency[bigram] = count + 1

output2=open("results.txt", "a")    
     
frequency_list = frequency.keys()
lenght = len(mytext)
enthropy = 0
for bigrams in frequency_list:
    print (bigrams, frequency[bigrams]/lenght)
    enthropy -= (frequency[bigrams]/lenght)*math.log(frequency[bigrams]/lenght,2)
output2.write('bigrams without spaces ')
output2.write(str(enthropy))
output2.write('\n---------------------------------------------\n')
output2.close()




















