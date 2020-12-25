from collections import *


def codable_things_of(alphabet):
    alphabet_length = len(alphabet)
    letter_index = {alphabet[key]: key for key in range(alphabet_length)}
    index_letter = {key: alphabet[key] for key in range(alphabet_length)}
    return letter_index, index_letter


def gcd(first_num, second_num):
    if second_num == 0:
        return first_num
    else:
        return gcd(second_num, first_num % second_num)


def conformity_index(text):
    letter_and_amount, letter_amount = Counter(text), len(text)
    letter_and_amount = list(sorted(letter_and_amount.items(), key=lambda t: t[0]))
    i_c = 0
    for pair in letter_and_amount:
        #            certain_letter_amount * (certain_letter_amount - 1)
        # i_c =  ∑   --------------------------------------------------
        #              total_letter_amount * (total_letter_amount - 1)
        i_c += (pair[1] * (pair[1] - 1)) / (letter_amount * (letter_amount - 1))
    return i_c


def inverse(a, mod):
    for number in range(mod):
        if number * a % mod == 1:
            return number
    return 0


def solve_equation(x_c, a, mod):    # x_c * x = a mod(mod)
    a = (mod + a) % mod
    x_c = (mod + x_c) % mod

    divider = gcd(a, mod)

    answers = []
    if (x_c % divider) == 0:
        x_c_inverse = inverse(a // divider, mod // divider)
        for answer_number in range(divider):
            # print(f"x = {x_c_inverse}*{x_c // divider} + {answer_number}*{mod // divider} mod {mod}")
            x = (x_c_inverse * (x_c // divider) + answer_number * (mod // divider)) % mod
            answers.append(x)

    return answers


def bigram_to_int(bigram, letter_index, alphabet_length):
    # print(f"{bigram} -> {letter_index[bigram[0]] * alphabet_length + letter_index[bigram[1]]} ")
    return letter_index[bigram[0]] * alphabet_length + letter_index[bigram[1]]


def int_to_bigram(integer, index_letter, alphabet_length):
    # print(f"{integer} -> {index_letter[(integer - integer % alphabet_length) / alphabet_length] + index_letter[integer % alphabet_length]} ")
    return index_letter[(integer - integer % alphabet_length) / alphabet_length] + index_letter[integer % alphabet_length]


def find_keys(popular_text_bigrams, popular_lang_bigrams, alphabet):
    print(f"From lang: {popular_lang_bigrams}")
    print(f"From text: {popular_text_bigrams}" + "\n")
    alphabet_length = len(alphabet)
    letter_index, _ = codable_things_of(alphabet)
    popular_text_bigrams = list(map(lambda x: bigram_to_int(x, letter_index, alphabet_length), popular_text_bigrams))
    popular_lang_bigrams = list(map(lambda x: bigram_to_int(x, letter_index, alphabet_length), popular_lang_bigrams))
    possible_keys = []
    mod = alphabet_length ** 2
    for pop_lan_big_ind1 in range(len(popular_lang_bigrams) - 1):
        for pop_lan_big_ind2 in range(pop_lan_big_ind1 + 1, len(popular_lang_bigrams)):

            for pop_text_big_ind1 in range(len(popular_text_bigrams)):
                for pop_text_big_ind2 in range(len(popular_text_bigrams)):

                    if not pop_text_big_ind1 == pop_text_big_ind2:
                        Y1, Y2 = popular_text_bigrams[pop_text_big_ind1], popular_text_bigrams[pop_text_big_ind2]
                        X1, X2 = popular_lang_bigrams[pop_lan_big_ind1], popular_lang_bigrams[pop_lan_big_ind2]
                        a_s = solve_equation(Y1-Y2, X1-X2, mod)
                        b_s = list(map(lambda x: (((Y1 - x * X1) % mod) + mod) % mod, a_s))
                        keys = list(map(lambda k: (a_s[k], b_s[k]), range(len(a_s))))
                        for key in keys:
                            possible_keys.append(key)
                        print(f"{Y1} = a*{X1} + b mod {mod}")
                        print(f"{Y2} = a*{X2} + b mod {mod}")
                        print()
    print(f"Keys: {possible_keys}\nAmount: {len(possible_keys)}\n")
    return list(set(possible_keys))


def brute(encoded_bigramed_text, possible_keys, alphabet):
    standart = 0.055
    standart_delta = 0.005
    alphabet_length = len(alphabet)
    letter_index, index_letter = codable_things_of(alphabet)
    mod = alphabet_length ** 2
    result = []
    for key in possible_keys:
        a_inverce = inverse(key[0], mod)
        if not a_inverce == 0:
            encoded_bigramed_text_values = list(map(lambda x: bigram_to_int(x, letter_index, alphabet_length), encoded_bigramed_text))
            decoded_bigramed_text_values = list(map(lambda x: a_inverce * (x-key[1] + 1000 * mod) % mod, encoded_bigramed_text_values))
            decoded_bigramed_text = list(map(lambda x: int_to_bigram(x, index_letter, alphabet_length), decoded_bigramed_text_values))
            decoded_text = "".join(decoded_bigramed_text)
            i_c = conformity_index(decoded_text)
            if standart - standart_delta < i_c < standart + standart_delta:
                result.append((key, i_c, decoded_text))
    return result

def hacking(encoded_text, alphabet):
    print(f"{alphabet}\n")
    # 2 means divide by non-crossed bigrams
    bigrammed_text = [encoded_text[i:i + 2] for i in range(0, len(encoded_text), 2)]
    top_five_lang_bigrams = ["ст", "но", "то", "на", "ен"][:3]
    top_five_text_bigrams = list(map(lambda x: x[0], Counter(bigrammed_text).most_common(5)))[:3]

    possible_keys = find_keys(top_five_text_bigrams, top_five_lang_bigrams, alphabet)

    decoded_text = brute(bigrammed_text, possible_keys, alphabet)
    return decoded_text


rus_alphabet = "абвгдежзийклмнопрстуфхцчшщьыэюя"

file = open("17.txt", "r", encoding="UTF-8")
text = file.read().lower().replace("\n", "").replace(" ", "")
decoded_variants = hacking(text, rus_alphabet)

for triplet in decoded_variants:
    print(f"Key: {triplet[0]}\nConformity index: {triplet[1]}\nDecoded: {triplet[2]}")

print(solve_equation(11, 22, 33))
