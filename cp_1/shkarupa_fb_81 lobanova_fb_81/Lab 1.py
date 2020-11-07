import collections, re, math


def entropia_count(count):
    entropia = 0
    for i in count:
        el = float(count[i])
        if el == 0:
            pass
        else:
            entropia += -(el) * math.log((el), 2)
    return entropia


def count_bigram(bigram_count):
    entropia = 0
    for i in bigram_count:
        el = float(bigram_count[i])
        if el == 0:
            entropia += 0
        else:
            entropia += -(el) * math.log((el), 2)
    return entropia


def count_r_bigram(bigram_r_count):
    entropia = 0
    for i in bigram_r_count:
        el = float(bigram_r_count[i])
        if el == 0:
            entropia += 0
        else:
            entropia += -(el) * math.log((el), 2)
    return entropia


def to_excess(entropia):
    return 1 - (entropia / math.log(32, 2))




def withprob():
    print('Текст без пробелами:')
    a = ord('а')
    alpha_bet = ''.join([chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)])
    file = open('result.txt', 'r', encoding='utf-8').read()
    file = file.lower()
    full_alpha_bet = [alpha_bet, alpha_bet + " "]
    r_alph = full_alpha_bet[0]
    for el in file:
        if el not in r_alph:
            file = file.replace(el, '')

    file = file.replace('ё', 'е').replace('ъ', 'ь').replace('/n', '')
    file = re.sub(" +", " ", file)

    print('Количество букв: ', len(file), "\n")

    # монограмма

    value_word = collections.Counter(file)

    for i in value_word:
        el = 100 * value_word[i] / (len(file))
        el = '%.5f' % el
        value_word[i] = el

    for i in value_word:
        print(i, value_word[i], end="\n")

    for i in value_word:
        el = float(value_word[i]) / 100
        el = '%.5f' % el
        value_word[i] = el

    bigrams = []
    bigrams_r = []

    # биграммы

    # пересечене

    for i in range(0, len(file) - 1, 1):
        bigrams.append(file[i] + file[i + 1])

    amount_bigram = collections.Counter(bigrams)
    g = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
         'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']
    print('Биграмы c пересечением', "\n")

    for i in amount_bigram:
        fr = 100 * float(amount_bigram[i]) / (len(bigrams))
        fr = '%.5f' % fr
        amount_bigram[i] = fr

    for i in range(len(g)):
        for j in range(len(g)):
            print(amount_bigram[g[i] + g[j]], end=" ")
        print('')

    for i in amount_bigram:
        fr = float(amount_bigram[i]) / 100
        amount_bigram[i] = fr

    # без пересечения
    g = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
         'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']
    print('Биграмы без пересечения', "\n")

    for i in range(0, len(file) - 1, 2):
        bigrams_r.append(file[i] + file[i + 1])

    amount_r_bigram = collections.Counter(bigrams_r)

    for i in amount_r_bigram:
        fr = 100 * float(amount_r_bigram[i]) / (len(bigrams_r))
        fr = '%.5f' % fr
        amount_r_bigram[i] = fr

    for i in range(len(g)):
        for j in range(len(g)):
            print(amount_r_bigram[g[i] + g[j]], end=" ")
        print('')

    for i in amount_r_bigram:
        fr = float(amount_r_bigram[i]) / 100
        amount_r_bigram[i] = fr

    # Энтропия
    entropia = entropia_count(value_word)
    excess = to_excess(entropia)

    print("Энтропия монограммы (H1) ", entropia)
    print("Избыточность монограммы (R1) ", excess, "\n")

    entropia = count_bigram(amount_bigram) / 2
    excess = to_excess(entropia)

    print("Энтропия биграммы с пересечением (H2) ", entropia)
    print("Избыточность биграммы с пересечением (R2) ", excess, "\n")

    entropia = count_r_bigram(amount_r_bigram) / 2
    excess = to_excess(entropia)

    print("Энтропия биграммы без пересечения (H3) ", entropia)
    print("Избыточность биграммы без пересечения (R3) ", excess)



def enothprob():
    a = ord('а')
    alpha_bet = ''.join([chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)])
    file = open('result.txt', 'r', encoding='utf-8').read()
    file = file.lower()
    full_alpha_bet = [alpha_bet, alpha_bet + " "]
    r_alph = full_alpha_bet[0]
    print('===================================')
    print('Текст с пробелов:')

    r_alph = full_alpha_bet[0]
    for el in file:
        if el not in r_alph:
            file = file.replace(el, ' ')

    file = file.replace('ё', 'е').replace('ъ', 'ь').replace('/n', '')
    file = re.sub(" +", " ", file)

    print('Количество букв: ', len(file), "\n")

    #монограмма

    value_word = collections.Counter(file)

    for i in value_word:
        el = 100 * value_word[i] / (len(file))
        el = '%.5f' % el
        value_word[i] = el

    for i in value_word:
        print(i, value_word[i], end="\n")

    for i in value_word:
        el = float(value_word[i]) / 100
        el = '%.5f' % el
        value_word[i] = el

    bigrams = []
    bigrams_r = []


    #биграммы

    #пересечене

    for i in range(0, len(file) - 1, 1):
        bigrams.append(file[i] + file[i + 1])

    amount_bigram = collections.Counter(bigrams)
    g = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
         'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']
    print('Биграмы c пересечением', "\n")

    for i in amount_bigram:
        fr = 100 * float(amount_bigram[i]) / (len(bigrams))
        fr = '%.5f' % fr
        amount_bigram[i] = fr

    for i in range(len(g)):
        for j in range(len(g)):
            print(amount_bigram[g[i] + g[j]], end=" ")
        print('')

    for i in amount_bigram:
        fr = float(amount_bigram[i]) / 100
        amount_bigram[i] = fr

    #без пересечения
    g=['а','б' ,'в', 'г', 'д', 'е', 'ж', 'з' ,'и' ,'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я' ]
    print('Биграмы без пересечения', "\n")

    for i in range(0, len(file) - 1, 2):
        bigrams_r.append(file[i] + file[i + 1])

    amount_r_bigram = collections.Counter(bigrams_r)

    for i in amount_r_bigram:
        fr = 100 * float(amount_r_bigram[i]) / (len(bigrams_r))
        fr = '%.5f' % fr
        amount_r_bigram[i] = fr

    for i in range(len(g)):
        for j in range(len(g)):
            print(amount_r_bigram[g[i]+g[j]], end=" ")
        print('')

    for i in amount_r_bigram:
        fr = float(amount_r_bigram[i]) / 100
        amount_r_bigram[i] = fr

    #Энтропия
    entropia = entropia_count(value_word)
    excess = to_excess(entropia)

    print("Энтропия монограммы (H1) ", entropia)
    print("Избыточность монограммы (R1) ", excess, "\n")

    entropia = count_bigram(amount_bigram) / 2
    excess = to_excess(entropia)

    print("Энтропия биграммы с пересечением (H2) ", entropia)
    print("Избыточность биграммы с пересечением (R2) ", excess, "\n")

    entropia = count_r_bigram(amount_r_bigram) / 2
    excess = to_excess(entropia)

    print("Энтропия биграммы без пересечения (H3) ", entropia)
    print("Избыточность биграммы без пересечения (R3) ", excess)



withprob()
enothprob()
