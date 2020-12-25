from math import log2
list_of_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                   'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']
count_of_letters = {}
count = 0
entropy = 0
frequency_of_letters = {}


def calculator_of_redundancy():
    return 1 - (entropy/log2(31))


def count_specific_letters():
    for letter in list_of_letters:
        text = open("filtered_text_without_spaces.txt", 'r', encoding='utf8')
        i = 0
        for line in text:
            for symbol in line:
                if letter == symbol:
                    i += 1
        count_of_letters[letter] = i
        text.close()


def count_letters():
    text = open("filtered_text_without_spaces.txt", 'r', encoding='utf8')
    for line in text:
        for _ in line:
            global count
            count += 1
    text.close()


def frequency_of_letters_func():
    for item_letter, value_letter in count_of_letters.items():
        frequency_of_letters[item_letter] = value_letter / count


def calculator_of_entropy():
    for value_inner in frequency_of_letters.values():
        global entropy
        entropy = entropy + value_inner*log2(1/value_inner)


if __name__ == "__main__":
    count_specific_letters()
    count_letters()
    frequency_of_letters_func()
    calculator_of_entropy()
    entropy_file = open("result_file.txt", 'a', encoding='utf8')
    entropy_file.write('Monograms and their count dictionary for text without spaces:' + '\n')
    entropy_file.write("{:^8}|{:^9}|\n".format("Monogram", "Frequency"))
    list_keys = list(count_of_letters.keys())
    list_keys.sort()
    for key in list_keys:
        entropy_file.write("{:^8}|{:^.7f}|\n".format(key, frequency_of_letters[key]))
    redundancy = calculator_of_redundancy()
    entropy_file.write('Entropy:' + str(entropy) + '\n')
    entropy_file.write('Redundancy:' + str(redundancy) + '\n\n')