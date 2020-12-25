def decode(text, key):
    kn=0
    out = open("decoded text.txt", "w")
    for i in range(0, len(text)):
        y=ord(text[i])-ord("а")
        k=ord(key[kn])-ord("а")
        x=y-k
        if x<0:
            x=x+32
        out.write(chr(x+ord("а")))
        if kn==len(key)-1:
            ##out.write("\n")
            kn=0
        else: kn+=1
    out.close()
inp = open("crypted.txt")
text = inp.read()
key="ключ"
decode(text, key)
