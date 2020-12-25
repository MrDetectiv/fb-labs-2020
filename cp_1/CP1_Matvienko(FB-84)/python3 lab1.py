import pprint, collections, re, string, math

file=open('d:/UniverziTET/Crypt/lab1/1.txt','r',encoding='utf-8').read()
file=file.lower()
rus_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
rus_alph2 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

alph=[rus_alph,rus_alph2]

for j in range(0,2,1):
    r_alph=alph[j]
    print()
    
    if j==0: print('----------Текст с пробелами: -----------')
    else: print('-----------Текст без пробелов: -----------')

    for letter in file:
        if letter not in r_alph:
            file=file.replace(letter,'')

    file=file.replace('ё','е').replace('ъ','ь').replace('/n','')
    file = re.sub(" +", " ", file)

    amount=len(file)
    print('Количество букв: ', amount)
    print()

# # монограма

    word_count = collections.Counter(file)

    for i in word_count:
        fr=100*word_count[i]/(amount)
        fr='%.5f' % fr
        word_count[i]=fr

    

    pprint.pprint(dict(word_count))
    print()

    for i in word_count:
        fr=float(word_count[i])/100
        fr='%.5f' % fr
        word_count[i]=fr

    bigram_count={}
    bigram_r_count={}
    bigrams=[]
    bigrams_r=[]
    length=len(file)-1

# # биграммы

#     #перетин

    for i in range(0,length,1) :
        bigrams.append(file[i]+file[i+1])
 
    bigram_count=collections.Counter(bigrams)

    
    print('Биграмы с перетином')
    print()
    for i in bigram_count:
        fr=100*float(bigram_count[i])/(len(bigrams))
        fr='%.5f' % fr
        bigram_count[i]=fr



    pprint.pprint(dict(bigram_count))
    
    for i in bigram_count:
        fr=float(bigram_count[i])/100
        bigram_count[i]=fr


#     #без перетину
    
    print('Биграмы без перетину')
    print()
    for i in range(0,length,2) :
        bigrams_r.append(file[i]+file[i+1])

    bigram_r_count=collections.Counter(bigrams_r)

    for i in bigram_r_count:
        fr=100*float(bigram_r_count[i])/(len(bigrams_r))
        fr='%.5f' % fr
        bigram_r_count[i]=fr

    pprint.pprint(dict(bigram_r_count))

    for i in bigram_r_count:
        fr=float(bigram_r_count[i])/100
        bigram_r_count[i]=fr

#     #Ентропия
    
    
    entr=0
    for i in word_count:
        fr=float(word_count[i])
        if fr==0: 
            entr+=0
        else: entr+=-(fr)*math.log((fr),2)
     
    
    nadl=1-(entr/math.log(32,2))

    print("Ентропія монограми: ",entr) 
    print("Надлишковість монограми: ",nadl) 
    print()

    entr=0
    for i in bigram_count:
        fr=float(bigram_count[i])
        if fr==0: 
            entr+=0
        else: entr+=-(fr)*math.log((fr),2)

    entr=entr/2
    nadl=1-(entr/math.log(32,2))

    print("Ентропія біграми з перетином: ",entr)  
    print("Надлишковість біграми з перетином: ",nadl)     
    print()
    
    entr=0
    for i in bigram_r_count:
        fr=float(bigram_r_count[i])
        if fr==0: 
            entr+=0
        else: entr+=-(fr)*math.log((fr),2)
    entr=entr/2
    nadl=1-(entr/math.log(32,2))

    print("Ентропія біграми без перетиу: ",entr)   
    print("Надлишковість біграми без перетину: ",nadl)
    print()
    
nadl1=nadl2=0
entr1=2.75209746140447
entr2=3.27790722401634
nadl1=1-(entr1/math.log(32,2))
nadl2=1-(entr2/math.log(32,2))

print("Ентропія:",entr1 ,"<H(10): ",entr2)   
print("Надлишковість: " ,nadl1,"<H(10): ",nadl2)
print()

nadl1=nadl2=0
entr1=2.8479692013934
entr2=3.36617789503918
nadl1=1-(entr1/math.log(32,2))
nadl2=1-(entr2/math.log(32,2))

print("Ентропія:",entr1 ,"<H(20): ",entr2)   
print("Надлишковість: " ,nadl1,"<H(20): ",nadl2)
print()

nadl1=nadl2=0
entr1=2.12762406575717
entr2=2.68397148189694
nadl1=1-(entr1/math.log(32,2))
nadl2=1-(entr2/math.log(32,2))
print()

print("Ентропія:",entr1 ,"<H(30): ",entr2)   
print("Надлишковість: " ,nadl1,"<H(30): ",nadl2)
print()

