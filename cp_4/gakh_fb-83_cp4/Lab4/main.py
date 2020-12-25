from RSA import *

def generate_credentials():
       print('\n----------------------------------------------------')
       print('Generating keys for new user...')
       print('----------------------------------------------------')
       login = str(input('Enter name of new user: '))
       key_len = int(input('Preferable key length(in bits): '))
       keys = GenerateKeyPair(key_len)
       user_credentials = {
              'User_name' : login,
              'Private_values' : {'p' : keys['p'], 'q' : keys['q'], 'd' : keys['d']},
              'Modulus' : keys['n'],
              'Public_exponent' : keys['e']
              }
       M__=Decrypt(123456, keys['d']*keys['e'], keys['n'])
       if M__ != 123456:
              print('P and/or Q are not prime! Exiting...')
              return None
       print('----------------------------------------------------\n')
       return user_credentials
def print_public_credentials(user_credentials):
       print('\n========================')
       print('Login: {}'.format(user_credentials['User_name']))
       print('Modulus: {}'.format(hex(user_credentials['Modulus'])))
       print('Public_exponent: {}'.format(hex(user_credentials['Public_exponent'])))
       #print('Private_exponent: {}'.format(hex(user_credentials['Private_values']['d'])))
       print('========================\n')
def encrypt_for_someone(user_credentials):
       print('\n----------------------------------------------------')
       print('Encrypting for someone out there')
       print('----------------------------------------------------')
       M = random.randint(2**10, 2**20)
       print('Plain message from {} : {}'.format(user_credentials['User_name'], hex(M)))
       print('Enter modulus of receiver: ', end='')
       n = int(input(),16)
       print('Enter public exponent of receiver: ', end='')
       e = int(input(),16)
       C = Encrypt(M, e, n)
       print('Enciphered message : {}'.format(hex(C)))
       print('----------------------------------------------------\n')  
def decrypt_from_someone(user_credentials):
       print('\n----------------------------------------------------')
       print('Decrypting message for {}'.format(user_credentials['User_name']))
       print('----------------------------------------------------')
       print('Enciphered message : ', end = '')
       C = int(input(),16)
       d = user_credentials['Private_values']['d']
       n = user_credentials['Modulus']
       M = Decrypt(C, d, n)
       print('Plain message for {} : {}'.format(user_credentials['User_name'], hex(M)))
       print('----------------------------------------------------\n')
def sign_for_someone(user_credentials):
       print('\n----------------------------------------------------')
       print('Signing message for someone out there')
       print('----------------------------------------------------')
       M = random.randint(2**10, 2**20)
       print('Plain message from {} : {}'.format(user_credentials['User_name'], hex(M)))
       d = user_credentials['Private_values']['d']
       n = user_credentials['Modulus']
       MS = Sign(M, d, n)
       print('Signed message : {}, signature={}'.format(hex(MS[0]), hex(MS[1])))
       print('----------------------------------------------------\n')
def verify_from_someone(user_credentials):
       print('\n----------------------------------------------------')
       print('Verifying message for {}'.format(user_credentials['User_name']))
       print('----------------------------------------------------')
       print('Enter message itself: ', end = '')
       M = int(input(),16)
       print('Enter its signature : ', end = '')
       S = int(input(),16)
       print('Enter modulus of signer : ', end = '')
       n = int(input(),16)
       print('Enter public exponent of signer : ', end = '')
       e = int(input(),16)
       MS = Verify([M,S], e, n)
       if MS != None:
              print('Message is verified : {}'.format(hex(MS)))
       else:
              print('Message was not verified!!!')
       print('----------------------------------------------------\n')
def send_key_to_someone(user_credentials):
       print('\n----------------------------------------------------')
       print('Generating and sending key to someone')
       print('----------------------------------------------------')
       K = random.randint(2**100, 2**200)
       print('Key to send : {}'.format(hex(K)))
       print('Enter modulus of receiver : ', end = '')
       n1 = int(input(),16)
       print('Enter public exponent of receiver : ', end = '')
       e1 = int(input(),16)
       d = user_credentials['Private_values']['d']
       n = user_credentials['Modulus']
       KS = SendKey(K, d, n, e1, n1)
       print('Signed&Enciphered key to send : {}, signature={}'.format(hex(KS[0]), hex(KS[1])))
       print('----------------------------------------------------\n')
def receive_key_from_someone(user_credentials):
       print('\n----------------------------------------------------')
       print('Receiving and verifying key for {}'.format(user_credentials['User_name']))
       print('----------------------------------------------------')
       print('Enter Signed&Enciphered key itself: ', end = '')
       K = int(input(),16)
       print('Enter its signature : ', end = '')
       S = int(input(),16)
       print('Enter modulus of sender : ', end = '')
       n1 = int(input(),16)
       print('Enter public exponent of sender : ', end = '')
       e1 = int(input(),16)
       d = user_credentials['Private_values']['d']
       n = user_credentials['Modulus']
       arr = []
       arr.append(K)
       arr.append(S)
       KS = ReceiveKey(arr , d, n, e1, n1)
       if KS != None:
              print('Key is received and verified : {}'.format(hex(KS)))
       else:
              print('Key was not verified or deciphered correctly!!!')
       print('----------------------------------------------------\n')
A = generate_credentials()
print_public_credentials(A)
B = generate_credentials()
print_public_credentials(B)
check = 'y'
i = 0
while check == 'y':
       print('Session#{}...'.format(i))
       #print_public_credentials(A)
       #encrypt_for_someone(A)
       #decrypt_from_someone(A)
       #sign_for_someone(A)
       #verify_from_someone(A)
       send_key_to_someone(A)
       receive_key_from_someone(B)
       print('Do you want to continue?(y/n)', end='')
       check = str(input())



