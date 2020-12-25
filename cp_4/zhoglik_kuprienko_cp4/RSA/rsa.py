from RSA.crypto_math import *


class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p * q
        euler_f = euler_func(p, q)
        self.e = 2 ** 16 + 1
        self.d = inverse(self.e, euler_f)

    @property
    def p(self):
        return self._p

    @property
    def q(self):
        return self._q

    @property
    def d(self):
        return self._d

    @property
    def n(self):
        return self._n

    @property
    def e(self):
        return self._e

    @p.setter
    def p(self, value):
        self._p = value

    @q.setter
    def q(self, value):
        self._q = value

    @d.setter
    def d(self, value):
        self._d = value

    @n.setter
    def n(self, value):
        self._n = value

    @e.setter
    def e(self, value):
        self._e = value

    def __str__(self) -> str:
        return f'p: {hex(self.p)}\n' \
               f'q: {hex(self.q)}\n' \
               f'n: {hex(self.n)}\n' \
               f'e: {hex(self.e)}\n' \
               f'd: {hex(self.d)}\n '

    @staticmethod
    def encrypt(message, e, n):
        return pow(message, e, n)

    @staticmethod
    def decrypt(encrypted_message, d, n):
        return pow(encrypted_message, d, n)

    @staticmethod
    def sign(message, d, n):
        s = pow(message, d, n)
        return message, s

    @staticmethod
    def verify(message, s, other_e, other_n):
        return message == pow(s, other_e, other_n)

    def send_key(self, k, receiver, e=None, n=None):
        if (e is not None):
            receiver.e = e
            receiver.n = n

        k1 = self.encrypt(k, receiver.e, receiver.n)
        _, s = self.sign(k, self.d, self.n)
        s1 = self.encrypt(s, receiver.e, receiver.n)
        return k1, s1

    def receive_key(self, k1, s1, sender):
        k = self.decrypt(k1, self.d, self.n)
        s = self.decrypt(s1, self.d, self.n)
        return self.verify(k, s, sender.e, sender.n)


if __name__ == '__main__':
    pass
