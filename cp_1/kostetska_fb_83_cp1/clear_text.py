import re

# ask for filename
print('Enter name of the file from directory text/ to clear: ', end='')
file_to_clear = input()

# read file
with open('text/'+file_to_clear, 'r', encoding='utf-8') as file:
    lines = file.readlines();

# replace all chars except Russian letters with spaces
text = re.sub('[^\u0430-\u044F\u0451 ]', ' ', ''.join(lines).lower())

# replace some chars and delete unnecessary spaces
text = text.replace('ъ', 'ь')
text = text.replace('ё', 'е')
while '  ' in text:
    text = text.replace('  ', ' ')

# write cleared text to file
with open('text/cleared_' + file_to_clear, 'w', encoding='utf-8') as file:
    file.write(text)

print('Text successfully cleared and written to text/cleared_' + file_to_clear)