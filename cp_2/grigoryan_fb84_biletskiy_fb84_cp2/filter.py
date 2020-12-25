with open("text.txt",'r',encoding='utf-8') as rf:
    lines = rf.readlines()
    lines = [line.replace('\n', '') for line in lines]
with open("text.txt",'w',encoding='utf-8') as rf:
    rf.writelines(lines)