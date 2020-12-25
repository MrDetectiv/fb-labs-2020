import numpy as np
key = np.array([2, 24, 5, 10, 17, 15, 8, 16, 1, 19, 16, 31], dtype=int)
R = len(key)
file = open("text.txt", "r", encoding='utf-8')
text = file.read()
y = np.zeros(len(text), dtype=int)
alphabet = np.array(['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                     'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'])
for i in range(len(alphabet)):  # iterating per alphabet
    for j in range(len(text)):  # iteration through the whole text
        if text[j] == alphabet[i]:  # checking for matching
            y[j] = i  # saving letter code
for i in range(R):
    for j in range(i, len(y), R):
        y[j] = (y[j] - key[i]) % len(alphabet)
open_text = alphabet[y]
output = open("open_text.txt", "w", encoding='utf-8')
for i in range(len(open_text)):
    output.write(open_text[i])
file.close()
