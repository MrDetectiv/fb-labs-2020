import codecs
import re
from collections import Counter
import math

alphabet1=['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я']
alphabet2=['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я',' ']

#function
#open file and edit
def Read_text_from_file(file_text,a):
    file=codecs.open(file_text,"r","utf-8") 
    text = file.read() 
    text=text.lower()
    text=text.replace('ъ','ь').replace('ё','е') 
    #reg1=re.compile("^\s+|\n|\r|\s+$")
    if a=='without':
        regular=re.compile('[^а-яА-Я]')
        text=regular.sub('',text)
    if a=='with':
        regular=re.compile('[^а-яА-Я ]')
        text=regular.sub('',text)
        text = re.sub(" +", " ", text)
    #print(text[:100])
    file.close() 
    return text;


def Letter_counter(text):
    count=Counter(text)
    return count;

def Letter_fr(old_dict,length):
    keys=list(old_dict.keys())
    #print(keys)
    keys.sort() 
    val=[]
    for i in keys:
     for key in old_dict:
      if i==key:
        val.insert(keys.index(i),(old_dict[key])) 
    new_dict={} 
    new_dict=dict(zip(keys, val)) 
    for k in new_dict:
        new_dict[k]=new_dict[k]/length
        #print(k,'->',new_dict[k])
    return new_dict;

def Entrophy(d):
    ent=0
    for key in d:
        ent+=-d[key]*math.log(d[key],2)
    return ent;

def Excess(entro,num):
    if num=='without':
        i=len(alphabet1)
    if num=='with':
        i=len(alphabet2)
        
    ex=1-((entro)/math.log(i,2))
    return ex;

#menu
def Menu(num):
    if num==1 or num==2:
        if num==1:
            print('MONOGRAMM WITHOUT SPACE')
            ftext=Read_text_from_file("text_w.txt",'without')
            
        else:
            print('MONOGRAMM WITH SPACE')
            ftext=Read_text_from_file("text_w.txt",'with')
        length=len(ftext)
        first_old_dic=Letter_counter(ftext)
        first_new_dic=Letter_fr(first_old_dic,length)
        entrophy=Entrophy(first_new_dic)
        if num==1:
            excess_ent=Excess(entrophy,'without')
        else:
            excess_ent=Excess(entrophy,'with')
        print('H1= ',entrophy)
        
    if num in range(3,7):
        if num==3 or num==4:
            print('BIGRAMM WITHOUT SPACE:')
            ftext=Read_text_from_file("text_w.txt",'without')
            if num==3:
                print('-intersect')
                couples=Couple(ftext,2,1)
            if num==4:
                 print('-no intersect')
                 couples=Couple(ftext,2,2)

            a=Letter_counter(couples)
            suma=sum(a.values())
            b=Couple_fr(a,suma,'without')
            ent_couple=Entrophy_couple(b)
            excess_ent=Excess(ent_couple,'without')
        if num==5 or num==6:
            print('BIGRAMM WITH SPACE:')
            ftext=Read_text_from_file("texr_w.txt",'with')
            if num==5:
                print('-intersect')
                couples=Couple(ftext,2,1)
            if num==6:
                 print('-no intersect')
                 couples=Couple(ftext,2,2)

            a=Letter_counter(couples)
            suma=sum(a.values())
            b=Couple_fr(a,suma,'with')
            ent_couple=Entrophy_couple(b)
            excess_ent=Excess(ent_couple,'with')
            
       
        print('H2=',ent_couple)
    print('R= ',excess_ent)
    print('')
                

    
#BIGRAMM
def Couple(text,step,num): 
    length=len(text)-1
    couples=[]
    if num==1:# пер
        for item in range(length):
            couples.append(text[item:item+step])
            #print(text[item:item+step])
    if num==2:# не пер
        for item in range(0,length,num):
            couples.append(text[item:item+step])
           # print(text[item:item+step])
    return couples


def Couple_fr(a,suma,num):
    if num=='without':
        alphabet=alphabet1
    if num=='with':
        alphabet=alphabet2
    n=m=len(alphabet)+1
    arr=[0]*n
    for i in range(n):
        arr[i]=[0]*m
    for j in range (1,len(arr[0])):
        arr[0][j]=alphabet[j-1]
    for i in range (1,len(arr)):
        arr[i][0]=alphabet[i-1]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for key in a:
                st=str(arr[i][0])+str(arr[0][j])
                if st==key:
                    arr[i][j]=a[key]/suma
    #for i in range (1,len(arr)):
     #   for j in range(1,len(arr[i])):
      #      print(arr[i][0]+arr[0][j],'->',"{:.6f}".format(arr[i][j]))
    return arr;

def Entrophy_couple(arr):
    ent=0
    item=0
    for i in range(1,len(arr)):
        for j in range(1,len(arr[i])):
            item=arr[i][j]
            if item==0:
                ent+=0
            else:
                ent+=-(item)*math.log((item),2)
        
    ent=ent/2;
    return ent;
    
def Cool(entro):
    ex=1-((entro)/math.log(32,2))
    return ex
#main
Menu(1)
Menu(2)
Menu(3)
Menu(4)
Menu(5)
Menu(6)

#COOL
H_10_min=2.10615438910484
H_10_max=2.90496204857619
H_20_min=1.4954425876343
H_20_max=2.24625822839247
H_30_min=0.992106545149207
H_30_max=1.60374130890315

R_10_min=Cool(H_10_min)
R_10_max=Cool(H_10_max)
R_20_min=Cool(H_20_min)
R_20_max=Cool(H_20_max)
R_30_min=Cool(H_30_min)
R_30_max=Cool(H_30_max)
print()
print('COOL PINK PROGRAM')
print(H_10_min," < H_10 < ",H_10_max)
print(R_10_min," < R_10 < ",R_10_max)
print(H_20_min," < H_20 < ",H_20_max)
print(R_20_min," < R_20 < ",R_20_max)
print(H_30_min," < H_30 < ",H_30_max)
print(R_30_min," < R_30 < ",R_30_max)



        



