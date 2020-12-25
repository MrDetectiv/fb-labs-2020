from funcs import *

enc_file = open("encrypted.txt", 'r', encoding='UTF-8')
enc_text = re.sub(r'\W', '', enc_file.read())

exceptions = ["ъ", "ё"]     # exeptions in our alphbet
most_common_russian_bigrams = ["ст", "но", "ен", "то", "на"]    # bigrams we are looking for in cyphered text by frequency analisis
impossible_russian_bigrams = ["аь", "оь", "еь", "иь", "уь", "оь", "щй", "щф", "щх", "щц", "щч", "щш", "щщ"]     # bigrams we are not looking for in decrypted text
russian_alphabet = russian_alphabet(exceptions)     # our russian alphabet with letter exeptions
indexed_russian_alphabet = index_alphabet(russian_alphabet)     # our russian indexed from 0 to 30 alphabet

amount_of_most_common_russian_bigrams, amount_of_most_common_encrypted_bigrams = 5, 2    # accuracy

print("\n" + "The alphabet we are using contains " + str(len(russian_alphabet)) + " characters:\n" + str(russian_alphabet))
print("Indexed version:\n" + str(indexed_russian_alphabet) + "\n")

most_common_russian_bigrams = most_common_russian_bigrams[:amount_of_most_common_russian_bigrams]
most_common_russian_bigrams_values_list, _ = bigram_indexer(most_common_russian_bigrams, indexed_russian_alphabet)
print(str("Most common russian bigrams: ") + str(most_common_russian_bigrams))
print("Most common russian bigrams values: " + str(most_common_russian_bigrams_values_list) + "\n")

most_common_encrypted_frequency_dict, encrypted_bigrams = bigram(enc_text)
most_common_encrypted_frequency_dict = OrderedDict(sorted(most_common_encrypted_frequency_dict.items(), key=lambda t: t[1], reverse=True))
most_common_encrypted_frequency_list = list(most_common_encrypted_frequency_dict.items())[:amount_of_most_common_encrypted_bigrams]

most_common_encrypted_bigrams_values_list, _ = bigram_indexer(most_common_encrypted_frequency_dict.keys(), indexed_russian_alphabet)
most_common_encrypted_bigrams_values_list = most_common_encrypted_bigrams_values_list[:amount_of_most_common_encrypted_bigrams]
print("Most common encpypted bigrams appear rate: " + str(list(x[1] for x in most_common_encrypted_frequency_list)))
print(str("Most common encrypted bigrams: ") + str(list(x[0] for x in most_common_encrypted_frequency_list)))
print(str("Most common encrypted bigrams values: ") + str(most_common_encrypted_bigrams_values_list) + "\n")


impossible_russian_bigrams_values_list, _ = bigram_indexer(impossible_russian_bigrams, indexed_russian_alphabet)
print(str("Impossible russian bigrams: ") + str(impossible_russian_bigrams))
print(str("Impossible russian bigram values: ") + str(impossible_russian_bigrams_values_list) + "\n")

possible_keys_list = removeDuplicates(param_counter(most_common_russian_bigrams_values_list, most_common_encrypted_bigrams_values_list))
print("Threre is " + str(len(possible_keys_list)) + " possible keys:\n" + str(possible_keys_list))

encrypted_bigrams_values_list, _ = bigram_indexer(encrypted_bigrams, indexed_russian_alphabet)

decipher(possible_keys_list, encrypted_bigrams_values_list, indexed_russian_alphabet, impossible_russian_bigrams_values_list)

enc_file.close()