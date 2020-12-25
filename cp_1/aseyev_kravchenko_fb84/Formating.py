import re

text = open('text.txt', 'r', encoding='utf8')
text2 = open('filtered_text.txt', 'w', encoding='utf8')
text1 = ""
for line in text:
    i = 0
    newline = re.sub(r"[^а-яА-Яё]+", " ", line)
    for symbol in newline:
        if symbol == "ё":
            newline = newline[:i] + 'е' + newline[i + 1:]
        elif symbol == "ъ":
            newline = newline[:i] + 'ь' + newline[i + 1:]
        i += 1
    new_newline = ' '.join(newline.split())
    text1 += new_newline.lower() + ' '
text2.write(text1)
