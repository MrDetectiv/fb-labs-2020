from math import log2
list_of_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                   'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я', ' ']
count = 0
frequency_of_bigrams = {}
count_of_bigrams = {}


def redundancy_calculator(entropy_inner, State):
    if State:
        letters = 32
    else:
        letters = 31
    return 1 - (entropy_inner/log2(letters))


def clear_dict():
    frequency_of_bigrams.clear()
    count_of_bigrams.clear()


def count_of_specific_bigrams(name_of_text, cross):
    if cross:
        step = 1
    else:
        step = 2
    text = open(name_of_text, 'r', encoding='utf8').read()
    count = 0
    for i in range(0, len(text) - 1, step):
        if text[i:i+2] not in count_of_bigrams:
            count_of_bigrams[text[i:i+2]] = 1
            count += 1
        else:
            count_of_bigrams[text[i:i+2]] += 1
            count += 1
    return count


def frequency_of_bigrams_func(count):
    for item, value in count_of_bigrams.items():
        frequency_of_bigrams[item] = value / count


def entropy_of_bigrams_func(entropy_inner):
    for value in frequency_of_bigrams.values():
        entropy_inner = entropy_inner + value * log2(1/value)
    entropy_inner *= 1/2
    return entropy_inner


def write_into_file(name_of_file, state_for_spaces, state_for_cross):
    entropy = 0
    count = count_of_specific_bigrams(name_of_file, state_for_cross)
    frequency_of_bigrams_func(count)
    list_keys = list(count_of_bigrams.keys())
    list_keys.sort()
    entropy_file.write("{:^6}|{:^9}|\n".format("Bigram", "Frequency"))
    entropy = entropy_of_bigrams_func(entropy)
    redundancy = redundancy_calculator(entropy, state_for_spaces)
    for key in list_keys:
        entropy_file.write("{:^6}|{:^.7f}|\n".format(key, frequency_of_bigrams[key]))
    entropy_file.write('Entropy:' + str(entropy) + '\n')
    entropy_file.write('Redundancy:' + str(redundancy) + '\n\n')
    clear_dict()
    return entropy


if __name__ == '__main__':
    entropy_file = open("result_file.txt", 'a', encoding='utf8')
    entropy_file.write('Bigrams and their count dictionary for text with spaces and without cross:' + '\n')
    write_into_file("filtered_text.txt", True, False)
    entropy_file.write('Bigrams and their count dictionary for text with spaces and cross:' + '\n')
    write_into_file("filtered_text.txt", True, True)
    entropy_file.write('Bigrams and their count dictionary for text without spaces and cross:' + '\n')
    write_into_file("filtered_text_without_spaces.txt", False, False)
    entropy_file.write('Bigrams and their count dictionary for text without spaces and with cross:' + '\n')
    write_into_file("filtered_text_without_spaces.txt", False, True)
    entropy_file.close()
