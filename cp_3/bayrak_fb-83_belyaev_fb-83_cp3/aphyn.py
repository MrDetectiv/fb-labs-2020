def aphyn(a, b):
    out = open("ap_crypted.txt", "w")
    alp = []
    for i in range(0, 32):
        if chr(ord('а')+i) !='ъ':
            alp.append(chr(ord('а')+i))
    text=open("aphyn_open.txt").read()
    print(text)
    l1=None
    l2=None
    for l in text:
        if l in alp:
            if l1==None:
                l1=l
            else:
                l2=l
                l1=alp.index(l1)
                l2=alp.index(l2)
                print(l1, l2)
                bg=31*l1+l2
                print(bg)
                l1=None
                bg=a*bg+b
                
                bg=bg%(31*31)
                print(bg)
                b2=bg%31
                b1=int((bg-b2)/31)
                print(b1, b2)
                b1=alp[b1]
                b2=alp[b2]
                out.write(b1+b2)
    out.close()

aphyn(1, 1)
            
