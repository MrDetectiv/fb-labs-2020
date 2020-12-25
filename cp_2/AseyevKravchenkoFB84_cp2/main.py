key_dictionary = {2: "он", 3: "том", 4: "укор", 5: "помню", 10: "авиатехник", 11: "кайфоломщик", 12: "ядерночистый",
                  13: "щелканувшийся", 14: "шизофренировав", 15: "обандероливавши", 16: "феминизироваться",
                  17: "отакелаживавшийся", 18: "частнопрактикующий", 19: "языкоблудствовавший",
                  20: "антитеррористический"}
list_of_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                   'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
frequency_for_language = {'а': '0.08267', 'б': '0.01787', 'в': '0.04306', 'г': '0.01597', 'д': '0.03169', 'е': '0.08788',
           'ж': '0.01063', 'з': '0.01618', 'и': '0.06673', 'й': '0.01210', 'к': '0.03309', 'л': '0.04911', 'м': '0.03424',
           'н': '0.06605', 'о': '0.10897', 'п': '0.02385', 'р': '0.04139', 'с': '0.05668', 'т': '0.06016', 'у': '0.02625',
           'ф': '0.00142', 'х': '0.00788', 'ц': '0.00292', 'ч': '0.01534', 'ш': '0.00846', 'щ': '0.00315', 'ъ': '0.00021',
           'ы': '0.01991', 'ь': '0.02139', 'э': '0.00498', 'ю': '0.00547', 'я': '0.02434'}
frequency_for_text = {}
compliance_index_dictionary = {}
count_of_letters = {}
all_key_compliance_index = {}


def count_specific_letters(text):
    for letter in list_of_letters:
        i = 0
        for line in text:
            for symbol in line:
                if letter == symbol:
                    i += 1
        count_of_letters[letter] = i


def count_letters(text, count):
    for _ in text:
        count += 1
    return count


def culc_compliance_index(count):
    sum_of_letter = 0
    for key in count_of_letters.keys():
        sum_of_letter += count_of_letters[key] * (count_of_letters[key] - 1)
    result = sum_of_letter * (1/count) * (1/(count-1))
    return result


def text_open_for_read(name_of_text):
    return open(name_of_text, 'r', encoding='utf8')


def text_open_for_write(name_of_text):
    return open(name_of_text, 'w', encoding='utf8')


def text_encr():
    for i in key_dictionary.keys():
        buff_text = ""
        text = text_open_for_read('filtered_text_for_encr.txt')
        text_name = 'encr_text' + str(i) + '.txt'
        encr_text = text_open_for_write(text_name)
        count = 0
        for line in text:
            key_letter_index = 0
            for letter in line:
                letter_index = list_of_letters.index(letter)
                key_word = key_dictionary[i]
                key_letter_index_correct = key_letter_index % i
                key_letter = key_word[key_letter_index_correct]
                key_letter_alph_index = list_of_letters.index(key_letter)
                letter_index = (letter_index + key_letter_alph_index) % 32
                buff_text += list_of_letters[letter_index]
                key_letter_index += 1
        count = count_letters(buff_text, count)
        count_specific_letters(buff_text)
        compliance_index_dictionary[i] = culc_compliance_index(count)
        count_of_letters.clear()
        encr_text.write(buff_text)
        text.close()
        encr_text.close()


def text_splice(length):
    text = text_open_for_read("filtered_text_of_variant_encr.txt")
    parts = []
    buff_text = ""
    for line in text:
        buff_text += line
    for i in range(0, length):
        part = ""
        for symbol in range(i, len(buff_text), length):
            part += buff_text[symbol]
        parts.append(part)
    return parts


def all_key_text():
    for key_length in range(2, 31):
        parts = text_splice(key_length)
        summary = 0
        for i in range(0, len(parts)):
            count = 0
            count = count_letters(parts[i], count)
            count_specific_letters(parts[i])
            summary += culc_compliance_index(count)
            count_of_letters.clear()
        all_key_compliance_index[key_length] = summary/len(parts)
    print(all_key_compliance_index)


def find_the_key_length(text):
    buff_text = ""
    for line in text:
        buff_text += line
    key_arr = []
    for key_l, value in all_key_compliance_index.items():
        if value > 0.05:
            key_arr.append(key_l)
    return key_arr


def find_key(key_length):
    for key_result in key_length:
        parts = text_splice(key_result)
        key_letter = ''
        for i in range(0, key_result):
            count_specific_letters(parts[i])
            most_common_letter_text = 'а'
            for item_letter, value_letter in count_of_letters.items():
                if value_letter > count_of_letters[most_common_letter_text]:
                    most_common_letter_text = item_letter
            print(most_common_letter_text)
            most_common_letter_alph = 'о'
            text_letter_index = list_of_letters.index(most_common_letter_text)
            alph_letter_index = list_of_letters.index(most_common_letter_alph)
            key_index = (text_letter_index - alph_letter_index) % 32
            key_letter += list_of_letters[key_index]
        return key_letter


def decrypting(key_letter_result):
    text = text_open_for_read("filtered_text_of_variant_encr.txt")
    text_1 = text_open_for_write("decr_text.txt")
    buff_text = ""
    for line in text:
        key_letter_index = 0
        for letter in line:
            letter_index = list_of_letters.index(letter)
            key_letter_index_correct = key_letter_index % len(key_letter_result)
            key_letter = key_letter_result[key_letter_index_correct]
            key_letter_alph_index = list_of_letters.index(key_letter)
            letter_index = (letter_index - key_letter_alph_index) % 32
            buff_text += list_of_letters[letter_index]
            key_letter_index += 1
    text_1.write(buff_text)


if __name__ == "__main__":
    # text_encr()
    print(compliance_index_dictionary)
    all_key_text()
    text = text_open_for_read('filtered_text_of_variant_encr.txt')
    key_length = find_the_key_length(text)
    print(key_length)
    key = find_key(key_length)
    print(key)
    key = "вшекспирбуря"
    decrypting(key)
