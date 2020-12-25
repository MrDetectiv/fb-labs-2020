import re

def clear_text(file):
    with open(file,'r') as with_spaces:
        text = with_spaces.read().lower()
        text = text.replace('ё','е')
        text = text.replace('ъ','ь')
        text = re.sub('[^а-я ]', '', text).strip()
        open('withspaces','w').write(text)

    with open(file, 'r') as without_spaces:
        text = without_spaces.read().lower()
        text = text.replace('ё', 'е')
        text = text.replace('ъ', 'ь')
        text = re.sub('[^а-я]','',text)
        open('withoutspaces', 'w').write(text)



clear_text('idiot.txt')