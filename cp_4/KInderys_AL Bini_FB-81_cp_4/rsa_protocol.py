import functions as rsa
import requests

# local test

[[n, e], [d, p, q]] = rsa.generate_key_pair(512)  # keys for A
[[n1, e1], [d1, p1, q1]] = rsa.generate_key_pair(512)  # keys for b
while n1 < n:
    [[n1, e1], [d1, p1, q1]] = rsa.generate_key_pair(512)
print(f"\nKeys of A\nn is: {hex(n)[2:]}\ne is: {hex(e)[2:]}\nfi(n) is: {hex(((p-1)*(q-1)))[2:]}\nd is: {hex(d)[2:]}\np is: {hex(p)[2:]}\nq is: {hex(q)[2:]}")
print(f"\nKeys of B\nn1 is: {hex(n1)[2:]}\ne1 is: {hex(e1)[2:]}\nfi(n1) is: {hex(((p1-1)*(q1-1)))[2:]}\nd1 is:"
      f" {hex(d1)[2:]}\np is: {hex(p1)[2:]}\nq is: {hex(q1)[2:]}")
# A encrypt msg and decrypt it
msg = rsa.random.randint(2, 99999)
C = rsa.encrypt(msg, e, n)
decrypted_msg = rsa.decrypt(C, d, n)
print("\n\n local test for encryption and decryption\n\nmsg is: " + str(msg) + "\nEncrypted msg is: " + str(C)
      + "\nDecrypted msg is: " + str(decrypted_msg))


print("\n\n--------------------------------------- local check for signing and verification --------------------------"
      "-------------\n\n")


# A send signed msg to B
msg = rsa.random.randint(2, 99999)
print("msg is: " + str(msg))
signed_msg = rsa.send(msg, n1, e1, d, n)
print("encrypted msg is:" + signed_msg[0] + "\nsignature is: " + signed_msg[1])
# B received signed_msg and knows e and n
[check, k] = rsa.receive(signed_msg[0], signed_msg[1], n1, d1, e, n)
if check:
    print("Signature is valid\nencrypted msg is: " + str(k))
else:
    print("invalid signature")


print("\n\n--------------------------------------- user-server check for signing and verification"
      " ---------------------------------------\n\n")


# exchange with server
pub_k_request = f"http://asymcryptwebservice.appspot.com/rsa/serverKey?keySize=515"
keygen_request = requests.get(pub_k_request)
print("Server public key:" + str(keygen_request.json()))
server_n = int(keygen_request.json()["modulus"], 16)
server_e = int(keygen_request.json()["publicExponent"], 16)

msg = rsa.random.randint(2, 99999)
print("msg is: " + str(msg))
signed_msg = rsa.send(msg, server_n, server_e, d, n)
send_pub_k = f"http://asymcryptwebservice.appspot.com/rsa/receiveKey?key={signed_msg[0]}&signature={signed_msg[1]}&" \
             f"modulus={hex(n)[2:]}&publicExponent={hex(e)[2:]}"
verify_signature_request = requests.get(send_pub_k, cookies=keygen_request.cookies)
verified_msg = int(verify_signature_request.json()["key"], 16)
verification_status = verify_signature_request.json()["verified"]
print("msg server got after verification: " + str(verified_msg) + "\nverification result: " + str(verification_status))
