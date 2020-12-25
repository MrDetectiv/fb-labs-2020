from RSA.exceptions import bad_status
from RSA.rsa import *
from RSA.crypto_math import *
import json
import requests


def generate_pair_less_then(n, length):
    p, q = generate_key_pair(length)

    if p * q <= n:
        return p, q
    return generate_pair_less_then(n, length)


if __name__ == '__main__':
    key_length = 256
    keygen_request = requests.get('http://asymcryptwebservice.appspot.com/rsa/serverKey?keySize=512')

    # if keygen_request.status_code != 200:
    #     raise bad_status()

    cookie = keygen_request.cookies
    cookie_name = cookie.keys()[0]
    cookie_value = cookie.values()[0]


    n1 = int(json.loads(keygen_request.text)['modulus'], 16)
    e1 = int(json.loads(keygen_request.text)['publicExponent'], 16)

    p, q = generate_pair_less_then(n1, key_length)

    rsa = RSA(p, q)

    print(f'cookie_name: {cookie_name}')
    print(f'cookie_value: {cookie_value}')

    print(f'n1: {hex(n1)}')
    print(f'e1: {hex(e1)}')
    print(rsa)

    x = random.randint(0, rsa.n - 1)

    k1, s1 = rsa.send_key(x, RSA(1, 3), e1, n1)


    key = hex(k1)[2:]
    signature = hex(s1)[2:]
    modulus = hex(rsa.n)[2:]
    publicExponent = hex(rsa.e)[2:]

    print(f'my random namber: {hex(x)}')
    print(f'key : {key}')
    print(f'signature : {signature}')
    print(f'modulus : {modulus}')
    print(f'publicExponent: {publicExponent}')

    request = f"http://asymcryptwebservice.appspot.com/rsa/receiveKey?key={key}&signature={signature}&modulus={modulus}&publicExponent={publicExponent}"
    cookie = {cookie_name: cookie_value}
    print(f"Response from ReceiveKey request: {requests.get(request, cookies=cookie).text}")

