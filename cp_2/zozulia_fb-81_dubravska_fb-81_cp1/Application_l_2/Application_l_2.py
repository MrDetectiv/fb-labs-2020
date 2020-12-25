import math

def encrypt(fname, fresult, key):
    alphabet = ('абвгдежзийклмнопрстуфхцчшщъыьэюя ')
    fin = open(fname, encoding="ANSI")
    fout = open(fresult, "wt", encoding="ANSI")

    m=0
    n=0
    k=0
    t=0
    mass_text= []
    mass_key=[]
    for let in fin.read():
        for num in alphabet:
            if (let!=num):
                m=m+1

            else: mass_text.append(m)
        k=k+1
    fin.close()
    for let in key:
        for num in alphabet:
            if (let!=num):
                m=m+1

            else: mass_key.append(m)
        t=t+1

    i=0

    while i!=k-t:
        mass_key.append(mass_key[i])
        i=i+1

    mass_cypher= [(x+y)%32 for x, y in zip(mass_text, mass_key)]
    letter_cypher=[]
    for let in mass_cypher:
        letter_cypher.append(alphabet[mass_cypher[n]])
        n=n+1
    fout.write(''.join(letter_cypher))

def de_encrypt(fname, fresult, key, operation):
    with open(fname, 'r') as file:
        text = file.read().replace('\n', '')

    fout = open(fresult, "wt", encoding="ANSI")

    i = 0

    if operation == 'e':
        for letter in text:
            fout.write(chr((( (ord(letter)-1072) + (ord(key[ i % len(key) ])-1072) ) % 32 ) + 1072 ))
            i += 1

    if operation == 'd':
        for letter in text:
            fout.write( chr((( (ord(letter)-1072) - (ord(key[ i % len(key) ])-1072) ) % 32 ) + 1072 ))
            i += 1


def index_file (fname):
    with open(fname, 'r') as file:
        text = file.read().replace('\n', '')

    alphabet = ('абвгдежзийклмнопрстуфхцчшщъыьэюя')

    a = 0

    for let in alphabet:
        num = 0
        for ch in text:
            if ch == let:
                num += 1
        a += num * ( num - 1 )

    ind = a / (len(text) * (len(text) - 1) )

    print(ind)

def index (text):

    alphabet = ('абвгдежзийклмнопрстуфхцчшщъыьэюя')

    a = 0

    for let in alphabet:
        num = 0
        for ch in text:
            if ch == let:
                num += 1
        a += num * ( num - 1 )

    ind = a / (len(text) * (len(text) - 1) )

    return(ind)

def r_search(fname, maxlen):

    searched_r = 0
    max_ind = 0

    for r_len in range(2, maxlen):
        with open(fname, 'r') as file:
            text = file.read().replace('\n', '')

        med_ind = 0

        for i in range(r_len):
            num = 0;
            string = ''
            for let in text:
                if num % r_len == i:
                    string += let
                num += 1
            med_ind += index(string) / r_len

        if med_ind > max_ind:
            max_ind = med_ind
            searched_r = r_len
        file.close()

    print('Длина ключа: ', searched_r)
    return(searched_r)

def r_index (fname, maxlen):

    for r_len in range(2, maxlen):
        with open(fname, 'r') as file:
            text = file.read().replace('\n', '')

        med_ind = 0

        for i in range(r_len):
            num = 0;
            string = ''
            for let in text:
                if num % r_len == i:
                    string += let
                num += 1
            med_ind += index(string) / r_len
        print(med_ind);

def fragments(fname, r_len):
    with open(fname, 'r') as file:
        text = file.read().replace('\n', '')

    med_ind = 0

    for i in range(r_len):
        num = 0;
        string = ''
        for let in text:
            if num % r_len == i:
                string += let
            num += 1
        print(string)
        print()
    file.close()

def most_common(string):
    alphabet = ('абвгдежзийклмнопрстуфхцчшщъыьэюя')

    max_counter=0
    max_let='о'

    for letter in alphabet:
        temp_counter = 0
        for let in string:
            if let == letter:
                temp_counter += 1
        if temp_counter > max_counter:
            max_let = letter
            max_counter = temp_counter

    return(max_let)

def get_key(fname, r_len):
    with open(fname, 'r') as file:
        text = file.read().replace('\n', '')

    med_ind = 0

    print('Ключ: ', end='')

    for i in range(r_len):
        num = 0;
        string = ''
        for let in text:
            if num % r_len == i:
                string += let
            num += 1

        print(chr ( (((ord(most_common(string))-1072) - 14) % 32) + 1072 ), end='')

    print()
    file.close()

def crack_key(fname):
    get_key(fname, r_search(fname, 30))
    print()

r_index('encrypted.txt', 30)

crack_key('encrypted.txt')