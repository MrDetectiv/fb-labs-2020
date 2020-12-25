import matplotlib.pylab as plt
import re
letters = list('абвгдежзийклмнопрстуфхцчшщъыьэюя' + 'абвгдежзийклмнопрстуфхцчшщъыьэюя'.upper())
alph_len = len(letters)
letters_map = {letters[key] : key for key in range(alph_len)}
numbers_map = {key : letters[key] for key in range(alph_len)}

def letters_to_numbers(letters):
    return list(map(lambda x: letters_map[x] if x in letters_map else x,list(letters)))

def numbers_to_letters(numbers):
    return list(map(lambda x: numbers_map[x] if type(x) is int else x,numbers))


def vignere_crypt(plain,key,mode):
    encrypted = []
    plain = letters_to_numbers(plain)
    key = letters_to_numbers(key)
    for i in range(len(plain)):
        try:
            if plain[i] > 32:
                if mode == "decrypt":
                    encrypted.append(((plain[i] - key[i % (len(key))]) % (alph_len // 2)) + (alph_len//2) )
                else:
                    encrypted.append(((plain[i] + key[i % (len(key))]) % (alph_len // 2)) + (alph_len // 2))
            else:
                if mode == "decrypt":
                    encrypted.append((plain[i] - key[i % (len(key))]) % (alph_len // 2))
                else:
                    encrypted.append((plain[i] + key[i % (len(key))]) % (alph_len // 2))


        except TypeError:
            encrypted.append(plain[i])
    return ''.join(numbers_to_letters(encrypted))


def icx(text):

    text = re.sub('[^а-я]','',text)
    len_of_text = len(text)
    letters_map = {i:0 for i in letters}
    for letter in text:
        if letter in letters_map:
            letters_map[letter] += 1
        else:
            continue
    arr = sum([letters_map[item] * (letters_map[item] - 1) for item in letters_map])
    div = len_of_text * (len_of_text - 1)
    result = arr / div
    return result


def print_icx(arr):
    arr_of_icx = {}
    for element in arr:
       encrypted = vignere_crypt(text, element, 'encrypt')
       print("инднекс совпадений для шифр текста,защифрованного ключом длинны {}: {}".format(len(element),icx(encrypted)))
       arr_of_icx[len(element)] = icx(encrypted)
    return arr_of_icx

if __name__ == "__main__":

    text = open('besy.txt','r').read()
    text = re.sub('ё','e',text)
    arr_of_keys = ['ая','кот','киев','гелла','установщик','аккумулятор','зерносушилка','импрессионист','бракосочетание','десятикопеечный','искусствоведение','анастигматический','высококачественный','ацетилхолинэстераза','автоматизированность']
    print("инднекс совпадений для открытого текста: {}".format(icx(text)))
    dict_of_icx = print_icx(arr_of_keys)
    plt.plot(list(dict_of_icx.keys()), list(dict_of_icx.values()))
    plt.xlabel('key length')
    plt.ylabel('index of coincidence')
    plt.show()
    plt.savefig('plot.png')






