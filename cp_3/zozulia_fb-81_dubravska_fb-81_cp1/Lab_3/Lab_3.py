from collections import Counter

class Error(Exception):
    pass

def ord(let):
    if let == 'а': return 0
    if let == 'б': return 1
    if let == 'в': return 2
    if let == 'г': return 3
    if let == 'д': return 4
    if let == 'е': return 5
    if let == 'ж': return 6
    if let == 'з': return 7
    if let == 'и': return 8
    if let == 'й': return 9
    if let == 'к': return 10
    if let == 'л': return 11
    if let == 'м': return 12
    if let == 'н': return 13
    if let == 'о': return 14
    if let == 'п': return 15
    if let == 'р': return 16
    if let == 'с': return 17
    if let == 'т': return 18
    if let == 'у': return 19
    if let == 'ф': return 20
    if let == 'х': return 21
    if let == 'ц': return 22
    if let == 'ч': return 23
    if let == 'ш': return 24
    if let == 'щ': return 25
    if let == 'ь': return 26
    if let == 'ы': return 27
    if let == 'э': return 28
    if let == 'ю': return 29
    if let == 'я': return 30

def chr (num):
    if num == 0: return 'а'
    if num == 1: return 'б' 
    if num == 2: return 'в'
    if num == 3: return 'г' 
    if num == 4: return 'д' 
    if num == 5: return 'е' 
    if num == 6: return 'ж' 
    if num == 7: return 'з' 
    if num == 8: return 'и'
    if num == 9: return 'й' 
    if num == 10: return 'к' 
    if num == 11: return 'л' 
    if num == 12: return 'м' 
    if num == 13: return 'н' 
    if num == 14: return 'о' 
    if num == 15: return 'п'
    if num == 16: return 'р'
    if num == 17: return 'с'
    if num == 18: return 'т'
    if num == 19: return 'у'
    if num == 20: return 'ф'
    if num == 21: return 'х'
    if num == 22: return 'ц'
    if num == 23: return 'ч'
    if num == 24: return 'ш'
    if num == 25: return 'щ'
    if num == 26: return 'ь'
    if num == 27: return 'ы'
    if num == 28: return 'э'
    if num == 29: return 'ю'
    if num == 30: return 'я'

def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a % b)

def inverse (a, m):
    if gcd(a, m)==1:
        x = 1
        for i in range(1000):
            if (a * x) % m == 1:
                return x
            x+=1
        return 34;
    raise Error("Обратный элемент не существует")

def bigramm_counter_no_intersection(fname): #Подсчет количества и частот биграмм без пересечений
    with open(fname, 'r') as file:
        text = file.read().replace('\n', '')
    arr = [text[i:i+2] for i in range(0, len(text), 2)]
    counts = Counter(arr)
    print(counts.most_common(5))
    return(counts.most_common(5))

def crack_key(xx1, xx2, yy1, yy2):
    numxx1=ord(xx1[0])*31+ord(xx1[1])
    numxx2=ord(xx2[0])*31+ord(xx2[1])
    numyy1=ord(yy1[0])*31+ord(yy1[1])
    numyy2=ord(yy2[0])*31+ord(yy2[1])

    num1 = (numxx1-numxx2) % 961
    num2 = (numyy1-numyy2) % 961

    #a num1 = num2 mod(961)

    d = gcd(num1, 961)

    if d == 1:
        a = (inverse(num1, 961) * num2) % 961
        key= [[a, (numyy1-a*numxx1) % 961],[0,0]]
        return key
    if d > 1:
        if num2 % d != 0:
            key= [666, 666]
            return key
        if num2 % d == 0:
            new_b = num2/d
            #a num1 = num2 mod(961/d)

            while True:
                if(num2 % num1 == 0):
                    x0 = num2 / num1
                    break
                num2 += new_b
            
            key_array=[]

            for i in range(d):
                key=[x0 + new_b*i, (numyy1-((x0 + new_b*d)*numxx1)) % 961]
                key_array.append(key)

            print(key_array)
            return key_array

