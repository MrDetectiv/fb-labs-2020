from math import log2
input = open("input.txt")
str = input.read()
str = str.lower()
a='а'
output = open("output.txt", 'w')


def letters_w():
    alp=[]
    lfrec=[0]*33
    for i in range(0, 32):
        alp.append(chr(ord('а')+i))
    alp.append(' ')
    num=0
    h1=0
    for l in str:
        if l in alp:
            if l == ' ':
                lfrec[32]+=1
                num+=1
            else:
                lfrec[ord(l)-ord(a)]+=1
                num+=1
    
    for i in range(0, 32):
        lfrec[i]=lfrec[i]/num
        if lfrec[i] != 0:
            h1+=lfrec[i]*log2(lfrec[i])
        output.write(chr(ord('а')+i)+" "+f'{lfrec[i]}' + '\n')
    lfrec[32]=lfrec[32]/num
    h1+=lfrec[32]*log2(lfrec[32])
    h1=h1*(-1)
    R=1 - (h1/log2(33))
    output.write("space"+" "+f'{lfrec[32]}' + '\n')
    output.write("h1"+" "+f'{h1}' + '\n')
    output.write("R"+" "+f'{R}' + '\n')
    output.close()

    
def letters_wo():
    alp=[]
    lfrec=[0]*32
    for i in range(0, 32):
        alp.append(chr(ord('а')+i))
    num=0
    h1=0
    for l in str:
        if l in alp:
            lfrec[ord(l)-ord(a)]+=1
            num+=1  
    for i in range(0, 32):
        lfrec[i]=lfrec[i]/num
        if lfrec[i] != 0:
            h1+=lfrec[i]*log2(lfrec[i])
        output.write(chr(ord('а')+i)+" "+f'{lfrec[i]}' + '\n')
    h1=h1*(-1)
    R=1 - (h1/log2(32))
    output.write("h1"+" "+f'{h1}' + '\n')
    output.write("R"+" "+f'{R}' + '\n')
    output.close()


def bigrams_wo_sp():
    alp=[]
    for i in range(0, 32):
        alp.append(chr(ord(a)+i))
    alp.append(' ')
    bfrec=[0]*1089
    num=0
    h2=0
    l1=None
    l2=None
    for l in str:
        if l in alp:
            if l1==None:
                l1=l
            else:
                l2=l
                if l1==' ':
                    n1=32
                else: n1=ord(l1)-ord(a)
                
                if l2==' ':
                    n2=32
                else: n2=ord(l2)-ord(a)
                bfrec[33*n1+n2]+=1
                l1=None
                num+=1



    for i in range(0, 32):
        output.write(" "+chr(ord('а')+i))
    output.write(" "+"space")
    output.write('\n')
    for i in range(0, 32):
        output.write(chr(ord('а')+i))
        for j in range(0,32):
            bfrec[33*i+j]/=num
            output.write(" "+"%.6f" % bfrec[33*i+j])
            if(bfrec[33*i+j]!=0):
                h2+=bfrec[33*i+j]*log2(bfrec[33*i+j])
        bfrec[33*i+32]/=num
        output.write(" "+"%.6f" % bfrec[33*i+32])
        if(bfrec[33*i+32]!=0):
            h2+=bfrec[33*i+32]*log2(bfrec[33*i+32])
        output.write('\n')
    
    output.write("space")
    for j in range(0,32):
        bfrec[33*32+j]/=num
        output.write(" "+"%.6f" % bfrec[33*32+j])
        if(bfrec[33*32+j]!=0):
            h2+=bfrec[33*32+j]*log2(bfrec[33*32+j])
    bfrec[33*32+32]/=num
    output.write(" "+"%.6f" % bfrec[33*32+32])
    if(bfrec[33*32+32]!=0):
        h2+=bfrec[33*32+32]*log2(bfrec[33*32+32])
    h2=h2*(-1)/2
    R=1 -(h2/log2(33*33))
    output.write('\n'+"h2"+" "+f'{h2}' + '\n')
    output.write("R"+" "+f'{R}' + '\n')
    output.write('\n')
    output.close()
            
