import os
import re

def ChangeSymbols(path, space = True):
    cwd = os.getcwd()

    try:
        with open(path, encoding="utf8") as f:
            text = f.read()
            f.seek(0)
    except UnicodeDecodeError:
        with open(path) as f:
            text = f.read()
            f.seek(0)

    new_text = text.lower()
    # symb = r'[abcdefghijklmnopqrstuvwxyz1234567890,./<>?`:;*-+()\&%$#@!~«»—[]]'
    if(space):
        symb = r'[^абвгдеёжзийклмнопрстуфхцчшщъыьэюя ]+'
    else:
        symb = r'[^абвгдеёжзийклмнопрстуфхцчшщъыьэюя]+'
    new_text = re.sub(symb, r'', new_text)
    new_text = re.sub(" +", " ", new_text)
    new_text = re.sub('ё', 'е', new_text)

    new_path = path[:-4] + '_modify.txt'
    with open(new_path, 'w') as new:
        new.write(new_text)

    return new_path


if __name__ == '__main__':
    c = os.getcwd()
    c = c + '\\crypto.txt'
    #print(c)
    ChangeSymbols(c)