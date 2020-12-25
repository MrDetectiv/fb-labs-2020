import cryptomath
import random

class RSA():
    def __init__(self,name,amount_of_bits):
        self.name = name
        self.q_and_p = []
        self.public_key = []
        self.private_key = []
        self.recived_keys = []
        self.GenerateKeyPair(amount_of_bits)

    def GenerateKeyPair(self,amount_of_bits):
        q = cryptomath.choose_random_prime(amount_of_bits,'q')
        p = cryptomath.choose_random_prime(amount_of_bits,'p')
        n = q*p
        euler_n = (q - 1) * (p - 1)
        e = pow(2, 16) + 1
        d = cryptomath.findModInverse(e, euler_n)
        self.public_key = [e,n]
        self.private_key = d
        self.recived_keys = []
        self.q_and_p = [q,p]

    def Text_to_num(self,m):
        m = list(bytes(m.encode('ascii')))
        m = '0x' + ''.join(list(map(lambda x: hex(x)[2:], m)))
        print("чисельне значення ВТ {}".format(m))
        m = int(m, 16)
        return m

    def Encrypt(self,message,public_key):
        e,n = public_key
        if type(message) is str:
            print("текстовий вит ВТ {}".format(message))
            message = self.Text_to_num(message)
        print("чисельний вид ВТ {}".format(hex(message)))
        if message > n:
            return None
        return pow(message,e,n)

    def Decrypt(self,ciphertext,n=None):
        if n == None:
            n = self.Get_n()
        return pow(ciphertext,self.private_key,n)

    def Sign(self,message,n,d=None):
        info_for_report = False
        if type(message) is str:
            message = self.Text_to_num(message)
            info_for_report = True
        orig_message = message
        if d == None:
            d = self.private_key
        s = pow(message,d,n)
        if info_for_report: print("цифровий підпис користувача {}: {}".format(self.name,(orig_message,hex(s))))
        return [orig_message,s]

    def Verify(self,message,signature):
        return message == pow(signature,self.public_key[0],self.public_key[1])

    def SendKey(self,reciver_public):
        print("Процедура SendKey")
        e,n = self.public_key
        print("n={}".format(hex(n)))
        print("e={}".format(hex(e)))
        e1,n1 = reciver_public
        print("n1={}".format(hex(n1)))
        print("e1={}".format(hex(e1)))
        d = self.private_key
        print("d={}".format(hex(d)))
        if n1 < n:
            return None
        k = random.randint(1,n-1)
        print("k={}".format(hex(k)))
        k1 = self.Encrypt(k,reciver_public)
        print("k1={}".format(hex(k1)))
        _,s = self.Sign(k,n)
        print("s={}".format(hex(s)))
        _,s1 = self.Sign(s,n1,e1)
        print("s1={}".format(hex(s1)))
        return (k1,s1)

    def ReciveKey(self,sender_public,k1_s1,sender_name):
        print("процедура ReciveKey")
        e,n = sender_public
        print("n={}".format(hex(n)))
        print("e={}".format(hex(e)))
        e1,n1 = self.public_key
        print("n1={}".format(hex(n1)))
        print("e1={}".format(hex(e1)))
        k1,s1 = k1_s1
        print("k1={}".format(hex(k1)))
        print("s1={}".format(hex(s1)))
        d1 = self.private_key
        print("d1={}".format(hex(d1)))
        k = self.Decrypt(k1,n1)
        print("k={}".format(hex(k)))
        _,s = self.Sign(s1,n1)
        print("s={}".format(hex(s)))
        print("s^e modn={}".format(hex(pow(s,e,n))))
        if k == pow(s,e,n):
            self.recived_keys.append({sender_name:k})
            return True

    def Get_n(self):
        return self.public_key[1]




    def GetInfoForReport(self):
        res = """
        q користувача {user} = {q}
        p користувача {user} = {p}
        n користувача {user} = {n}
        e користувача {user} = {e}
        d користувача {user} = {d}
        """.format(user=self.name,q=hex(self.q_and_p[0]),p=hex(self.q_and_p[1]),n=hex(self.public_key[1]),e=hex(self.public_key[0]),d=hex(self.private_key))
        print(res)

