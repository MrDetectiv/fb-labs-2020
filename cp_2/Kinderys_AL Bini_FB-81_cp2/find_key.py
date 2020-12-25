import numpy as np
import matplotlib.pyplot as plt
file = open("text.txt", "r", encoding='utf-8')
text = file.read()
temporary = np.zeros(len(text))
alphabet = np.array(['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                     'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'])
for i in range(len(alphabet)):  # iterating per alphabet
    for j in range(len(text)):  # iteration through the whole text
        if text[j] == alphabet[i]:  # checking for matching
            temporary[j] = i  # saving letter code

I_val = np.zeros(31)  # масив що матиме індеуси для можливих довжин ключа 2-30
D_val = np.zeros(31, dtype=int)
for r in range(2, len(I_val)):  # цикл у якому рахуватиметься цей індекс для кожної довжини
    I_of_Y = np.zeros(r)  # масив що зберігатиме індеси дляблоків на які розбит текст
    # D_of_Y = np.zeros(r, dtype=int)
    temp_rarity = np.zeros((r, len(alphabet)), dtype=int)  # матриця у строках якої будуть частоти для кожного блока
    for t in range(r):  # цикл для блоків
        for k in range(t, len(temporary), r):  # цикл що рухатиметься в одному й тому ж блоці
            tmp = int(temporary[k])  # зчитуємо букву
            temp_rarity[t][tmp] = temp_rarity[t][tmp] + 1  # додаємо кількість її появи
        for l in range(t, len(temporary) - r, r):
            if temporary[l] == temporary[l + r]:
                D_val[r] += 1
        I_of_Y[t] = np.dot(temp_rarity[t], temp_rarity[t] - 1) / (sum(temp_rarity[t]) * (sum(temp_rarity[t]) - 1))  # рахуємо індекс блока
    I_val[r] = sum(I_of_Y)/len(I_of_Y)  # знаходимо середнє значення індексу для певної довжини ключа
R = np.argmax(I_val)
print(D_val)
lengths = np.arange(2, 31, 1, dtype=int)
I_of_r = I_val[2:]
D_of_r = D_val[2:]
print("Key length is ", R)
plt.figure(figsize=(9, 3))
plt.subplot(111)
plt.bar(lengths, I_of_r)
plt.suptitle('Індекс відповідності для ключів довжиною 2-30')
"""plt.subplot(111)
plt.bar(lengths, D_of_r)
plt.suptitle('Статистика співпадання (Dr) для ключів довжиною 2-30')"""
plt.show()
most_common_letter = 14  # код буквы о
key = np.zeros(R, dtype=int)  # масив для сдвигов
for a in range(R):  # цикл по всем блокам 0, 1, 2 ... 11
    block_rarity = np.zeros(len(alphabet), dtype=int)  # масив с количеством появления каждой буквы
    most_common_in_block = 0  # переменная в которой будет кранится код (индекс) самой встречаемой буквы блока
    for b in range(a, len(temporary), R):  # цикл с шагом 12 (длину ключа) и сдвигом на i для i-го блока
        tmp2 = int(temporary[b])  # получаю с текста код буквы
        block_rarity[tmp2] += 1  # увеличиваю количество появления данной буквы
    most_common_in_block = np.argmax(block_rarity)
    key[a] = most_common_in_block - most_common_letter  # считаю ключ блока
print("key is: ", alphabet[key])  # вывод ключа
file.close()
