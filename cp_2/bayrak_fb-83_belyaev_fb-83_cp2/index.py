a='а'
alp=[]
for i in range(0, 32):
    alp.append(chr(ord(a)+i))
text = open("ind_input.txt").read()
n = [0]*32
size=0
for l in text:
    if l in alp:
        n[alp.index(l)]+=1
        size+=1
index=0.0
for i in n:
    index+=i*(i-1)
index=index/(size*(size-1))
print(index)

