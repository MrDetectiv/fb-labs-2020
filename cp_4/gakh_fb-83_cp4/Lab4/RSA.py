from Miller_Rabin import *
def GenerateKeyPair(n_bits):
       ans = {'p':0, 'q':0, 'n':0, 'e':0, 'd':0}
       print('Generating random prime p...')
       p = get_prime_between(n_bits//2)
       print('Generating random prime q...')
       q = get_prime_between(n_bits//2)
       n = p*q
       fi = (p-1)*(q-1)
       print('Generating random prime e...')
       e = get_prime_between(n_bits//8)
              
       d = reverse_mod(e,fi)

       if (e*d) % fi == 1:
              print('Public and secret keys are correct.')
       else:
              print('Keys weren`t generated correctly.')
              return None
       ans['p'] = p
       ans['q'] = q
       ans['n'] = n
       ans['e'] = e
       ans['d'] = d
       return ans
def Encrypt(M, e, n):
       return fast_power(M, e, n)
def Decrypt(C, d, n):
       return fast_power(C, d, n)
def Sign(M, d, n):
       sign = Encrypt(M, d, n)
       return [M, sign]
def Verify(S, e, n):
       M_deciphered = Decrypt(S[1], e, n)
       if S[0] == M_deciphered:
              return S[0]
       return None
def SendKey(k, d, n, e1, n1):
       k1_S = Sign(k, d, n)
       #print(k1_S)
       k_S = []
       k_S.append(Encrypt(k1_S[0], e1, n1))
       k_S.append(Encrypt(k1_S[1], e1, n1))
       return k_S
def ReceiveKey(MS, d1, n1, e, n):
       k_S = []
       k_S.append(Decrypt(MS[0], d1, n1))
       k_S.append(Decrypt(MS[1], d1, n1))
       #print(k_S)
       return Verify(k_S, e, n)

























       
