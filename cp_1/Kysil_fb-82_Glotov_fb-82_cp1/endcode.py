import codecs, re, math
from collections import Counter

alphabet1 = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
             'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']
alphabet2 = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
             'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я', ' ']
#cleaner
with open('arka.txt','r') as with_spaces:
    t_with = with_spaces.read().lower()
    t_with = t_with.replace('ъ', 'ь').replace('ё', 'е')
    t_with = re.sub('[^а-я ]','', t_with).strip()
    #open('withspaces','w').write(text)

with open('arka.txt', 'r') as without_spaces:
    t_without = without_spaces.read().lower()
    t_without = t_without.replace('ъ', 'ь').replace('ё', 'е')
    t_without = re.sub('[^а-я]','',t_without)
    #open('withoutspaces','w').write(text)

def Letter_counter(text):
    count = Counter(text)
    return count;


print('MONOGRAMM WITHOUT SPACE')

lenth_without = len(t_without)
count_without = Letter_counter(t_without)

keys_1 = list(count_without.keys())
keys_1.sort()
val_1 = []
for i in keys_1:
    for key in count_without:
        if i == key:
            val_1.insert(keys_1.index(i), (count_without[key]))
dic_1 = dict(zip(keys_1,val_1))
for p in dic_1:
    dic_1[p] = dic_1[p] / lenth_without

ent_1 = 0
for key in dic_1:
    ent_1 += -dic_1[key] * math.log2(dic_1[key])   # ентропия монограма без пробела
print(ent_1)
ex_1_mono = 1 - ((ent_1) / math.log2(31))
print(ex_1_mono)


print('MONOGRAMM WITH SPACE')

lenth_with = len(t_with)
count_with = Letter_counter(t_with)

keys_2 = list(count_with.keys())
keys_2.sort()
val_2 = []
for i in keys_2:
    for key in count_with:
        if i == key:
            val_2.insert(keys_2.index(i), (count_with[key]))
dic_2 = dict(zip(keys_2,val_2))
for p in dic_2:
    dic_2[p] = dic_2[p] / lenth_with

ent_2 = 0
for key in dic_2:
    ent_2 += -dic_2[key] * math.log2(dic_2[key])   # ентропия монограма без пробела
print(ent_2)
ex_2_mono = 1 - ((ent_2) / math.log2(32))
print(ex_2_mono)

print('BIGRAMM WITHOUT SPACE:')

print('-Intersect') #перетин
length2_without = len(t_without) - 1
couples_1 = []
for item in range(length2_without):
    couples_1.append(t_without[item:item + 2])
a_1_without = Letter_counter(couples_1)
sum_1_without = sum(a_1_without.values())

n = m = len(alphabet1) +1
arr_1 = [0] * n
for i in range(n):
    arr_1[i] = [0] * m
for j in range(1, len(arr_1[0])):
    arr_1[0][j] = alphabet1[j - 1]
for i in range(1, len(arr_1)):
    arr_1[i][0] = alphabet1[i - 1]
for i in range(len(arr_1)):
    for j in range(len(arr_1[i])):
        for key in a_1_without:
            st = str(arr_1[i][0]) + str(arr_1[0][j])
            if st == key:
                arr_1[i][j] = a_1_without[key] / sum_1_without

ent_couple_without_1 = 0
item_1 = 0
for i in range(1, len(arr_1)):
    for j in range(1, len(arr_1[i])):
        item_1 = arr_1[i][j]
        if item_1 == 0:
            ent_couple_without_1 += 0
        else:
            ent_couple_without_1 += -(item_1) * math.log2((item_1))

ent_couple_without_1 = ent_couple_without_1 / 2

ex_1_couple = 1 - ((ent_couple_without_1) / math.log2(31))
print('H2=',ent_couple_without_1)
print('R=',ex_1_couple)


print('-No intersect') #не перетин

length2_without = len(t_without) - 1
couples_2 = []

for item in range(0, length2_without):
    couples_2.append(t_without[item:item + 2])
a_2_without = Letter_counter(couples_2)
sum_2_without = sum(a_2_without.values())
#тут закопано золото ------------------------------------
t = p = len(alphabet2) +1
arr_2 = [0] * t
for i in range(t):
    arr_2[i] = [0] * m
for j in range(1, len(arr_2[0])):
    arr_2[0][j] = alphabet2[j - 1]
for i in range(1, len(arr_2)):
    arr_2[i][0] = alphabet2[i - 1]
for i in range(len(arr_2)):
    for j in range(len(arr_2[i])):
        for key in a_2_without:
            st = str(arr_2[i][0]) + str(arr_2[0][j])
            if st == key:
                arr_2[i][j] = a_2_without[key] / sum_2_without


