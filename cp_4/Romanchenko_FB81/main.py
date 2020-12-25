from rsa import *
import requests

class Person:

    def __init__(self, key_lentgh):
        public_key, private_key = generate_key_pair(key_lentgh)
        self.public_key = public_key
        self.private_key = private_key
        print()
        print(f"Alice public key:"
              f"\n\tpublic exponent: {public_key[0]}"
              f"\n\tmodulus: {public_key[1]}")
        print(f"Alice private key:"
              f"\n\tsecret: {public_key[0]}"
              f"\n\tmodulus: {public_key[1]}")
        print()


def pretty_hexed(num):
    return "0" + hex(num)[2:]


alice = Person(512)
alice_message = 123456789
encrypted_message = encrypt(alice_message, alice.public_key)

rec = requests.get(f"http://asymcryptwebservice.appspot.com/rsa/encrypt"
                   f"?modulus={pretty_hexed(alice.public_key[1])}"
                   f"&publicExponent={pretty_hexed(alice.public_key[0])}"
                   f"&message={pretty_hexed(alice_message)}")

print(f"Api and local encryptions are same? - {int(rec.json()['cipherText'], 16) == encrypted_message}\n")

print(f"Local decryption test passed { decrypt(encrypted_message, alice.private_key) == alice_message }\n")

signature = sign(alice_message, alice.private_key)

rec = requests.get(f"http://asymcryptwebservice.appspot.com/rsa/verify"
                   f"?message={pretty_hexed(alice_message)}"
                   f"&signature={pretty_hexed(signature)}"
                   f"&modulus={pretty_hexed(alice.public_key[1])}"
                   f"&publicExponent={pretty_hexed(alice.public_key[0])}")

print(f"Local verification: {verify(alice_message, signature, alice.public_key)}\n"
      f"Api verification {rec.json()['verified']}\n")

rec = requests.get(f"http://asymcryptwebservice.appspot.com/rsa/serverKey?keySize=520")

bob_public_key = (int(rec.json()["publicExponent"], 16), int(rec.json()["modulus"], 16))

encrypted_message, encrypted_message_signature = send_key(alice_message, alice.private_key, bob_public_key)


rec = requests.get(f"http://asymcryptwebservice.appspot.com/rsa/receiveKey"
                   f"?key={pretty_hexed(encrypted_message)}"
                   f"&signature={pretty_hexed(encrypted_message_signature)}"
                   f"&modulus={pretty_hexed(alice.public_key[1])}"
                   f"&publicExponent={pretty_hexed(alice.public_key[0])}",
                   cookies=rec.cookies)

print(f"Bob got message {int(rec.json()['key'], 16)} is valid message? - {rec.json()['verified']}")
