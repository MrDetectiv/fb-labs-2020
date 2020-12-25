
def antielem(a, m):
    from math import gcd
    if gcd(a, m)!=1:
        return None
    else:
        for i in range(0, m):
            b=a*i
            while b>m:
                b-=(b-(b%m))
            while b<0:
                b+=m
            if b==1:
                return i
def equation(x, y, m):##ax=y modm
    from math import gcd
    if gcd(x, m)==1:
        a=y*antielem(x, m)
        while a>m:
            a-=(a-a%m)
        while a<0:
            a+=m
        a1=[a]
        return a1
    else:
        if y%gcd(x, m)==0:
            d=gcd(x,m)
            a0=(y/d)*antielem(int(x/d), int(m/d))
            while a0>m/d:
                a0-=(a0-a0%(m/d))
            while a0<0:
                a0+=m/d
            a=[]
            for i in range(0, d):
                a.append(int(a0+i*m/d))
            return a
        else: return None

def bigrams(text):
    a='а'
    alp=[]
    for i in range(0, 32):
        if chr(ord(a)+i)!='ъ':
            alp.append(chr(ord(a)+i))
    bfrec=[0]*(31*31)
    num=0
    h2=0
    l1=None
    l2=None
    for l in text:
        if l in alp:
            if l1==None:
                l1=l
            else:
                l2=l
                n1=alp.index(l1)
                n2=alp.index(l2)
                bfrec[31*n1+n2]+=1
                l1=None
                num+=1
    return bfrec
    
##print(equation(4, 8, 16))
##text=open("input.txt").read()
##b=bigrams(text)

##print(bigrams("аапяяяя")


