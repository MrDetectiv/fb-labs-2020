import numpy as np

key = "матан"
R = len(key)
encoded_key = np.zeros(R, dtype=int)
print(key[0])
alphabet = np.array(['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                     'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'])
file = open('small_text.txt', "r", encoding="utf-8")
small_text = file.read()
temporary = np.zeros(len(small_text), dtype=int)
for i in range(len(alphabet)):  # iterating per alphabet
    for j in range(len(small_text)):  # iteration through the whole text
        if small_text[j] == alphabet[i]:  # checking for matching
            temporary[j] = i  # saving letter code
    for k in range(R):
        if key[k] == alphabet[i]:
            encoded_key[k] = i
for i in range(R):
    for j in range(i, len(temporary), R):
        temporary[j] = (temporary[j] + encoded_key[i]) % len(alphabet)
cipher_text = alphabet[temporary]
output = open("cipher_text_ r=5.txt", "w", encoding='utf-8')
for i in range(len(cipher_text)):
    output.write(cipher_text[i])
output.write("\n\n key is ")
output.write(key)
file.close()
