from krypt_math import *
alp = []
for i in range(0, 32):
    if chr(ord('а')+i) !='ъ':
        alp.append(chr(ord('а')+i))
j = alp.index('ы')
alp[j]='ь'
alp[j+1]='ы'
##output = open("decr.txt", "w")
inputf=open("aphyn.txt")
text=inputf.read()
text=text.replace('\n', '')
b = bigrams(text)
bi=[]
for i in range(0, 5 ):
    n=max(b)
    n=b.index(n)
    b[n]=0
    n2=n%31
    n1=int((n-n2)/31)
    n1=alp[n1]
    n2=alp[n2]
    print(n1, n2)
    bi.append(n)
bi1=[]
for i in [['с','т'],['н','о'],['т','о'],['н','а'],['е','н']]:
    n1=alp.index(i[0])
    n2=alp.index(i[1])
    n=31*n1+n2
    bi1.append(n)
key=[]
for x1 in bi1:
    for x2 in bi1:
        if x1!=x2:
            for y1 in bi:
                for y2 in bi:
                    if y1!=y2:
##                        print(x1, x2, y1, y2)
                        a1=equation(x1-x2, y1-y2, 31*31)
                        if a1!=None:
                            for a in a1:                        
                                b=y1-a*x1
                                b = b%(31*31)
                                key.append([a, b])
key1=[]
for k in key:
    if k not in key1:
        key1.append(k)
from deaphyn import decode
from is_text import is_text
for k in key1:
    t = decode(text, k[0], k[1])
    if is_text(t):
        out=open("out.txt", "w")
        out.write(t)
        print(k, "text found")
        out.close()
        input()
    else:
        print(k, "false", "  ", key1.index(k)+1, "/", len(key1))
                            
                                

                        
    
    
                        
