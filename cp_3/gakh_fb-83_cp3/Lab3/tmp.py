from Affine_cipher import *


text = filter_raw_text(".\\06.txt").upper()
cur_counts=get_counts_of_bigramms(text)

cur_counts = sorted(cur_counts.items(), key=lambda item: item[1])[::-1]

for i in range(0,20):
       print("{},  ".format(cur_counts[i][0]), end=" ")

#with codecs.open('.\\bigramms.txt', "w","utf-8") as file:
#       for c in cur_counts:
#              file.write("'{}', ".format(c[0]))
#file.close()