def bigrams_wo():
    alp=[]
    for i in range(0, 32):
        alp.append(chr(ord(a)+i))
    bfrec=[0]*(32*32)
    num=0
    h2=0
    l1=None
    l2=None
    for l in str:
        if l in alp:
            if l1==None:
                l1=l
            else:
                l2=l
                n1=ord(l1)-ord(a)
                n2=ord(l2)-ord(a)
                bfrec[32*n1+n2]+=1
                l1=None
                num+=1



    for i in range(0, 32):
        output.write(" "+chr(ord('а')+i))
    output.write('\n')
    for i in range(0, 32):
        output.write(chr(ord('а')+i))
        for j in range(0,32):
            bfrec[32*i+j]/=num
            output.write(" "+"%.6f" % bfrec[32*i+j])
            if(bfrec[32*i+j]!=0):
                h2+=bfrec[32*i+j]*log2(bfrec[32*i+j])
        output.write('\n')
    h2=h2*(-1)/2
    R=1 -(h2/log2(33*33))
    output.write('\n'+"h2"+" "+f'{h2}' + '\n')
    output.write("R"+" "+f'{R}' + '\n')
    output.write('\n')
    output.close()
    
def bigrams_w_sp():
    alp=[]
    for i in range(0, 32):
        alp.append(chr(ord(a)+i))
    alp.append(' ')
    bfrec=[0]*1089
    num=0
    h2=0
    l1=None
    l2=None
    for l in str:
        if l in alp:
            if l1==None:
                l1=l
            else:
                l2=l
                if l1==' ':
                    n1=32
                else: n1=ord(l1)-ord(a)
                
                if l2==' ':
                    n2=32
                else: n2=ord(l2)-ord(a)
                bfrec[33*n1+n2]+=1
                l1=l2
                num+=1



    for i in range(0, 32):
        output.write(" "+chr(ord('а')+i))
    output.write(" "+"space")
    output.write('\n')
    for i in range(0, 32):
        output.write(chr(ord('а')+i))
        for j in range(0,32):
            bfrec[33*i+j]/=num
            output.write(" "+"%.6f" % bfrec[33*i+j])
            if(bfrec[33*i+j]!=0):
                h2+=bfrec[33*i+j]*log2(bfrec[33*i+j])
        bfrec[33*i+32]/=num
        output.write(" "+"%.6f" % bfrec[33*i+32])
        if(bfrec[33*i+32]!=0):
            h2+=bfrec[33*i+32]*log2(bfrec[33*i+32])
        output.write('\n')
    
    output.write("space")
    for j in range(0,32):
        bfrec[33*32+j]/=num
        output.write(" "+"%.6f" % bfrec[33*32+j])
        if(bfrec[33*32+j]!=0):
            h2+=bfrec[33*32+j]*log2(bfrec[33*32+j])
    bfrec[33*32+32]/=num
    output.write(" "+"%.6f" % bfrec[33*32+32])
    if(bfrec[33*32+32]!=0):
        h2+=bfrec[33*32+32]*log2(bfrec[33*32+32])
    h2=h2*(-1)/2
    R=1 -(h2/log2(33*33))
    output.write('\n'+"h2"+" "+f'{h2}' + '\n')
    output.write("R"+" "+f'{R}' + '\n')
    output.write('\n')
    output.close()
    
def bigrams_w():
    alp=[]
    for i in range(0, 32):
        alp.append(chr(ord(a)+i))
    bfrec=[0]*(32*32)
    num=0
    h2=0
    l1=None
    l2=None
    for l in str:
        if l in alp:
            if l1==None:
                l1=l
            else:
                l2=l
                n1=ord(l1)-ord(a)
                n2=ord(l2)-ord(a)
                bfrec[32*n1+n2]+=1
                l1=l2
                num+=1



    for i in range(0, 32):
        output.write(" "+chr(ord('а')+i))
    output.write('\n')
    for i in range(0, 32):
        output.write(chr(ord('а')+i))
        for j in range(0,32):
            bfrec[32*i+j]/=num
            output.write(" "+"%.6f" % bfrec[32*i+j])
            if(bfrec[32*i+j]!=0):
                h2+=bfrec[32*i+j]*log2(bfrec[32*i+j])
        output.write('\n')
    h2=h2*(-1)/2
    R=1 -(h2/log2(33*33))
    output.write('\n'+"h2"+" "+f'{h2}' + '\n')
    output.write("R"+" "+f'{R}' + '\n')
    output.write('\n')
    output.close()

            
            
    

    
   
##letters_w()
##letters_wo()
##bigrams_wo_sp()
##bigrams_wo()
##bigrams_w_sp()
##bigrams_w()
print("done")
