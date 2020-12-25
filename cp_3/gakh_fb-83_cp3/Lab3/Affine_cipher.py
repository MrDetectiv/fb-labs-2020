from Alphabet_and_funcs import *
from Math_operations import *
m=alphabet_len*alphabet_len

def encode_bigramm(bigramm):
       if len(bigramm)!=2:
              return None
       return num(bigramm[0])*alphabet_len+num(bigramm[1])
def decode_bigramm(a):
       if a<0 or a>alphabet_len*alphabet_len-1:
              return None
       return char(a//alphabet_len)+char(a%alphabet_len)

def encipher_affine(plain_text, a, b):
       if GCD(a,m)!=1:
              return None
       cipher_text=''
       for i in range(0,len(plain_text),2):
              X=encode_bigramm(plain_text[i]+plain_text[i+1])
              Y=(a*X+b)%m
              cipher_text+=decode_bigramm(Y)
       return cipher_text
def decipher_affine(cipher_text, a, b):
       if GCD(a,m)!=1:
              return None
       plain_text=''
       a_new=reverse_mod(a, m)
       b_new=-a_new*b
       for i in range(0,len(cipher_text),2):
              X=encode_bigramm(cipher_text[i]+cipher_text[i+1])
              Y=(a_new*X+b_new)%m
              plain_text+=decode_bigramm(Y)
       return plain_text
