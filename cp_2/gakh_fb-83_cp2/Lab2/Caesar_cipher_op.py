from Alphabet_and_funcs import *

def c_encode(c_text, key):
       global alphabet_len
       c_nmbrs=get_numbers_of_characters(c_text)
       result=[]
       for i in range(0,len(c_nmbrs)):
              result.append((c_nmbrs[i] + key)%alphabet_len)
       return get_characters_of_numbers(result)

def c_decode(c_text, key):
       global alphabet_len
       c_nmbrs=get_numbers_of_characters(c_text)
       result=[]
       for i in range(0,len(c_nmbrs)):
              result.append((c_nmbrs[i] - key)%alphabet_len)
       return get_characters_of_numbers(result)

def c_deduce_key(text):
       cur_counts=get_counts_in_text(text)
       cur_freq_rating = sorted(cur_counts.items(), key=lambda item: item[1])[::-1]
       cur_freq_char=cur_freq_rating[0][0]
       key=alphabet[cur_freq_char]-alphabet[freq_rating[0]]
       return key
 

def c_break_ciphertext(text):
       return c_decode(text, c_deduce_key(text))
