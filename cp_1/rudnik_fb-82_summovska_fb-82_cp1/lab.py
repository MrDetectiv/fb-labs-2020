import math

def pretty_freq_print(freq):
    for elem in freq:
        print("{}: {}".format(elem,freq[elem]))


def ngram_freq(text,n,intersect):
    if not intersect and n > 1:
        step = 2
    else:
        step = 1
    bigram_dict = {}
    text_len = len(text)
    bigram_counter = 0
    for i in range(0,len(text)-(n-1),step):
        if text[i:i+n] not in bigram_dict:
            bigram_dict[text[i:i+n]] = 1
            bigram_counter += 1
        else:
            bigram_dict[text[i:i + n]] += 1
            bigram_counter += 1

    to_sort = [(key,bigram_dict[key]) for key in bigram_dict]
    to_sort.sort(key=lambda x:x[1],reverse=True)
    bigram_dict = {key:value for key,value in to_sort}
    for bigram in bigram_dict:
        bigram_dict[bigram] = float(bigram_dict[bigram] / bigram_counter)
    return bigram_dict


def find_entroypy(text,n,intersect):
    prob_arr = ngram_freq(text,n,intersect).values()
    entropy = sum(list(map(lambda x: -x * math.log2(x), prob_arr)))
    entropy *= 1/n
    return entropy

redundency = lambda x: 1 - (x / math.log2(32))





# text_with_spaces = open('withspaces', 'r+').read()
# text_without_spaces = open('withoutspaces','r+').read()
# print("{} МОНОГРАММЫ С ПРОБЕЛАМИ {}".format("\n"*4,"\n"*4))
# pretty_freq_print(ngram_freq(text_with_spaces,1,True))
# print("{} БИГРАММЫ С ПРОБЕЛАМИ И ПЕРЕСЕЧЕНИЯМИ {}".format("\n"*4,"\n"*4))
# pretty_freq_print(ngram_freq(text_with_spaces,2,True))
# print("{} БИГРАММЫ С ПРОБЕЛАМИ И БЕЗ ПЕРЕСЕЧЕНИЯМИ {}".format("\n"*4,"\n"*4))
# pretty_freq_print(ngram_freq(text_with_spaces,2,False))
# print("{} МОНОГРАММЫ БЕЗ ПРОБЕЛАМИ {}".format("\n"*4,"\n"*4))
# pretty_freq_print(ngram_freq(text_without_spaces,1,True))
# print("{} БИГРАММЫ БЕЗ ПРОБЕЛАМИ И ПЕРЕСЕЧЕНИЯМИ {}".format("\n"*4,"\n"*4))
# pretty_freq_print(ngram_freq(text_without_spaces,2,True))
# print("{} БИГРАММЫ БЕЗ ПРОБЕЛАМИ И БЕЗ ПЕРЕСЕЧЕНИЯМИ {}".format("\n"*4,"\n"*4))
# pretty_freq_print(ngram_freq(text_without_spaces,2,False))
text_with_spaces = open('withspaces','r+').read()
text_without_spaces = open('withoutspaces','r+').read()

h1_with_spaces = find_entroypy(text_with_spaces,1,False)
h2_with_spaces_intersect = find_entroypy(text_with_spaces,2,True)
h2_with_spaces = find_entroypy(text_with_spaces,2,False)
h1_without_spaces = find_entroypy(text_without_spaces,1,False)
h2_without_spaces_intersect = find_entroypy(text_without_spaces,2,True)
h2_without_spaces = find_entroypy(text_without_spaces,2,False)

print("H1 текст с пробелами",h1_with_spaces)
print("избыточность H1 текст с пробелами",redundency(h1_with_spaces))
print("H2 текст с пробелами и пересечениями",h2_with_spaces_intersect)
print("избыточность H2 текст с пробелами и пересечениями",redundency(h2_with_spaces_intersect))
print("H2 текст с пробелами без пересечений",h2_with_spaces)
print("избыточность H2 текст с пробелами без пересечений",redundency(h2_with_spaces))
print("H1 текст без пробелов",h1_without_spaces)
print("избыточность H1 текст без пробелов",redundency(h1_without_spaces))
print("H2 текст без и пересечениями",h2_without_spaces_intersect)
print("избыточность H2 текст без и пересечениями",redundency(h2_without_spaces_intersect))
print("H2 текст без и пересечений",h2_without_spaces)
print("избыточность H2 текст без и пересечений",redundency(h2_without_spaces))