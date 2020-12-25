from random import randint
import math


def gcd(x, y):
	while (y):
		x, y = y, x % y

	return x


def pseudosimple(a, p):
	if gcd(a, p) == 1 and (a ** (p - 1)) % p == 1 % p:
		return True
	return False


def Miller_Rabin_Test(p, k):
	for i in [2, 3, 5, 7]:
		if p % i == 0:
			return False

	s = 0
	d = p - 1

	while d % 2 == 0:
		d //= 2
		s += 1

	for i in range(k):

		a = randint(2, p - 1)

		x = pow(a, d, p)

		if x == 1 or x == p - 1:
			continue

		for j in range(s - 1):
			x = pow(x, 2, p)

			if x == 1:
				return False
			elif x == p - 1:
				break
		else:
			return False
	return True


def random_prime(num_len):
	n0 = int(math.pow(2, num_len // 2 - 1))
	n1 = int(math.pow(2, num_len // 2))

	x = randint(n0, n1)
	m0 = x if x % 2 != 0 else x + 1

	for i in range(0, (n1 - m0) // 2):
		p = m0 + 2 * i
		if Miller_Rabin_Test(p, 10):
			return p, True
		else:
			return p, False


def reverse_euclid(a, b):
	buff_b = b
	x, xx, y, yy = 1, 0, 0, 1
	while b:
		q = a // b
		a, b = b, a % b
		x, xx = xx, x - xx * q
		y, yy = yy, y - yy * q
	while x < 0:
		x += buff_b

	return x
