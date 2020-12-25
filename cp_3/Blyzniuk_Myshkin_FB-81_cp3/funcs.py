import math
import re
from collections import Counter, OrderedDict


def bigram(spaceless_file):
    bigrams = re.findall(r'..?', spaceless_file)

    grams = Counter(bigrams)  # Count the frequency of each pair of letters in the text
    grams_amount = len(bigrams)  # Return amount of pair of the letters

    frequency_dict = {}  # Create empty dict for letter frequency

    for element in grams:
        frequency_dict[element] = grams[element] / grams_amount  # Count frequency for each element

    entropy = 0  # Define starting value of entropy

    for element in frequency_dict:
        ent = frequency_dict[element] * math.log(frequency_dict[element], 2)  # Count entropy for each element
        entropy -= ent  # Count overall entropy

    entropy = entropy / 2

    return frequency_dict, bigrams


def russian_alphabet(exeptions):
    alp = list(map(lambda letter: ord(letter), exeptions))
    alphabet = list(map(lambda letter: chr(letter), [ind for ind in range(1072, 1104) if ind not in alp]))
    if not ("ы" in exeptions or "ь" in exeptions):
        index1 = alphabet.index("ы")
        index2 = alphabet.index("ь")
        alphabet[index1] = "ь"
        alphabet[index2] = "ы"
    return alphabet


def index_alphabet(alphabet):
    return {key: v for v, key in enumerate(alphabet)}


def gcd(first_number, second_number):
    coefs = []
    # print("gcd of " + str(first_number) + " and " + str(second_number), end=" is ")
    while second_number != 0:
        t = second_number
        if first_number > second_number:
            coefs.append(math.floor(first_number / second_number))
        second_number = first_number % second_number
        first_number = t
    # print(first_number)
    return first_number, coefs


def find_a_key(X, Y, mod):
    X = X % mod  # make sure no number in owr equation
    Y = Y % mod  # is not higher then our mod

    divider, _ = gcd(X, mod)
    answers = []
    if divider == 1:
        a_opp = find_opposite(X, mod)
        # print("x = " + str(a_opp) + "*" + str(Y) + "mod" + str(mod))
        x = (a_opp * Y) % mod
        answers.append(x)
    elif divider > 1:
        if (Y % divider) == 0:
            a_opp = find_opposite(math.floor(X / divider), math.floor(mod / divider))
            for answer in range(0, (divider)):
                # print("x = " + str(a_opp) + "*" + str(Y/divider) + " + " + str(answer) + "*" + str(mod/divider) + " " + "mod" + str(mod))
                x = ((a_opp * math.floor(Y / divider)) + (answer * math.floor(mod / divider))) % mod
                answers.append(x)
        else:
            amount_of_answers = 0
    #print("x = " + str(answers))
    return answers


def find_opposite(a, mod):
    _, coefs = gcd(a, mod)
    # print("coefs: " + str(coefs))
    x = 1
    y = 0
    t = 0
    for index in range(0, (len(coefs) - 1)):
        t = x
        x = x * -(coefs[index]) + y
        y = t
    if x < 0:
        x = x + mod
    # print("opposite is: " + str(x))
    return x


def bigram_indexer(bigrams, indexed_alphabet_dict):
    indexed_bigrams = list(map(lambda bgm: indexed_alphabet_dict[bgm[0]] * 31 + indexed_alphabet_dict[bgm[1]], bigrams))
    reference_bigrams = dict(zip(indexed_bigrams, bigrams))
    return indexed_bigrams, reference_bigrams




