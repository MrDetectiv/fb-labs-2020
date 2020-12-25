from prime import *

class RSA():
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.private_key = []
        self.public_key = []
        self.get_key = []
        self.generate_key()


    def generate_key(self):
        #print("p")
        with open('test.log', 'a') as f:
            p = Random_prime(f, 'p', length=self.length)
            f.write('\n')
        #print("q")
        with open('test.log', 'a') as f:
            q = Random_prime(f, 'q', length=self.length)
            f.write('\n')
        #print("n")
        n = p*q
        #print("fe")
        fe = (p-1)*(q-1)
        #print("e")
        e = gorn(2, 16) + 1
        #print("d")
        d = inversmod(e, fe)
        self.private_key = [d, p, q]
        self.public_key = [n, e]

    def encrypt(self, message):
        #text = message.encode('utf-8')
        #hextext = text.hex()
        #numtext = int(hextext, 16)
        numtext = message
        #print("open: ", numtext)
        cypher = gorn(numtext, self.get_key[1], self.get_key[0])
        return cypher

    def decrypt(self, cypher):
        numtext = gorn(cypher, self.private_key[0], self.public_key[0])
        message = numtext
        #print("decr: ", message)
        #hextext = str(hex(numtext))[2:]
        #print(hextext)
        #mb = hextext.decode("hex")
        #mb = bytes.fromhex(hextext)
        #message = mb.decode('utf-8')
        return message

    def Sign(self, message):
        d = self.private_key[0]
        n = self.public_key[0]
        sign = pow(message, d, n)
        #sign = gorn(message, self.private_key[0], self.public_key[0])
        return [message, sign]

    def Verify(self, sign):
        s = sign[1]
        e = self.get_key[1]
        n = self.get_key[0]
        #message = gorn(sign[1], self.get_key[1], self.get_key[0])
        message = pow(s, e, n)
        if message == sign[0]:
            return True
        else:
            return False

    def send_key(self):
        n, e = self.public_key
        n1, e1 = self.get_key
        d = self.private_key[0]
        if n > n1:
            return None
        else:
            k = random.randint(1, n-1)
            print("k: ", hex(k))
            s = pow(k, d, n)
            print("s: ", hex(s))
            k1 = pow(k, e1, n1)
            s1 = pow(s, e1, n1)
            return [k1, s1]

    def Receive(self, public):
        k1, s1 = public
        n, e = self.get_key
        n1, e1 = self.public_key
        d1 = self.private_key[0]
        k = pow(k1, d1, n1)
        s = pow(s1, d1, n1)
        #print("s f s1: ", s)
        ver = gorn(s, e, n)
        #print("k, ver: ", k, ver)
        V = False
        if k == ver:
            V = True
        return [k, V]

    def getpublickey(self, public):
        n = public[0]
        e = public[1]
        self.get_key = [n, e]



    def info(self):
        print("Name: ", self.name)
        print("Public key: ", self.public_key)
        print("Private key: ", self.private_key)
        print("Geted key: ", self.get_key)


    def hexinfo(self):
        print("Name: ", self.name)
        hexpublic_key = []
        hexprivate_key = []
        hexget_key = []
        for l in self.public_key:
            t = str(hex(l))[2:]
            hexpublic_key.append(t)
        for l in self.private_key:
            t = str(hex(l))[2:]
            hexprivate_key.append(t)
        for l in self.get_key:
            t = str(hex(l))[2:]
            hexget_key.append(t)
        print("Public key: ", hexpublic_key)
        print("Private key: ", hexprivate_key)
        print("Geted key: ", hexget_key)



if __name__ == "__main__":
    Alice = RSA("Alice", 128)
    Bob = RSA("Bob", 128)
    public_Bob = Bob.public_key
    public_Alice = Alice.public_key
    Alice.getpublickey(public_Bob)
    Alice.info()
    Bob.getpublickey(public_Alice)
    Bob.info()
    # key = Alice.send_key()
    # print("akey:", key)
    # if key == None:
    #     key = Bob.send_key()
    #     print("bkey: ",key)
    #     print(Alice.Receive(key))
    # else:
    #     print(Bob.Receive(key))
    # open = 132557566468465156518615151
    open = 123456789
    signa = Alice.Sign(open)
    message = Bob.Verify(signa)
    print(message)




