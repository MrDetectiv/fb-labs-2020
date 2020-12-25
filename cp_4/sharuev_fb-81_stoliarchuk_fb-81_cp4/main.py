from functions import *


# Alice
print("Alice:")
Alice_keys = generate_key_pair(256)
Alice_open_key = Alice_keys[0]
Alice_secret_key = Alice_keys[1]


# Bob
print()
print("Bob:")
Bob_keys = generate_key_pair(256)
Bob_open_key = Alice_keys[0]
Bob_secret_key = Alice_keys[1]


# Alice encrypts a message for Bob
message = int(input("\nWrite a message: "))
print("Message:", hex(message))
encrypted_message = encrypt(message, Bob_open_key)
print("Encrypted message:", hex(encrypted_message))


# Alice creates a digital signature
signature = sign(message, Alice_secret_key)
print("Signature:", hex(signature))


# Alice encrypts a digital signature
encrypted_signature = encrypt(signature, Bob_open_key)
print("Encrypted signature:", hex(encrypted_signature))

# Alice sends Bob: (encrypted_message, encrypted_signature)
print()
print("*" * 175)
print()


# Bob deciphers a message from Alice

decrypted_message = decrypt(encrypted_message, Bob_secret_key)
print("Decrypted message:", hex(decrypted_message))


# Bob deciphers a signature from Alice
decrypted_signature = decrypt(encrypted_signature, Bob_secret_key)
print("Decrypted signature:", hex(decrypted_signature))


# Bob checks Alice's digital signature
print("Signature verification:", verify(decrypted_message, signature, Alice_open_key))


# Confidential key distribution protocol
print("\n\nConfidential key distribution protocol".upper())
print("\n\nSender:")
sender_open_key, sender_secret_key = generate_key_pair(256)
print("\n\nRecipient:")
recipient_open_key, recipient_secret_key = generate_key_pair(256)

message = randint(0, pow(2, 256 - 1))
print("\nMessage:", hex(message))

sent_message = send_key(message, sender_secret_key, recipient_open_key)
print("\nSent message:\n\tEncrypted message: {}\n\tEncrypted signature: {}\n\n".format(hex(sent_message[0]), hex(sent_message[1])))
checked_message = receive_key(sent_message, sender_open_key, recipient_secret_key)
print("Received message:\n\tMessage: {}\n\tVerification: {}\n\n".format(hex(checked_message[0]), checked_message[1]))


# Confidential key distribution protocol with site
print("\n\nConfidential key distribution protocol with site".upper())
print("\n\nSender:")
sender_open_key, sender_secret_key = generate_key_pair(256)
print("\n\nRecipient:")
recipient_open_key = [int(input("\tEnter public exponent: "), 16), int(input("\tEnter modulus: "), 16)]
"""
Enter public exponent: 10001
Enter modulus: CC470BADA243EF8C68876D4A98071C3555AAFAE6CAD334C401BFCA5534B57B859099615FCC2852DC0221E8652B2FA2C968A78C22BEE76B7A79AD29FE8DC57109
"""
message = randint(0, pow(2, 256 - 1))
print("\nMessage:", hex(message))

sent_message = send_key(message, sender_secret_key, recipient_open_key)
print("\nSent message:\n\tEncrypted message: {}\n\tEncrypted signature: {}".format(hex(sent_message[0]), hex(sent_message[1])))
print("\tModulus: {}\n\tPublic exponent: {}\n\n".format(hex(sender_open_key[1]), hex(sender_open_key[0])))
checked_message = int(input("\nMessage: "), 16)
print("Checked message:", hex(checked_message))
