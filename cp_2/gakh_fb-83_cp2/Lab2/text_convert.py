from Alphabet_and_funcs import *


def filter_raw_text(f_name):
       global alphabet
       raw_text = codecs.open( f_name, "r", "utf-8" ).read()
       filtered_text=''
       for char in raw_text:
              if char in alphabet.keys():
                     filtered_text+=char.lower()
       return filtered_text
with codecs.open('.\\my_text\\plain_text.txt', "w","utf-8") as file:
       file.write(filter_raw_text('.\\my_text\\raw_plaintext.txt'))
file.close()
       
