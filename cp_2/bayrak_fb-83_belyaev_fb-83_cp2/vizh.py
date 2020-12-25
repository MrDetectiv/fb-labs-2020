file = open("open.txt")
text = file.read()
text = text.lower()
output = open("crypted.txt", 'w')
key = input()
klen = len(key)
knum=0
alp=[]
for i in range(0, 32):
    alp.append(chr(ord('а')+i))
for l in text:
    if l == 'ё':
        l='е'
    if l in alp:
        n = ord(l)-ord('а')+ord(key[knum])-ord('а')
        if n>31:
            n-=32
        output.write(alp[n])
        if knum==len(key)-1:
            knum=0
        else:
            knum+=1
output.close()
print("done")
