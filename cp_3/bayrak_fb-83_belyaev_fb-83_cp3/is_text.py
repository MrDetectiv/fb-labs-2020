def is_text(text):
    alp = []
    for i in range(0, 32):
        if chr(ord('а')+i) !='ъ':
            alp.append(chr(ord('а')+i))
    lfrec=[0]*31
    len=0
    for l in text:
        if l in alp:
            n=alp.index(l)
            lfrec[n]+=1
            len+=1
    if len==0:
        return False
    for i in range(0, 31):
        lfrec[i]/=len
##    print(alp[lfrec.index(min(lfrec))])
    if lfrec.index(max(lfrec))==alp.index('о') or lfrec.index(max(lfrec))==alp.index('а'):
            if lfrec.index(min(lfrec))==alp.index('э') or lfrec.index(min(lfrec))==alp.index('щ') or lfrec.index(min(lfrec))==alp.index('ц') or lfrec.index(min(lfrec))==alp.index('ф'):
                return True
            else:
                print("most rare symbol is ", alp[lfrec.index(min(lfrec))])
                return False
    else:
        print("most frecuent symbol is ", alp[lfrec.index(max(lfrec))])
        return False





















##text = open("decoded text.txt").read()
##print(is_text(text))
