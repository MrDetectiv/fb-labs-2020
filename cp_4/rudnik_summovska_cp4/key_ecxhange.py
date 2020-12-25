import rsa
import json
import requests
tolik = rsa.RSA("tolik",512)
keygen_request = requests.get('http://asymcryptwebservice.appspot.com/rsa/serverKey?keySize=512')
cookie = keygen_request.cookies
cookie_name = cookie.keys()[0]
cookie_value = cookie.values()[0]
print("ім'я cookie: {}".format(cookie_name))
print("значення cookie: {}".format(cookie_value))
n1 = keygen_request.text
n1 = json.loads(n1)['modulus']
n1 = int(n1,16)
e1 = 65537
while tolik.Get_n() > n1:
    tolik.GenerateKeyPair(512)
tolik.GetInfoForReport()
print('n1 сайта {}'.format(hex(n1)))
print('e1 сайта {}'.format(hex(e1)))
k1,s1=tolik.SendKey([e1,n1])
e,n = tolik.public_key
request = "http://asymcryptwebservice.appspot.com/rsa/receiveKey?key={k}&signature={s}&modulus={n}&publicExponent={e}".format(k=hex(k1)[2:],s=hex(s1)[2:],n=hex(n)[2:],e=hex(e)[2:])
cookie = {cookie_name:cookie_value}
print("відповідь ReciveKey сайту: ")
print(requests.get(request,cookies=cookie).text)