def param_counter(stat_frequency, enc_bigram_frequency):
    # print(stat_frequency)
    # print(enc_bigram_frequency)
    possible_keys_list = []
    for stat_frequency_index1 in range(0, len(stat_frequency)-1):
        for enc_frequency_index1 in range(0, len(enc_bigram_frequency)):
            for stat_frequency_index2 in range(stat_frequency_index1+1, len(stat_frequency)):
                for enc_frequency_index2 in range(0, len(enc_bigram_frequency)):
                    if enc_frequency_index2 == enc_frequency_index1:
                        continue
                    # print(str(enc_bigram_frequency[enc_frequency_index1]) + " = a * " + str(stat_frequency[stat_frequency_index1]) + " + b")
                    # print(str(enc_bigram_frequency[enc_frequency_index2]) + " = a * " + str(stat_frequency[stat_frequency_index2]) + " + b")
                    # print(str(enc_bigram_frequency[enc_frequency_index1]) + " - " + str(enc_bigram_frequency[enc_frequency_index2]) + " = (" + str(stat_frequency[stat_frequency_index1]) + " - " + str(stat_frequency[stat_frequency_index2]) + ") * a")
                    b = enc_bigram_frequency[enc_frequency_index1] - enc_bigram_frequency[enc_frequency_index2]
                    a = stat_frequency[stat_frequency_index1] - stat_frequency[stat_frequency_index2]
                    # print(str(b) + " mod 31^2 = " + str(a) + " * a ")
                    # print(str(b) + " * " + str(a) + "^(-1) mod 31^2 = a ")

                    res = find_a_key(a, b, 31**2)

                    # print(res)
                    for sub_resa in res:
                        # print((enc_bigram_frequency[enc_frequency_index1] - (sub_resa * stat_frequency[stat_frequency_index1] % 961) + 961) % 961)
                        sub_resb = (enc_bigram_frequency[enc_frequency_index1] - (sub_resa * stat_frequency[stat_frequency_index1] % 961) + 961) % 961
                        key = (sub_resa, sub_resb)
                        possible_keys_list.append(key)
    return possible_keys_list


def removeDuplicates(lst):
    return [t for t in (set(tuple(i) for i in lst))]

def bigramDetecter(bigram_value, indexed_russian_alphabet):
    second_letter_value = bigram_value % len(indexed_russian_alphabet)
    first_letter_value = math.floor((bigram_value - second_letter_value) / 31)

    key_list = list(indexed_russian_alphabet.keys())
    val_list = list(indexed_russian_alphabet.values())

    key_list[val_list.index(first_letter_value)]

    first_letter = key_list[val_list.index(first_letter_value)]
    second_letter = key_list[val_list.index(second_letter_value)]
    return str(first_letter) + str(second_letter)

def stuff_counter(counted, amount):
    letter_frequency = {}  # Create empty dict for letter frequency

    for element in counted:
        letter_frequency[element] = counted[element] / amount  # Count frequency for each element
        print( element + ' = ' +  str( " %.5f" % letter_frequency[element]))  # Print frequency for each element

    return letter_frequency  # Return value of entropy and frequency dictionary

def decipher(keys_list, encrypted_bigrams_values, indexed_russian_alphabet, impossible_begrams_values):
    for lst in keys_list:
        print("\nKEY: " + str (lst) )
        a = lst[0]
        b = lst[1]
        text = ''
        a_opp = find_opposite(a, 31**2)
        #print("opposite a = " + str(a_opp))
        #print("x = " + str(a_opp) + " * (yi -" + str(b) + ") mod 961")
        for bigram_index in range(len(encrypted_bigrams_values)):
            #print(str(bigram))
            open_bigram_value = a_opp * (encrypted_bigrams_values[bigram_index] - b + 10*961) % 961

            #print(open_bigram_value)
            #open_bigram = bigramDetecter(bigram, indexed_russian_alphabet)
            open_bigram = bigramDetecter(open_bigram_value, indexed_russian_alphabet)
            if open_bigram_value in impossible_begrams_values:
                text = "Impossible bigram found: " + open_bigram
                print(text)
                break
            # print(open_bigram)
            # return
            text += open_bigram
            if bigram_index == len(encrypted_bigrams_values)-1:

                grams = Counter(text)
                if list(x[0] for x in grams.most_common(1)) == ['о']:
                    print(text)
                    print(grams)
                else:
                    print("Failed to frequency analysis: " + str(list(x[0] for x in grams.most_common(5))))
        text = ''


