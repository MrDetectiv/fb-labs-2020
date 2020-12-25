from math import gcd

list_of_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                   'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']
count_of_bigrams = {}
frequency_of_bigrams = {"": 0}
list_of_bigrams = ["ст", "но", "ен", "то", "на"]
count_of_letters = {}


def algorithm_euclid_second_step(number, field):
    if number == 0:
        return field, 0, 1
    else:
        nod, x, y = algorithm_euclid_second_step(field % number, number)
        return nod, y - (field // number) * x, x


def algorithm_euclid_first_step(number, field):
    nod, x, y = algorithm_euclid_second_step(number, field)
    return x % field


def count_of_specific_bigrams(name_of_text):
    text = open(name_of_text, 'r', encoding='utf8').read()
    count = 0
    count_of_bigrams.clear()
    for i in range(0, len(text) - 1, 2):
        if text[i:i+2] not in count_of_bigrams:
            count_of_bigrams[text[i:i+2]] = 1
            count += 1
        else:
            count_of_bigrams[text[i:i+2]] += 1
            count += 1
    return count


def frequency_of_bigrams_func(count):
    for item, value in count_of_bigrams.items():
        frequency_of_bigrams[item] = 0
        frequency_of_bigrams[item] = value / count


def possible_keys(name_of_text):
    count = count_of_specific_bigrams(name_of_text)
    frequency_of_bigrams_func(count)
    list_of_bigrams_by_frequency = []
    for _ in range(0, 5):
        most_common_item = ""
        for item, value in frequency_of_bigrams.items():
            if item in list_of_bigrams_by_frequency:
                continue
            elif value > frequency_of_bigrams[most_common_item]:
                most_common_item = item
        list_of_bigrams_by_frequency.append(most_common_item)
    print(list_of_bigrams_by_frequency)
    list_of_possible_keys = []
    for i in range(0, 5):
        x1_1 = list_of_letters.index(list_of_bigrams[i][0])
        x1_2 = list_of_letters.index(list_of_bigrams[i][1])
        for c in range(0, 5):
            if c == i:
                continue
            x2_1 = list_of_letters.index(list_of_bigrams[c][0])
            x2_2 = list_of_letters.index(list_of_bigrams[c][1])
            x1 = x1_1 * 31 + x1_2
            x2 = x2_1 * 31 + x2_2
            x = (x1 - x2) % (31 ** 2)
            for k in range(0, 5):
                y1_1 = list_of_letters.index(list_of_bigrams_by_frequency[k][0])
                y1_2 = list_of_letters.index(list_of_bigrams_by_frequency[k][1])
                for e in range(0, 5):
                    if e == k:
                        continue
                    y2_1 = list_of_letters.index(list_of_bigrams_by_frequency[e][0])
                    y2_2 = list_of_letters.index(list_of_bigrams_by_frequency[e][1])
                    y1 = y1_1 * 31 + y1_2
                    y2 = y2_1 * 31 + y2_2
                    y = (y1 - y2) % (31 ** 2)
                    nod = gcd(x, 31 ** 2)
                    if nod != 1 and y % nod != 0:
                        continue
                    elif nod != 1 and y % nod == 0:
                        a = (algorithm_euclid_first_step(x, (31 ** 2) // nod) * y) % (31 ** 2 // nod)
                        while a < 31 ** 2:
                            b = (y1 - a*x1) % (31 ** 2)
                            tuple_of_keys = (a, b)
                            list_of_possible_keys.append(tuple_of_keys)
                            a += (31 ** 2) // nod
                        continue
                    else:
                        a = (algorithm_euclid_first_step(x, 31 ** 2) * y) % (31 ** 2)
                        b = (y1 - a*x1) % (31 ** 2)
                    tuple_of_keys = (a, b)
                    list_of_possible_keys.append(tuple_of_keys)
    return list_of_possible_keys


def checking_text_for_content(text, a, b):
    count_of_letters.clear()
    count = 0
    for _ in text:
        count += 1
    for letter in list_of_letters:
        i = 0
        for line in text:
            for symbol in line:
                if letter == symbol:
                    i += 1
        count_of_letters[letter] = i
    sum_of_letter = 0
    for key in count_of_letters.keys():
        sum_of_letter += count_of_letters[key] * (count_of_letters[key] - 1)
    result = sum_of_letter * (1/count) * (1/(count-1))
    file_open = open("Index_for_all_not_needed.txt", 'a', encoding='utf8')
    if result <= 0.0553:
        text_index = str(result) + "- (" + str(a) + " + " + str(b) + ")\n"
        file_open.write(text_index)
        return False
    return True


def decrypting(list_of_possible_keys, name_of_text):
    text_encr = open(name_of_text, "r", encoding="utf8").read()
    buff_text = ''
    for a, b in list_of_possible_keys:
        for i in range(0, len(text_encr), 2):
            y12 = text_encr[i:i+2]
            y_1 = list_of_letters.index(y12[0])
            y_2 = list_of_letters.index(y12[1])
            y = y_1 * 31 + y_2
            a_reverse = algorithm_euclid_first_step(a, 31 ** 2)
            x = (a_reverse * (y - b)) % (31 ** 2)
            x_1 = x // 31
            x_2 = x % 31
            x = list_of_letters[x_1] + list_of_letters[x_2]
            buff_text += x
        if checking_text_for_content(buff_text, a, b):
            text_name = "Test_text_V1_key_(" + str(a) + ", " + str(b) + ").txt"
            text_decr = open(text_name, 'w', encoding="utf8")
            text_decr.write(buff_text)
            text_decr.close()
        buff_text = ''


if __name__ == "__main__":
    print("-----Second text(MAIN) cryptanalysis started-----")
    text = "filtered_encr_text_V1.txt"
    list_of_letters[26] = "ь"
    list_of_letters[27] = "ы"
    list_of_possible_keys = possible_keys(text)
    decrypting(list_of_possible_keys, text)
