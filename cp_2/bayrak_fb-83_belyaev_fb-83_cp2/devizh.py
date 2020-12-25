file = open("crypted1.txt")
text = file.read()
##text = text.lower()
output = open("open1.txt", 'w')
text=text.replace('\n', '')

def frec(text):
    fr=[0]*32
    for l in text:
        if(l!='\n'):
            fr[ord(l)-ord('а')]+=1
    n = fr.index(max(fr))
    return n

Dr=[0]*30
for k in range(2,31):
    for i in range(0, len(text)-k):
        if text[i]==text[i+k]:
            Dr[k-2]+=1
    print((f'{k}'+ " = " + f'{Dr[k-2]}'))
klen = Dr.index(max(Dr))+2
print("suggested key length: "+str(klen))
print("input key length")
klen=int(input())
##klen=8
t=['']*klen
key = ''
for i in range(0, len(text)):
    t[i%klen]+=text[i]
for k in range(0, klen):
    y=frec(t[k])
    x=ord('о')-ord('а')
    d = y-x
    if d<0:
        d+=32
    d=chr(d+ord('а'))
    key+=d
##print(Dr.index(max(Dr))+2)
##print(frec(text))
print(key)

from decoder import decode
decode(text, key)
output.close()
key = input()
decode(text, key)
b = frec(t[3])-(ord(key[3])-ord('а'))
b = chr(b+ord('а'))
print("Most frequent letter in cyphertext[4] is ", b)
output.close()
print("done")
