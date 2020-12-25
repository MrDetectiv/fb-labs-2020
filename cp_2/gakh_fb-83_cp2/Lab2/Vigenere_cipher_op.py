from Alphabet_and_funcs import *

def v_encode(c_text, key):
       global alphabet_len
       c_nmbrs=get_numbers_of_characters(c_text)
       result=[]
       for i in range(0,len(c_nmbrs)):
              result.append((c_nmbrs[i] + num(key[i%len(key)]))%alphabet_len)
       return get_characters_of_numbers(result)

def v_decode(c_text, key):
       global alphabet_len
       c_nmbrs=get_numbers_of_characters(c_text)
       result=[]
       for i in range(0,len(c_nmbrs)):
              result.append((c_nmbrs[i] - num(key[i%len(key)]))%alphabet_len)
       return get_characters_of_numbers(result)

def divide_text(text, key_len):
       result = ['']*key_len
       for offset in range(0,key_len):
              for i in range(offset, len(text), key_len):
                     result[offset]+=text[i]
       return result

