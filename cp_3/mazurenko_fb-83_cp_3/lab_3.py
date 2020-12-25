# extended euclidean algorithm
def extended_euclids_algo(a, b):
    u0, u1 = 1, 0
    v0, v1 = 0, 1
    while b:
        q = a // b
        #u_(i+1) = u_(i-1) - q_(i)*u_(i)
        #v_(i+1) = v_(i-1) - q_(i)*v_(i)
        u1, u0 = u0 - q*u1, u1
        v1, v0 = v0 - q*v1, v1
        a, b = b, a % b
    return a, u0, v0
    
# modular multiplicative inverse
def mod_multi_inverse(a, m):
    gcd, u, v = extended_euclids_algo(a, m)
    if (gcd == 1):
        # a*u = 1 % m
        return u
        
# finding solutions for linear comparisons
def linear_comparisons(a, b, m):
    gcd, u, v = extended_euclids_algo(a, m)
    list_of_solutions = []
    if (gcd == 1):
        # a*x = b % m
        x = (b*mod_multi_inverse(a, m)) % m
        list_of_solutions.append(x)
        return list_of_solutions
    else:
        if ((b % gcd) != 0):
            return 0
        else:
            a1, b1, m1 = a // gcd, b // gcd, m // gcd
            x0 = (b1*mod_multi_inverse(a1, m1)) % m1
            list_of_solutions.append(x0)
            for i in range(1, gcd):
                list_of_solutions.append(x0 + m1*i)
            return list_of_solutions

#print(linear_comparisons(876, 643, 4234))
#print(linear_comparisons(10, 44, 943))
#print(linear_comparisons(1287, 447, 516))
#print(linear_comparisons(789, 342, 3456))
 
# converting text from file to string
def convert_text():
	text = []
	text_file = open("C:\\Users\\shell\\Desktop\\everything\\lab_3\\var.txt", encoding = "utf-8", mode = "r")
	text = text_file.read()
	text_file.close()
	return text

# choose frequency of the bigram
def take_frequency(element):
    temp = 0
    if (len(element) == 4):
        temp = int(element[2] + element[3])
    else:
        temp = int(element[2])
    return temp

# finding all of the bigrams and their frequencies in the text
def find_bigrams():
	bigrams = []
	bigrams_frequency = []
	bigram_count = 0
	text = convert_text()
	
	for i in range(0, len(text) - 2, 2):
		bigrams.append(text[i] + text[i + 1])
		bigram_count += 1
	
	temp = bigrams.copy()
	
	for i in bigrams:
	    while (bigrams.count(i) != 1):
	        bigrams.remove(i)
	        bigram_count -= 1
	
	frequency = 0
	
	for i in range(0, bigram_count):
		for j in range(0, len(temp)):
			if (bigrams[i] == temp[j]):
				frequency += 1
		bigrams_frequency.append(bigrams[i] + str(frequency)) 
		frequency = 0
	
	# sorting bigrams by frequency in a reverse order (from the highest to the lowest frequency)
	bigrams_frequency.sort(key = take_frequency, reverse = True)
		
	return bigrams_frequency

# select top five bigrams from the given text
def find_top_bigrams():
	temp = find_bigrams()
	top_bigrams = []
	for i in range(5):
		top_bigrams.append(temp[i][0] + temp[i][1])
	return top_bigrams

def alphabet_numeration():
	alphabet = "абвгдежзийклмнопрстуфхцчшщьыэюя"
	alphabet_list = []
	for i in range(len(alphabet)):
		alphabet_list.append(alphabet[i] + str(i))
	return alphabet_list

# find the position of the letter
def alpha_numeration(alpha):
	alphabet = "абвгдежзийклмнопрстуфхцчшщьыэюя"
	alphabet_list = alphabet_numeration()
	for i in range(len(alphabet)):
		if (alpha == alphabet[i]):
			if (len(alphabet_list[i]) == 2):
				return alphabet_list[i][1]
			elif (len(alphabet_list[i]) == 3):
				return alphabet_list[i][1] + alphabet_list[i][2]

# find the letter from the known position
def reverse_alpha_numeration(number):
	alphabet = "абвгдежзийклмнопрстуфхцчшщьыэюя"
	alphabet_list = alphabet_numeration()
	for i in range(len(alphabet)):
		if ((number < 10) and (len(alphabet_list[i]) == 2)):
			if (number == int(alphabet_list[i][1])):
				return alphabet[i][0]
		elif ((number > 9) and (len(alphabet_list[i]) == 3)):
			if (number == int(alphabet_list[i][1] + alphabet_list[i][2])):
				return alphabet[i][0]

