from decrypt import decrypt, exclude_letters, decrypt_file, decrypt_slice

make_check = False


if __name__ == '__main__':
    # получение вариантов дешифровки текста с целью проведения второго раунда отбора ключа вручную
    decrypt_slice('10.txt')

    # дешифровка полного файла с выбранным ключом, запись в файл
    decrypt_file('10.txt', 300, 400)

    # перебор ключей с целью поиска другой результативной комбинации
    if make_check:
        with open('10.txt', 'r', encoding='utf-8') as f:
            text = ''.join([line for line in f])
        text = exclude_letters(text)[:40]
        print(text)
        for a in range(0, 961):
            for b in range(0, 961):
                res = decrypt(text, a, b)
                if res[:39] == 'поздновечеромнаверандесиделколяичтотопи':
                    print(a, ' ', b)

