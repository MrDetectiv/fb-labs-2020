import logging
from sys import stdout
from typing import Dict, List, Tuple

from functions import *
from functions.jacobi import JacobiSymbol

sh = logging.StreamHandler(stdout)
fh = logging.FileHandler('report.txt', 'w') 
logging.basicConfig(level=logging.DEBUG, format="%(message)s", handlers=(sh, fh))



def test_with_server_key():
    server_modulus_str = '0x9F7C062AF66FE39A065A57AA6826EE45CE350953725EAEB1A6EFCC44E534B8AB'
    signed_message_str = '0x1D2F016E33204AAEB83516A8A314B43EA8A507E6976F7267F5DCE55DB537DC7D'
    e = 0x10001
    message = 0x1111
    server_modulus = int(server_modulus_str, 16)
    signed_message = int(signed_message_str, 16)
    print(hex(encrypt(message, e, server_modulus))[2:])
    print(verify(0x1234, signed_message, e, server_modulus))

def test_verification():
    server_modulus_str = '0x9F7C062AF66FE39A065A57AA6826EE45CE350953725EAEB1A6EFCC44E534B8AB'
    signed_message_str = '0x1D2F016E33204AAEB83516A8A314B43EA8A507E6976F7267F5DCE55DB537DC7D'
    e = 0x10001
    message = 0x1234
    server_modulus = int(server_modulus_str, 16)
    signed_message = int(signed_message_str, 16)
    print(verify(message, signed_message, e, server_modulus))

def test_send_key():  
    server_modulus_str = '0x9F7C062AF66FE39A065A57AA6826EE45CE350953725EAEB1A6EFCC44E534B8AB'
    e, d, n = gen_key_pair(64) 
    e1 = 0x10001
    message = 0x1234
    server_modulus = int(server_modulus_str, 16)
    k1, s1 = send_key(message, d, n, e1, server_modulus)
    print (hex(k1) + '\n' + hex(s1))

def main():
    bits_len = 256
    e, d, n = gen_key_pair(bits_len)
    
    # Test encryption/decryption
    open_bytes = 123554323
    encrypted_bytes = encrypt(open_bytes, e, n)
    decrypted_bytes = decrypt(encrypted_bytes, d, n)
    logging.info("[*] RSA TEST\n    [-] Open bytes:      {}\n    [-] Encrypted bytes: {}\n    [-] Decrypted bytes: {}" \
        .format(open_bytes, encrypted_bytes, decrypted_bytes))


    logging.info("[*] Generating another key pair for testing key exchange")

    e1, d1, n1 = gen_key_pair(bits_len)

    # Value to be exchanged
    k = 11110000

    while n1 < n:
        e, d, n = gen_key_pair(bits_len)
        e1, d1, n1 = gen_key_pair(bits_len)

    logging.info("[*] Preparing data for sending ...")
    k1, S1 = send_key(k, d, n, e1, n1)
    logging.info("[*] Sending ...") 
    logging.info("[*] Receiving ...")

    if receive_key(k1, S1, d1, n1, e, n):
        logging.info("[!] Verified!")
    else:
        logging.info("[X] Not verified!")



if __name__ == '__main__':
    # test_verification()    
    test_send_key()
