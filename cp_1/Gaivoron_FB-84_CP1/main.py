from collections import Counter
from math import log2


def count_frequencies(text):
    freqs = Counter()
    for e in text:
        freqs[e] += 1
    max = len(text)
    for e in freqs:
        freqs[e] /= max
    return freqs


def split_with_overlapping(sequence, size, step=1):
    num_of_chunks = int((len(sequence) - size) / step) + 1
    for i in range(0, num_of_chunks * step, step):
        yield sequence[i:i + size]


def split_without_overlapping(sequence, size):
    return split_with_overlapping(sequence, size, size)


def read_str(path):
    f = open(path, 'r', encoding='utf8')
    text = f.read()
    f.close()
    return text


def H(frequencies):
    k = next(iter(frequencies))
    n = 1
    if k is not chr:
        n = len(k)
    sum = 0
    for value in frequencies.values():
        sum += value * (log2(value))
    return -sum / n


def pprint_dict(dct, num_in_str):
    count = 0
    for (k, v) in sort_by_val(dct).items():
        if count == num_in_str:
            print()
            count = 0
        print(f'{k}:{v:.6f},', end='')
        count += 1
    print()

def sort_by_val(dct):
    return {k: v for k, v in sorted(dct.items(), key=lambda item: item[1], reverse=True)}


l = 12


def stat(path):
    text = read_str(path)

    print('Частоты букв: ')
    f = count_frequencies(text)
    pprint_dict(f, 1)
    h = H(f)
    print(f'H1: {h}')

    print('Частоты биграмм: ')
    f_bi = count_frequencies(list(split_without_overlapping(text, 2)))
    pprint_dict(f_bi, l)
    h_bi = H(f_bi)
    print(f'H2: {h_bi}')

    print('Частоты биграмм(с пересечениями): ')
    f_bi_over = count_frequencies(list(split_with_overlapping(text, 2)))
    pprint_dict(f_bi_over, l)
    h_bi_over = H(f_bi_over)
    print(f'H2(с пересечениями): {h_bi_over}')


if __name__ == '__main__':
    print('Текст с пробелами')
    stat('ve4naya_zhizn_smerti_s')
    print('Текст без пробелов')
    stat('ve4naya_zhizn_smerti_ws')
