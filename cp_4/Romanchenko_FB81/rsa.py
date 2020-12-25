from rsa_math import *


def generate_key_pair(key_length):
    first_prime = random_prime_bit(key_length)
    second_prime = random_prime_bit(key_length)

    modulus = first_prime * second_prime
    euler = (second_prime - 1) * (first_prime - 1)
    public_exponent = random_int(2, (euler - 1))

    while not gcd(public_exponent, euler) == 1:
        public_exponent += 1
        if public_exponent + 1 == euler:
            public_exponent = random_int(2, (euler - 1))

    secret = opposite(public_exponent, euler)

    public_key = (public_exponent, modulus)
    private_key = (secret, modulus)

    return public_key, private_key


def encrypt(message, public_key):
    public_exponent, modulus = public_key
    encrypted_message = pow(message, public_exponent, modulus)
    return encrypted_message


def decrypt(message, private_key):
    secret, modulus = private_key
    decrypted_message = pow(message, secret, modulus)
    return decrypted_message


def sign(message, private_key):
    secret, modulus = private_key
    signature = pow(message, secret, modulus)
    return signature


def verify(message, signature, public_key):
    public_exponent, modulus = public_key
    passed_verification = (message == pow(signature, public_exponent, modulus))
    return passed_verification


def send_key(message, user_a_private, user_b_public):
    encrypted_message = encrypt(message, user_b_public)
    message_signature = sign(message, user_a_private)
    encrypted_message_signature = encrypt(message_signature, user_b_public)
    return encrypted_message, encrypted_message_signature


def receive_key(encrypted_message, encrypted_message_signature, user_a_public_key, user_b_private_key):
    message = decrypt(encrypted_message, user_b_private_key)
    signature = decrypt(encrypted_message_signature, user_b_private_key)
    return verify(message, signature, user_a_public_key)
