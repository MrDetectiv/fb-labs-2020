from collections import *
import re
import sys
import os
import math


def filter_text(l_text):
    l_text = re.sub("[^А-аЯ-я ]", "", l_text)       # removing unneeded letters
    l_text_with_spaces = l_text     # text with spaces
    l_text_without_spaces = l_text.replace(" ", "")     # text without spaces
    return l_text_with_spaces, l_text_without_spaces


def frequency(counter, n_gram_lenght):
    counter = OrderedDict(sorted(counter.items(), key=lambda t: t[0]))
    frequency_list = []
    total_amount = sum(counter.values())

    for n_gram in counter:  # frequency counting
        frequency_list.append((n_gram, counter[n_gram] / total_amount))

    entropy = 0
    for index in range(len(frequency_list)):  # entropy = -∑[chunk_frequency * log2(chunk_frequency)]
        entropy -= frequency_list[index][1] * math.log(frequency_list[index][1], 2)

    if int(n_gram_lenght) > 1:  # entropy depends size of chunk of letters
        entropy /= n_gram_lenght
    return frequency_list, entropy, n_gram_lenght


def form_up_info(frequency_entropy_ngram, crossing, whitespaces):
    crossing = "" if crossing else "no-"    # choosing output string component
    whitespaces = "with" if whitespaces else "without"    # choosing output string component
    print(f"\nThe text divided as {frequency_entropy_ngram[2]}-grammed text with {crossing}crossing and {whitespaces} whitespaces ")

    for pair in frequency_entropy_ngram[0]:
        print(f"{pair[0]}-{str('%.5f' % pair[1])}")

    print("H =", str(frequency_entropy_ngram[1]))
    print("R =", str(1 - (frequency_entropy_ngram[1] / math.log(32, 2))) + "\n")


def text_info(l_text):
    text_with_spaces, text_without_spaces = filter_text(l_text)
    n = 2
    # m, b - monogram, bigram
    # w, nw - whitespaces, no whitespaces
    # c, nc - crossing, no crossing
    m_w = Counter(text_with_spaces)
    m_nw = Counter(text_without_spaces)
    b_w_nc = Counter([text_with_spaces[i:i + n] for i in range(0, len(text_with_spaces), n)])
    b_nw_nc = Counter([text_without_spaces[i:i + n] for i in range(0, len(text_without_spaces), n)])
    b_w_c = Counter([text_with_spaces[i:i + n] for i in range(0, len(text_with_spaces), n - 1)])
    b_nw_c = Counter([text_without_spaces[i:i + n] for i in range(0, len(text_without_spaces), n - 1)])
    # frequency(counter_of_chunks, chunk_size)
    # form_up_info(frequency_entropy_ngram, crossing_case?, with_whitespaces?)
    form_up_info(frequency(m_w, 1), False, True)
    form_up_info(frequency(m_nw, 1), False, False)
    form_up_info(frequency(b_w_nc, 2), False, True)
    form_up_info(frequency(b_nw_nc, 2), False, False)
    form_up_info(frequency(b_w_c, 2), True, True)
    form_up_info(frequency(b_nw_c, 2), True, False)


if len(sys.argv) > 1:   # run from console
    for argument_index in range(len(sys.argv)):
        if argument_index == 0:
            continue
        else:
            print("\n" + str(sys.argv[argument_index]) + "\n")
            file = open(sys.argv[argument_index], "r", encoding="UTF-8")
            text = file.read().lower()
            text_info(text)
    pass
else:   # run script in IDE
    file = open("text.txt", "r", encoding="UTF-8")
    text = file.read().lower()
    text_info(text)


# screenshot task
h1 = (2.59121733429369, 3.29947057079725)
h2 = (1.69328914931809, 2.35930728772129)
h3 = (1.98463818100934, 2.65621351403701)
cool_pink_list = [(10, h1), (20, h2), (30, h3)]

for experiment in cool_pink_list:
    print("Порядок ен-граммы " + str(experiment[0]))
    print(f"{experiment[1][0]} < H < {experiment[1][1]}")
    print(f"{1 - (experiment[1][1] / math.log(32, 2))} < R < {1 - (experiment[1][0] / math.log(32, 2))}")
