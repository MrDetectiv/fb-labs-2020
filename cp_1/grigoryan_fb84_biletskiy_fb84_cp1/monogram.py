import re
import math

alphabet = (
'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
'ч', 'ш', 'щ', 'ь', 'ы', 'э', 'ю', 'я', ' ')

sumletters = 0
sum = 0
formula = 0


result_file = open("filteredtext.txt", 'r', encoding='utf-8')
for i in result_file:
    for j in i:
        if j in alphabet:
            sumletters += 1


from collections import Counter


for i in alphabet:
    result_file = open("filteredtext.txt", 'r', encoding='utf-8')
    n = result_file.read().count(i) / sumletters
    if n > 0 and n<1:
        print(i,n)
        formula += ((-n) * math.log2(n))

print("Entropy:",round(formula, 4))

print("Izbytochnost':" + str(round((1 - (formula)/math.log(31,2)),5)))

