from rsa import RSA

import requests
import json

key_req = requests.get('http://asymcryptwebservice.appspot.com/rsa/serverKey?keySize=256')

n1 = key_req.text
n1 = int(json.loads(n1)['modulus'], 16)
e1 = key_req.text
e1 = int(json.loads(e1)['publicExponent'], 16)

a = RSA(256, 'A')
a.GenerateKeyPair()

while a.o_key[1] > n1:
	a = RSA(256, 'A')
	a.GenerateKeyPair()
e, n = a.o_key

a.log += f"Отримані Modulus та publicExponent: n1 = {n1} , e1 ={e1}\n"

request = f"http://asymcryptwebservice.appspot.com/rsa/sendKey?modulus={hex(n)[2:]}&publicExponent={hex(e)[2:]}"

keygen_request = requests.get(request, cookies=key_req.cookies).text

k1 = int(json.loads(keygen_request)['key'], 16)
s1 = int(json.loads(keygen_request)['signature'], 16)

a.log += f"Отримані Key та Signature: k1 = {k1} , s1 = {s1}\n"

a.ReciveKey(e1, n1, k1, s1)
sendKey = open('reciveKey.txt', 'w', encoding="utf8")
sendKey.write(a.log)
sendKey.close()