ent_couple_without_2 = 0
item_2 = 0
for i in range(1, len(arr_2)):
    for j in range(1, len(arr_2[i])):
        item_2 = arr_2[i][j]
        if item_2 == 0:
            ent_couple_without_2 += 0
        else:
            ent_couple_without_2 += -(item_2) * math.log2((item_2))

ent_couple_without_2 = ent_couple_without_2 / 2

ex_2_couple = 1 - ((ent_couple_without_2) / math.log2(31))
print('H2=',ent_couple_without_2)
print('R=',ex_2_couple)


print('BIGRAMM WITH SPACE:')

print('-Intersect') #перетин
length2_with = len(t_with) - 1
couples_3 = []
for item in range(length2_with):
    couples_3.append(t_with[item:item + 2])
a_1_with = Letter_counter(couples_3)
sum_1_with = sum(a_1_with.values())

n = m = len(alphabet2) +1
arr_3 = [0] * n
for i in range(n):
    arr_3[i] = [0] * m
for j in range(1, len(arr_3[0])):
    arr_3[0][j] = alphabet2[j - 1]
for i in range(1, len(arr_2)):
    arr_3[i][0] = alphabet2[i - 1]
for i in range(len(arr_3)):
    for j in range(len(arr_3[i])):
        for key in a_1_with:
            st = str(arr_3[i][0]) + str(arr_3[0][j])
            if st == key:
                arr_3[i][j] = a_1_with[key] / sum_1_with

ent_couple_with_1 = 0
item_3 = 0
for i in range(1, len(arr_3)):
    for j in range(1, len(arr_3[i])):
        item_3 = arr_3[i][j]
        if item_3 == 0:
            ent_couple_with_1 += 0
        else:
            ent_couple_with_1 += -(item_3) * math.log2((item_3))

ent_couple_with_1 = ent_couple_with_1 / 2

ex_3_couple = 1 - ((ent_couple_with_1) / math.log2(31))
print('H2=',ent_couple_with_1)
print('R=',ex_3_couple)


print('-No intersect') #не перетин

length2_with = len(t_with) - 1
couples_4 = []
for item in range(length2_with):
    couples_4.append(t_with[item:item + 2])
a_2_with = Letter_counter(couples_4)
sum_2_with = sum(a_2_with.values())
#тут закопано золото =============================
t = p = len(alphabet2) +1
arr_4 = [0] * t
for i in range(t):
    arr_4[i] = [0] * m
for j in range(1, len(arr_4[0])):
    arr_4[0][j] = alphabet2[j - 1]
for i in range(1, len(arr_4)):
    arr_4[i][0] = alphabet2[i - 1]
for i in range(len(arr_4)):
    for j in range(len(arr_4[i])):
        for key in a_2_with:
            st = str(arr_4[i][0]) + str(arr_4[0][j])
            if st == key:
                arr_4[i][j] = a_2_with[key] / sum_2_with


ent_couple_with_2 = 0
item_4 = 0
for i in range(1, len(arr_4)):
    for j in range(1, len(arr_4[i])):
        item_4 = arr_4[i][j]
        if item_4 == 0:
            ent_couple_with_2 += 0
        else:
            ent_couple_with_2 += -(item_4) * math.log2((item_4))

ent_couple_with_2 = ent_couple_with_2 / 2

ex_4_couple = 1 - ((ent_couple_with_2) / math.log2(31))
print('H2=',ent_couple_with_2)
print('R=',ex_4_couple)



# pink
print("Pink program ent and red")
H10_min = 2.10611777618689
H10_max = 2.85173259480082
R10_min = 1-(H10_min/math.log(32,2))
R10_max = 1-(H10_max/math.log(32,2))
print("Entropy: ",H10_min ," < H(10) < ",H10_max)
print("Redundancy: " ,R10_min," < H(10) < ",R10_max)

H20_min = 1.88132459213154
H20_max = 2.68185663787509
R20_min = 1-(H20_min/math.log(32,2))
R20_max = 1-(H20_max/math.log(32,2))
print("Entropy: ",H20_min ," < H(20) < ",H20_max)
print("Redundancy: " ,R20_min," < H(20) < ",R20_max)

H30_min = 1.77203806492132
H30_max = 2.43173743342247
R30_min = 1-(H30_min/math.log(32,2))
R30_max = 1-(H30_max/math.log(32,2))
print("Entropy: ",H30_min ," < H(30) < ",H30_max)
print("Redundancy: " ,R30_min," < H(30) < ",R30_max)
