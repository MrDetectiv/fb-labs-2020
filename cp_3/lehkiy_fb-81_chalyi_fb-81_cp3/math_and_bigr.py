import math

def gcd_Evkl(a,n,mode):  #функция для нахождения НСД(а,n) расширеным алгоритмом Эвклида

    r ={} #словарь для хранения ri
    q = {} # словарь для хранения qi
    #if (a < n): a,n=n,a #меняем местами для коректной работы алгоритма
    r[0]=a
    r[1]=n
    iter = 1 #итератор
    while(r[iter-1]%r[iter]!=0):
        r[iter+1]=r[iter-1]%r[iter]
        q[iter] = r[iter - 1] // r[iter]
        iter += 1

    gcd = r[iter] #переменная для НСД
    if mode == 0:return gcd
    if mode == 1: return gcd, r,
    if mode == 2: return gcd, r, q

def converse_a(a,n): #вычисляет обратный элемент для а по модулю n
    gcd_result=gcd_Evkl(n,a,2)
    gcd=gcd_result[0]
    if (gcd!=1):
        #print('Невозможно найти значение, НСД не равен 1.')
        return None
    else:
     q=gcd_result[2]
     u = {}
     v = {}
     u[0] = 1
     u[1] = 0
     v[0] = 0
     v[1] = 1
     iter=1
     while (iter<=len(q)):
        u[iter+1] = u[iter-1]-q[iter]*u[iter]
        v[iter + 1] = v[iter - 1] - q[iter] * v[iter]
        iter+=1
    result =  v[len(v)-1]
    if result<0: return n+result
    else:return result

def solve_lin_por(a,b,n): #розв`язуємо лінійне порівняння виду ax=b(mod n)
   d=gcd_Evkl(a,n,0)
   if (d==1): #одно решение
       if(converse_a(a, n)!=None):
           x = (converse_a(a, n) * b)%n
           return x%n
       else:
           return None
   elif gcd_Evkl(d,b,0)==1: #нет решений
       return None
   elif d>1:#получаем d решений в массиве
       x0=solve_lin_por(a//d,b//d,n//d)
       X= []
       for i in range(0,d):
          x=x0+(n//d)*i
          X.append(x)
       return X

def clear_text(text,alf): #чистим текст от символов которых нет в заданом алфавите
    text1=text
    text2=''
    for letter in alf:
        text1 = text1.replace(letter.upper(), letter)
    for letter in text1:
        if alf.find(letter)!=-1:
            text2=text2+letter
    return text2

def count_bigr_freq(text,n): #выводит самых встречающихся биграм
   freq={}
   sum=0
   for i in range(0,len(text)-1,2):
       key=text[i]+text[i+1]
       if freq.get(key,-1)==-1:
           freq[key]=0
       freq[key]+=1
       sum+=1

   for key1 in freq:
       freq[key1]=freq[key1]/len(text)
   n_max_keys=[]
   freq1=freq.copy()
   for i in range(0,n):
       maximum = max(freq1.values())
       for key, value in freq1.items():
           if value == maximum:
              n_max_keys.append(key)
              freq1[key]=0
   return n_max_keys

def count_mono_freq(text,n,mode): #выводит самых встречающихся биграм
   freq={}
   sum=0
   for i in range(0,len(text)):
       key=text[i]
       if freq.get(key,-1)==-1:
           freq[key]=0
       freq[key]+=1
       sum+=1


   for key1 in freq:
       freq[key1]=freq[key1]/len(text)
   n_max_keys=[]
   freq1=freq.copy()
   for i in range(0,n):
       if mode == 'min':
          minimum = min(freq1.values())
          for key, value in freq1.items():
             if value == minimum:
                 n_max_keys.append(key)
                 freq1[key]=1
       if mode == 'max':
          maximum = max(freq1.values())
          for key, value in freq1.items():
             if value == maximum:
                 n_max_keys.append(key)
                 freq1[key]=0
   return n_max_keys

def entrophy(text):
    freq = {}
    sum = 0
    for i in range(0, len(text)):
        key = text[i]
        if freq.get(key, -1) == -1:
            freq[key] = 0
        freq[key] += 1
        sum += 1
    for key1 in freq:
        freq[key1] = freq[key1] / len(text)
    entr=0
    for key2 in freq:
        entr=entr+freq[key2]*math.log2(freq[key2])
    return -entr

if __name__ == '__main__':
 print(gcd_Evkl(132,2671234,2))
 print(converse_a(19,31))
 print(solve_lin_por(2,7,8))