def check_rus(text):
    alphabet = ('оеафэщ')
    let_count = 0
    for let in text:
                let_count += 1
    
    for c in alphabet:
        temp_count = 0
        for let in text:
            if c == let:
                temp_count += 1
        if c == 'о' and temp_count*100/let_count < 7:
            print('Частота o=',round(temp_count*100/let_count, 3), end='')
            return 0
        if c == 'е' and temp_count*100/let_count < 6:
            print('Частота е=',round(temp_count*100/let_count, 3), end='')
            return 0
        if c == 'а' and temp_count*100/let_count < 6:
            print('Частота а=',round(temp_count*100/let_count, 3), end='')
            return 0
        if c == 'ф' and temp_count*100/let_count > 1:
            print('Частота ф=',round(temp_count*100/let_count, 3), end='')
            return 0
        if c == 'э' and temp_count*100/let_count > 1:
            print('Частота э=',round(temp_count*100/let_count, 3), end='')
            return 0
        if c == 'щ' and temp_count*100/let_count > 1:
            print('Частота щ=',round(temp_count*100/let_count, 3), end='')
            return 0
    print('ВЕРОЯТНО ПРАВИЛЬНЫЙ ТЕКСТ')
    return 1

def decrypt(fname, fresult, a, b):
    with open(fname, 'r') as file:
        text = file.read().replace('\n', '')
    fout = open(fresult, "wt", encoding="utf-8")

    arr = [text[i:i+2] for i in range(0, len(text), 2)]
    
    alphabet = []
    for n in range(31):
        for m in range(31):
            bigramm = chr(n) + chr(m)
            alphabet.append(bigramm)

    newtext = ''

    for bigramm in arr:
        new_bigramm = chr( ((inverse(a, 961) * (( ord(bigramm[0]) * 31) + ord(bigramm[1]) - b)) % 961) // 31) + chr( ((inverse(a, 961) * (( ord(bigramm[0]) * 31) + ord(bigramm[1]) - b)) % 961) % 31)
        newtext += new_bigramm
        fout.write(new_bigramm)

    check_rus(newtext)

def decrypt_nowrite(fname, fresult, a, b):
    with open(fname, 'r') as file:
        text = file.read().replace('\n', '')

    arr = [text[i:i+2] for i in range(0, len(text), 2)]
    
    alphabet = []
    for n in range(31):
        for m in range(31):
            bigramm = chr(n) + chr(m)
            alphabet.append(bigramm)

    newtext = ''

    for bigramm in arr:
        new_bigramm = chr( ((inverse(a, 961) * (( ord(bigramm[0]) * 31) + ord(bigramm[1]) - b)) % 961) // 31) + chr( ((inverse(a, 961) * (( ord(bigramm[0]) * 31) + ord(bigramm[1]) - b)) % 961) % 31)
        newtext += new_bigramm
    check_rus(newtext)
    print()

def bruteforce(fname, fresult):

    language_bigramms=['ст','но','то','на']

    bigramms = bigramm_counter_no_intersection(fname)
    bigramms = [bigramms[0][0], bigramms[1][0], bigramms[2][0], bigramms[3][0], bigramms[4][0]]
    print(bigramms)

    for b1 in language_bigramms:
        for b2 in language_bigramms:
            for bigramm1 in bigramms:
                for bigramm2 in bigramms:
                    if(b1 != b2 and bigramm1 != bigramm2):
                        key = crack_key(b1, b2, bigramm1, bigramm2)
                        for a,b in key:
                            if (a !=0 and b!=0) and (a !=666 and b != 666):
                                if gcd(a, 961)==1:
                                    print(a, b, end='  ')
                                    decrypt_nowrite(fname, fresult, a, b)

bruteforce('file.txt', 'decrypted.txt')

#decrypt('file.txt', 'decrypted.txt', 441, 310)