import numpy as np
import math
output = open("output.txt", "w", encoding='utf-8')


def euclid(a, n):
    if a == 0:
        return 0
    m = n
    q = np.zeros(15, dtype=int)
    i = 0
    while n % a:
        q[i] = -(n / a)
        i += 1
        n, a = a, n % a
    q[i] = -(n / a)
    a_1 = np.zeros(15, dtype=int)
    a_1[1] = 1
    a_1[2] = q[0]
    for j in range(2, i + 1):
        j += 1
        a_1[j] = q[j - 2] * a_1[j - 1] + a_1[j - 2]
    return a_1[i + 1] % m


def solver(a, b, m):
    if a * b * m == 0:
        if a == b == m:
            print("There is no answer a == b == m == 0.")
            return np.array([1000], dtype=int)
        elif a == b == 0:
            return np.arange(m)
        elif a == 0 and b != 0:
            print("There is no answer a == 0, b != 0.")
            return np.array([1000], dtype=int)
        elif a != 0 and b == 0:
            return np.array([0], dtype=int)
    else:
        a = a % m
        d = math.gcd(a, m)
        if b % d == 0:
            ans = np.zeros(d, dtype=int)
            a1, b1, m1 = int(a / d), int(b / d), int(m / d)
            inv_a = euclid(a1, m1)
            x0 = (b1 * inv_a) % m1
            for k in range(d):
                ans[k] = x0 + k * m1
            return ans
        else:
            # print("There is no answer because b % d != 0")
            return np.array([1000], dtype=int)


def decrypt(a, b, cipher_text):
    open_bigrams = np.zeros(len(cipher_text), dtype=int)
    open_text = np.zeros(len(cipher_text) * 2, dtype=int)
    inverse_a = euclid(a, 961)
    for i in range(0, len(open_bigrams)):
        open_bigrams[i] = (inverse_a * (cipher_text[i] - b)) % 961
        open_text[2 * i] = int(open_bigrams[i] / 31)
        open_text[2 * i + 1] = int(open_bigrams[i] % 31)
    return open_text


def check_rus(open_text):
    quantity = np.zeros(31, dtype=int)
    for i in range(0, len(open_text)):
        quantity[open_text[i]] += 1
    if np.argmax(quantity) == 14:
        frequency = quantity / sum(quantity)
        H = -np.dot(frequency, np.log2(frequency))
        if 4.35 <= H <= 4.55:
            return True
        else:
            print("Літера о є найзустрічаємою однак ентропія тексту H =", H,
                  "знатно відрізняється від ентропії мови отриманої в ЛР№1 ~ 4.45", sep=' ', file=output)
            return False
    else:
        print("У тексті літера о не є найчастішою", file=output)
        return False


alphabet = np.array(['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                     'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'э', 'ю', 'я'])
file = open("text.txt", "r", encoding='utf-8')
text = file.read()
text = text[1:]
temporary = np.zeros(len(text), dtype=int)
for i in range(0, len(alphabet)):  # iterating per alphabet
    for j in range(0, len(text)):  # iteration through the whole text
        if text[j] == alphabet[i]:  # checking for matching
            temporary[j] = i  # saving letter code
temp_bigrams = np.zeros(int(len(text) / 2), dtype=int)
rarity2 = np.zeros(len(alphabet) ** 2, dtype=int)  # creating array of rarity for begram
most_common_bigrams = np.array([545, 417, 572, 414, 168], dtype=int)
for i in range(0, len(temp_bigrams)):
    temp_bigrams[i] = temporary[2 * i] * len(alphabet) + temporary[2 * i + 1]
    rarity2[temp_bigrams[i]] += 1
most_common_cipher_bigrams = np.zeros(5, dtype=int)
tempr = np.array(rarity2, dtype=int)
for l in range(0, len(most_common_cipher_bigrams)):
    most_common_cipher_bigrams[l] = np.argmax(tempr)
    tempr[most_common_cipher_bigrams[l]] = 0
key = np.zeros(2, dtype=int)
for i in range(0, 625):
    i1 = int(i / 125)
    i2 = int((i % 125) / 25)
    i3 = int((i % 25) / 5)
    i4 = int(i % 5)
    if i1 == i2 or i3 == i4:
        continue
    a = solver(most_common_bigrams[i1] - most_common_bigrams[i2], most_common_cipher_bigrams[i3] -
               most_common_cipher_bigrams[i4], len(alphabet) ** 2)
    # print(i1, i2, i3, i4)
    if a.all() == [1000]:
        print("\n")
    else:
        b = np.zeros(len(a), dtype=int)
        for j in range(0, len(b)):
            b[j] = solver(1, most_common_cipher_bigrams[i3] - a[j] * most_common_bigrams[i1], len(alphabet) ** 2)
            open_text = decrypt(a[j], b[j], temp_bigrams)
            print("ключ що перевіряється: (", a[j], ";", b[j], ")", sep=" ", file=output)

            if check_rus(open_text):
                print("ключ (", a[j], ";", b[j], ")", "є шуканим ключем", sep=" ", file=output)
                key[0], key[1] = a[j], b[j]
                # break
        # if key.all() != 0:
        #     break
print("\n\n Маємо ключ : (", key[0], ";", key[1], ")", "є шуканим ключем\n\n Відкритий текст: \n", sep=" ", file=output)
plain_text = decrypt(key[0], key[1], temp_bigrams)
for i in range(0, len(plain_text)):
    print(alphabet[plain_text[i]], sep='', end='', file=output)
