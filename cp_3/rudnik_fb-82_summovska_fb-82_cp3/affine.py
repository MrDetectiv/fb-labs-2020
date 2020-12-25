import cryptomath

letters = list('абвгдежзийклмнопрстуфхцчшщьыэюя')
alph_len = len(letters)
letters_map = {letters[key] : key for key in range(alph_len)}
bigrams_map = {}
for i in letters:
    for j in letters:
        x2i_1 = letters_map[i]
        x2i = letters_map[j]
        bigrams_map[x2i_1*alph_len+x2i] = i + j


def cipher(text,a,b,mode):
    if cryptomath.gcd(a,alph_len) != 1:
        return None
    text = [tuple(text[i:i+2]) for i in range(0,len(text),2)]
    text = [letters_map[i]*alph_len + letters_map[j] for i,j in text]
    text = [(a*X + b) % alph_len ** 2  for X in text] if mode == "encrypt" else [cryptomath.findModInverse(a,alph_len ** 2)*(X - b) % alph_len ** 2  for X in text]
    text = ''.join(list(map(lambda x: bigrams_map[x],text)))
    return text

