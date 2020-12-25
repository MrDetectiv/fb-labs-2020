import re, math, string, collections, pprint, operator,collections, operator

popular_bigr=['ст','но','то','на','ен']
rus_alph_crypt = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
letter_place={}
bigram_afin_amount={}
bigram_afin_place_amount={}
i=0
for letter in rus_alph_crypt:
    letter_place[letter]=i
    # place_letter[i]=letter
    i+=1

for letter1 in rus_alph_crypt:
    for letter2 in rus_alph_crypt:
        bigr=letter1+letter2
        bigr_amount=letter_place[letter1]*31+letter_place[letter2]
        bigram_afin_amount[bigr_amount]=bigr
        bigram_afin_place_amount[bigr]=bigr_amount

        
def gcd(a, b):
  if b == 0: return a
  else: return gcd(b, a % b)

def Evkl(a, b):
    if a == 0: return (b, 0, 1)
    else: 
        g, x, y = Evkl(b % a, a)
        return (g, y - (b // a) * x, x)
 
def Evkl_exp(b, n):
    g, x, y = Evkl(b, n)
    if g == 1:
        return x % n


def Test(val1,val2,mod):
    
    d=gcd(val1,mod)
    A=[]
    if d==1:    
        a=(Evkl_exp(val1, mod)*val2)%mod
        A.append(a)
        return A

    else:
        if val2%d==0:
            n=mod/d
            a0=((Evkl_exp(val1/d, n))*(val2/d))%n
          
            for i in range (0, d, 1):
                a=int((a0+i*n)%(mod**2))
                A.append(a)
                
        return A


def Analysis(mass):
    th_index=0.055
    closest=9999
    key_r=0
    print("\tFinding of index\n")
    for i in range(0,len(mass),1):
        iq=math.fabs(th_index-mass[i][1])
        if iq<closest:
            print("Closest meaning is:",mass[i][1],"with key=(",mass[i][2],",",mass[i][3],"):", iq,"<",closest)
            closest=iq
            closest_amount=mass[i][1]
            key_r=i
    print("\nINDEX IS:",mass[key_r][1])
    #print("\nKey=(",mass[key_r][2],",",mass[key_r][3],") Index=", closest_amount)
    return(key_r, closest_amount)


def Analysis_check(mass,closest_amount):
    print("\n\tCheck\n")
    if 'о' in mass[4] and 'а' in mass[4] and 'е' in mass[4] and 'ф' not in mass[4] and 'щ' not in mass[4] and 'ь' not in mass[4]:
        #print("\nEverything is right, dude. It is your decrypted text.\n\n")
        print("Decrypted text with key=(",mass[2],",",mass[3],") with index=", closest_amount ,": \n\n", mass[0])
        return("nice work")
    else:
        print("Key=(",mass[2],",",mass[3],"). Error is:")
        if 'о' in mass[4]:
            print('о is absent\n')
        if 'а' in mass[4]: 
            print('а is absent\n')
        if 'е' in mass[4]:
            print('е is absent\n')
        if 'ф' not in mass[4]:
            print('ф is present\n')
        if 'щ' not in mass[4]: 
            print('щ is present\n')
        if 'ь' not in mass[4]:
            print('ь is present\n')
        print("\nDecrypted text is wrong. I will try again")
        return(mass)


##TASK

file=open('d:/UniverziTET/Crypt/lab3/15.txt','r',encoding='utf-8').read()
file=file.replace('\n','')
bigrams_r=[]
bigram_count={}
bigr_count_fr={}
c=[]

for i in range(0,len(file)-1,2) :
    bigrams_r.append(file[i]+file[i+1])

bigram_count=collections.Counter(bigrams_r)

for i in bigram_count:
    bigr_count_fr[i]=round(int(bigram_count[i])/len(file)*100,4)

bigram_count = sorted(bigram_count.items(), key=operator.itemgetter(1),reverse=True)
bigr_count_fr = sorted(bigr_count_fr.items(), key=operator.itemgetter(1),reverse=True)
for i in range(5):
    c.append(bigram_count[i][0])
    # print(bigr_count_fr[i])

print("\nLanguage:",popular_bigr, "\n\nEncrypted:", c)
X=[]
Y=[]

print("\n\nEncrypted text:\n",file,"\n\n")
for i in range(0,5,1):
    x=letter_place[str(popular_bigr[i])[0]]*31+letter_place[str(popular_bigr[i])[1]]
    y=letter_place[str(c[i])[0]]*31+letter_place[str(c[i])[1]]
    X.append(x%(31**2))
    Y.append(y%(31**2))

A=[]
B=[]
Y_mass=[]
X_mass=[]
A_mass=[]
var=4

for i in range (4):
    for j in range(4):    
        if i!=j:
            y_diff=int((Y[i]-Y[j])%(31**2))
            x_diff=int((X[i]-X[j])%(31**2))
            Y_mass.append((y_diff,Y[i]))
            X_mass.append((x_diff,X[i]))       
    #var=var-1

for i in range(len(X_mass)):
    for j in range(len(Y_mass)):    
        A_mass=Test(X_mass[i][0], Y_mass[j][0], 31**2)
        for a in A_mass:
            b=(Y_mass[j][1]-a*X_mass[i][1])%(31**2)
            A.append(a)
            B.append(b)          
        A_mass=Test(X_mass[j][0], Y_mass[i][0], 31**2)
        for a in A_mass:
            b=(Y_mass[i][1]-a*X_mass[j][1])%(31**2)
            A.append(a)
            B.append(b)          


# print("\nKeys:")
# for i in range (0, len(A),1):
#     print(A[i],B[i])
Analysis_mass=[]
print("\n")
for i in range (0, len(A),1):
    decr_text=""
    for j in range (0, len(bigrams_r),1):
        amount=bigram_afin_place_amount[bigrams_r[j]]
        xi=Test(A[i],amount-B[i], 31**2)
        x_am=""
        for k in xi:
            x_am=bigram_afin_amount[k]

        decr_text+=x_am
    
    word_count_pop=[]
    word_count=collections.Counter(decr_text)
    word_count1 = sorted(word_count.items(), key=operator.itemgetter(1),reverse=True)
    for k in range(5):
        word_count_pop.append(word_count1[k][0])
    index_decr_text=0
    for j in word_count:
        index_decr_text+=word_count[j]*(word_count[j]-1)

    index_decr_text=index_decr_text/(len(decr_text)*(len(decr_text)-1))
    Analysis_mass.append((decr_text, index_decr_text,A[i],B[i], word_count_pop))

ret="a"
while ret!="nice work":
    key=Analysis(Analysis_mass)

    ret=Analysis_check(Analysis_mass[key[0]],key[1])    
    if ret!="nice work":
        del Analysis_mass[key]

 