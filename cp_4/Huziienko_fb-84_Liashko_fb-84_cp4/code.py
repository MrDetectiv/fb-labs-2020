import math
import random
import binascii
####
## find gcd of numbers p, x 
def GCD(p,x): 
   while(x): 
       p,x = x,p % x 
   return p
####
## Reverse element function 
def ReverseE(e,fn):
    if fn==0:
        return e,1,0
    else:
        gcd,x,y=ReverseE(fn,e%fn)
        return gcd,y,x-y*(e//fn)
####
## generate number first and last byte -  '1'  
def GenerateP(n):
    p=2**(n-1)
    k=0
    for i in xrange(n-2,0,-1):
        k=random.randint(0,1)
        p+=((2**i)*k)
    p+=1
    return math.trunc(p)
####
## Find d and s: p-1=d*(2**s)
def FindDS(p):
    p=p-1
    i=0
    while(p%2==0):
        p=p/2
        i+=1
    return p,i

## Test Miller-Rabin
def TESTMillerRabin(p,k):
    if p==2:
        return True
    for i in  (2,3,5,7):
        if p%i==0:
            print hex(p),"- Miller-Rabin test failed."
            return False
    s=FindDS(p)[1]
    d=FindDS(p)[0]
    for one in xrange(k):
        x = random.randrange(10, p - 1)
        gcd=GCD(p,x)
        if gcd==1:
            xd = pow(x, d, p)
            if xd == 1 or xd == p - 1:
                continue
                for two in xrange(s - 1):
                    xr = pow(x, 2, p)
                    if xr == p - 1:
                       break
            else:
                return False
                print hex(p),"- Miller-Rabin test failed."
        else:
            print hex(p),"- Miller-Rabin test failed."
            return False
    print hex(p),"- Miller-Rabin test passed."
    return True

####
## Generate numbers p,q,p1,q1
def GenPQ(n):
    L=[]
    for i in xrange(4): # generate p,q,p1,q1
        a=False
        while(a==False):
            p=GenerateP(n)
            a=TESTMillerRabin(p,100)
        L.append(p)
    L.sort()
    return L

#### MAIN FUNCTIONS ####
####
##  Generate Keys 
def GenerateKeyPair(p,q):
    n=p*q
    fn=(p-1)*(q-1)
    e=pow(2,16)+1
    if GCD(e,fn)==1:
        d=ReverseE(e,fn)[1]
    if d<0:
        d=fn+d
    return (d,p,q),(n,e)
####
## Encryption function
def Encrypt(msg,pkey):
    n=pkey[1][0]
    e=pkey[1][1]
    C=pow(msg,e,n)
    return C
####
## Decription function 
def Decrypt(cmsg,key):
    n=key[1][0]
    d=key[0][0]
    M=pow(cmsg,d,n)
    return M
####
## Sign fucntion
def Sign(msg,key):
    d=key[0][0]
    n=key[1][0]
    S=pow(msg,d,n)
    return (msg,S)
####
## Verify fucntion
def Verify(sign,key):
    n=key[1][0]
    e=key[1][1]
    M=pow(sign,e,n)
    return (M,S)
####
##
def SendKey(Akey,Bkey):
    e,n=Akey[1][1],Akey[1][0]
    print'-e', hex(e)
    print'-n', hex(n)
    d=Akey[0][0]
    e1,n1=Bkey[1][1],Bkey[1][0]
    print
    print'-e1', hex(e1)
    print'-n1', hex(n1)
    k=random.randrange(1,n-1)
    print 
    k1=Encrypt(k,Bkey)
    print '-k1', hex(k1)
    S=Sign(k,Akey)[1]
    print '-S', hex(S)
    S1=Encrypt(S,Bkey)
    print '-S1', hex(S1)
    return (k1,S1)

####
##
def ReciveKey(smsg,Bkey,Akey):
    k=Decrypt(smsg[0],Bkey)
    S=Decrypt(smsg[1],Bkey)
    ka=Verify(S,Akey)
    return()


####
##main 
##  p,q; p1,q1
print("1. Generate: P Q P1 Q1")
PQ=GenPQ(256)
p=PQ[0]
q=PQ[2]
p1=PQ[1]
q1=PQ[3]
print("---P---")
print hex(p)
print("---Q---")
print hex(q)
print("---P1---")
print hex(p1)
print("---Q1---")
print hex(q1)
print
## Keys for A and B
A=GenerateKeyPair(p,q)
B=GenerateKeyPair(p1,q1)
print("2. Generate Keys for A and B")
print("For A")
print("Private key")
print '-d',hex(A[0][0])
print '-p',hex(A[0][1])
print '-q',hex(A[0][2])
print
print("Public key")
print '-n',hex(A[1][0])
print '-e',hex(A[1][1])
print
print("For B")
print("Private key")
print '-d1',hex(B[0][0])
print '-p1',hex(B[0][1])
print '-q1',hex(B[0][2])
print
print
print("Public key")
print '-n1',hex(B[1][0])
print '-e1',hex(B[1][1])
## Generate massenge
MSG=random.randrange(1,A[1][0])
## Check Encrypt and Decrypt functions

print("3.Check Encrypt and Decrypt and Sign functions")
print("FOR A")
print '-MSG',hex(MSG)
C=Encrypt(MSG,A)
M=Decrypt(C,A)
S=Sign(M,A)[1]
print '-C', hex(C)
print '-M', hex(M)
print '-S', hex(S)

print
print("FOR B")
MSG1=random.randrange(1,B[1][0])
print '-MSG',hex(MSG1)
C1=Encrypt(MSG1,B)
M1=Decrypt(C1,B)
S1=Sign(M1,B)[1]
print '-C', hex(C1)
print '-M', hex(M1)
print '-S', hex(S1)
print

print("4.SendKey")
sn=int(0xA7F8397F572CD90F1151FC58E0939F5809B6E6D8FB7AC75A3A423CCF259ADC404F5308B8F965BFD1C59391CBAEA90CCB9CF96A10071CED61F394154295DC93A7)
se=int(0x10001)
print(sn,se)
Skey=((0,0,0),(sn,se))
SendKey(A,Skey)
k=Decrypt(int(0x50557784547f718b581c096fb1df144f8da0818c861f348e0e6619674f025baaa1e0871911ba589eefb5d36f05339bb63528d7511d5ac9c5802aeb55ea11d71),Skey)
print "k", hex(k)






















