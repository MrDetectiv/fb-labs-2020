import sys
import itertools
import re
import collections
import os
from math import log
import pandas
import xlsxwriter
from collections import OrderedDict
import numpy
import warnings

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


def count_letters(freq, l):
    """ слияние словарь подсчитанных частот """
    c1 = collections.Counter()
    c1.update(l)
    c1.update(freq)
    return c1


def freq(space=True, file=None):
    """ метод подсчета частоты букв и биграмм в файле
        space - флаг учета пробелов
        file - файл, обработка которого производится """
    if not file:
        return

    abc = alphabet if not space else alphabet + ' '

    # формирование словарей букв и биграмм
    letters, bigramms, bigramms_intersection = {letter: 0 for letter in abc}, \
                        {''.join(biletter): 0 for biletter in itertools.product(abc, abc)}, \
                        {''.join(biletter): 0 for biletter in itertools.product(abc, abc)}

    # чтение файла
    with open(file, 'r') as f:
        for line in f:
            # замена буквы ё на ё
            line = re.sub(r'ё', 'е', line)
            # выделение слов регулярным выражением
            match = re.findall(r'[а-еж-я]{1,}' if not space else r'[а-еж-я ]{1,}', line.lower())
            match = [''.join(match)]
            # перебор результатов применения реулярного выражения
            for item in match:
                # определение частоты букв через Counter класса collections
                freq1 = dict(collections.Counter(item))
                # определение частоты биграмм
                freq2 = [item[i:i+2] for i in range(0, len(item) - 1)]
                if len(item) / 2 != len(item) // 2:
                    item += item + ' '
                freq3 = [item[2*i:2*i+2] for i in range(0, int(len(item) / 2))]
                # добавление определенных частот в общий словарь частот
                letters, bigramms, bigramms_intersection = count_letters(freq1, letters), \
                                                           count_letters(freq2, bigramms), \
                                                           count_letters(freq3, bigramms_intersection)
    return letters, bigramms, bigramms_intersection


def export_data(h_dict, filename, sheetname):
    """ метод записи полученных данных в листы Excel
        промежуточная структура данных Pandas.DataFrame """
    od = OrderedDict(sorted(h_dict.items(), key=lambda t: t[0]))
    res = 0
    if len(list(od.keys())[0]) == 1:
        # единичные буквы
        letters = [item for item in od]
        freq = [od[item] for item in od]
        df = pandas.DataFrame({'Frequencies': freq}, index=letters)
        df['Frequencies'] = df['Frequencies'] / df['Frequencies'].sum()
        for item in list(df['Frequencies']):
            res += item * log(item, 2)
    else:
        # биграммы
        df = pandas.DataFrame()
        for key in h_dict:
            df.at[key[0], key[1]] = h_dict[key]
        df.fillna(0)
        df = df / df.sum().sum()
        res = (df * (numpy.log2(df)).replace(-numpy.inf, 0)).sum().sum()
    df.to_excel(filename, sheet_name=sheetname)
    return res


def main():
    """ основной метод запуска приложения
    обрабатывает допустимые аргументы командной строки """
    warnings.filterwarnings("ignore")
    if os.path.exists(sys.argv[1]):
        # получение результата
        h1, h2, h3 = freq(file=sys.argv[1], space=True)
        h4, h5, h6 = freq(file=sys.argv[1], space=False)
        # запись в файл через методы pandas
        with pandas.ExcelWriter('freq.xlsx') as xlwr:
            h1 = export_data(h1, xlwr, 'h1(spaces)')
            h4 = export_data(h4, xlwr, 'h1(no spaces)')
            h2 = export_data(h2, xlwr, 'h2(spaces, interseption)')
            h3 = export_data(h3, xlwr, 'h2(spaces, no interseption)')
            h5 = export_data(h5, xlwr, 'h2 (no spaces, interseption)')
            h6 = export_data(h6, xlwr, 'h2_(no spaces, no interseption)')

            pandas.DataFrame(index=['With spaces', 'H1=', 'H2=', "H2'=",
                                    'Without spaces', 'H1=', 'H2=', "H2'="],
                             data={'values': ['', (-1) * h1, -1 / 2 * h2, -1 / 2 * h3,'',
                                              (-1) * h4, -1 / 2 * h5, -1 / 2 * h6]}).to_excel(xlwr, 'values')


if __name__ == '__main__':
    main()
