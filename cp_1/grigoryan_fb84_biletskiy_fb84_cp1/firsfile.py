import re
import math

alphabet = (
'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
'ч', 'ш', 'щ', 'ь', 'ы', 'э', 'ю', 'я', ' ')

sumletters = 0
sum = 0



result_file = open("filteredtext.txt", 'r', encoding='utf-8')
for i in result_file:
    for j in i:
        if j in alphabet:
            sumletters += 1

for i in alphabet:
    result_file = open("filteredtext.txt", 'r', encoding='utf-8')
    print(i, result_file.read().count(i) / sumletters)
    p = result_file.read().count(i)/sumletters
    sum += p
    if p > 0 and p < 1:
        formula = (-sum) * math.log2(p)
        print(round(formula))
