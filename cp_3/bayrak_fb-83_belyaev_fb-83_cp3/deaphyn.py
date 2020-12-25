def decode(text, a, b):
    from krypt_math import equation
    alp = []
    for i in range(0, 32):
        if chr(ord('а')+i) !='ъ':
            alp.append(chr(ord('а')+i))
    j = alp.index('ы')
    alp[j]='ь'
    alp[j+1]='ы'
    l1=None
    l2=None
    open=''
    for l in text:
        if l1==None:
            l1=l
        else:
            l2=l
            l1=alp.index(l1)
            l2=alp.index(l2)
            y=l1*31+l2
##            ax+b=y
            x1 = equation(a, y-b, 31*31)
            if x1!=None:
                for x in x1:
                    l1=x%31
                    l2=int((x-l1)/31)
                    l1=alp[int(l1)]
                    l2=alp[int(l2)]
                    open+=(l2+l1)
            l1=None
    return open

























##print(decode("апправ", 96000, 1))
