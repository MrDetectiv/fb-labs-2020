import json
import requests
from requests import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ServerSide:
    def __init__(self):
        self.session = requests.Session()
    
    def generatekeys(self,keysize):
        response = self.session.get(f'http://asymcryptwebservice.appspot.com/rsa/serverKey?keySize={keysize}').text
        response = json.loads(response)
        e1 = int(response['publicExponent'],16)
        n1 = int(response['modulus'],16)
        return n1,e1

    def encrypt(self,text,e,n):
        response_encrypt = self.session.get('http://asymcryptwebservice.appspot.com/rsa/encrypt',params={'modulus':str(hex(n))[2:],'publicExponent':str(hex(e))[2:], 'message':str(hex(text))[2:],'type':'BYTES'}).text
        ciphertext = int(json.loads(response_encrypt)['cipherText'],16)
        return ciphertext
    
    def decrypt(self,ciphertext):
        response_encrypt = self.session.get('http://asymcryptwebservice.appspot.com/rsa/decrypt',params={'cipherText':str(hex(ciphertext))[2:],'expectedType':'BYTES'}).text
        opentext = int(json.loads(response_encrypt)['message'],16)
        return opentext

