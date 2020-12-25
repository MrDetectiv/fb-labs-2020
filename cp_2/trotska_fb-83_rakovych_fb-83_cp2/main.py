from collections import Counter

alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_length = len(alphabet)

letter_to_number = {k: v for v, k in enumerate(alphabet[:])}
number_to_letter = {v: k for v, k in enumerate(alphabet[:])}


def ciphering(text, cipher_key, key_len):
    ciphered = ''
    index = 0
    text = text.upper()
    for i in text:
        if i == ' ':
            continue
        c = (letter_to_number[i] + letter_to_number[cipher_key[index % key_len].upper()]) % alphabet_length
        ciphered += number_to_letter[c]
        index += 1
    return ciphered


def deciphering(ciphered, cipher_key, key_len):
    deciphered = ''
    index = 0
    ciphered = ciphered.upper()
    for i in ciphered:
        if i == ' ':
            continue
        c = (alphabet_length + letter_to_number[i] - letter_to_number[
            cipher_key[index % key_len].upper()]) % alphabet_length
        deciphered += number_to_letter[c]
        index += 1
    return deciphered


def count_frequency(text):
    frequency = {}
    text = text.replace(' ', '').upper()
    counts = Counter(text)
    for i in counts:
        frequency[i] = counts[i]
    return frequency


def count_index(text):
    text = text.replace(' ', '')
    length = len(text)
    if length == 1:
        result = 1 / ((length) * length)
    else:
        result = 1 / ((length - 1) * length)

    freq = count_frequency(text)
    sum = 0
    for letter in freq:
        sum += freq[letter] * (freq[letter] - 1)
    return result * sum


def split_blocks(nonsplited, n):
    return [nonsplited[i:i + n] for i in range(0, len(nonsplited), n)]


def find_key_len(ciphered):
    for i in range(2, 31):
        splitted = split_blocks(ciphered, i)
        temp_str = ""
        for n in splitted:
            temp_str = temp_str + n[0]
        sum_of_blocks = count_index(temp_str)
        print("i = ", i, "index = ", sum_of_blocks)


def most_freq_letter(frequency):
    max_val = max(frequency.values())

    return get_key(frequency, max_val)


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def crack_the_key(ciphered_text, key_len):
    key_list = split_blocks(ciphered_text, key_len)
    popular = "ОЕАИНТ"
    for letter in popular:
        result = ""
        for i in range(0, key_len):
            temp_str = ""
            for n in key_list:
                if len(n) > i:
                    temp_str = temp_str + n[i]
            y = most_freq_letter(count_frequency(temp_str))

            key = (letter_to_number[y] - letter_to_number[letter]) % alphabet_length
            result = result + number_to_letter[key]
        print("С буквой ", letter, " = ", result)


f = open('text.txt', encoding="utf8")
text = f.read().replace('\n', '')

key = input('Enter the key: ')
r = len(key)

ciphered_text = ciphering(text, key, r)
print(ciphered_text)
deciphered_text = deciphering(ciphered_text, key, r)
print(deciphered_text)
print("----------------Открытый текст-------------------")
print(count_index(text))
print("-----------------------------------")
print(count_index(ciphered_text))

# task 3
print("----------------Task 3-------------------")
f = open('ciphered_text.txt', encoding="utf8")
ciphered_text_17 = f.read().replace('\n', '')
find_key_len(ciphered_text_17)
crack_the_key(ciphered_text_17, 15)
print(deciphering(ciphered_text_17, "АБСОЛЮТНЫЙИГРОК", 15))
