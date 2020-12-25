from kostetska_fb_83_cp1.functions.functions import *


# ask for filename
print('Print name of the file from directory text/ (d for default): ', end='')
file_to_open = input()
if file_to_open == 'd':
    file_to_open = 'cleared_text.txt'


# get text from file, clean text from spaces
with open('text/'+file_to_open, 'r', encoding='utf-8') as file:
    text = ''.join(file.readlines())

text_no_spaces = text.replace(' ', '')


# open file for results
res_file = open('results/results_'+file_to_open, 'w', encoding='utf-8')


# write to file frequencies for 6 cases
res_file.write('                                             FREQUENCIES (in %)\n')

res_file.write('\n\n                                             unigrams with spaces\n')
fr_uni_with_spaces = count_unigrams(text)
for c in fr_uni_with_spaces:
    res_file.write(c + ": " + "{:.4f}".format(fr_uni_with_spaces[c]*100) + '\n')

res_file.write('\n\n                                             unigrams no spaces\n')
fr_uni_no_spaces = count_unigrams(text_no_spaces)
for c in fr_uni_no_spaces:
    res_file.write(c + ": " + "{:.4f}".format(fr_uni_no_spaces[c]*100) + '\n')

res_file.write('\n\n                                             bigrams with spaces, intersection yes\n')
fr_bi_with_spaces_yes = count_bigrams(text, True)
print_bigrams_table(fr_bi_with_spaces_yes, res_file)

res_file.write('\n\n                                             bigrams no spaces, intersection yes\n')
fr_bi_no_spaces_yes = count_bigrams(text_no_spaces, True)
print_bigrams_table(fr_bi_no_spaces_yes, res_file)

res_file.write('\n\n                                             bigrams with spaces, intersection no\n')
fr_bi_with_spaces_no = count_bigrams(text, False)
print_bigrams_table(fr_bi_with_spaces_no, res_file)

res_file.write('\n\n                                             bigrams no spaces, intersection no\n')
fr_bi_no_spaces_no = count_bigrams(text_no_spaces, False)
print_bigrams_table(fr_bi_no_spaces_no, res_file)


# write to file entropy for 6 cases

res_file.write('\n\n                                                      ENTROPY (in bits)\n\n')
res_file.write('Unigrams with spaces:                                    '+"{:.4f}".format(entropy(fr_uni_with_spaces))+'\n')
res_file.write('Unigrams no spaces:                                      '+"{:.4f}".format(entropy(fr_uni_no_spaces))+'\n')
res_file.write('Bigrams with spaces, intersection yes:                   '+"{:.4f}".format(entropy(fr_bi_with_spaces_yes))+'\n')
res_file.write('Bigrams no spaces, intersection yes:                     '+"{:.4f}".format(entropy(fr_bi_no_spaces_yes))+'\n')
res_file.write('Bigrams with spaces, intersection no:                    '+"{:.4f}".format(entropy(fr_bi_with_spaces_no))+'\n')
res_file.write('Bigrams no spaces, intersection no:                      '+"{:.4f}".format(entropy(fr_bi_no_spaces_no))+'\n')


# write to file redundancy for 6 cases + 3 for pink program
res_file.write('\n\n                                                      REDUNDANCY\n\n')
res_file.write('Unigrams with spaces:                                    '+"{:.4f}".format(redundancy(entropy(fr_uni_with_spaces), len(set(''.join(fr_uni_with_spaces))))*100)+'%\n')
res_file.write('Unigrams no spaces:                                      '+"{:.4f}".format(redundancy(entropy(fr_uni_no_spaces), len(set(''.join(fr_uni_no_spaces))))*100)+'%\n')
res_file.write('Bigrams with spaces, intersection yes:                   '+"{:.4f}".format(redundancy(entropy(fr_bi_with_spaces_yes), len(set(''.join(fr_bi_with_spaces_yes))))*100)+'%\n')
res_file.write('Bigrams no spaces, intersection yes:                     '+"{:.4f}".format(redundancy(entropy(fr_bi_no_spaces_yes), len(set(''.join(fr_bi_no_spaces_yes))))*100)+'%\n')
res_file.write('Bigrams with spaces, intersection no:                    '+"{:.4f}".format(redundancy(entropy(fr_bi_with_spaces_no), len(set(''.join(fr_bi_with_spaces_no))))*100)+'%\n')
res_file.write('Bigrams no spaces, intersection no:                      '+"{:.4f}".format(redundancy(entropy(fr_bi_no_spaces_no), len(set(''.join(fr_bi_no_spaces_no))))*100)+'%\n')

res_file.write('CoolPinkProgram H(10):                                   '+"{:.6f}".format(redundancy(3.15148903446785,32))+'<R<'+"{:.6f}".format(redundancy(2.25684412683459, 32))+'\n')
res_file.write('CoolPinkProgram H(20):                                   '+"{:.6f}".format(redundancy(2.7164756600148,32))+'<R<'+"{:.6f}".format(redundancy(1.84869890253276, 32))+'\n')
res_file.write('CoolPinkProgram H(30):                                   '+"{:.6f}".format(redundancy(2.61598090820483,32))+'<R<'+"{:.6f}".format(redundancy(1.6863475402192, 32))+'\n')


# close file with results
res_file.close()