# from letters to numbers
def bigram_numeration(bigram):
	x1 = int(alpha_numeration(bigram[0]))
	x2 = int(alpha_numeration(bigram[1]))
	X = x1 * 31 + x2
	return X

# from numbers to letters
def reverse_bigram_numeration(X):
	x1 = X // 31
	x2 = X - x1 * 31
	X1 = reverse_alpha_numeration(x1)
	X2 = reverse_alpha_numeration(x2)
	return X1, X2


def find_key():
	top_rus_bigrams = ["ст", "но", "то", "на", "ен"]
	top_bigrams = find_top_bigrams()
	keys_list = []
	f = open("C:\\Users\\shell\\Desktop\\everything\\lab_3\\temp_results.txt", encoding = "utf-8", mode = "w")
	for i in range(5):
		for k in range(5):
			y1 = top_bigrams[i]
			y2 = top_bigrams[k]
			if (y1 != y2):
				for j in range(5):
					for l in range(5):
						x1 = top_rus_bigrams[j]
						x2 = top_rus_bigrams[l]
						if (x1 != x2):
							X1 = bigram_numeration(x1)
							X2 = bigram_numeration(x2)
							Y1 = bigram_numeration(y1)
							Y2 = bigram_numeration(y2)
							a = linear_comparisons((X1 - X2), (Y1 - Y2), pow(31, 2))
							if (a != 0):
								text_1 = "x1 = " + str(x1) + " x2 = " + str(x2) + '\n'
								text_2 = "y1 = " + str(y1) + " y2 = " + str(y2) + '\n'
								text_3 = "X1 = " + str(X1) + " X2 = " + str(X2) + " Y1 = " + str(Y1) + " Y2 = " + str(Y2) + '\n'
								for n in range(len(a)):
									b = (Y1 - a[n] * X1) % pow(31, 2)
									text_4 = "a = " + str(a[n]) + " b = " + str(b) + '\n'
									f.write(text_1 + text_2 + text_3 + text_4 + '\n')
									keys_list.append(str(a[n]) + " " + str(b))
									#print('\n')
	f.close()
	new_keys_list = list(dict.fromkeys(keys_list))	
	return new_keys_list				

# take a and b from the chosen element from the list of keys
def take_key(element):
	a, b = "", ""
	i = 0
	while (element[i] != " "):
		a = a + element[i]
		pos = i
		i += 1
	for i in range(pos + 2, len(element)):
		b = b + element[i]
	return int(a), int(b)

# decode the encrypted text with the given key (a, b)
def decode_with_key(a, b):
	bigrams = []
	bigram_count = 0
	text = convert_text()
	decoded_text = ""
	p = pow(31, 2)
	for i in range(0, len(text) - 2, 2):
		bigrams.append(text[i] + text[i + 1])
		bigram_count += 1
	for i in range(bigram_count):
		Y = bigram_numeration(bigrams[i])
		X = (mod_multi_inverse(a, p)*(Y - b)) % p
		x1, x2 = reverse_bigram_numeration(X)
		decoded_text += x1 + x2
	return decoded_text

# index of conformity for text
def index_for_text(text):
	alphabet = "абвгдежзийклмнопрстуфхцчшщыьэюя"
	n, sum_n = 0, 0
	for i in range(31):
		for j in range(len(text)):
			if (text[j] == alphabet[i]):
				n += 1
		if (n > 1):
			sum_n += n * (n - 1)
		else:
			sum_n += 0
		n = 0
	index = (1 / (len(text) * (len(text) - 1))) * sum_n
	return index			

# go through the found keys and find the right one
def decode_text():
	keys_list = find_key()
	f1 = open("C:\\Users\\shell\\Desktop\\everything\\lab_3\\decoded_text.txt", encoding = "utf-8", mode = "w")
	f2 = open("C:\\Users\\shell\\Desktop\\everything\\lab_3\\keys_results.txt", encoding = "utf-8", mode = "w")
	for i in range(len(keys_list)):
		a, b = take_key(keys_list[i])
		decoded_text = decode_with_key(a, b)
		key = "(" + str(a) + "," + str(b) + ")"
		index = "index = " + str(index_for_text(decoded_text))
		f2.write(key + " " + index + '\n')
		if (index_for_text(decoded_text) >= 0.05):
			f1.write(key + '\n' + decoded_text + '\n' + index)
	f2.close()
	f1.close()

decode_text()
