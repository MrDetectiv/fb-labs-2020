import math
from auxiliary_functions import reverse_euclid, random_prime
from random import getrandbits


class RSA:

	def __init__(self, bits, user):
		self.user = user
		self.bits = bits
		self.pairs = None
		self.o_key = None
		self.p_key = None
		self.e = None
		self.log = 'Результати тестувань :\n'

	def GenerateKeyPair(self):

		p = False
		status = False

		while not status:
			p, status = random_prime(self.bits)
			if status is False:
				self.log += f'p провалило тест на прстоту p = {p}\n'
		q = False
		status = False
		while not status:
			q, status = random_prime(self.bits)
			if status is False:
				self.log += f'q провалило тест на прстоту q = {q}\n'

		self.e = int(math.pow(2, 16) + 1)

		n = p * q
		f_e = (p - 1) * (q - 1)
		d = reverse_euclid(self.e, f_e)
		self.pairs = (p, q)
		self.o_key = (self.e, n)
		self.p_key = d

		self.log += f'p користувача p = {p}\n'
		self.log += f'q користувача q = {q}\n'
		self.log += f'e користувача e = {self.e}\n'
		self.log += f'n користувача n = {n}\n'
		self.log += f'd користувача d = {d}\n'

	def Encrypt(self, mess, e, n):
		self.log += f'Шифрування повідомлення {hex(mess)}\n'
		if mess > n:
			self.log += 'Повідомлення занадто довге!'
			quit()
		e_mess = pow(mess, e, n)
		self.log += f'Зашифроване повідомлення {hex(e_mess)}\n'
		return e_mess

	def Decrypt(self, c_text, n, d):
		self.log += f'Розшифрування повідомлення {hex(c_text)}\n'
		d_mess = pow(c_text, d, n)
		self.log += f'Розшифроване повідомлення {hex(d_mess)}\n'
		return d_mess

	def Sign(self, mess, n, d):
		self.log += f'Створення підпису для повідомлення {hex(mess)}\n'
		start_mess = mess
		s = pow(mess, d, n)
		self.log += f'Підпис s = {hex(mess)}\n'
		return start_mess, s

	@staticmethod
	def Verify(m, s, e, n):
		result = m == pow(s, e, n)
		return result

	def SendKey(self, e1, n1):
		self.log += f'Операція SendKey :\n'
		e, n = self.o_key
		d = self.p_key

		k = getrandbits(30)
		self.log += f'k = {hex(k)}\n'
		k1 = self.Encrypt(k, e1, n1)
		self.log += f'k1 = {hex(k1)}\n'
		_, s = self.Sign(k, n, d)
		self.log += f's = {hex(s)}\n'
		_, s1 = self.Sign(s, n1, e1)
		self.log += f's1 = {hex(s1)}\n'
		return k1, s1

	def ReciveKey(self, e, n, k1, s1):
		self.log += f'Операція ReciveKey :\n'
		d1 = self.p_key
		e1, n1 = self.o_key

		self.log += f'k1 = {hex(k1)}\n'
		self.log += f's1 = {hex(s1)}\n'

		k = self.Decrypt(k1, n1, d1)
		_, s = self.Sign(s1, n1, d1)

		self.log += f'k = {hex(k)}\n'
		self.log += f's = {hex(s)}\n'
		res = self.Verify(k, s, e, n)
		self.log += f'Результат верифікації {res}'
		return res
