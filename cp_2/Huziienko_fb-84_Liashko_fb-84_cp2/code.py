import codecs
import re
from collections import Counter

alp='абвгдежзийклмнопрстуфхцчшщъыьэюя'

def Open_file(file):
 file_o=codecs.open(file,"r","utf-8")
 text=file_o.read()
 text=text.lower()
 text=text.replace('ё','е')
 regular=re.compile('[^а-яА-Я]')
 text=regular.sub('',text)
 #print(text)
 return text;

def Keys(num):
    if num in range(2,6):
        if num==2:
            key='та'
        if num==3:
            key='род'
        if num==4:
            key='сова'
        if num==5:
            key='каноэ'
    else:
        key='абстракционизм'
    return key;

def Decr_Encr(text,alp,key,de):
    values=list()
    numbers=list()
    new_text=''
    for value in range(32):
            values.append(value)
    dictionary={}
    dictionary=dict(zip(alp,values))
    for item in range(len(text)):
            if de=='encr':
                a=(dictionary[text[item]]+dictionary[key[item]])%len(alp)
            if de=='decr':
                a=(dictionary[text[item]]-dictionary[key[item]])%len(alp)  
            numbers.append(a)
    for num in numbers:
       for key in dictionary:
            if num==dictionary[key]:
                new_text+=key
    return new_text;

def BigKey(key,text):
    Big_key=''
    for i in range(len(text)):
            Big_key+=key[i%len(key)] 
    return Big_key;

def Print_encr(num,T):
    print()
    print('KEY:', Keys(num))
    print('r =',num)
    Big_key=BigKey(Keys(num),T)
    print("ENCRYPTED TEXT")
    encr_text=Decr_Encr(T,alp,Big_key,'encr')
    print(encr_text)
    
def Enc_value(num,T):
    Big_key=BigKey(Keys(num),T)
    encr_text=Decr_Encr(T,alp,Big_key,'encr')
    return encr_text
    
#COUNT
def Letter_counter(text):
    count=Counter(text)
    return count;
#INDEX
def Index(diction,n):
    i=0
    for key in diction:
        i+=diction[key]*(diction[key]-1)
    i=i*(1/(n*(n-1)))
    return i

def Index_check(diction,length):
    index=0
    for key in diction:
        diction[key]=diction[key]/length
        index+=diction[key]*diction[key]
    return index

def Print_index(text,n,num):
    dic=Letter_counter(text)
    index=Index(dic,len(text))
    print('INDEX FOR TEXT')
    if n==2:
        print('With key length ',num)
    print('I(Y) = ',index)
    if n==1:
        M=Open_file("text_c.txt")
        dic_M=Letter_counter(M)
        index_ch=Index_check(dic_M,len(M))
        print('MI(Y) = ',index_ch)    
    print()
    
def Make_Y(text,r):
    l=list()
    n=len(text)
    for item in range(r):
        new_text=''
        for i in range(item,n,r):
            #print(text[i])
            new_text+=text[i]
        l.insert(item,new_text)
    #print(l)
    return l;
 
def Index_Y(list_r):
    n=len(list_r)
    new_list=[]
    print('For r= ', n)
    for i in range(n):
        a=Letter_counter(list_r[i])
        num=len(list_r[i])
        b=Index(a,num)
        #print('Index for Y',i,'=',b)
        new_list.append(b)
    return new_list

def Index_middle(list_k):
    mid=0
    for i in range(len(list_k)):
        mid+=list_k[i]
    mid=mid/len(list_k)
    print("Index=",mid)
    return mid

def Print_index_Y(key,text):
    Yi=list()
    Yi=Make_Y(text,key)
    index_Yi=[]
    index_Yi=Index_Y(Yi)
    Index_middle(index_Yi)
#STATISTIC 
def Statistic(list_Y,r):
    cron=list()
    item=0
    for item in range(0,r):
        a=''
        n=len(list_Y[item])
        a=list_Y[item]
        it=0
        for i in range(0,n-r):
            if a[i]==a[i+r]:
                it=it+1
        cron.append(it)
    return(cron)

def Sum_statistic(list_k):
    mid=0
    for i in range(len(list_k)):
        mid+=list_k[i]
    return mid

def Key_find(Yi,dic):
    most_comm=[14,5]
    kis=list()
    keysss=keysss1=keysss0=list()
    ki=0
    k=''
    print("Most common letters")
    for item in range(15):
        li=list()
        print("-----Y",item,"-----")
        dict_Y=Letter_counter(Yi[item])
        y=''
        y=dict_Y.most_common(1)[0][0]
        print(y)
        y_value=0
        kis.append(y)
    for it in range(15):
        for key in dic:
            if kis[it]==key:
                y_value=dic[key]
                keysss.append(y_value)
    print("Most kommon letters in Yi")
    print(keysss)
    a=b=''
    print ("k=(y-x)mod m")
    print ("x=о - 1 of most common letters in lenguage")
    for i in range(15):
        keysss0[i]=(keysss[i]-most_comm[0])%32
    print(keysss0)
    for i in range(15):
        for key in dic:
            if keysss0[i]==dic[key]:
                a+=key
    print (a)
    print ("x=и - 2 of most common letters in lenguage")
    for i in range(15):
        keysss1[i]=(keysss[i]+most_comm[0]-most_comm[1])%32
    print(keysss1)    
    for i in range(15):
        for key in dic:
            if keysss1[i]==dic[key]:
                b+=key
    print (b)
                
        


#main
print("TASK 1")
print()
print("TEXT")
T=Open_file("1.txt")
print(T)
print()
for i in range(2,7,1):
    if i==6:
        Print_encr(14,T)
    else:
        Print_encr(i,T)
    
print("TASK 2")
print()
for i in range(1,7):
    if i==1 or i==6:
        if i==1:
            Print_index(T,1,0)
        else:
            Print_index(Enc_value(14,T),2,14)
    else:
        Print_index(Enc_value(i,T),2,i)

print("TASK 3")
V=Open_file("var7.txt")
print("INDEX")
for i in range(2,31):
    Print_index_Y(i,V)
    print()
print("STATISTIC")
for it in range(2,31):
    Yi=list()
    Yi=Make_Y(V,it)
    test_cron=[]
    test_cron=Statistic(Yi,it)
    print("Statistic for r=",it," :",Sum_statistic(test_cron))
    
values=list()
for value in range(32):
    values.append(value)
dictionary={}
dictionary=dict(zip(alp,values))

print()
print("----------------r=15-----------------")
print()
print("FIND KEY")
Key_find(Yi,dictionary)
print()
key='арудазовархимаг'
print("------------KEY: ",key,"--------------")
print()
Yi=list()
Yi=Make_Y(V,15)

print("TEXT-Encr")
print()
print(V)
B_key=BigKey(key,V)
print()
print("TEXT-Decr")
print()
print(Decr_Encr(V,alp,B_key,'decr'))    
