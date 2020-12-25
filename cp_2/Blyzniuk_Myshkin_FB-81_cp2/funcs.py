from collections import Counter, OrderedDict
import wordninja
import matplotlib.pyplot as plt
import re, math, os, sys


def entropy_counter(counted):
    grams = Counter(counted)  # Count the frequency of each pair of letters in the text
    grams = OrderedDict(sorted(grams.items(), key=lambda t: t[1], reverse=True))  # Sorts the dict
    grams_amount = len(counted)  # Return amount of pair of the letters

    frequency_dict = {}  # Create empty dict for letter frequency

    for element in grams:
        frequency_dict[element] = grams[element] / grams_amount  # Count entropy of each letter
    return frequency_dict


def encryptor(key, indexed_text, indexed_alphabet):
    text_to_return = []  # Set dict to write encrypted text

    key_len = len(key)  # Get length of the key
    alphabet_len = len(indexed_alphabet)  # Get length of alphabet

    key_list = list(indexed_alphabet.keys())  # Get list of the letters of the alphabet
    val_list = list(indexed_alphabet.values())  # Get list of the values of the alphabet

    for i in range(0, len(indexed_text)):
        text_to_return.append(
            key_list[val_list.index((indexed_text[i] + indexed_alphabet[
                key[i % key_len]]) % alphabet_len)])  # Encrypt each letter with corresponding letter of the key

    return ''.join(text_to_return)  # Return the encrypted text


def decryptor(key, indexed_text, indexed_alphabet):
    deciphered_text = []  # Set dict to write decrypted text

    key_len = len(key)  # Get length of the key
    alphabet_len = len(indexed_alphabet)  # Get length of alphabet

    key_list = list(indexed_alphabet.keys())  # Get list of the letters of the alphabet
    val_list = list(indexed_alphabet.values())  # Get list of the values of the alphabet

    for i in range(0, len(indexed_text)):
        deciphered_text.append(
            key_list[val_list.index((indexed_text[i] - indexed_alphabet[
                key[i % key_len]]) % alphabet_len)])  # Decrypt each letter with corresponding letter of the key
    return ''.join(deciphered_text)  # Return the decrypted text


def partial_caesar_decryptor(text, reference_dict, key_len):
    key_stat = []  # List of most frequent letters of each position of the key
    alphabet = list(map(lambda letter: chr(letter), range(1072, 1104)))  # Get russian alphabet
    indexed_alphabet = {key: v for v, key in enumerate(alphabet)}  # Enumerate russian alphabet with indexes

    key_list = list(indexed_alphabet.keys())  # Get list of the letters of the alphabet
    val_list = list(indexed_alphabet.values())  # Get list of the values of the alphabet

    for element in range(0, key_len):
        letter_list = text[element::key_len]  # Get chunk of each n-th letter of encrypted text
        txt = "".join(map(str, letter_list))  # Convert that chunk into string
        stat = entropy_counter(txt)  # Count entropy of each letter of chunk of encrypted text
        key_stat.append(max(stat, key=stat.get))  # Append the most common letter to the list

    indexed_key_stat = list(map(lambda i: indexed_alphabet[i], key_stat))  # Index each letter with proper index
    for shift in reference_dict.keys():
        possible_key = ''  # Set possible key variable to empty string
        for index in indexed_key_stat:
            possible_index = (index - indexed_alphabet[shift]) % 32  # Decrypt letter as Caesar cipher
            possible_key += key_list[val_list.index(possible_index)]  # Append letter to possible key
        print(wordninja.split(possible_key))  # Split set of letter to meaningful words


def conformity_index(text):
    text_length = len(text)  # Get text length
    grams = Counter(text)  # Count frequency of each letter
    grams = OrderedDict(sorted(grams.items(), key=lambda t: t[0]))  # Order dict by frequency of use of each letter

    index = 0  # Set conformity index to zero

    for element in grams:
        index += (grams[element] * (grams[element] - 1)) / (
                    text_length * (text_length - 1))  # Count index of each letter

    return index  # Return index


def key_length(text):
    index_dict = {} # Set empty index dictionary
    for chunk in range(2, 31):
        index = 0 # Set conformity index to zero
        for element in range(0, chunk):
            letter_list = text[element::chunk] # Split text into chunk by n-th letter
            txt = "".join(map(str, letter_list)) # Unit all the letter in one string
            index += conformity_index(txt) # Sum conformity index of each chunk
        index_dict[chunk] = index / chunk # Count average conformity index
    return index_dict # Return dictionary of key length and conformity index corresponding each other
