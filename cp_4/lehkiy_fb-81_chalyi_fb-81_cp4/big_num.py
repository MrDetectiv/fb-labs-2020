import random

def ext_gcd(num1,num2):
    u1 = 1;
    v1 = 0;
    u2 = 0;
    v2 = 1
    while (1):
        quot = -(num1 // num2)
        num1 = num1 % num2
        u1 = u1 + quot * u2;
        v1 = v1 + quot * v2
        if (num1 == 0):
            return [num2, u2, v2]
        quot = -(num2 // num1)
        num2 = num2 % num1;
        u2 = u2 + quot * u1;
        v2 = v2 + quot * v1
        if (num2 == 0):
            return [num1, u1, v1]

def gcd(num1,num2):
    res = ext_gcd(num1,num2)
    return res[0]

def converse_a(a,n):
    res = ext_gcd(a,n)
    if res[0]==1:
      if a<=n: return res[1]
      if a>n: return res[2]
    else: return None

def rand_num(min,max):
    return random.randint(min,max)

def generate_prime(len_in_bits):
    min = 2**(len_in_bits-1)+1
    max = 2**len_in_bits-1
    while True:
       r_num = rand_num(min,max)
       for i in range(0,(max-r_num+(1-r_num%2))//2):
           if r_num % 2 == 0:
              r_num+=1
           if small_dividers_test(r_num):
              if Miller_Rabin_test(r_num):
                 return r_num
           r_num+=2

def small_dividers_test(num):
    small_primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,
                    53,59,61,67,71,73,79,83,89,97,101,103]
    for i in small_primes:
        if num%i==0 and num//i!=1: return False
    return True

def Miller_Rabin_test(num):
   k = 100
   d = num - 1
   s = 0

   while d%2 == 0:
       s+=1
       d = d // 2

   for i in range(k):
       x = rand_num(2, num - 1)
       if gcd(x, num)>1:
           return False
       x1 = pow(x,d,num)
       if x1 == 1 or x1 == num - 1: continue
       else:
          pseudo_p = False
          for r in range(1,s):
              xr = x1*pow(x,2**r,num)
              if xr == -1 or xr ==num - 1: pseudo_p=True
              elif xr == 1:  return False
          if pseudo_p==False:
              return False
   return True


if __name__ == '__main__':
   # print(ext_gcd(31,17))
   # print(converse_a(31,17))
   print(small_dividers_test((2**103)-1))
   print(Miller_Rabin_test(66858743038727231331219171450172577743735442856553093406016762546768143241799))
   print(generate_prime(256))


