import random
from rsa import RSA

if __name__ == "__main__":
    print("TESTING ON LOCAL MACHINE")
    with open('test.log', 'w') as f:
        f.seek(0)
    Alice = RSA("Alice", 256)
    Bob = RSA("Bob", 256)
    public_Bob = Bob.public_key
    public_Alice = Alice.public_key
    Alice.getpublickey(public_Bob)
    print("Info about Alice")
    Alice.info()
    Bob.getpublickey(public_Alice)
    print("Info about Bob")
    Bob.info()
    print("Test encryption and decryption")
    open = random.randint(1000000, 9999999999)
    print("Open text: ", open)
    cypher = Alice.encrypt(open)
    print("Encrypted by Alice: ", cypher)
    message = Bob.decrypt(cypher)
    print("Decrypted by Bob: ", message)
    print("Test signature and verification")
    signa = Bob.Sign(open)
    print("Message: {}\nSignature: {}".format(signa[0], signa[1]))
    Ver = Alice.Verify(signa)
    print("Verification: ", Ver)
    print("Test for sending keys")
    key = Alice.send_key()
    if key == None:
        key = Bob.send_key()
        get = Alice.Receive(key)
        print(get)
        print("Key from Bob to Alice")
        print("Key: {}".format(get[0]))
        print("Validation: ", get[1])
    else:
        get = Bob.Receive(key)
        print(get)
        print("Key from Alice to Bob")
        print("Key: {}".format(get[0]))
        print("Validation: ", get[1])
    print("FINISH TESTING ON LOCAL MACHINE")



