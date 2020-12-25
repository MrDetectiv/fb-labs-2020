import requests
from rsa import RSA

import json

key_req = requests.get('http://asymcryptwebservice.appspot.com/rsa/serverKey?keySize=256')

n1 = key_req.text
n1 = int(json.loads(n1)['modulus'], 16)
e1 = key_req.text
e1 = int(json.loads(e1)['publicExponent'], 16)

a = RSA(256, 'A')
a.GenerateKeyPair()

a.log += f"Отримані Modulus та publicExponent: n1 = {n1} , e1 ={e1}\n"

while a.o_key[1] > n1:
	a = RSA(256, 'A')
	a.GenerateKeyPair()

k1, s1 = a.SendKey(e1, n1)
e, n = a.o_key

request = f"http://asymcryptwebservice.appspot.com/rsa/receiveKey?key={hex(k1)[2:]}&signature={hex(s1)[2:]}&modulus={hex(n)[2:]}&publicExponent={hex(e)[2:]}"
a.log += "Перевірка на сайті :\n"
a.log += requests.get(request, cookies=key_req.cookies).text

sendKey = open('sendKey.txt', 'w', encoding="utf8")
sendKey.write(a.log)
sendKey.close()
