import re

#github_test

def symbols_filter(f,rf,buffer):
    a = input("Filter extra symbols?")
    if a == str(1):
        for line in f:
            newline = re.sub(r'[^а-яА-Я]+', ' ', line)
            buffer += newline
    a = input("Lower case?")
    if a == str(1):
        rf.write(buffer.lower())
    else: rf.write(buffer)


def delete_spaces():
    a = input("Delete spaces?")
    if a == str(1):
        with open("filteredtext.txt",'r',encoding='utf-8') as rf:
            lines = rf.readlines()
        lines = [line.replace(' ', '') for line in lines]
        with open("filteredtext.txt",'w',encoding='utf-8') as rf:
            rf.writelines(lines)

def letters_replace():
    a = input("Replace letters?")
    if a == str(1):
        with open("filteredtext.txt", 'r', encoding='utf-8') as rf:
            lines = rf.readlines()
        lines = [line.replace('ё','е') for line in lines]
        lines = [line.replace('ъ', 'ь') for line in lines]
        with open("filteredtext.txt",'w',encoding='utf-8') as rf:
            rf.writelines(lines)


file = open("book.txt","r", encoding='utf-8')
result_file = open("filteredtext.txt",'w',encoding='utf-8')
buffer = ''


symbols_filter(file,result_file,buffer)
delete_spaces()
letters_replace()