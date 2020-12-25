import random, sys, math

def Miller_Rabin(n):
    r=int(math.log(n,2))
    if n == 2:
        return(True)
    elif n == 3:
        return(True)
    elif n % 2 == 0:
        return(False)
    else:
        power=0
        t=n-1
        while t%2==0:
            t=t//2
            power+=1
        for k in range(r):
            a= random.randint(2, n-1)
            x=pow(a, t, n)
            i=0
            if x==1: continue
            elif x==n-1: continue
            while i<power-1:
                x=pow(x,2,n)
                if x==n-1: break
                i=i+1
            else: return(False)
        return(True)

def Test(ran):
    if ran%2==0 or ran%3==0 or ran%5==0 or ran%7==0 or ran%11==0: 
        return False
    if Miller_Rabin(ran)==False: 
        print('Value %s is not prime number. I will try again.'% hex(ran))
        return False
    return ran

def Random_num(size):
    num=2**(size-1)
    for i in range(1,size-1,1):
        b=random.randint(0,1)
        num+=((2**i)*b)
    num=num+1
    return num

def Generate(size):
    ran_mass=[]
    for i in range(0,2,1):
        ran=Random_num(size)
        while Test(ran)==False:
            ran=Random_num(size)
        ran_mass.append(ran)
    return ran_mass

def OiLera(n):
    i=3
    eul=n
    if n%2==0:
        while n%2==0:
            n=n//2
        eul=eul//2
    while (i*i)<=n:
        if n%i==0:
            while n%i==0:
                n=n//i
            eul=eul//i
            eul=eul*(i-1)
        i+=2
    if n>1:
        eul=eul//n
        eul=eul*(n-1)
    return eul

def gcd(a, b):
  if b == 0: return a
  else: return gcd(b, a % b)

def Evkl(a, b):
    if a == 0: return (b, 0, 1)
    else: 
        g, x, y = Evkl(b % a, a)
        return (g, y - (b // a) * x, x)
 
def Reverse(b, n):
    g, x, y = Evkl(b, n)
    if g == 1:
        return x % n

def GenerateKeyPair(pq):
    n=int(pq[0])*int(pq[1])
    e=0
    Oiler=(pq[0]-1)*(pq[1]-1)
    while gcd(e,Oiler)!=1:
        e=random.randint(2,Oiler-1) 
    d=Reverse(e,Oiler)
    open_key=[n,e]
    secret_key=[d,pq,n]
    return(open_key,secret_key)

def Encrypt(mess, open_key):
    C=pow(mess,open_key[1],open_key[0])
    return C

def Decrypt(C, secret_key):
    M=pow(C,secret_key[0],secret_key[2])
    return M

def Sign(M, key, N):
    S=pow(M,key,N)
    return S

def Verify(S,M,open_key):
    print(open_key)
    if M==pow(S,open_key[1],open_key[0]):
        return True
    else: return False

def SendKey(A_key,B_open, M):
    print('\nAlice has sent key for Bob.\n\n\tSEND KEY\n')
    k1=Encrypt(M,B_open)
    print('\nSecret text is encrypted. K1=%s'% hex(k1))
    S=Sign(M,A_key[1][0],A_key[1][2])
    print('The message has been signed with Alice\'s secret key. S=%s'% hex(S))
    S1=Encrypt(S,B_open)
    print('Alice\'s sign has been signed with Bob\'s open key. S1=%s'% hex(S1))
    A_message=[k1,S1]
    return A_message

def ReceiveKey(mess,B_secret,A_open):
    print('Bob is checking Alice\'s sign.\n\n\tRECEIVE KEY\n')
    k=Decrypt(mess[0], B_secret)
    print('Value k is %s'% hex(k))
    S=Decrypt(mess[1],B_secret)
    print('Value S is %s'% hex(S))
    print('S^(e)mod(n)=',hex(pow(S,A_open[1],A_open[0])))
    return Verify(S,k,A_open)

#TASK
print('\nHello! Choose:\n1) Website\n2) Python')
choose=input()

if int(choose)==1:
    print("\nI'm generating a pair p and q for Alice:\n")
    pairs=Generate(256)
    A_keys=GenerateKeyPair(pairs)
    message=random.randint(0,A_keys[0][0]-1)
    print('\nI have generated open key (n=%s, e=%s) and secret key (d=%s, pq=%s, %s) for Alice.'% (hex(A_keys[0][0]),hex(A_keys[0][1]),hex(A_keys[1][0]),hex(A_keys[1][1][0]),hex(A_keys[1][1][1])))
    print('\nAlice has generated secret message \'%s\' for Bob.'% hex(message))
    nB=int(0x8B856D59DE4C42D743D2A1F90915A2B57BB93FB6A18C642F954F0011296E322185D566CBB6083E6E5CDC10143EF991960E7D689D4B4DD77C7C84878433575445)
    eB=int(0x10001)
    B_open=[nB,eB]
    print('\nWebsite has generated open key (n=%s, e=%s for Bob)'% (B_open[0],B_open[1]))
    k,S=SendKey(A_keys,B_open,message)
    print('\nk1=',hex(k)[2:],'\nS1=',hex(S)[2:])
    print('\nn=',hex(A_keys[0][0])[2:],'\ne=',hex(A_keys[0][1])[2:])

if int(choose)==2:
    pairs=[]
    for i in range(0,2,1):
        if i==0: 
            print("\nI'm generating a pair p and q for Alice:\n")
            pair=Generate(256)
            pairs.append(pair)
            print("\nPair p and q for Alice:%s, %s"% (hex(pairs[0][0]),hex(pairs[0][1])))
            
        if i==1: 
            print("\nI'm generating a pair p and q for Bob:\n")
            pair=Generate(256)
            pairs.append(pair)
            while pairs[0][0]*pairs[0][1]>=pairs[1][0]*pairs[1][1]: 
                pair=Generate(256)
                pairs.pop(1)
                pairs.append(pair)
            print("\nPair p and q for Bob:%s, %s"% (hex(pairs[1][0]),hex(pairs[1][1])))

    A_keys=GenerateKeyPair(pairs[0])
    B_keys=GenerateKeyPair(pairs[1])
    while B_keys[0][0]<A_keys[0][0]:
        A_keys=GenerateKeyPair(pairs[0])

    print('\nI have generated open key (n=%s, e=%s) and secret key (d=%s, pq=%s, %s) for Alice.'% (hex(A_keys[0][0]),hex(A_keys[0][1]),hex(A_keys[1][0]),hex(A_keys[1][1][0]),hex(A_keys[1][1][1])))
    print('I have generated open key (n=%s, e=%s) and secret key (d=%s, pq=%s, %s) for Bob.\n'% (hex(B_keys[0][0]),hex(B_keys[0][1]),hex(B_keys[1][0]),hex(B_keys[1][1][0]), hex(B_keys[1][1][0])))

    message=random.randint(0,A_keys[0][0]-1)
    print('Alice has generated secret message \'%s\' for Bob.'% hex(message))

    A_mess=SendKey(A_keys,B_keys[0],message)
    if ReceiveKey(A_mess,B_keys[1],A_keys[0])==True: print('\nRSA succeeded')
    else: print('\nRSA failed')
