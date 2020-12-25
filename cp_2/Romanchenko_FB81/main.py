import matplotlib.pyplot as plot
from collections import Counter


def codable_things_of(alphabet):
    # returns two dictionaries that converts char->int, int->char and amount of letters in alphabet
    alphabet_length = len(alphabet)
    letter_index = {alphabet[key_id]: key_id for key_id in range(alphabet_length)}
    index_letter = {key_id: alphabet[key_id] for key_id in range(alphabet_length)}
    return letter_index, index_letter, alphabet_length


def encode_with_keys(l_text, alphabet):
    encoding_keys = ["ад", "рай", "ключ", "жесть", "оченьбольшоеслово"]
    encoded_texts = []
    for encoding_key in encoding_keys:
        encoded_text = encode(list(l_text), list(encoding_key), alphabet)
        encoded_texts.append(encoded_text)
    return encoded_texts, encoding_keys


def encode(l_text, l_key, alphabet):
    letter_index, index_letter, alphabet_length = codable_things_of(alphabet)
    key_len = len(l_key)
    for i in range(len(l_text)):
        l_text[i] = index_letter[(letter_index[l_text[i]] + letter_index[l_key[i % key_len]]) % alphabet_length]
    return "".join(l_text)


def decode(l_text, l_key, alphabet):
    letter_index, index_letter, alphabet_length = codable_things_of(alphabet)
    key_len = len(l_key)
    for i in range(len(l_text)):
        l_text[i] = index_letter[(letter_index[l_text[i]] - letter_index[l_key[i % key_len]]) % alphabet_length]
    return "".join(l_text)


def conformity_index(text):
    letter_amount = len(text)
    letter_and_amount = Counter(text)
    letter_and_amount = list(sorted(letter_and_amount.items(), key=lambda t: t[0]))
    i_c = 0
    for pair in letter_and_amount:
        #            certain_letter_amount * (certain_letter_amount - 1)
        # i_c =  ∑   --------------------------------------------------
        #              total_letter_amount * (total_letter_amount - 1)
        i_c += (pair[1] * (pair[1] - 1)) / (letter_amount * (letter_amount - 1))
    return i_c


def draw_plot(key_lengths, i_cs):
    for key_length in range(len(key_lengths)):
        plot.bar(key_lengths[key_length], i_cs[key_length], width=0.8, bottom=None, align="center", data=None)

    plot.grid(which="major", color="r", linestyle="--", linewidth=0.1)
    plot.xlabel("Key length")
    plot.ylabel("Index of coincidence")
    plot.show()


def detect_possible_key_length(text, standart):
    candidates = []
    key_lengths = []
    i_cs = []
    for delta in range(2, 30):
        i_c = 0
        for j in range(0, delta):
            splited_text = ""
            for i in range(j, len(text), delta):
                splited_text += text[i]
            i_c += conformity_index(splited_text)
        i_c /= delta
        if standart - 0.005 < i_c < standart + 0.005:
            candidates.append((delta, i_c))
        i_cs.append(i_c)
        key_lengths.append(delta)
        print(f"Key {delta}, index of coincidence {i_c}")
    # draw_plot(key_lengths, i_cs)
    return candidates


def find_key(text, possible_variants, alphabet):
    letter_index, index_letter, alphabet_length = codable_things_of(alphabet)
    possible_keys = []
    theoretical_common_letters = ["о", "е", "а", "и"]
    for possible_variant in possible_variants:
        key_length = possible_variant[0]

        possible_key_list = []

        for cases in range(len(theoretical_common_letters)):
            possible_key_list.append("")

        for j in range(0, key_length):
            splited_text = ""
            for i in range(j, len(text), key_length):
                splited_text += text[i]

            most_common_letter = Counter(splited_text).most_common(1)[0][0]
            for i in range(len(theoretical_common_letters)):
                key_letter = index_letter[(letter_index[most_common_letter] - letter_index[theoretical_common_letters[i]] + len(alphabet)) % len(alphabet)]
                possible_key_list[i] += key_letter

        possible_keys.append(possible_key_list)
    print("Possible keys:")
    for same_key_length_variants in possible_keys:
        for key in same_key_length_variants:
            print(key)


russ_alphabet = list("абвгдежзийклмнопрстуфхцчшщъыьэюя")

file = open("mytext.txt", "r", encoding="UTF-8")
text = file.read().lower()

print(f"\nPlain text (text conformity index {conformity_index(text)})")
print(str(text) + "\n")
encoded, keys = encode_with_keys(text, russ_alphabet)
for index in range(len(encoded)):
    i_c = conformity_index(encoded[index])
    print(f"Encoding text with {len(keys[index])} length key {keys[index]}" +
          f" (text conformity index {i_c}): \n{encoded[index]}\n")


file = open("text.txt", "r", encoding="UTF-8")
text = file.read().lower()
print(f"\nEncoded text (text conformity index {conformity_index(text)})")
print("\n" + text + "\n")

possible_variants = detect_possible_key_length(text, 0.055)
print("\nCandidates: \n" + str(possible_variants) + "\n")

find_key(text, possible_variants, russ_alphabet)

print()
key = "абсолютныйигрок"
print(key)
decoded = decode(list(text), list(key), russ_alphabet)
print(decoded)

