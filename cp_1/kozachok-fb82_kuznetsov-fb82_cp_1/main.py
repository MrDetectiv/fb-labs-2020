import os
from sys import stdout, argv
from pathlib import Path
from pprint import pprint
from typing import Dict, List, Tuple
import logging
import math

sh = logging.StreamHandler(stdout)
fh = logging.FileHandler('report.txt', 'w') 
logging.basicConfig(level=logging.INFO, format="%(message)s", handlers=(sh, fh))

letters = {
    'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0, 'ё': 0, 'ж': 0,
    'з': 0, 'и': 0, 'й': 0, 'к': 0, 'л': 0, 'м': 0, 'н': 0, 'о': 0,
    'п': 0, 'р': 0, 'с': 0, 'т': 0, 'у': 0, 'ф': 0, 'х': 0, 'ц': 0,
    'ч': 0, 'ш': 0, 'щ': 0, 'ъ': 0, 'ы': 0, 'ь': 0, 'э': 0, 'ю': 0,
    'я': 0
}
letters_with_space = {
    'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0, 'ё': 0, 'ж': 0,
    'з': 0, 'и': 0, 'й': 0, 'к': 0, 'л': 0, 'м': 0, 'н': 0, 'о': 0,
    'п': 0, 'р': 0, 'с': 0, 'т': 0, 'у': 0, 'ф': 0, 'х': 0, 'ц': 0,
    'ч': 0, 'ш': 0, 'щ': 0, 'ъ': 0, 'ы': 0, 'ь': 0, 'э': 0, 'ю': 0,
    'я': 0, ' ': 0
}

letters_list = sorted([ letter for letter in letters])
letters_with_space_list = sorted([ letter for letter in letters_with_space])


def get_filtered_text_from_file(file_name: str, with_spaces: bool=True) -> str:     
    logging.info("Opening file {}".format(file_name))
    try:
        with open(file_name) as f:
            # read all text to variable
            logging.info("Reading text from file {}".format(file_name))
            text = f.read()
    except (NameError, FileNotFoundError):
        logging.error("Could not open file... Exiting...")
        exit()

    logging.info("Lowering text from file {}".format(file_name))
    lowered_text = text.lower()
    
    # filter characters
    filtered_text = ""
    if with_spaces:
        for letter in lowered_text:
            if letter in letters_with_space:
                filtered_text += letter
            elif letter == '\n':
                filtered_text += ' '
    else:
        for letter in lowered_text:
            if letter in letters:
                filtered_text += letter

    logging.info("Replacing spaces")

    while not filtered_text.find("  ") == -1:
        filtered_text = filtered_text.replace("  ", " ")

    return filtered_text



def count_letters(text: str, letters: Dict[str, int]) -> None:
    "Count all letters and write count in 'letters' dict"
    logging.info("Counting letters ...")
    for letter in text:
        try: 
            letters[letter.lower()] += 1
        except KeyError:
            pass

def count_bigrams(text: str, letters: Dict[str, int],
                  intersected: bool=True) -> List[List[int]]:
    """
    Count bigrams in matrix 
    [0, 5, 0, ...]
    [4, 0, 7, ...]
    [0, 8, 0, ...]
    ...

    :return: matrix
    """
    step = 1
    logging.info("Counting bigrams ...")
    if intersected == False:
        step = 2

    # fill matrix with 0
    bigrams = [ [ 0 for _ in letters ] for _ in letters ]

    for i in range(0, len(text) - 1, step):
        letter1, letter2 = text[i:i+2]

        # enumerate every letter like - 'a': 1, 'b': 2
        ledict = { letter: i for letter, i in zip(letters, range(len(letters))) }
        
        bigrams[ledict[letter1]][ledict[letter2]] += 1

    return bigrams


def print_letters_list(letters_list: List[ Tuple[str, int] ]) -> None:
    "Print statistics of monograms with entropy and redundancy"
    sum_of_letters_value = sum( [ value for _, value in letters_list ] )
    probabiliies = []
    logging.info("   count  percentage")
    for letter, value in letters_list:
        percentage = value / sum_of_letters_value
        try:
            probabiliies.append(percentage * math.log2(percentage))
        except ValueError:
            probabiliies.append(0)
        logging.info("{letter}: {value:6}, {percentage:2.5%}".format(
            letter=letter, value=value, percentage=percentage))
    h = -1 * sum(probabiliies)
    r = 1 - h / math.log2(len(letters_list))
    logging.info("---\nEntropy: {}\n Redundancy: {}\n---".format(h, r))

def most_used_letters(letters: Dict[str, int]) -> None:
    "print list sorted by most used letters"
    l = list(letters.items())
    l.sort(key=lambda x: x[1])
    l.reverse()
    print_letters_list(l)


def less_used_letters(letters: Dict[str, int]) -> None:
    "Print list sorted by less used letters"
    l = list(letters.items())
    l.sort(key=lambda x: x[1])
    print_letters_list(l)


def sorted_by_letter(letters: Dict[str, int]) -> None:
    "Print list sorted by letters"
    l = list(letters.items())
    l.sort(key=lambda x: x[0])
    print_letters_list(l)


def print_bigrams(bigrams: List[List[int]], letters: Dict) -> None:
    "Print bigram statisctics with entropy and redundancy"
    probabiliies = []
    sum_of_bigrams_value = 0
    l = " {:^7}" * len(letters)
    logging.info("   " + l.format(*letters))

    for row in bigrams:
        for value in row:
            sum_of_bigrams_value += value

    for letter, row in zip(letters, bigrams):
        percentage_row = []
        for value in row:
            percentage = value / sum_of_bigrams_value
            percentage_row.append(percentage)
            try:
                probabiliies.append(percentage * math.log2(percentage))
            except ValueError:
                probabiliies.append(0)
        s = "{} " + " {:.4%}" * len(percentage_row)
        logging.info(s.format(letter, *percentage_row))

    h = -1 * sum(probabiliies) / 2
    r = 1 - h / math.log2(len(letters_list))
    logging.info("--- Entropy: {}, Redundancy: {} ---".format(h, r))


def create_report(input_file: str):
    global letters, letters_with_space, letters_with_space_list, letters_list
    text_with_spaces = get_filtered_text_from_file(file_name)
    text = get_filtered_text_from_file(file_name, False)

    count_letters(text_with_spaces, letters_with_space)
    count_letters(text, letters)

    bigrams_with_spaces_intersected = count_bigrams(text_with_spaces, letters_with_space_list)
    bigrams_intersected = count_bigrams(text, letters_list)
    bigrams_with_spaces = count_bigrams(text_with_spaces, letters_with_space_list, False)
    bigrams = count_bigrams(text, letters_list, False)

    most_used_letters(letters)
    most_used_letters(letters_with_space)
    
    letters_with_space_list = [ l for l in "".join(letters_with_space_list).replace(" ", "_") ]

    logging.info("--- Bigrams with spaces intersected ---")
    print_bigrams(bigrams_with_spaces_intersected, letters_with_space_list)

    logging.info("--- Bigrams without spaces intersected ---")
    print_bigrams(bigrams_intersected, letters_list)

    logging.info("--- Bigrams with spaces not-intersected ---")
    print_bigrams(bigrams_with_spaces, letters_with_space_list)

    logging.info("--- Bigrams without spaces not-intersected ---")
    print_bigrams(bigrams, letters_list)


if __name__ == '__main__':
    
    file_name = None
    file_name = input("Enter file name (file[.txt]): ")
    if file_name == "":
        file_name = "anna.txt"

    create_report(file_name)
    