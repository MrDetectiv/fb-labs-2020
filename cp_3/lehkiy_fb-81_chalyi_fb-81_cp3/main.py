import math_and_bigr as mbi
alph_rus='абвгдежзийклмнопрстуфхцчшщьыэюя'
log=' '
def int_b(bigr):
    return (alph_rus.find(bigr[0])*len(alph_rus))+alph_rus.find(bigr[1])

def attack_bigr(enc_b1,enc_b2,dec_b1,dec_b2,container):
    x1 = int_b(enc_b1)
    x2 = int_b(enc_b2)
    y1 = int_b(dec_b1)
    y2 = int_b(dec_b2)
    A =  x1 - x2
    B =  y1 - y2
    if A < 0: A = A+len(alph_rus) * len(alph_rus)
    if B < 0: B = B + len(alph_rus) * len(alph_rus)
    if(mbi.solve_lin_por(A,B, len(alph_rus) * len(alph_rus))!=None):
        if type(mbi.solve_lin_por(A,B, len(alph_rus) * len(alph_rus))) is int:
           a = mbi.solve_lin_por(A,B, len(alph_rus) * len(alph_rus))
           if mbi.gcd_Evkl(a,961,0)==1:
               b=(y1 - a * x1) % (len(alph_rus) * len(alph_rus))
               ddd = (a,b)
               if (ddd in container.values()) == False:
                 container[len(container)]=(a,b)
                 print(enc_b1 + '->' + dec_b1 + ' , ' + enc_b2 + '->' + dec_b2, 'key: ('+str(a)+','+str(b)+')')
                 fl=open('log.txt','a')
                 fl.write(enc_b1 + '->' + dec_b1 + ' , ' + enc_b2 + '->' + dec_b2+' key: ('+str(a)+','+str(b)+')\n')
                 fl.close()
        if type(mbi.solve_lin_por(A, B, len(alph_rus) * len(alph_rus))) is list:
            a = mbi.solve_lin_por(A, B, len(alph_rus) * len(alph_rus))
            for solution in a:
                b=(y1 - solution * x1) % (len(alph_rus) * len(alph_rus))
                if ((solution,b) in container.values())==False:
                   container[len(container)] = (solution,b)
                   print(enc_b1 + '->' + dec_b1 + ' , ' + enc_b2 + '->' + dec_b2,
                      'key: (' + str(solution) + ',' + str(b) + ')')
                   fl = open('log.txt', 'a')
                   fl.write(enc_b1 + '->' + dec_b1 + ' , ' + enc_b2 + '->' + dec_b2 + ' key: (' + str(solution) + ',' + str(
                      b) + ')\n')
                   fl.close()
    else:
        print(enc_b1+'->'+dec_b1+' , '+enc_b2+'->'+dec_b2, 'ЛП не розвязується')
        fl = open('log.txt', 'a')
        fl.write(
        enc_b1 + '->' + dec_b1 + ' , ' + enc_b2 + '->' + dec_b2 + ' ЛП не розвязується\n')
        fl.close()

def decrypt_bigr(bigr,key,value):
    a = key
    b = value
    Y = int_b(bigr)
    X = (mbi.converse_a(a,961)*(Y-b))%961
    decr_bigr = alph_rus[(X//31)]+ alph_rus[X%31]
    return decr_bigr
def encrypt_bigr(bigr,key,value):
    a = key
    b=value
    X = int_b(bigr)
    Y = (a*X+b)%961
    encr_bigr = alph_rus[(Y//31)]+ alph_rus[Y%31]
    return encr_bigr
def decrypt_text(text,key,value):
   decr_text=''
   for i in range(0,len(text),2):
     decr_text= decr_text+decrypt_bigr(text[i]+text[i+1],key,value)
   return decr_text
def encrypt_text(text,key,value):
   decr_text=''
   for i in range(0,len(text),2):
     decr_text= decr_text+encrypt_bigr(text[i]+text[i+1],key,value)
   return decr_text
def check_rus_text(text,key,value):
   encr_text=decrypt_text(text, key, value)
   entr=mbi.entrophy(encr_text)
   if (abs(entr-4.46))<0.1:
       print('('+str(key)+','+str(value)+'):','entrophy: '+str(entr), 'OK')
       fl = open('log.txt', 'a')
       fl.write(
           '('+str(key)+','+str(value)+'): '+'entrophy: '+str(entr)+ ' OK\n')
       fl.close()
       fd=open('decrypted.txt','w')
       fd.write(encr_text)
       fd.close()
   else:
       print('('+str(key)+','+str(value)+'):','entrophy: '+str(entr), 'FALSE')
       fl = open('log.txt', 'a')
       fl.write(
           '(' + str(key) + ',' + str(value) + '): ' + 'entrophy: ' + str(entr) + ' FALSE\n')
       fl.close()

def bigr_comb_attack(VT_b,SHT_b,n,keys):
    for i in range(0, n):
        for j in range(0, n):
            for k in range(1,n):
              if i!=k:
                attack_bigr(VT_b[i % n], VT_b[(i + k) % n], SHT_b[j % n], SHT_b[(j + 1) % n], keys)
                attack_bigr(VT_b[i % n], VT_b[(i + k) % n], SHT_b[(j + 1) % n], SHT_b[j % n], keys)

f = open('10.txt',encoding='UTF-8')
f1 = f.read()
f1 = mbi.clear_text(f1,alph_rus)
fl = open('log.txt','w')
fl.write('')
fl.close()
keys = {}
print(len(keys))
VT_b = ['ст','но','то','на','ен','ов','ни','ра','во','ко']
SHT_b = mbi.count_bigr_freq(f1,10)

bigr_comb_attack(VT_b,SHT_b,5,keys)


for key in keys.values():
  check_rus_text(f1,key[0],key[1])
#print(mbi.solve_lin_por(2,4,8))
