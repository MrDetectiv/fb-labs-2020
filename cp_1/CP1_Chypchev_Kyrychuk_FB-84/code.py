import re
import math
from collections import Counter,OrderedDict

class Text:
    def __init__(self,path):
        self.rusalpha = r'[^а-яА-Я|\s]+'
        self.spaces_removed = []
        self.symbols_removed = []
        self.path = path
    
    def getcleartext(self):
        with open(self.path,'r',encoding='utf-8') as cryptofile:
            for line in cryptofile:
                cleared_line = re.sub(self.rusalpha,'',line)
                #удаляем переносы строк
                cleared_line = cleared_line.lower().rstrip()
                cleared_line = cleared_line.replace('ъ','ь').replace('ё','е')
                #без знаков но с пробелами
                self.symbols_removed.append(cleared_line.replace('  ',''))
                #без знаков и без пробелов
                self.spaces_removed.append(cleared_line.replace(' ',''))
        self.symbols_removed = ' '.join(self.symbols_removed)
        self.spaces_removed = ''.join(self.spaces_removed)
        #return self.symbols_removed,self.spaces_removed

    def entropy(self,frequencies_dict):
        entropy_sum = 0
        entropy_dict = {}
        for frequency in frequencies_dict.items():
            freq = frequency[1]
            entr = freq * math.log(freq,2)
            entropy_dict.update(
                    {frequency[0]:entr}
                )
        for e in entropy_dict.items():
            entropy_sum += e[1]

        return entropy_sum

class Monograms:
    #если вызываем функцию для монограмм без пробелов, то параметр spaces_exist == False (будет == None)
    def __init__(self,text,spaces_exist):
        self.monograms = {}
        self.entropy = 0
        self.text = text
        self.freq = {}
        if spaces_exist:
            self.space = ' '
        else:
            self.space = None


    def break_into_monograms(self):
        monograms_list = []        
        for line in self.text:
            for character in line:
                monograms_list.append(character)
        self.monograms = OrderedDict(dict(Counter(monograms_list)))

    def frequencies(self):
        for char in self.monograms.items():
            self.freq[char[0]] = char[1]/len(self.text)

class Bigramms:
    def __init__(self,text):
        self.text = text
        self.bigramms_amount = 0
        self.bigramms_intersect_amount = 0
        self.bigramms = {}
        self.bigramms_intersect = {}
        
    def bigramms_with_intersect(self):
        n = 1
        bigramms_list = []
        for i in range(0,len(self.text),n):
            bigramms_list.append(self.text[i-1:i+n])
        self.bigramms_intersect_amount = len(bigramms_list)
        self.bigramms_intersect = OrderedDict(dict(Counter(bigramms_list)))

    def bigramms_no_intersect(self):
        n = 2
        bigramms_list = []
        for i in range(0,len(self.text),n):
            bigramms_list.append(self.text[i:i+n])
        self.bigramms_amount = len(bigramms_list)
        self.bigramms = OrderedDict(dict(Counter(bigramms_list)))

    def frequency(self,dictionary,bigramms_amount):
        freq = {}
        for char in dictionary.items():
            freq[char[0]] = char[1]/bigramms_amount
            # print(
            #     char[0],
            #     '{:.12f}'.format(freq[char[0]])
            # )
        return freq

text = Text(r'C:\Users\funro\Desktop\univer\kripta\sample_text.txt')
text.getcleartext()

# #монограммы без символов
monograms_no_symbols = Monograms(text.symbols_removed,True)
monograms_no_symbols.break_into_monograms()
monograms_no_symbols.frequencies()
monograms_no_symbols.entropy = abs(text.entropy(monograms_no_symbols.freq))
# #монограммы без пробелов
monograms_no_spaces = Monograms(text.spaces_removed,False)
monograms_no_spaces.break_into_monograms()
monograms_no_spaces.frequencies()
monograms_no_spaces.entropy = abs(text.entropy(monograms_no_spaces.freq))

# print('Энтропия без пробелов:' + str(monograms_no_spaces.entropy))
# print('Энтропия с пробелами:' + str(monograms_no_symbols.entropy))

#ИНИЦИАЛИЗАЦИЯ БИГРАММЫ БЕЗ СИМВОЛОВ
bigramms_no_symbols = Bigramms(text.symbols_removed)
#ИНИЦИАЛИЗАЦИЯ БИГРАММЫ БЕЗ ПРОБЕЛОВ
bigramms_no_spaces = Bigramms(text.spaces_removed)


# #ДЛЯ ПЕРЕСЕКАЮЩИХСЯ БИГРАММ БЕЗ СИМВОЛОВ
bigramms_no_symbols.bigramms_with_intersect()
bi_no_symbols_freq = bigramms_no_symbols.frequency(bigramms_no_symbols.bigramms_intersect,bigramms_no_symbols.bigramms_intersect_amount)
# # #ДЛЯ ПЕРЕСЕКАЮЩИХСЯ БИГРАММ БЕЗ ПРОБЕЛОВ
bigramms_no_spaces.bigramms_with_intersect()
bi_no_spaces_freq = bigramms_no_spaces.frequency(bigramms_no_spaces.bigramms_intersect,bigramms_no_spaces.bigramms_intersect_amount)

#ДЛЯ НЕПЕРЕСЕКАЮЩИХСЯ БИГРАММ БЕЗ СИМВОЛОВ
bigramms_no_symbols.bigramms_no_intersect()
bi_no_symbols_freq_no_intersect  = bigramms_no_symbols.frequency(bigramms_no_symbols.bigramms,bigramms_no_symbols.bigramms_amount)
#ДЛЯ НЕПЕРЕСЕКАЮЩИХСЯ БИГРАММ БЕЗ ПРОБЕЛОВ
bigramms_no_spaces.bigramms_no_intersect()
bi_no_spaces_freq_no_intersect = bigramms_no_spaces.frequency(bigramms_no_spaces.bigramms,bigramms_no_spaces.bigramms_amount)

#ЭНТРОПИЯ ПЕРЕСЕКАЮЩИХСЯ БИГРАММ БЕЗ СИМВОЛОВ
bi_entropy_no_symbols = abs(text.entropy(bi_no_symbols_freq))/2

#ЭНТРОПИЯ ПЕРЕСЕКАЮЩИХСЯ БИГРАММ БЕЗ ПРОБЕЛОВ
bi_entropy_no_spaces = abs(text.entropy(bi_no_spaces_freq))/2


#ЭНТРОПИЯ НЕПЕРЕСЕКАЮЩИХСЯ БИГРАММ БЕЗ СИМВОЛОВ
bi_entropy_no_symbols_no_intersect = abs(text.entropy(bi_no_symbols_freq_no_intersect))/2
#ЭНТРОПИЯ НЕПЕРЕСЕКАЮЩИХСЯ БИГРАММ БЕЗ ПРОБЕЛОВ
bi_entropy_no_spaces_no_intersect = abs(text.entropy(bi_no_spaces_freq_no_intersect))/2