from collections import Counter
from main import filter_text, alphabet

text = filter_text(open('cp_2/kozachok-fb82_kuznetsov-fb82_cp_2/anna.txt', 'r').read())

bigrams = []

for letter1 in alphabet:
    for letter2 in alphabet:
        bigrams.append(letter1 + letter2)

c = Counter()
for bigram in bigrams:
    c[bigram] = text.count(bigram)

print(c.most_common())