from collections import Counter, OrderedDict
import re, math


def extra_remover(file):
    space_file = file.read().lower()  # Read data from file and convert to lowercase
    space_file = re.sub(r'[^А-Яа-я ]', '',
                        space_file)  # Remove all the characters, accept for cyrillic letters and whitespaces
    spaceless_file = re.sub(r'\W', '', space_file)  # Remove also whitespaces
    return space_file, spaceless_file


def monogram(space_file, spaceless_file):

    entropy = entropy_counter(space_file) * 2

    print("Entropy with spaces = " + str(entropy))  # Print the result
    print("R = " + str(1 - (entropy / math.log(32, 2))))  # Print the redundancy

    entropy = entropy_counter(spaceless_file) * 2

    print("Entropy without spaces = " + str(entropy))  # Print entropy of the text without whitespaces
    print("R = " + str(1 - (entropy / math.log(32, 2))))  # Count the redundancy without whitespaces


def bigram(space_file, spaceless_file):
    s_letter_pairs = re.findall(r'..?', space_file)
    entropy = entropy_counter(s_letter_pairs)
    print("Entropy with spaces = " + str(entropy))  # Print that value
    print("R = " + str(1 - (entropy / math.log(32, 2))))  # Count the redundancy

    s_letter_pairs_crossed = list(
        map(''.join, zip(space_file, space_file[1:])))  # Get letter pairs (including whitespaces)
    entropy = entropy_counter(s_letter_pairs_crossed)
    print("Entropy with spaces (crossed) = " + str(entropy))  # Print that value
    print("R = " + str(1 - (entropy / math.log(32, 2))))  # Count the redundancy

    letter_pairs = re.findall(r'..?', spaceless_file)
    entropy = entropy_counter(letter_pairs)
    print("Entropy without spaces = " + str(entropy))  # Print that value
    print("R = " + str(1 - (entropy / math.log(32, 2))))  # Count the redundancy

    letter_pairs_crossed = list(
        map(''.join, zip(spaceless_file, spaceless_file[1:])))  # Get letter pairs without whitespaces
    entropy = entropy_counter(letter_pairs_crossed)
    print("Entropy without spaces (crossed) = " + str(entropy))  # Print that value
    print("R = " + str(1 - (entropy / math.log(32, 2))))  # Count the redundancy


def stuff_counter(counted, amount):
    frequency_dict = {}  # Create empty dict for letter frequency

    for element in counted:
        frequency_dict[element] = counted[element] / amount  # Count frequency for each element
        print( element + ' = ' +  str( " %.5f" % frequency_dict[element]))  # Print frequency for each element

    entropy = 0  # Define starting value of entropy

    for element in frequency_dict:
        ent = frequency_dict[element] * math.log(frequency_dict[element], 2)  # Count entropy for each element
        entropy -= ent  # Count overall entropy

    return entropy, frequency_dict  # Return value of entropy and frequency dictionary


def entropy_counter(counted):
    grams = Counter(counted)  # Count the frequency of each pair of letters in the text
    grams = OrderedDict(sorted(grams.items(), key=lambda t: t[0]))  # Sorts the dict
    grams_amount = len(counted)  # Return amount of pair of the letters

    entropy, frequency_dict = stuff_counter(grams, grams_amount)  # Return overall entropy for the pairs with

    # whitespaces and the dict with frequency of
    # each pair
    entropy = entropy / 2  # Get proper value of entropy for text

    return entropy
